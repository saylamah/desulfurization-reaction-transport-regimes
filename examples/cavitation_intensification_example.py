"""
Cavitation-assisted desulfurization intensification screening example.

This module compares a hydrodynamic-cavitation-assisted case with a defined
reference case using product-based sulfur reduction, apparent-rate
enhancement, measured energy demand, hydraulic cross-checks, and one common
cavitation-number definition.

The script deliberately distinguishes among:

* gross sulfur excluded from the recovered product;
* incremental sulfur benefit relative to a reference;
* gross electrical energy for each case;
* incremental electrical energy relative to the reference;
* hydraulic power across the cavitating device;
* estimated pump-drive electrical demand;
* apparent kinetic enhancement;
* evidence of cavitation occurrence;
* evidence of useful overall process performance.

Scientific scope
----------------
The calculations are screening relationships, not a mechanistic cavitation
model. The example assumes that the reference and intensified cases use
equivalent feed, treatment time, thermal history, analytical method,
separation boundary, and product-recovery basis.

The product-based sulfur metric used here is:

    sulfur in feed - sulfur in recovered product

It is not a complete sulfur balance. Sulfur may remain in solvent, water,
gas, solids, catalyst, adsorbent, deposits, lost hydrocarbon, or unmeasured
products. Complete validation therefore requires sulfur accounting across
all relevant phases and deposits.

The apparent-rate coefficients are comparison metrics only. They must not be
interpreted as intrinsic kinetic constants unless external transfer, internal
diffusion, hydrodynamics, deactivation, reactant depletion, and separation
effects have been excluded.

The cavitation number implemented here is one commonly used form:

    sigma = (p_ref - p_v) / (0.5 * rho * v**2)

Its value depends on the selected pressure location, absolute-pressure basis,
velocity definition, temperature-dependent vapor pressure, fluid properties,
and device geometry. Equal cavitation number does not guarantee equal cavity
dynamics, erosion, chemical effect, or scale-up behavior.

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


JOULES_PER_KWH = 3.6e6
ZERO_TOLERANCE = 1.0e-12


@dataclass(frozen=True, slots=True)
class DesulfurizationCase:
    """Measured basis for one desulfurization case.

    Parameters
    ----------
    name:
        Human-readable case identifier.
    apparent_rate_coefficient_s_inv:
        Apparent pseudo-first-order coefficient, s^-1. This is a comparison
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
        Measured total electrical energy within the stated process boundary,
        kWh. This may include pumping and other declared auxiliaries.
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
        return self.final_temperature_k - self.initial_temperature_k

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
    implemented cavitation-number expression. Another study may use a
    different pressure location, but it must state that definition explicitly.
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

    @property
    def pressure_drop_pa(self) -> float:
        """Return pressure drop across the defined device boundary, Pa."""
        return (
            self.upstream_pressure_abs_pa
            - self.downstream_reference_pressure_abs_pa
        )

    @property
    def hydraulic_power_w(self) -> float:
        """Return hydraulic power dissipated across the device, W."""
        return self.pressure_drop_pa * self.loop_flow_rate_m3_s

    @property
    def estimated_electrical_power_w(self) -> float:
        """Return pump-drive electrical power estimated from efficiencies."""
        return self.hydraulic_power_w / (
            self.pump_efficiency * self.drive_efficiency
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
        """Return one commonly used cavitation-number definition."""
        dynamic_pressure_pa = (
            0.5
            * self.density_kg_m3
            * self.characteristic_velocity_m_s**2
        )

        return (
            self.downstream_reference_pressure_abs_pa
            - self.vapor_pressure_pa
        ) / dynamic_pressure_pa

    def nominal_passes(self, liquid_inventory_m3: float) -> float:
        """Return nominal loop throughput divided by liquid inventory.

        This is not the pass count experienced by every fluid element.
        A recirculating system has a pass distribution governed by mixing
        and residence-time behavior.
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


def _require_finite_positive(name: str, value: float) -> None:
    """Require a finite value strictly greater than zero."""
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and greater than zero.")


def _require_finite_nonnegative(name: str, value: float) -> None:
    """Require a finite value greater than or equal to zero."""
    if not math.isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be finite and non-negative.")


def _require_efficiency(name: str, value: float) -> None:
    """Require a finite fractional efficiency in the interval (0, 1]."""
    if not math.isfinite(value) or not 0.0 < value <= 1.0:
        raise ValueError(
            f"{name} must be finite and satisfy 0 < {name} <= 1."
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
    sulfur benefit or for zero or negative incremental energy. Those cases
    require direct interpretation rather than a misleading ratio.
    """
    _require_finite_positive(
        "incremental_sulfur_g",
        incremental_sulfur_g,
    )
    _require_finite_positive(
        "incremental_energy_kwh",
        incremental_energy_kwh,
    )

    return incremental_sulfur_g / incremental_energy_kwh


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

    return incremental_energy_kwh / incremental_sulfur_g


def _approximately_equal(
    first: float,
    second: float,
    *,
    relative_tolerance: float = 1.0e-6,
    absolute_tolerance: float = 1.0e-12,
) -> bool:
    """Return whether two comparison-basis values are numerically equivalent."""
    return math.isclose(
        first,
        second,
        rel_tol=relative_tolerance,
        abs_tol=absolute_tolerance,
    )


def assess_comparability(
    reference: DesulfurizationCase,
    intensified: DesulfurizationCase,
) -> tuple[str, ...]:
    """Return explicit notes about non-equivalent comparison conditions."""
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
        if not _approximately_equal(reference_value, intensified_value):
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
        energy_normalized = energy_normalized_incremental_sulfur(
            incremental_sulfur_g=incremental_sulfur_g,
            incremental_energy_kwh=incremental_energy_kwh,
        )
        specific_energy_kwh_per_g = incremental_specific_energy(
            incremental_energy_kwh=incremental_energy_kwh,
            incremental_sulfur_g=incremental_sulfur_g,
        )
        specific_energy_kwh_per_kg = (
            specific_energy_kwh_per_g * 1000.0
        )
        incremental_energy_intensity = (
            incremental_energy_kwh / intensified.feed_volume_m3
        )

    return IncrementalComparisonResult(
        apparent_enhancement_factor=enhancement,
        incremental_sulfur_excluded_from_product_g=(
            incremental_sulfur_g
        ),
        incremental_electrical_energy_kwh=incremental_energy_kwh,
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


def default_reference_case() -> DesulfurizationCase:
    """Return the illustrative non-cavitating reference case."""
    return DesulfurizationCase(
        name="Illustrative non-cavitating reference",
        apparent_rate_coefficient_s_inv=4.0e-3,
        initial_sulfur_in_feed_g=6.0,
        sulfur_in_recovered_product_g=4.0,
        feed_volume_m3=2.0e-1,
        treatment_time_s=1800.0,
        measured_total_electrical_energy_kwh=2.5e-1,
        initial_temperature_k=298.15,
        final_temperature_k=300.15,
    )


def default_cavitation_case() -> DesulfurizationCase:
    """Return the illustrative cavitation-assisted case."""
    return DesulfurizationCase(
        name="Illustrative cavitation-assisted case",
        apparent_rate_coefficient_s_inv=1.2e-2,
        initial_sulfur_in_feed_g=6.0,
        sulfur_in_recovered_product_g=5.0e-1,
        feed_volume_m3=2.0e-1,
        treatment_time_s=1800.0,
        measured_total_electrical_energy_kwh=1.0,
        initial_temperature_k=298.15,
        final_temperature_k=300.15,
    )


def default_cavitation_operating_point() -> CavitationOperatingPoint:
    """Return illustrative hydraulic data for the cavitation case."""
    return CavitationOperatingPoint(
        upstream_pressure_abs_pa=5.5e5,
        downstream_reference_pressure_abs_pa=1.5e5,
        vapor_pressure_pa=3.17e3,
        density_kg_m3=8.30e2,
        characteristic_velocity_m_s=25.0,
        loop_flow_rate_m3_s=2.0e-3,
        operating_time_s=1800.0,
        pump_efficiency=0.70,
        drive_efficiency=0.90,
    )


def _format_optional(
    value: float | None,
    format_specification: str,
    undefined_text: str,
) -> str:
    """Format an optional metric without inventing a numerical value."""
    if value is None:
        return undefined_text

    return format(value, format_specification)


def render_results(
    reference: DesulfurizationCase,
    intensified: DesulfurizationCase,
    hydraulics: CavitationOperatingPoint,
    comparison: IncrementalComparisonResult,
) -> str:
    """Return a human-readable engineering-screening report."""
    nominal_passes = hydraulics.nominal_passes(
        intensified.feed_volume_m3
    )

    estimated_to_measured_energy_fraction = (
        hydraulics.estimated_electrical_energy_kwh
        / intensified.measured_total_electrical_energy_kwh
        if intensified.measured_total_electrical_energy_kwh > 0.0
        else None
    )

    lines = [
        "CAVITATION-ASSISTED DESULFURIZATION SCREENING",
        "=" * 72,
        "REFERENCE AND INTENSIFIED CASES",
        "-" * 72,
        (
            f"{'Reference case':<39}: "
            f"{reference.name}"
        ),
        (
            f"{'Cavitation-assisted case':<39}: "
            f"{intensified.name}"
        ),
        (
            f"{'Reference apparent coefficient':<39}: "
            f"{reference.apparent_rate_coefficient_s_inv:.3e} s^-1"
        ),
        (
            f"{'HC apparent coefficient':<39}: "
            f"{intensified.apparent_rate_coefficient_s_inv:.3e} s^-1"
        ),
        (
            f"{'Apparent enhancement factor':<39}: "
            f"{comparison.apparent_enhancement_factor:.4f}"
        ),
        "",
        "PRODUCT-BASED SULFUR ACCOUNTING",
        "-" * 72,
        (
            f"{'Initial sulfur basis, reference':<39}: "
            f"{reference.initial_sulfur_in_feed_g:.3f} g"
        ),
        (
            f"{'Initial sulfur basis, HC':<39}: "
            f"{intensified.initial_sulfur_in_feed_g:.3f} g"
        ),
        (
            f"{'Sulfur in recovered product, reference':<39}: "
            f"{reference.sulfur_in_recovered_product_g:.3f} g"
        ),
        (
            f"{'Sulfur in recovered product, HC':<39}: "
            f"{intensified.sulfur_in_recovered_product_g:.3f} g"
        ),
        (
            f"{'Sulfur excluded from product, reference':<39}: "
            f"{reference.sulfur_excluded_from_product_g:.3f} g"
        ),
        (
            f"{'Sulfur excluded from product, HC':<39}: "
            f"{intensified.sulfur_excluded_from_product_g:.3f} g"
        ),
        (
            f"{'Reference product sulfur reduction':<39}: "
            f"{100.0 * reference.product_sulfur_reduction_fraction:.2f} %"
        ),
        (
            f"{'HC product sulfur reduction':<39}: "
            f"{100.0 * intensified.product_sulfur_reduction_fraction:.2f} %"
        ),
        (
            f"{'Incremental product-based sulfur benefit':<39}: "
            f"{comparison.incremental_sulfur_excluded_from_product_g:.3f} g"
        ),
        "",
        "MEASURED ELECTRICAL ENERGY",
        "-" * 72,
        (
            f"{'Reference total electrical energy':<39}: "
            f"{reference.measured_total_electrical_energy_kwh:.4f} kWh"
        ),
        (
            f"{'HC total electrical energy':<39}: "
            f"{intensified.measured_total_electrical_energy_kwh:.4f} kWh"
        ),
        (
            f"{'Incremental electrical energy':<39}: "
            f"{comparison.incremental_electrical_energy_kwh:.4f} kWh"
        ),
        (
            f"{'Reference gross energy intensity':<39}: "
            f"{reference.gross_energy_intensity_kwh_m3:.4f} kWh/m^3"
        ),
        (
            f"{'HC gross energy intensity':<39}: "
            f"{intensified.gross_energy_intensity_kwh_m3:.4f} kWh/m^3"
        ),
        (
            f"{'Incremental energy intensity':<39}: "
            f"{_format_optional(comparison.incremental_energy_intensity_kwh_m3, '.4f', 'not applicable')} "
            f"{'kWh/m^3' if comparison.incremental_energy_intensity_kwh_m3 is not None else ''}"
        ).rstrip(),
        "",
        "INCREMENTAL ENERGY-NORMALIZED METRICS",
        "-" * 72,
        (
            f"{'Incremental sulfur per additional energy':<39}: "
            f"{_format_optional(comparison.energy_normalized_incremental_sulfur_g_per_kwh, '.4f', 'not applicable')} "
            f"{'g S/kWh' if comparison.energy_normalized_incremental_sulfur_g_per_kwh is not None else ''}"
        ).rstrip(),
        (
            f"{'Incremental specific energy':<39}: "
            f"{_format_optional(comparison.incremental_specific_energy_kwh_per_g_s, '.6f', 'not applicable')} "
            f"{'kWh/g S' if comparison.incremental_specific_energy_kwh_per_g_s is not None else ''}"
        ).rstrip(),
        (
            f"{'Incremental specific energy':<39}: "
            f"{_format_optional(comparison.incremental_specific_energy_kwh_per_kg_s, '.3f', 'not applicable')} "
            f"{'kWh/kg S' if comparison.incremental_specific_energy_kwh_per_kg_s is not None else ''}"
        ).rstrip(),
        "",
        "CAVITATION HYDRAULIC CROSS-CHECK",
        "-" * 72,
        (
            f"{'Upstream absolute pressure':<39}: "
            f"{hydraulics.upstream_pressure_abs_pa:.3e} Pa"
        ),
        (
            f"{'Downstream reference absolute pressure':<39}: "
            f"{hydraulics.downstream_reference_pressure_abs_pa:.3e} Pa"
        ),
        (
            f"{'Pressure drop':<39}: "
            f"{hydraulics.pressure_drop_pa:.3e} Pa"
        ),
        (
            f"{'Loop flow rate':<39}: "
            f"{hydraulics.loop_flow_rate_m3_s:.3e} m^3/s"
        ),
        (
            f"{'Hydraulic power':<39}: "
            f"{hydraulics.hydraulic_power_w:.2f} W"
        ),
        (
            f"{'Estimated pump-drive electrical power':<39}: "
            f"{hydraulics.estimated_electrical_power_w:.2f} W"
        ),
        (
            f"{'Estimated pump-drive electrical energy':<39}: "
            f"{hydraulics.estimated_electrical_energy_kwh:.4f} kWh"
        ),
        (
            f"{'Estimated/measured HC energy fraction':<39}: "
            f"{_format_optional(estimated_to_measured_energy_fraction, '.4f', 'not applicable')}"
        ),
        (
            f"{'Cavitation number, stated definition':<39}: "
            f"{hydraulics.cavitation_number:.4f}"
        ),
        (
            f"{'Nominal recirculation passes':<39}: "
            f"{nominal_passes:.2f}"
        ),
        "",
        "COMPARABILITY CHECK",
        "-" * 72,
    ]

    lines.extend(
        f"- {note}" for note in comparison.comparability_notes
    )

    lines.extend(
        [
            "",
            "SCREENING OUTCOME",
            "-" * 72,
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
                "boundary and assumed pump-drive efficiencies. The measured "
                "total electrical energy remains the preferred basis when "
                "it includes the complete declared process boundary."
            ),
            (
                "The cavitation number is a hydrodynamic descriptor, not a "
                "direct measure of radical generation, chemical performance, "
                "erosion, or industrial usefulness."
            ),
            (
                "A defensible study should include a non-cavitating "
                "hydrodynamic control and a matched thermal control, because "
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
    """Run the illustrative repository example."""
    reference = default_reference_case()
    intensified = default_cavitation_case()
    hydraulics = default_cavitation_operating_point()

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
        )
    )


if __name__ == "__main__":
    main()
