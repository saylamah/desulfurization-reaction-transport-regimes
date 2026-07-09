"""
Cavitation-Assisted Desulfurization Intensification Screening Example
====================================================================

Purpose
-------
This example compares a hydrodynamic-cavitation-assisted case with a
defined reference case using:

1. apparent rate enhancement
2. energy-normalized sulfur removal
3. specific energy demand

It is intended for early screening of whether cavitation-assisted
desulfurization provides useful process benefit relative to a baseline.

Important
---------
The numerical values are illustrative demonstration parameters.
They are not validated design data.

Reference frameworks
--------------------
Reaction–Transport Regime Analysis for Desulfurization of Gas and
Petroleum Streams: An Engineering Diagnostic Framework

Industrial Usefulness and Technology Selection in Process Intensification:
Energy-Normalized Metrics for Hydrodynamic Cavitation
"""


def apparent_enhancement(k_app_hc, k_app_ref):
    """Calculate apparent cavitation enhancement factor."""
    if k_app_ref <= 0:
        raise ValueError("Reference apparent rate constant must be positive.")
    if k_app_hc < 0:
        raise ValueError("HC apparent rate constant cannot be negative.")
    return k_app_hc / k_app_ref


def energy_normalized_sulfur_removal(delta_sulfur_g, energy_kwh):
    """Calculate sulfur removed per unit energy."""
    if delta_sulfur_g < 0:
        raise ValueError("Sulfur removal cannot be negative.")
    if energy_kwh <= 0:
        raise ValueError("Energy input must be positive.")
    return delta_sulfur_g / energy_kwh


def specific_energy_demand(energy_kwh, delta_sulfur_g):
    """Calculate energy consumed per gram of sulfur removed."""
    if energy_kwh < 0:
        raise ValueError("Energy input cannot be negative.")
    if delta_sulfur_g <= 0:
        raise ValueError("Sulfur removal must be positive.")
    return energy_kwh / delta_sulfur_g


def classify_usefulness(en_s_g_per_kwh, enhancement_factor):
    """
    Provide a simple qualitative screening statement.

    These thresholds are illustrative only and must be replaced by
    project-specific technical, economic, and environmental criteria.
    """
    if enhancement_factor <= 1.0:
        return "No apparent kinetic benefit relative to reference"

    if en_s_g_per_kwh < 1.0:
        return "Weak energy-normalized benefit"

    if en_s_g_per_kwh < 10.0:
        return "Moderate screening-level benefit"

    return "Strong screening-level benefit"


def main():
    # Illustrative demonstration parameters
    k_app_ref_s = 0.004
    k_app_hc_s = 0.012

    sulfur_removed_ref_g = 2.0
    sulfur_removed_hc_g = 5.5

    additional_energy_hc_kwh = 0.75

    # Incremental sulfur removal relative to reference case
    delta_sulfur_g = sulfur_removed_hc_g - sulfur_removed_ref_g

    enhancement = apparent_enhancement(k_app_hc_s, k_app_ref_s)
    en_s = energy_normalized_sulfur_removal(
        delta_sulfur_g,
        additional_energy_hc_kwh,
    )
    sec_s = specific_energy_demand(
        additional_energy_hc_kwh,
        delta_sulfur_g,
    )

    usefulness = classify_usefulness(en_s, enhancement)

    print("CAVITATION-ASSISTED DESULFURIZATION SCREENING")
    print("=" * 52)
    print(f"Reference apparent rate constant : {k_app_ref_s:.3e} s^-1")
    print(f"HC apparent rate constant        : {k_app_hc_s:.3e} s^-1")
    print(f"Apparent enhancement factor      : {enhancement:.3f}")
    print("-" * 52)
    print(f"Reference sulfur removed         : {sulfur_removed_ref_g:.3f} g")
    print(f"HC sulfur removed                : {sulfur_removed_hc_g:.3f} g")
    print(f"Incremental sulfur removed       : {delta_sulfur_g:.3f} g")
    print(f"Additional HC energy input       : {additional_energy_hc_kwh:.3f} kWh")
    print("-" * 52)
    print(f"Energy-normalized removal        : {en_s:.3f} g S/kWh")
    print(f"Specific energy demand           : {sec_s:.3f} kWh/g S")
    print(f"Screening result                 : {usefulness}")

    print("\nEngineering interpretation:")
    print(
        "An apparent rate enhancement is not sufficient by itself. "
        "The cavitation-assisted case should also be checked for oxidant "
        "utilization, pressure drop, erosion, emulsion formation, downstream "
        "separation, product quality, operability, maintenance, and scale-up "
        "transferability."
    )


if __name__ == "__main__":
    main()
