"""
HDS internal-diffusion regime screening example.

This module evaluates a deliberately simplified first-order reaction in an
isothermal spherical porous catalyst particle. It calculates the Thiele
modulus, the exact spherical-particle effectiveness factor, the model-implied
Weisz-Prater parameter, and a qualitative engineering screening statement.

Authoritative inputs
--------------------
Illustrative numerical inputs are loaded from:

    data/example_parameters.csv

The shared loader validates the CSV structure, units, duplicate definitions,
case labels, and numerical values before the model is evaluated.

Scientific scope
----------------
The model assumes:

* a spherical porous particle;
* a first-order intrinsic rate law;
* an intrinsic rate coefficient expressed on a catalyst-particle-volume basis;
* constant effective diffusivity;
* isothermal operation;
* uniform pore structure;
* no external-film resistance;
* a known concentration at the external particle surface;
* no catalyst deactivation during the evaluated interval.

The numerical values are illustrative. They are not validated design data for
a specific hydrodesulfurization catalyst, feed, reactor, or industrial unit.

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


SMALL_PHI_THRESHOLD = 1.0e-4
LARGE_PHI_THRESHOLD = 50.0

EXAMPLE_ID = "hds_internal_diffusion"
CASE_ID = "hds_default"


@dataclass(frozen=True, slots=True)
class HDSInternalDiffusionCase:
    """Input parameters for the simplified spherical-particle model.

    Parameters
    ----------
    name:
        Human-readable case identifier.
    particle_radius_m:
        Catalyst-particle radius, m.
    volumetric_rate_constant_s_inv:
        Intrinsic first-order rate coefficient on a compatible catalyst
        particle-volume basis, s^-1.
    effective_diffusivity_m2_s:
        Effective diffusivity of the representative sulfur species in the
        porous particle, m^2/s.
    """

    name: str
    particle_radius_m: float
    volumetric_rate_constant_s_inv: float
    effective_diffusivity_m2_s: float

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Case name must not be empty.")

        _require_finite_positive(
            "particle_radius_m",
            self.particle_radius_m,
        )
        _require_finite_nonnegative(
            "volumetric_rate_constant_s_inv",
            self.volumetric_rate_constant_s_inv,
        )
        _require_finite_positive(
            "effective_diffusivity_m2_s",
            self.effective_diffusivity_m2_s,
        )


@dataclass(frozen=True, slots=True)
class HDSInternalDiffusionResult:
    """Calculated screening quantities."""

    thiele_modulus: float
    effectiveness_factor: float
    model_implied_weisz_prater: float
    internal_utilization_loss_percent: float
    screening_statement: str


def _require_finite_positive(name: str, value: float) -> None:
    """Require a finite value strictly greater than zero."""
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(
            f"{name} must be finite and greater than zero."
        )


def _require_finite_nonnegative(name: str, value: float) -> None:
    """Require a finite value greater than or equal to zero."""
    if not math.isfinite(value) or value < 0.0:
        raise ValueError(
            f"{name} must be finite and non-negative."
        )


def thiele_modulus(
    particle_radius_m: float,
    volumetric_rate_constant_s_inv: float,
    effective_diffusivity_m2_s: float,
) -> float:
    """Return the first-order Thiele modulus for an isothermal sphere.

    The implemented relationship is:

        phi = R_p * sqrt(k_v / D_eff)

    The coefficient ``k_v`` must be expressed on a volumetric
    catalyst-particle basis. A mass-based, external-area-based, or
    active-site-based coefficient must first be converted to a compatible
    volumetric basis.
    """
    _require_finite_positive(
        "particle_radius_m",
        particle_radius_m,
    )
    _require_finite_nonnegative(
        "volumetric_rate_constant_s_inv",
        volumetric_rate_constant_s_inv,
    )
    _require_finite_positive(
        "effective_diffusivity_m2_s",
        effective_diffusivity_m2_s,
    )

    return particle_radius_m * math.sqrt(
        volumetric_rate_constant_s_inv
        / effective_diffusivity_m2_s
    )


def effectiveness_factor_sphere(phi: float) -> float:
    """Return the effectiveness factor for a first-order spherical particle.

    The exact isothermal expression is:

        eta = (3 / phi**2) * (phi / tanh(phi) - 1)

    A series expansion is used for very small ``phi`` to avoid numerical
    cancellation. A large-``phi`` asymptotic expression is used to avoid
    unnecessary numerical loss.
    """
    _require_finite_nonnegative("phi", phi)

    if phi == 0.0:
        return 1.0

    if phi < SMALL_PHI_THRESHOLD:
        phi_squared = phi * phi

        eta = (
            1.0
            - phi_squared / 15.0
            + 2.0 * phi_squared * phi_squared / 315.0
        )

    elif phi > LARGE_PHI_THRESHOLD:
        eta = 3.0 / phi - 3.0 / (phi * phi)

    else:
        eta = (
            3.0
            / (phi * phi)
            * (phi / math.tanh(phi) - 1.0)
        )

    # Floating-point protection for the theoretical interval 0 < eta <= 1.
    return min(1.0, max(0.0, eta))


def model_implied_weisz_prater(
    phi: float,
    eta: float,
) -> float:
    """Return the model-implied Weisz-Prater parameter.

    For the present first-order spherical model:

        C_WP = eta * phi**2

    This is a model-consistency quantity. In an experimental assessment,
    the Weisz-Prater parameter should instead be constructed from:

    * observed rate on a particle-volume basis;
    * sulfur concentration at the external particle surface;
    * particle radius;
    * independently justified effective diffusivity.

    Bulk concentration should not replace surface concentration when
    external-film resistance is significant.
    """
    _require_finite_nonnegative("phi", phi)

    if not math.isfinite(eta) or not 0.0 < eta <= 1.0:
        raise ValueError(
            "eta must be finite and satisfy 0 < eta <= 1."
        )

    return eta * phi * phi


def classify_internal_diffusion(
    phi: float,
    eta: float,
) -> str:
    """Return an illustrative qualitative screening statement.

    Classification is based primarily on internal catalyst utilization
    represented by the effectiveness factor.

    These categories are explicit screening conventions, not universal
    design criteria. Project-specific limits should consider uncertainty,
    catalyst cost, reactor configuration, pressure drop, and the acceptable
    loss of catalyst utilization.
    """
    _require_finite_nonnegative("phi", phi)

    if not math.isfinite(eta) or not 0.0 < eta <= 1.0:
        raise ValueError(
            "eta must be finite and satisfy 0 < eta <= 1."
        )

    if eta >= 0.95:
        return (
            "Weak internal diffusion influence in this simplified model"
        )

    if eta >= 0.80:
        return (
            "Mild reaction-diffusion coupling in this simplified model"
        )

    if eta >= 0.50:
        return (
            "Significant reaction-diffusion coupling in this simplified model"
        )

    return (
        "Strong internal diffusion influence likely in this simplified model"
    )


def evaluate_case(
    case: HDSInternalDiffusionCase,
) -> HDSInternalDiffusionResult:
    """Evaluate one internal-diffusion screening case."""
    phi = thiele_modulus(
        particle_radius_m=case.particle_radius_m,
        volumetric_rate_constant_s_inv=(
            case.volumetric_rate_constant_s_inv
        ),
        effective_diffusivity_m2_s=(
            case.effective_diffusivity_m2_s
        ),
    )

    eta = effectiveness_factor_sphere(phi)

    weisz_prater = model_implied_weisz_prater(
        phi=phi,
        eta=eta,
    )

    return HDSInternalDiffusionResult(
        thiele_modulus=phi,
        effectiveness_factor=eta,
        model_implied_weisz_prater=weisz_prater,
        internal_utilization_loss_percent=(1.0 - eta) * 100.0,
        screening_statement=classify_internal_diffusion(
            phi=phi,
            eta=eta,
        ),
    )


def case_from_parameter_store(
    store: ParameterStore,
) -> HDSInternalDiffusionCase:
    """Build the documented HDS case from the validated CSV dataset."""
    return HDSInternalDiffusionCase(
        name=store.case_label(
            EXAMPLE_ID,
            CASE_ID,
        ),
        particle_radius_m=store.value(
            EXAMPLE_ID,
            CASE_ID,
            "particle_radius_m",
            expected_unit="m",
        ),
        volumetric_rate_constant_s_inv=store.value(
            EXAMPLE_ID,
            CASE_ID,
            "volumetric_rate_constant_s_inv",
            expected_unit="s^-1",
        ),
        effective_diffusivity_m2_s=store.value(
            EXAMPLE_ID,
            CASE_ID,
            "effective_diffusivity_m2_s",
            expected_unit="m^2/s",
        ),
    )


def default_case(
    store: ParameterStore | None = None,
) -> HDSInternalDiffusionCase:
    """Return the authoritative illustrative HDS case.

    When no store is supplied, the repository CSV is loaded and validated.
    """
    parameter_store = (
        store
        if store is not None
        else load_default_parameter_store()
    )

    return case_from_parameter_store(parameter_store)


def render_results(
    case: HDSInternalDiffusionCase,
    result: HDSInternalDiffusionResult,
    parameter_source: str | Path | None = None,
) -> str:
    """Return a human-readable screening report."""
    lines = [
        "HDS INTERNAL-DIFFUSION REGIME SCREENING",
        "=" * 64,
        f"{'Case':<31}: {case.name}",
    ]

    if parameter_source is not None:
        lines.append(
            f"{'Authoritative input source':<31}: {parameter_source}"
        )

    lines.extend(
        [
            (
                f"{'Particle radius':<31}: "
                f"{case.particle_radius_m:.3e} m"
            ),
            (
                f"{'Volumetric rate coefficient':<31}: "
                f"{case.volumetric_rate_constant_s_inv:.3e} s^-1"
            ),
            (
                f"{'Effective diffusivity':<31}: "
                f"{case.effective_diffusivity_m2_s:.3e} m^2/s"
            ),
            "-" * 64,
            (
                f"{'Thiele modulus, phi':<31}: "
                f"{result.thiele_modulus:.4f}"
            ),
            (
                f"{'Effectiveness factor':<31}: "
                f"{result.effectiveness_factor:.4f}"
            ),
            (
                f"{'Model-implied C_WP':<31}: "
                f"{result.model_implied_weisz_prater:.4f}"
            ),
            (
                f"{'Internal utilization loss':<31}: "
                f"{result.internal_utilization_loss_percent:.2f} %"
            ),
            (
                f"{'Screening statement':<31}: "
                f"{result.screening_statement}"
            ),
            "",
            "Scientific interpretation:",
            (
                "The effectiveness factor represents internal catalyst "
                "utilization only under the stated first-order, isothermal, "
                "spherical-particle assumptions."
            ),
            (
                "The model does not include external-film resistance, "
                "hydrogen transport, competitive adsorption, "
                "sulfur-species-dependent kinetics, catalyst deactivation, "
                "heat effects, pore-size distributions, or reactor "
                "hydrodynamics."
            ),
            "",
            "Required validation before engineering use:",
            (
                "Use traceable kinetic and diffusivity data on compatible "
                "bases; test particle-size sensitivity; evaluate external "
                "mass transfer independently; characterize sulfur "
                "speciation, pore structure, wetting, deactivation, "
                "temperature, pressure, and feed composition; and quantify "
                "uncertainty."
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
