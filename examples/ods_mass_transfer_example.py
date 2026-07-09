"""
ODS Reaction–Mass-Transfer Regime Screening Example
===================================================

Purpose
-------
This example compares an apparent reaction-rate constant with a
volumetric mass-transfer coefficient using a Damköhler-type diagnostic
ratio.

It is intended for simplified screening of oxidative desulfurization
(ODS) or other multiphase desulfurization systems where apparent
performance may be controlled by reaction, mass transfer, or both.

Important
---------
The numerical values below are illustrative demonstration parameters.
They are not validated design data.

Reference framework
-------------------
Reaction–Transport Regime Analysis for Desulfurization of Gas and
Petroleum Streams: An Engineering Diagnostic Framework
"""


def damkohler_ratio(rate_constant_s, kla_s):
    """Calculate a simple reaction-to-mass-transfer diagnostic ratio."""
    if rate_constant_s < 0:
        raise ValueError("Rate constant cannot be negative.")

    if kla_s <= 0:
        raise ValueError("kLa must be positive.")

    return rate_constant_s / kla_s


def classify_regime(da):
    """Classify the approximate controlling regime."""
    if da < 0.1:
        return "Reaction-controlled tendency"

    if da <= 10.0:
        return "Mixed reaction–mass-transfer regime"

    return "External mass-transfer-limited tendency"


def main():
    # Illustrative demonstration parameters
    rate_constant_s = 0.02
    kla_s = 0.005

    da = damkohler_ratio(rate_constant_s, kla_s)
    regime = classify_regime(da)

    print("ODS REACTION–MASS-TRANSFER REGIME SCREENING")
    print("=" * 50)
    print(f"Apparent reaction-rate constant : {rate_constant_s:.3e} s^-1")
    print(f"Volumetric mass-transfer kLa    : {kla_s:.3e} s^-1")
    print("-" * 50)
    print(f"Diagnostic Damköhler ratio      : {da:.3f}")
    print(f"Screening result                : {regime}")

    print("\nEngineering interpretation:")
    print(
        "If the process is mass-transfer-limited, increasing catalyst "
        "activity or oxidant reactivity may provide limited benefit unless "
        "phase contacting, interfacial area, dispersion, or reactor "
        "hydrodynamics are also improved."
    )


if __name__ == "__main__":
    main()
