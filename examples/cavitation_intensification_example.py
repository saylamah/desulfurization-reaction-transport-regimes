"""
Cavitation-assisted desulfurization intensification screening example.

This module compares a hydrodynamic-cavitation-assisted case with a defined
reference case using product-based sulfur reduction, apparent-rate
enhancement, measured electrical energy, hydraulic cross-checks, and one
explicit cavitation-number definition.

The script distinguishes among:

* sulfur absent from the recovered product;
* incremental product-based sulfur benefit relative to a reference;
* gross electrical energy for each case;
* incremental electrical energy;
* hydraulic power across the defined device boundary;
* estimated pump-drive electrical demand;
* apparent kinetic enhancement;
* evidence of cavitation occurrence;
* evidence of useful overall process performance.

Authoritative inputs
--------------------
Illustrative numerical inputs are loaded from:

    data/example_parameters.csv

The shared loader validates:

* CSV structure;
* parameter names;
* units;
* case identity;
* duplicate definitions;
* finite numerical values;
* documented case schemas.

Scientific scope
----------------
The calculations are screening relationships, not a mechanistic cavitation
model. Direct comparison requires equivalent feed, sulfur inventory,
treatment time, thermal history, analytical method, separation boundary, and
product-recovery basis.

The product-based sulfur metric used here is:

    sulfur in feed - sulfur in recovered product

It is not a complete sulfur balance. Sulfur may remain in solvent, water,
gas, solids, catalyst, adsorbent, deposits, lost hydrocarbon, or unmeasured
products. Complete validation therefore requires sulfur accounting across
all relevant phases, deposits, samples, and losses.

The apparent-rate coefficients are comparison metrics only. They must not be
interpreted as intrinsic kinetic constants unless external transfer, internal
diffusion, hydrodynamics, deactivation, reactant depletion, and separation
effects have been excluded.

The cavitation number implemented here is:

    sigma = (p_ref - p_v) / (0.5 * rho * v**2)

Its numerical value depends on the stated pressure location, absolute-pressure
basis, velocity definition, temperature-dependent vapor pressure, fluid
properties, and device geometry. Equal cavitation number does not guarantee
equal cavity dynamics, erosion, chemical effect, or scale-up behavior.

Evidence status
---------------
E3 -- executable engineering-screening research prototype.

Reference frameworks
--------------------
Reaction-Transport Regime Analysis for Desulfurization of Gas and Petroleum
Streams: An Engineering Diagnostic Framework.

Industrial Usefulness and Technology Selection in Process Intensification:
Energy-Normalized Metrics for Hydrodynamic Cavitation.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from pathlib import Path

try:
    from .example_parameter_loader import (
        ParameterStore,
        load_default_parameter_store,
    )
except ImportError:
    from example_parameter_loader import (
        ParameterStore,
        load_default_parameter_store,
    )


JOULES_PER_KWH = 3.6e6
ZERO_TOLERANCE = 1.0e-12
COMPARABILITY_REL_TOLERANCE = 1.0e-6
COMPARABILITY_ABS_TOLERANCE = 1.0e-12

COMPARISON_EXAMPLE_ID = "cavitation_comparison"
REFERENCE_CASE_ID = "reference_case"
CAVITATION_CASE_ID = "cavitation_case"

HYDRAULICS_EXAMPLE_ID = "cavitation_hydraulics"
HYDRAULICS_CASE_ID = "hc_operating_point"


@dataclass(frozen=True, slots=True)
class DesulfurizationCase:
    """Measured basis for one desulfurization case.

    Parameters
    ----------
    name:
        Human-readable case identifier.
    apparent_rate_coefficient_s_inv:
        Apparent pseudo-first-order coefficient, s^-1. It is a comparison
        metric and is not assumed to be intrinsic.
    initial_sulfur_in_feed_g:
        Sulfur mass entering with the defined feed inventory, g.
    sulfur_in_recovered_product_g:
        Sulfur mass measured in the recovered final product after the defined
        reaction and separation sequence, g.
    feed_volume_m3:
        Feed inventory used as the comparison basis, m^3.
    treatment_time_s:
        Total treatment time, s.
    measured_total_electrical_energy_kwh:
        Measured total electrical energy within the declared process boundary,
        kWh.
    initial_temperature_k:
        Initial bulk temperature, K.
    final_temperature_k:
        Final bulk temperature, K.
    """

    name: str
    apparent_rate_coefficient_s_inv: float
    initial_sulfur_in_feed_g: float
    sulfur_in_recovered_product_g: float
    feed_volume_m3: float
    treatment_time_s: float
    measured_total_electrical_energy_kwh: float
    initial_temperature_k: float
    final_temperature_k: float

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Case name must not be empty.")

        _require_finite_nonnegative(
            "apparent_rate_coefficient_s_inv",
            self.apparent_rate_coefficient_s_inv,
        )
        _require_finite_positive(
            "initial_sulfur_in_feed_g",
            self.initial_sulfur_in_feed_g,
        )
        _require_finite_nonnegative(
            "sulfur_in_recovered_product_g",
            self.sulfur_in_recovered_product_g,
        )
        _require_finite_positive(
            "feed_volume_m3",
            self.feed_volume_m3,
        )
        _require_finite_positive(
            "treatment_time_s",
            self.treatment_time_s,
        )
        _require_finite_nonnegative(
            "measured_total_electrical_energy_kwh",
            self.measured_total_electrical_energy_kwh,
        )
        _require_finite_positive(
            "initial_temperature_k",
            self.initial_temperature_k,
        )
        _require_finite_positive(
            "final_temperature_k",
            self.final_temperature_k,
        )

        if (
            self.sulfur_in_recovered_product_g
            > self.initial_sulfur_in_feed_g
        ):
            raise ValueError(
                "Sulfur in recovered product cannot exceed sulfur in feed "
                "for this simplified closed comparison basis."
            )

    @property
    def sulfur_excluded_from_product_g(self) -> float:
        """Return sulfur absent from the recovered product, g."""
        return (
            self.initial_sulfur_in_feed_g
            - self.sulfur_in_recovered_product_g
        )

    @property
    def product_sulfur_reduction_fraction(self) -> float:
        """Return the product-based sulfur reduction fraction."""
        return (
            self.sulfur_excluded_from_product_g
            / self.initial_sulfur_in_feed_g
        )

    @property
    def temperature_rise_k(self) -> float:
        """Return final minus initial bulk temperature, K."""
        return (
            self.final_temperature_k
            - self.initial_temperature_k
        )

    @property
    def gross_energy_intensity_kwh_m3(self) -> float:
        """Return measured gross electrical energy per feed volume."""
        return (
            self.measured_total_electrical_energy_kwh
            / self.feed_volume_m3
        )


@dataclass(frozen=True, slots=True)
class CavitationOperatingPoint:
    """Hydraulic operating data for the cavitation-assisted case.

    All pressures must be absolute.

    ``downstream_reference_pressure_abs_pa`` is used as ``p_ref`` in the
    implemented cavitation-number expression. A different study may use a
    different pressure location, but it must state and justify that definition.
    """

    upstream_pressure_abs_pa: float
    downstream_reference_pressure_abs_pa: float
    vapor_pressure_pa: float
    density_kg_m3: float
    characteristic_velocity_m_s: float
    loop_flow_rate_m3_s: float
    operating_time_s: float
    pump_efficiency: float
    drive_efficiency: float

    def __post_init__(self) -> None:
        _require_finite_positive(
            "upstream_pressure_abs_pa",
            self.upstream_pressure_abs_pa,
        )
        _require_finite_positive(
            "downstream_reference_pressure_abs_pa",
            self.downstream_reference_pressure_abs_pa,
        )
        _require_finite_positive(
            "vapor_pressure_pa",
            self.vapor_pressure_pa,
        )
        _require_finite_positive(
            "density_kg_m3",
            self.density_kg_m3,
        )
        _require_finite_positive(
            "characteristic_velocity_m_s",
            self.characteristic_velocity_m_s,
        )
        _require_finite_positive(
            "loop_flow_rate_m3_s",
            self.loop_flow_rate_m3_s,
        )
        _require_finite_positive(
            "operating_time_s",
            self.operating_time_s,
        )
        _require_efficiency(
            "pump_efficiency",
            self.pump_efficiency,
        )
        _require_efficiency(
            "drive_efficiency",
            self.drive_efficiency,
        )

        if (
            self.upstream_pressure_abs_pa
            <= self.downstream_reference_pressure_abs_pa
        ):
            raise ValueError(
                "Upstream absolute pressure must exceed downstream "
                "reference absolute pressure."
            )

        if (
            self.downstream_reference_pressure_abs_pa
            <= self.vapor_pressure_pa
        ):
            raise ValueError(
                "Downstream reference absolute pressure must exceed vapor "
                "pressure for the stated positive cavitation-number form."
            )

    @property
    def pressure_drop_pa(self) -> float:
        """Return pressure drop across the defined device boundary, Pa."""
        return (
            self.upstream_pressure_abs_pa
            - self.downstream_reference_pressure_abs_pa
        )

    @property
    def hydraulic_power_w(self) -> float:
        """Return hydraulic power across the stated pressure-drop boundary."""
        return (
            self.pressure_drop_pa
            * self.loop_flow_rate_m3_s
        )

    @property
    def estimated_electrical_power_w(self) -> float:
        """Return pump-drive electrical power estimated from efficiencies."""
        return self.hydraulic_power_w / (
            self.pump_efficiency
            * self.drive_efficiency
        )

    @property
    def estimated_electrical_energy_kwh(self) -> float:
        """Return estimated pump-drive electrical energy, kWh."""
        return (
            self.estimated_electrical_power_w
            * self.operating_time_s
            / JOULES_PER_KWH
        )

    @property
    def cavitation_number(self) -> float:
        """Return the stated cavitation-number definition."""
        dynamic_pressure_pa = (
            0.5
            * self.density_kg_m3
            * self.characteristic_velocity_m_s**2
        )

        return (
            self.downstream_reference_pressure_abs_pa
            - self.vapor_pressure_pa
        ) / dynamic_pressure_pa

    def nominal_inventory_turnovers(
        self,
        liquid_inventory_m3: float,
    ) -> float:
        """Return circulated loop volume divided by liquid inventory.

        The result is a nominal inventory-turnover count, not the number of
        identical cavitation events experienced by every fluid element.
        A recirculating system has a treatment-history distribution governed
        by mixing, bypassing, and residence-time behavior.
        """
        _require_finite_positive(
            "liquid_inventory_m3",
            liquid_inventory_m3,
        )

        return (
            self.loop_flow_rate_m3_s
            * self.operating_time_s
            / liquid_inventory_m3
        )


@dataclass(frozen=True, slots=True)
class IncrementalComparisonResult:
    """Calculated comparison between reference and intensified cases."""

    apparent_enhancement_factor: float
    incremental_sulfur_excluded_from_product_g: float
    incremental_electrical_energy_kwh: float
    energy_normalized_incremental_sulfur_g_per_kwh: float | None
    incremental_specific_energy_kwh_per_g_s: float | None
    incremental_specific_energy_kwh_per_kg_s: float | None
    incremental_energy_intensity_kwh_m3: float | None
    outcome_statement: str
    comparability_notes: tuple[str, ...]


def _require_finite_positive(
    name: str,
    value: float,
) -> None:
    """Require a finite value strictly greater than zero."""
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(
            f"{name} must be finite and greater than zero."
        )


def _require_finite_nonnegative(
    name: str,
    value: float,
) -> None:
    """Require a finite value greater than or equal to zero."""
    if not math.isfinite(value) or value < 0.0:
        raise ValueError(
            f"{name} must be finite and non-negative."
        )


def _require_efficiency(
    name: str,
    value: float,
) -> None:
    """Require a finite fractional efficiency in the interval (0, 1]."""
    if not math.isfinite(value) or not 0.0 < value <= 1.0:
        raise ValueError(
            f"{name} must be finite and satisfy 0 < {name} <= 1."
        )


def _approximately_equal(
    first: float,
    second: float,
) -> bool:
    """Return whether two comparison-basis values are equivalent."""
    return math.isclose(
        first,
        second,
        rel_tol=COMPARABILITY_REL_TOLERANCE,
        abs_tol=COMPARABILITY_ABS_TOLERANCE,
    )


def apparent_enhancement_factor(
    intensified_rate_coefficient_s_inv: float,
    reference_rate_coefficient_s_inv: float,
) -> float:
    """Return the apparent-rate enhancement factor.

    Both coefficients must be fitted on equivalent concentration, time,
    temperature, analytical, and process-boundary bases.
    """
    _require_finite_nonnegative(
        "intensified_rate_coefficient_s_inv",
        intensified_rate_coefficient_s_inv,
    )
    _require_finite_positive(
        "reference_rate_coefficient_s_inv",
        reference_rate_coefficient_s_inv,
    )

    return (
        intensified_rate_coefficient_s_inv
        / reference_rate_coefficient_s_inv
    )


def energy_normalized_incremental_sulfur(
    incremental_sulfur_g: float,
    incremental_energy_kwh: float,
) -> float:
    """Return positive incremental sulfur benefit per additional energy.

    The metric is intentionally undefined for zero or negative incremental
    sulfur benefit or for zero or negative incremental energy.
    """
    _require_finite_positive(
        "incremental_sulfur_g",
        incremental_sulfur_g,
    )
    _require_finite_positive(
        "incremental_energy_kwh",
        incremental_energy_kwh,
    )

    return (
        incremental_sulfur_g
        / incremental_energy_kwh
    )


def incremental_specific_energy(
    incremental_energy_kwh: float,
    incremental_sulfur_g: float,
) -> float:
    """Return additional electrical energy per incremental gram of sulfur."""
    _require_finite_positive(
        "incremental_energy_kwh",
        incremental_energy_kwh,
    )
    _require_finite_positive(
        "incremental_sulfur_g",
        incremental_sulfur_g,
    )

    return (
        incremental_energy_kwh
        / incremental_sulfur_g
    )


def assess_comparability(
    reference: DesulfurizationCase,
    intensified: DesulfurizationCase,
) -> tuple[str, ...]:
    """Return explicit notes about the numerical comparison basis."""
    notes: list[str] = []

    checks = (
        (
            "initial sulfur inventory",
            reference.initial_sulfur_in_feed_g,
            intensified.initial_sulfur_in_feed_g,
            "g",
        ),
        (
            "feed volume",
            reference.feed_volume_m3,
            intensified.feed_volume_m3,
            "m^3",
        ),
        (
            "treatment time",
            reference.treatment_time_s,
            intensified.treatment_time_s,
            "s",
        ),
        (
            "initial temperature",
            reference.initial_temperature_k,
            intensified.initial_temperature_k,
            "K",
        ),
        (
            "final temperature",
            reference.final_temperature_k,
            intensified.final_temperature_k,
            "K",
        ),
    )

    for label, reference_value, intensified_value, unit in checks:
        if not _approximately_equal(
            reference_value,
            intensified_value,
        ):
            notes.append(
                f"Non-equivalent {label}: reference="
                f"{reference_value:.6g} {unit}, intensified="
                f"{intensified_value:.6g} {unit}."
            )

    if not notes:
        notes.append(
            "The numerical demonstration uses equivalent sulfur inventory, "
            "feed volume, treatment time, and bulk-temperature endpoints."
        )

    notes.append(
        "Equivalent analytical methods, sulfur speciation, separation "
        "procedures, product recovery, and sulfur-balance boundaries must "
        "also be verified experimentally; they cannot be established from "
        "these scalar inputs."
    )

    return tuple(notes)


def _require_direct_case_comparability(
    reference: DesulfurizationCase,
    intensified: DesulfurizationCase,
) -> None:
    """Require equivalent scalar bases before direct case subtraction.

    This check cannot establish equivalence of feed chemistry, analytical
    methods, separation procedures, or complete temperature histories. Those
    requirements remain experimental responsibilities.
    """
    checks = (
        (
            "initial sulfur inventory",
            reference.initial_sulfur_in_feed_g,
            intensified.initial_sulfur_in_feed_g,
            "Normalize both cases to a common sulfur-inventory basis.",
        ),
        (
            "feed volume",
            reference.feed_volume_m3,
            intensified.feed_volume_m3,
            "Normalize both cases to a common feed-volume basis.",
        ),
        (
            "treatment time",
            reference.treatment_time_s,
            intensified.treatment_time_s,
            "Use a common treatment interval before comparing removed mass.",
        ),
        (
            "initial temperature",
            reference.initial_temperature_k,
            intensified.initial_temperature_k,
            "Use a matched initial thermal condition.",
        ),
        (
            "final temperature",
            reference.final_temperature_k,
            intensified.final_temperature_k,
            "Use a matched final thermal condition or a matched full thermal "
            "history.",
        ),
    )

    for label, reference_value, intensified_value, remedy in checks:
        if not _approximately_equal(
            reference_value,
            intensified_value,
        ):
            raise ValueError(
                f"Direct comparison requires equivalent {label}. "
                f"Reference={reference_value:.6g}; "
                f"intensified={intensified_value:.6g}. {remedy}"
            )


def _outcome_statement(
    apparent_enhancement: float,
    incremental_sulfur_g: float,
    incremental_energy_kwh: float,
) -> str:
    """Return a non-threshold-based engineering screening statement."""
    if incremental_sulfur_g <= ZERO_TOLERANCE:
        return (
            "No positive incremental product-based sulfur benefit relative "
            "to the reference; energy-normalized benefit is not applicable."
        )

    if incremental_energy_kwh > ZERO_TOLERANCE:
        if apparent_enhancement > 1.0:
            return (
                "Positive incremental product-based sulfur benefit and "
                "apparent-rate enhancement were obtained at positive "
                "additional electrical energy. Usefulness must be judged "
                "against project-specific energy, separation, product, "
                "materials, durability, safety, and economic criteria."
            )

        return (
            "Positive incremental product-based sulfur benefit was obtained "
            "at positive additional electrical energy, but no apparent-rate "
            "enhancement was demonstrated. Review measurement uncertainty, "
            "separation effects, and the fitted-rate basis."
        )

    if abs(incremental_energy_kwh) <= ZERO_TOLERANCE:
        return (
            "Positive incremental product-based sulfur benefit was obtained "
            "with no measured incremental electrical energy. Verify the "
            "energy boundary, measurement resolution, and uncertainty before "
            "interpreting this as an energy-neutral improvement."
        )

    return (
        "Positive incremental product-based sulfur benefit was obtained "
        "with lower measured electrical energy than the reference. Verify "
        "equivalent boundaries and uncertainty before interpreting this as "
        "a dominant process improvement."
    )


def compare_cases(
    reference: DesulfurizationCase,
    intensified: DesulfurizationCase,
) -> IncrementalComparisonResult:
    """Compare an intensified case with its defined reference."""
    _require_direct_case_comparability(
        reference=reference,
        intensified=intensified,
    )

    enhancement = apparent_enhancement_factor(
        intensified_rate_coefficient_s_inv=(
            intensified.apparent_rate_coefficient_s_inv
        ),
        reference_rate_coefficient_s_inv=(
            reference.apparent_rate_coefficient_s_inv
        ),
    )

    incremental_sulfur_g = (
        intensified.sulfur_excluded_from_product_g
        - reference.sulfur_excluded_from_product_g
    )
    incremental_energy_kwh = (
        intensified.measured_total_electrical_energy_kwh
        - reference.measured_total_electrical_energy_kwh
    )

    energy_normalized: float | None = None
    specific_energy_kwh_per_g: float | None = None
    specific_energy_kwh_per_kg: float | None = None
    incremental_energy_intensity: float | None = None

    if (
        incremental_sulfur_g > ZERO_TOLERANCE
        and incremental_energy_kwh > ZERO_TOLERANCE
    ):
        energy_normalized = (
            energy_normalized_incremental_sulfur(
                incremental_sulfur_g=incremental_sulfur_g,
                incremental_energy_kwh=incremental_energy_kwh,
            )
        )
        specific_energy_kwh_per_g = (
            incremental_specific_energy(
                incremental_energy_kwh=incremental_energy_kwh,
                incremental_sulfur_g=incremental_sulfur_g,
            )
        )
        specific_energy_kwh_per_kg = (
            specific_energy_kwh_per_g
            * 1000.0
        )
        incremental_energy_intensity = (
            incremental_energy_kwh
            / intensified.feed_volume_m3
        )

    return IncrementalComparisonResult(
        apparent_enhancement_factor=enhancement,
        incremental_sulfur_excluded_from_product_g=(
            incremental_sulfur_g
        ),
        incremental_electrical_energy_kwh=(
            incremental_energy_kwh
        ),
        energy_normalized_incremental_sulfur_g_per_kwh=(
            energy_normalized
        ),
        incremental_specific_energy_kwh_per_g_s=(
            specific_energy_kwh_per_g
        ),
        incremental_specific_energy_kwh_per_kg_s=(
            specific_energy_kwh_per_kg
        ),
        incremental_energy_intensity_kwh_m3=(
            incremental_energy_intensity
        ),
        outcome_statement=_outcome_statement(
            apparent_enhancement=enhancement,
            incremental_sulfur_g=incremental_sulfur_g,
            incremental_energy_kwh=incremental_energy_kwh,
        ),
        comparability_notes=assess_comparability(
            reference=reference,
            intensified=intensified,
        ),
    )


def desulfurization_case_from_store(
    store: ParameterStore,
    case_id: str,
) -> DesulfurizationCase:
    """Build one documented comparison case from the validated CSV."""
    return DesulfurizationCase(
        name=store.case_label(
            COMPARISON_EXAMPLE_ID,
            case_id,
        ),
        apparent_rate_coefficient_s_inv=store.value(
            COMPARISON_EXAMPLE_ID,
            case_id,
            "apparent_rate_coefficient_s_inv",
            expected_unit="s^-1",
        ),
        initial_sulfur_in_feed_g=store.value(
            COMPARISON_EXAMPLE_ID,
            case_id,
            "initial_sulfur_in_feed_g",
            expected_unit="g",
        ),
        sulfur_in_recovered_product_g=store.value(
            COMPARISON_EXAMPLE_ID,
            case_id,
            "sulfur_in_recovered_product_g",
            expected_unit="g",
        ),
        feed_volume_m3=store.value(
            COMPARISON_EXAMPLE_ID,
            case_id,
            "feed_volume_m3",
            expected_unit="m^3",
        ),
        treatment_time_s=store.value(
            COMPARISON_EXAMPLE_ID,
            case_id,
            "treatment_time_s",
            expected_unit="s",
        ),
        measured_total_electrical_energy_kwh=store.value(
            COMPARISON_EXAMPLE_ID,
            case_id,
            "measured_total_electrical_energy_kwh",
            expected_unit="kWh",
        ),
        initial_temperature_k=store.value(
            COMPARISON_EXAMPLE_ID,
            case_id,
            "initial_temperature_k",
            expected_unit="K",
        ),
        final_temperature_k=store.value(
            COMPARISON_EXAMPLE_ID,
            case_id,
            "final_temperature_k",
            expected_unit="K",
        ),
    )


def hydraulic_operating_point_from_store(
    store: ParameterStore,
) -> CavitationOperatingPoint:
    """Build the documented cavitation operating point from the CSV."""
    return CavitationOperatingPoint(
        upstream_pressure_abs_pa=store.value(
            HYDRAULICS_EXAMPLE_ID,
            HYDRAULICS_CASE_ID,
            "upstream_pressure_abs_pa",
            expected_unit="Pa",
        ),
        downstream_reference_pressure_abs_pa=store.value(
            HYDRAULICS_EXAMPLE_ID,
            HYDRAULICS_CASE_ID,
            "downstream_reference_pressure_abs_pa",
            expected_unit="Pa",
        ),
        vapor_pressure_pa=store.value(
            HYDRAULICS_EXAMPLE_ID,
            HYDRAULICS_CASE_ID,
            "vapor_pressure_pa",
            expected_unit="Pa",
        ),
        density_kg_m3=store.value(
            HYDRAULICS_EXAMPLE_ID,
            HYDRAULICS_CASE_ID,
            "density_kg_m3",
            expected_unit="kg/m^3",
        ),
        characteristic_velocity_m_s=store.value(
            HYDRAULICS_EXAMPLE_ID,
            HYDRAULICS_CASE_ID,
            "characteristic_velocity_m_s",
            expected_unit="m/s",
        ),
        loop_flow_rate_m3_s=store.value(
            HYDRAULICS_EXAMPLE_ID,
            HYDRAULICS_CASE_ID,
            "loop_flow_rate_m3_s",
            expected_unit="m^3/s",
        ),
        operating_time_s=store.value(
            HYDRAULICS_EXAMPLE_ID,
            HYDRAULICS_CASE_ID,
            "operating_time_s",
            expected_unit="s",
        ),
        pump_efficiency=store.value(
            HYDRAULICS_EXAMPLE_ID,
            HYDRAULICS_CASE_ID,
            "pump_efficiency",
            expected_unit="dimensionless",
        ),
        drive_efficiency=store.value(
            HYDRAULICS_EXAMPLE_ID,
            HYDRAULICS_CASE_ID,
            "drive_efficiency",
            expected_unit="dimensionless",
        ),
    )


def default_reference_case(
    store: ParameterStore | None = None,
) -> DesulfurizationCase:
    """Return the authoritative illustrative reference case."""
    parameter_store = (
        store
        if store is not None
        else load_default_parameter_store()
    )

    return desulfurization_case_from_store(
        parameter_store,
        REFERENCE_CASE_ID,
    )


def default_cavitation_case(
    store: ParameterStore | None = None,
) -> DesulfurizationCase:
    """Return the authoritative illustrative cavitation-assisted case."""
    parameter_store = (
        store
        if store is not None
        else load_default_parameter_store()
    )

    return desulfurization_case_from_store(
        parameter_store,
        CAVITATION_CASE_ID,
    )


def default_cavitation_operating_point(
    store: ParameterStore | None = None,
) -> CavitationOperatingPoint:
    """Return the authoritative illustrative hydraulic operating point."""
    parameter_store = (
        store
        if store is not None
        else load_default_parameter_store()
    )

    return hydraulic_operating_point_from_store(
        parameter_store
    )


def _format_optional(
    value: float | None,
    format_specification: str,
    undefined_text: str,
) -> str:
    """Format an optional metric without inventing a numerical value."""
    if value is None:
        return undefined_text

    return format(
        value,
        format_specification,
    )


def render_results(
    reference: DesulfurizationCase,
    intensified: DesulfurizationCase,
    hydraulics: CavitationOperatingPoint,
    comparison: IncrementalComparisonResult,
    parameter_source: str | Path | None = None,
) -> str:
    """Return a human-readable engineering-screening report."""
    if not _approximately_equal(
        hydraulics.operating_time_s,
        intensified.treatment_time_s,
    ):
        raise ValueError(
            "Hydraulic operating time must match the cavitation-case "
            "treatment time for this direct energy and turnover comparison."
        )

    nominal_inventory_turnovers = (
        hydraulics.nominal_inventory_turnovers(
            intensified.feed_volume_m3
        )
    )

    if (
        intensified.measured_total_electrical_energy_kwh
        > ZERO_TOLERANCE
    ):
        estimated_to_measured_energy_fraction: float | None = (
            hydraulics.estimated_electrical_energy_kwh
            / intensified.measured_total_electrical_energy_kwh
        )
    else:
        estimated_to_measured_energy_fraction = None

    lines = [
        "CAVITATION-ASSISTED DESULFURIZATION SCREENING",
        "=" * 78,
    ]

    if parameter_source is not None:
        lines.append(
            f"{'Authoritative input source':<44}: "
            f"{parameter_source}"
        )

    lines.extend(
        [
            "",
            "REFERENCE AND INTENSIFIED CASES",
            "-" * 78,
            (
                f"{'Reference case':<44}: "
                f"{reference.name}"
            ),
            (
                f"{'Cavitation-assisted case':<44}: "
                f"{intensified.name}"
            ),
            (
                f"{'Reference apparent coefficient':<44}: "
                f"{reference.apparent_rate_coefficient_s_inv:.3e} s^-1"
            ),
            (
                f"{'HC apparent coefficient':<44}: "
                f"{intensified.apparent_rate_coefficient_s_inv:.3e} s^-1"
            ),
            (
                f"{'Apparent enhancement factor':<44}: "
                f"{comparison.apparent_enhancement_factor:.4f}"
            ),
            "",
            "PRODUCT-BASED SULFUR ACCOUNTING",
            "-" * 78,
            (
                f"{'Initial sulfur basis, reference':<44}: "
                f"{reference.initial_sulfur_in_feed_g:.3f} g"
            ),
            (
                f"{'Initial sulfur basis, HC':<44}: "
                f"{intensified.initial_sulfur_in_feed_g:.3f} g"
            ),
            (
                f"{'Sulfur in recovered product, reference':<44}: "
                f"{reference.sulfur_in_recovered_product_g:.3f} g"
            ),
            (
                f"{'Sulfur in recovered product, HC':<44}: "
                f"{intensified.sulfur_in_recovered_product_g:.3f} g"
            ),
            (
                f"{'Sulfur excluded from product, reference':<44}: "
                f"{reference.sulfur_excluded_from_product_g:.3f} g"
            ),
            (
                f"{'Sulfur excluded from product, HC':<44}: "
                f"{intensified.sulfur_excluded_from_product_g:.3f} g"
            ),
            (
                f"{'Reference product sulfur reduction':<44}: "
                f"{100.0 * reference.product_sulfur_reduction_fraction:.2f} %"
            ),
            (
                f"{'HC product sulfur reduction':<44}: "
                f"{100.0 * intensified.product_sulfur_reduction_fraction:.2f} %"
            ),
            (
                f"{'Incremental product-based sulfur benefit':<44}: "
                f"{comparison.incremental_sulfur_excluded_from_product_g:.3f} g"
            ),
            "",
            "MEASURED ELECTRICAL ENERGY",
            "-" * 78,
            (
                f"{'Reference total electrical energy':<44}: "
                f"{reference.measured_total_electrical_energy_kwh:.4f} kWh"
            ),
            (
                f"{'HC total electrical energy':<44}: "
                f"{intensified.measured_total_electrical_energy_kwh:.4f} kWh"
            ),
            (
                f"{'Incremental electrical energy':<44}: "
                f"{comparison.incremental_electrical_energy_kwh:.4f} kWh"
            ),
            (
                f"{'Reference gross energy intensity':<44}: "
                f"{reference.gross_energy_intensity_kwh_m3:.4f} kWh/m^3"
            ),
            (
                f"{'HC gross energy intensity':<44}: "
                f"{intensified.gross_energy_intensity_kwh_m3:.4f} kWh/m^3"
            ),
            (
                f"{'Incremental energy intensity':<44}: "
                f"{_format_optional(comparison.incremental_energy_intensity_kwh_m3, '.4f', 'not applicable')} "
                f"{'kWh/m^3' if comparison.incremental_energy_intensity_kwh_m3 is not None else ''}"
            ).rstrip(),
            "",
            "INCREMENTAL ENERGY-NORMALIZED METRICS",
            "-" * 78,
            (
                f"{'Incremental sulfur per additional energy':<44}: "
                f"{_format_optional(comparison.energy_normalized_incremental_sulfur_g_per_kwh, '.4f', 'not applicable')} "
                f"{'g S/kWh' if comparison.energy_normalized_incremental_sulfur_g_per_kwh is not None else ''}"
            ).rstrip(),
            (
                f"{'Incremental specific energy':<44}: "
                f"{_format_optional(comparison.incremental_specific_energy_kwh_per_g_s, '.6f', 'not applicable')} "
                f"{'kWh/g S' if comparison.incremental_specific_energy_kwh_per_g_s is not None else ''}"
            ).rstrip(),
            (
                f"{'Incremental specific energy, kilogram basis':<44}: "
                f"{_format_optional(comparison.incremental_specific_energy_kwh_per_kg_s, '.3f', 'not applicable')} "
                f"{'kWh/kg S' if comparison.incremental_specific_energy_kwh_per_kg_s is not None else ''}"
            ).rstrip(),
            "",
            "CAVITATION HYDRAULIC CROSS-CHECK",
            "-" * 78,
            (
                f"{'Upstream absolute pressure':<44}: "
                f"{hydraulics.upstream_pressure_abs_pa:.3e} Pa"
            ),
            (
                f"{'Downstream reference absolute pressure':<44}: "
                f"{hydraulics.downstream_reference_pressure_abs_pa:.3e} Pa"
            ),
            (
                f"{'Pressure drop':<44}: "
                f"{hydraulics.pressure_drop_pa:.3e} Pa"
            ),
            (
                f"{'Loop flow rate':<44}: "
                f"{hydraulics.loop_flow_rate_m3_s:.3e} m^3/s"
            ),
            (
                f"{'Hydraulic power':<44}: "
                f"{hydraulics.hydraulic_power_w:.2f} W"
            ),
            (
                f"{'Estimated pump-drive electrical power':<44}: "
                f"{hydraulics.estimated_electrical_power_w:.2f} W"
            ),
            (
                f"{'Estimated pump-drive electrical energy':<44}: "
                f"{hydraulics.estimated_electrical_energy_kwh:.4f} kWh"
            ),
            (
                f"{'Estimated/measured HC energy fraction':<44}: "
                f"{_format_optional(estimated_to_measured_energy_fraction, '.4f', 'not applicable')}"
            ),
            (
                f"{'Cavitation number, stated definition':<44}: "
                f"{hydraulics.cavitation_number:.4f}"
            ),
            (
                f"{'Nominal feed-volume turnovers':<44}: "
                f"{nominal_inventory_turnovers:.2f}"
            ),
            "",
            "COMPARABILITY CHECK",
            "-" * 78,
        ]
    )

    lines.extend(
        f"- {note}"
        for note in comparison.comparability_notes
    )

    lines.extend(
        [
            "",
            "SCREENING OUTCOME",
            "-" * 78,
            comparison.outcome_statement,
            "",
            "Scientific interpretation:",
            (
                "The apparent enhancement factor compares fitted apparent "
                "coefficients only. It does not prove intrinsic kinetic "
                "enhancement or identify a cavitation mechanism."
            ),
            (
                "The product-based sulfur metric is not a complete sulfur "
                "balance. Final validation must quantify sulfur in the "
                "product, aqueous and solvent phases, gas, solids, catalyst "
                "or adsorbent, deposits, samples, and losses."
            ),
            (
                "The hydraulic estimate covers the stated pressure-drop "
                "boundary and assumed pump-drive efficiencies. Measured "
                "total electrical energy remains the preferred basis when "
                "it covers the complete declared process boundary."
            ),
            (
                "The cavitation number is a hydrodynamic descriptor, not a "
                "direct measure of radical generation, chemical performance, "
                "erosion, or industrial usefulness."
            ),
            (
                "A defensible study should include a non-cavitating "
                "hydrodynamic control and a matched thermal control because "
                "pressure drop, recirculation, mixing, and temperature rise "
                "can independently change apparent desulfurization."
            ),
            "",
            "Required validation before engineering use:",
            (
                "Establish sulfur-balance closure, sulfur speciation, "
                "analytical uncertainty, equivalent product recovery, "
                "oxidant utilization, downstream separation, measured energy, "
                "temperature history, pressure and flow definitions, erosion, "
                "corrosion, fouling, emulsion behavior, durability, safety, "
                "and pilot-scale transferability."
            ),
            "",
            "Evidence status:",
            "E3 engineering-screening research prototype.",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    """Load, validate, and evaluate the illustrative repository cases."""
    store = load_default_parameter_store()

    reference = desulfurization_case_from_store(
        store,
        REFERENCE_CASE_ID,
    )
    intensified = desulfurization_case_from_store(
        store,
        CAVITATION_CASE_ID,
    )
    hydraulics = hydraulic_operating_point_from_store(
        store
    )

    comparison = compare_cases(
        reference=reference,
        intensified=intensified,
    )

    print(
        render_results(
            reference=reference,
            intensified=intensified,
            hydraulics=hydraulics,
            comparison=comparison,
            parameter_source=store.source_path,
        )
    )


if __name__ == "__main__":
    main()
