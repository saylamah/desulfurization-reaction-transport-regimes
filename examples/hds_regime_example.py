"""
HDS Internal-Diffusion Regime Screening Example
================================================

Purpose
-------
This example calculates the Thiele modulus and effectiveness factor
for a simplified first-order reaction in a spherical porous catalyst
particle.

It is intended as an engineering diagnostic example for screening
possible internal diffusion limitations in hydrodesulfurization (HDS).

Important
---------
The numerical values below are illustrative demonstration parameters.
They are not validated design data for a specific catalyst, feed,
reactor, or industrial HDS unit.

Reference framework
-------------------
Reaction–Transport Regime Analysis for Desulfurization of Gas and
Petroleum Streams: An Engineering Diagnostic Framework
"""

import math


def thiele_modulus(particle_radius_m, rate_constant_s, effective_diffusivity_m2_s):
    """
    Calculate the Thiele modulus for a simplified first-order reaction
    in a spherical porous catalyst particle.
    """
    if particle_radius_m <= 0:
        raise ValueError("Particle radius must be positive.")

    if rate_constant_s < 0:
        raise ValueError("Rate constant cannot be negative.")

    if effective_diffusivity_m2_s <= 0:
        raise ValueError("Effective diffusivity must be positive.")

    return particle_radius_m * math.sqrt(
        rate_constant_s / effective_diffusivity_m2_s
    )


def effectiveness_factor_sphere(phi):
    """
    Calculate the effectiveness factor for an isothermal spherical
    catalyst particle with simplified first-order kinetics.

    eta = (3 / phi^2) * (phi / tanh(phi) - 1)

    For phi approaching zero, eta approaches 1.
    """
    if phi < 0:
        raise ValueError("Thiele modulus cannot be negative.")

    if phi < 1.0e-8:
        return 1.0

    return (3.0 / phi**2) * ((phi / math.tanh(phi)) - 1.0)


def classify_internal_diffusion(phi, eta):
    """
    Provide a qualitative engineering screening classification.

    The thresholds are illustrative diagnostic categories and should
    not be interpreted as universal design limits.
    """
    if phi < 0.3 and eta > 0.95:
        return "Weak internal diffusion limitation"

    if phi < 1.0 and eta > 0.75:
        return "Mild reaction–diffusion coupling"

    if phi < 3.0 and eta > 0.40:
        return "Significant reaction–diffusion coupling"

    return "Strong internal diffusion limitation likely"


def main():
    # ------------------------------------------------------------
    # Illustrative demonstration parameters
    # ------------------------------------------------------------

    particle_radius_m = 1.0e-3
    rate_constant_s = 0.05
    effective_diffusivity_m2_s = 1.0e-8

    # ------------------------------------------------------------
    # Calculations
    # ------------------------------------------------------------

    phi = thiele_modulus(
        particle_radius_m,
        rate_constant_s,
        effective_diffusivity_m2_s,
    )

    eta = effectiveness_factor_sphere(phi)

    regime = classify_internal_diffusion(phi, eta)

    # ------------------------------------------------------------
    # Results
    # ------------------------------------------------------------

    print("HDS INTERNAL-DIFFUSION REGIME SCREENING")
    print("=" * 44)
    print(f"Particle radius       : {particle_radius_m:.3e} m")
    print(f"Rate constant         : {rate_constant_s:.3e} s^-1")
    print(
        f"Effective diffusivity : "
        f"{effective_diffusivity_m2_s:.3e} m^2/s"
    )
    print("-" * 44)
    print(f"Thiele modulus, phi   : {phi:.4f}")
    print(f"Effectiveness factor  : {eta:.4f}")
    print(f"Screening result      : {regime}")

    print("\nEngineering interpretation:")
    print(
        "The result is a simplified screening indicator. A rigorous "
        "HDS assessment should also consider sulfur speciation, "
        "competitive adsorption, hydrogen availability, catalyst "
        "deactivation, external mass transfer, pore structure, "
        "temperature, pressure, and feed composition."
    )


if __name__ == "__main__":
    main()
