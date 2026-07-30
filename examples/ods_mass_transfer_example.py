"""
ODS reaction-mass-transfer regime screening example.

This module compares a pseudo-first-order reaction coefficient with an
effective first-order interphase-transfer coefficient for a simplified
multiphase oxidative desulfurization system.

The script calculates:

* a reaction-to-transfer diagnostic ratio;
* characteristic reaction and transfer times;
* an overall coefficient for two linear sequential resistances;
* the fractional contribution of each modeled resistance;
* a qualitative regime statement;
* the response to equal proportional improvements in reaction and transfer.

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
The screening model assumes:

* one effective chemical-reaction step;
* one effective interphase-transfer step;
* linear or appropriately linearized sequential resistances;
* pseudo-first-order behavior over the evaluated interval;
* constant reaction and transfer coefficients;
* constant effective interfacial area;
* compatible concentration and phase-volume bases;
* no catalyst deactivation;
* no oxidant depletion;
* no thermal limitation;
* no residence-time-distribution effects;
* no explicit downstream separation limitation.

The effective transfer coefficient must represent the relevant transported
species and use a basis compatible with the reaction coefficient.

Depending on the physical ODS system, the transported quantity may involve:

* an organosulfur compound;
* oxidant;
* catalyst precursor;
* reactive intermediate;
* oxidation product.

Partition equilibrium, phase-volume ratio, chemical enhancement, and any
required concentration-basis conversion must be incorporated consistently
before the coefficient is used in this simplified model.

The implemented diagnostic ratio is not a universal Damkohler-number
definition. Real multiphase ODS systems may involve multiple transfer steps,
interfacial reaction, changing droplet size, catalyst partitioning, oxidant
decomposition, emulsification, and downstream extraction or adsorption.

The numerical values are illustrative. They are not validated design data for
a specific feed, catalyst, oxidant, reactor, or industrial ODS process.

Evidence status
---------------
E3 -- executable engineering-screening research prototype.

Reference framework
-------------------
Reaction-Transport Regime Analysis for Desulfurization of Gas and Petroleum
Streams: An Engineering Diagnostic Framework.
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


EXAMPLE_ID = "ods_reaction_transfer"
CASE_ID = "ods_default"


@dataclass(frozen=True, slots=True)
class ODSReactionTransferCase:
    """Inputs for the simplified reaction-transfer screening model.

    Parameters
    ----------
    name:
        Human-readable case identifier.
    reaction_coefficient_s_inv:
        Pseudo-first-order reaction coefficient, s^-1.

        It must represent chemical transformation on the same concentration
        and phase-volume basis used for the effective transfer coefficient.
    effective_transfer_coefficient_s_inv:
        Effective first-order interphase-transfer coefficient, s^-1.

        This may be based on a volumetric coefficient such as kLa only after
        equilibrium, partitioning, phase-volume, and concentration-basis
        effects have been handled consistently.
    dominance_fraction:
        Fraction of total modeled resistance required before one contribution
        is described as dominant.

        This is an explicit screening convention, not a universal physical
        threshold.
    sensitivity_factor:
        Multiplicative factor used to compare equal proportional improvements
        in reaction and transfer coefficients.
    """

    name: str
    reaction_coefficient_s_inv: float
    effective_transfer_coefficient_s_inv: float
    dominance_fraction: float
    sensitivity_factor: float

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Case name must not be empty.")

        _require_finite_positive(
            "reaction_coefficient_s_inv",
            self.reaction_coefficient_s_inv,
        )
        _require_finite_positive(
            "effective_transfer_coefficient_s_inv",
            self.effective_transfer_coefficient_s_inv,
        )

        if (
            not math.isfinite(self.dominance_fraction)
            or not 0.50 < self.dominance_fraction < 1.00
        ):
            raise ValueError(
                "dominance_fraction must be finite and satisfy "
                "0.50 < dominance_fraction < 1.00."
            )

        if (
            not math.isfinite(self.sensitivity_factor)
            or self.sensitivity_factor <= 1.0
        ):
            raise ValueError(
                "sensitivity_factor must be finite and greater than 1.0."
            )


@dataclass(frozen=True, slots=True)
class ODSReactionTransferResult:
    """Calculated reaction-transfer screening quantities."""

    diagnostic_ratio: float
    reaction_time_s: float
    transfer_time_s: float
    overall_time_s: float
    overall_coefficient_s_inv: float
    reaction_resistance_fraction: float
    transfer_resistance_fraction: float
    screening_statement: str
    reaction_improved_overall_coefficient_s_inv: float
    transfer_improved_overall_coefficient_s_inv: float
    reaction_improvement_gain_percent: float
    transfer_improvement_gain_percent: float


def _require_finite_positive(name: str, value: float) -> None:
    """Require a finite numerical value strictly greater than zero."""
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(
            f"{name} must be finite and greater than zero."
        )


def diagnostic_reaction_to_transfer_ratio(
    reaction_coefficient_s_inv: float,
    effective_transfer_coefficient_s_inv: float,
) -> float:
    """Return the reaction-to-transfer diagnostic ratio.

    The implemented relationship is:

        Da_diag = k_rxn / k_mt,eff

    Using characteristic times:

        tau_rxn = 1 / k_rxn
        tau_mt  = 1 / k_mt,eff

    therefore:

        Da_diag = tau_mt / tau_rxn

    The ratio is dimensionless only when both coefficients are expressed as
    compatible first-order quantities on the same concentration and
    phase-volume basis.
    """
    _require_finite_positive(
        "reaction_coefficient_s_inv",
        reaction_coefficient_s_inv,
    )
    _require_finite_positive(
        "effective_transfer_coefficient_s_inv",
        effective_transfer_coefficient_s_inv,
    )

    return (
        reaction_coefficient_s_inv
        / effective_transfer_coefficient_s_inv
    )


def characteristic_time_s(
    coefficient_s_inv: float,
) -> float:
    """Return the characteristic time of a first-order coefficient."""
    _require_finite_positive(
        "coefficient_s_inv",
        coefficient_s_inv,
    )

    return 1.0 / coefficient_s_inv


def series_overall_coefficient(
    reaction_coefficient_s_inv: float,
    effective_transfer_coefficient_s_inv: float,
) -> float:
    """Return the coefficient for two linear sequential resistances.

    The implemented relationship is:

        1 / k_overall = 1 / k_rxn + 1 / k_mt,eff

    This relationship is valid only as a linear screening approximation.

    It does not automatically apply to:

    * nonlinear kinetics;
    * parallel pathways;
    * interfacial reaction;
    * changing interfacial area;
    * multiple coupled transfer steps;
    * transient partition equilibrium;
    * reactive extraction;
    * changing oxidant concentration.
    """
    reaction_time_s = characteristic_time_s(
        reaction_coefficient_s_inv
    )
    transfer_time_s = characteristic_time_s(
        effective_transfer_coefficient_s_inv
    )

    return 1.0 / (
        reaction_time_s + transfer_time_s
    )


def resistance_fractions(
    reaction_coefficient_s_inv: float,
    effective_transfer_coefficient_s_inv: float,
) -> tuple[float, float]:
    """Return modeled reaction and transfer resistance fractions.

    In the linear sequential-resistance model:

        R_rxn is proportional to 1 / k_rxn
        R_mt  is proportional to 1 / k_mt,eff

    The returned fractions sum to one.

    These fractions represent contributions within the simplified model.
    They are not direct experimental measurements of physical resistance.
    """
    reaction_time_s = characteristic_time_s(
        reaction_coefficient_s_inv
    )
    transfer_time_s = characteristic_time_s(
        effective_transfer_coefficient_s_inv
    )

    total_time_s = (
        reaction_time_s + transfer_time_s
    )

    reaction_fraction = (
        reaction_time_s / total_time_s
    )
    transfer_fraction = (
        transfer_time_s / total_time_s
    )

    return reaction_fraction, transfer_fraction


def classify_regime(
    reaction_resistance_fraction: float,
    transfer_resistance_fraction: float,
    dominance_fraction: float,
) -> str:
    """Return a transparent qualitative regime statement.

    Classification is based on the modeled resistance fractions rather than
    on universal Damkohler-number thresholds.

    The selected dominance fraction is an engineering-screening convention.
    It must be stated explicitly and should be changed only with documented
    project-specific justification.
    """
    for name, value in (
        (
            "reaction_resistance_fraction",
            reaction_resistance_fraction,
        ),
        (
            "transfer_resistance_fraction",
            transfer_resistance_fraction,
        ),
    ):
        if (
            not math.isfinite(value)
            or value < 0.0
            or value > 1.0
        ):
            raise ValueError(
                f"{name} must be finite and between zero and one."
            )

    if not math.isclose(
        reaction_resistance_fraction
        + transfer_resistance_fraction,
        1.0,
        rel_tol=1.0e-12,
        abs_tol=1.0e-12,
    ):
        raise ValueError(
            "Reaction and transfer resistance fractions must sum to one."
        )

    if (
        not math.isfinite(dominance_fraction)
        or not 0.50 < dominance_fraction < 1.00
    ):
        raise ValueError(
            "dominance_fraction must be finite and satisfy "
            "0.50 < dominance_fraction < 1.00."
        )

    if reaction_resistance_fraction >= dominance_fraction:
        return (
            "Reaction-dominated tendency in the simplified "
            "two-resistance model"
        )

    if transfer_resistance_fraction >= dominance_fraction:
        return (
            "External-transfer-dominated tendency in the simplified "
            "two-resistance model"
        )

    return (
        "Mixed reaction-transfer control in the simplified "
        "two-resistance model"
    )


def relative_gain_percent(
    baseline_value: float,
    modified_value: float,
) -> float:
    """Return the percentage increase from a positive baseline."""
    _require_finite_positive(
        "baseline_value",
        baseline_value,
    )
    _require_finite_positive(
        "modified_value",
        modified_value,
    )

    return (
        modified_value / baseline_value - 1.0
    ) * 100.0


def evaluate_case(
    case: ODSReactionTransferCase,
) -> ODSReactionTransferResult:
    """Evaluate one simplified ODS reaction-transfer case."""
    reaction_time_s = characteristic_time_s(
        case.reaction_coefficient_s_inv
    )
    transfer_time_s = characteristic_time_s(
        case.effective_transfer_coefficient_s_inv
    )
    overall_time_s = (
        reaction_time_s + transfer_time_s
    )

    diagnostic_ratio = (
        diagnostic_reaction_to_transfer_ratio(
            reaction_coefficient_s_inv=(
                case.reaction_coefficient_s_inv
            ),
            effective_transfer_coefficient_s_inv=(
                case.effective_transfer_coefficient_s_inv
            ),
        )
    )

    overall_coefficient_s_inv = (
        series_overall_coefficient(
            reaction_coefficient_s_inv=(
                case.reaction_coefficient_s_inv
            ),
            effective_transfer_coefficient_s_inv=(
                case.effective_transfer_coefficient_s_inv
            ),
        )
    )

    (
        reaction_resistance_fraction,
        transfer_resistance_fraction,
    ) = resistance_fractions(
        reaction_coefficient_s_inv=(
            case.reaction_coefficient_s_inv
        ),
        effective_transfer_coefficient_s_inv=(
            case.effective_transfer_coefficient_s_inv
        ),
    )

    reaction_improved_overall_coefficient_s_inv = (
        series_overall_coefficient(
            reaction_coefficient_s_inv=(
                case.reaction_coefficient_s_inv
                * case.sensitivity_factor
            ),
            effective_transfer_coefficient_s_inv=(
                case.effective_transfer_coefficient_s_inv
            ),
        )
    )

    transfer_improved_overall_coefficient_s_inv = (
        series_overall_coefficient(
            reaction_coefficient_s_inv=(
                case.reaction_coefficient_s_inv
            ),
            effective_transfer_coefficient_s_inv=(
                case.effective_transfer_coefficient_s_inv
                * case.sensitivity_factor
            ),
        )
    )

    return ODSReactionTransferResult(
        diagnostic_ratio=diagnostic_ratio,
        reaction_time_s=reaction_time_s,
        transfer_time_s=transfer_time_s,
        overall_time_s=overall_time_s,
        overall_coefficient_s_inv=(
            overall_coefficient_s_inv
        ),
        reaction_resistance_fraction=(
            reaction_resistance_fraction
        ),
        transfer_resistance_fraction=(
            transfer_resistance_fraction
        ),
        screening_statement=classify_regime(
            reaction_resistance_fraction=(
                reaction_resistance_fraction
            ),
            transfer_resistance_fraction=(
                transfer_resistance_fraction
            ),
            dominance_fraction=(
                case.dominance_fraction
            ),
        ),
        reaction_improved_overall_coefficient_s_inv=(
            reaction_improved_overall_coefficient_s_inv
        ),
        transfer_improved_overall_coefficient_s_inv=(
            transfer_improved_overall_coefficient_s_inv
        ),
        reaction_improvement_gain_percent=(
            relative_gain_percent(
                baseline_value=(
                    overall_coefficient_s_inv
                ),
                modified_value=(
                    reaction_improved_overall_coefficient_s_inv
                ),
            )
        ),
        transfer_improvement_gain_percent=(
            relative_gain_percent(
                baseline_value=(
                    overall_coefficient_s_inv
                ),
                modified_value=(
                    transfer_improved_overall_coefficient_s_inv
                ),
            )
        ),
    )


def case_from_parameter_store(
    store: ParameterStore,
) -> ODSReactionTransferCase:
    """Build the documented ODS case from the validated CSV dataset."""
    return ODSReactionTransferCase(
        name=store.case_label(
            EXAMPLE_ID,
            CASE_ID,
        ),
        reaction_coefficient_s_inv=store.value(
            EXAMPLE_ID,
            CASE_ID,
            "reaction_coefficient_s_inv",
            expected_unit="s^-1",
        ),
        effective_transfer_coefficient_s_inv=store.value(
            EXAMPLE_ID,
            CASE_ID,
            "effective_transfer_coefficient_s_inv",
            expected_unit="s^-1",
        ),
        dominance_fraction=store.value(
            EXAMPLE_ID,
            CASE_ID,
            "dominance_fraction",
            expected_unit="dimensionless",
        ),
        sensitivity_factor=store.value(
            EXAMPLE_ID,
            CASE_ID,
            "sensitivity_factor",
            expected_unit="dimensionless",
        ),
    )


def default_case(
    store: ParameterStore | None = None,
) -> ODSReactionTransferCase:
    """Return the authoritative illustrative ODS case.

    When no store is supplied, the repository CSV is loaded and validated.
    """
    parameter_store = (
        store
        if store is not None
        else load_default_parameter_store()
    )

    return case_from_parameter_store(
        parameter_store
    )


def render_results(
    case: ODSReactionTransferCase,
    result: ODSReactionTransferResult,
    parameter_source: str | Path | None = None,
) -> str:
    """Return a human-readable engineering-screening report."""
    dominance_percent = (
        case.dominance_fraction * 100.0
    )

    lines = [
        "ODS REACTION-TRANSFER REGIME SCREENING",
        "=" * 72,
        f"{'Case':<39}: {case.name}",
    ]

    if parameter_source is not None:
        lines.append(
            f"{'Authoritative input source':<39}: "
            f"{parameter_source}"
        )

    lines.extend(
        [
            (
                f"{'Reaction coefficient':<39}: "
                f"{case.reaction_coefficient_s_inv:.3e} s^-1"
            ),
            (
                f"{'Effective transfer coefficient':<39}: "
                f"{case.effective_transfer_coefficient_s_inv:.3e} s^-1"
            ),
            (
                f"{'Selected dominance criterion':<39}: "
                f"{dominance_percent:.1f} % of modeled resistance"
            ),
            (
                f"{'Sensitivity multiplication factor':<39}: "
                f"{case.sensitivity_factor:.2f}"
            ),
            "-" * 72,
            (
                f"{'Reaction characteristic time':<39}: "
                f"{result.reaction_time_s:.2f} s"
            ),
            (
                f"{'Transfer characteristic time':<39}: "
                f"{result.transfer_time_s:.2f} s"
            ),
            (
                f"{'Overall characteristic time':<39}: "
                f"{result.overall_time_s:.2f} s"
            ),
            (
                f"{'Diagnostic ratio, k_rxn/k_mt':<39}: "
                f"{result.diagnostic_ratio:.4f}"
            ),
            (
                f"{'Overall series coefficient':<39}: "
                f"{result.overall_coefficient_s_inv:.4e} s^-1"
            ),
            (
                f"{'Reaction resistance contribution':<39}: "
                f"{100.0 * result.reaction_resistance_fraction:.2f} %"
            ),
            (
                f"{'Transfer resistance contribution':<39}: "
                f"{100.0 * result.transfer_resistance_fraction:.2f} %"
            ),
            (
                f"{'Screening statement':<39}: "
                f"{result.screening_statement}"
            ),
            "",
            "EQUAL-FACTOR SENSITIVITY COMPARISON",
            "-" * 72,
            (
                f"Multiplying the reaction coefficient by "
                f"{case.sensitivity_factor:.2f} changes the modeled "
                f"overall coefficient to "
                f"{result.reaction_improved_overall_coefficient_s_inv:.4e} "
                f"s^-1."
            ),
            (
                f"Predicted overall-coefficient gain from reaction "
                f"improvement: "
                f"{result.reaction_improvement_gain_percent:.2f} %."
            ),
            "",
            (
                f"Multiplying the transfer coefficient by "
                f"{case.sensitivity_factor:.2f} changes the modeled "
                f"overall coefficient to "
                f"{result.transfer_improved_overall_coefficient_s_inv:.4e} "
                f"s^-1."
            ),
            (
                f"Predicted overall-coefficient gain from transfer "
                f"improvement: "
                f"{result.transfer_improvement_gain_percent:.2f} %."
            ),
            "",
            "Scientific interpretation:",
            (
                "For this illustrative case, the effective transfer step "
                "contributes the larger fraction of the modeled total "
                "resistance."
            ),
            (
                "Under the stated linear sequential-resistance assumptions, "
                "an equal proportional improvement in transfer therefore "
                "produces a larger increase in the overall coefficient than "
                "the same proportional improvement in reaction."
            ),
            (
                "This result is a diagnostic hypothesis, not experimental "
                "proof of an external mass-transfer mechanism."
            ),
            "",
            "Required discrimination experiments:",
            (
                "Control and vary mixing intensity, recirculation, flow "
                "rate, interfacial area, phase ratio, viscosity, droplet "
                "size, reactor geometry, and temperature."
            ),
            (
                "Where possible, measure the relevant transfer coefficient "
                "independently and verify that the reaction and transfer "
                "coefficients use compatible concentration and phase-volume "
                "bases."
            ),
            "",
            "Model limitations:",
            (
                "The model does not explicitly represent oxidant depletion, "
                "partition equilibrium, chemical enhancement, interfacial "
                "reaction, multiple transfer steps, catalyst deactivation, "
                "changing interfacial area, emulsification, residence-time "
                "distribution, or downstream sulfur-product removal."
            ),
            (
                "Complete ODS validation must distinguish chemical "
                "conversion from phase transfer and final sulfur removal "
                "after extraction, adsorption, phase separation, or another "
                "downstream operation."
            ),
            "",
            "Evidence status:",
            "E3 engineering-screening research prototype.",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    """Load, validate, and evaluate the illustrative repository case."""
    store = load_default_parameter_store()
    case = case_from_parameter_store(store)
    result = evaluate_case(case)

    print(
        render_results(
            case=case,
            result=result,
            parameter_source=store.source_path,
        )
    )


if __name__ == "__main__":
    main()
