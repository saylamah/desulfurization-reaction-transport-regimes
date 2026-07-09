# Desulfurization Reaction–Transport Regimes

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21278797.svg)](https://doi.org/10.5281/zenodo.21278797)

Engineering diagnostic framework for desulfurization reaction–transport regimes, process intensification, and scale-up evaluation in gas and petroleum streams.

## DOI

Repository archive DOI: [10.5281/zenodo.21278797](https://doi.org/10.5281/zenodo.21278797)

Companion scientific paper DOI: [10.5281/zenodo.20095695](https://doi.org/10.5281/zenodo.20095695)

## Citation

If you use this repository, please cite the archived software repository:

> Saylam, A. (2026). *Desulfurization Reaction–Transport Regimes* (v1.0.0). Zenodo. DOI: 10.5281/zenodo.21278797

For the scientific and engineering framework underlying this repository, please also cite:

> Saylam, A. (2026). *Reaction–Transport Regime Analysis for Desulfurization of Gas and Petroleum Streams: An Engineering Diagnostic Framework*. Zenodo. DOI: 10.5281/zenodo.20095695

## Scope

This repository supports regime-based analysis of sulfur removal from:

- natural gas and acid-gas streams
- light hydrocarbons
- diesel and middle distillates
- heavy petroleum fractions

The framework connects intrinsic reaction chemistry with mass transfer, internal diffusion, adsorption, hydrodynamics, downstream separation, energy input, and scale-up constraints.

## Technical Focus

- Hydrodesulfurization
- Oxidative desulfurization
- Adsorptive and reactive adsorptive desulfurization
- Catalytic oxidation and sweetening
- Radical-assisted oxidation
- Hydrodynamic cavitation as a process-intensification layer
- Energy-normalized sulfur removal
- Reaction-controlled, mass-transfer-limited, diffusion-limited, separation-limited, and mixed regimes

## Basis

This repository is based on the companion technical work:

**Reaction–Transport Regime Analysis for Desulfurization of Gas and Petroleum Streams: An Engineering Diagnostic Framework**

and supported by the process-intensification framework:

**Industrial Usefulness and Technology Selection in Process Intensification: Energy-Normalized Metrics for Hydrodynamic Cavitation**

## Supporting Process-Intensification Framework

The desulfurization regime-analysis methodology is complemented by the following independent technical work:

**Industrial Usefulness and Technology Selection in Process Intensification: Energy-Normalized Metrics for Hydrodynamic Cavitation**

DOI: [10.5281/zenodo.20593905](https://doi.org/10.5281/zenodo.20593905)

This supporting framework introduces the **Industrial Usefulness Window** and energy-normalized decision metrics for evaluating whether a process-intensification technology creates transferable industrial value after accounting for energy demand, chemical use, pressure drop, separation burden, erosion, fouling, maintenance, product quality, reliability, and scale-up constraints.

Within the present desulfurization repository, hydrodynamic cavitation is treated as a potential **reaction–transport intensification layer**, not as a universal stand-alone solution. Its usefulness depends on whether it addresses an identified process bottleneck and provides positive net benefit relative to a defined reference case.

## Repository Structure

```text
docs/       Technical documentation and framework notes
examples/   Simple calculation examples
data/       Example parameters and demonstration data
```

## Technical Limitations and Responsible Use

The models, equations, classifications, example scripts, and demonstration parameters in this repository are intended for engineering screening, regime diagnosis, methodological development, and educational or research use.

The example calculations use illustrative parameters and should not be interpreted as validated design data for a specific feedstock, sulfur species, catalyst, adsorbent, reactor, industrial unit, or operating condition.

Application to real desulfurization systems requires appropriate validation of sulfur speciation, sulfur balances, reaction kinetics, mass transfer, internal diffusion, adsorption performance, oxidant utilization, downstream separation, energy consumption, materials compatibility, catalyst or adsorbent durability, product quality, process safety, reliability, and scale-up transferability.

The repository does not constitute a final process design package, safety assessment, regulatory recommendation, or guarantee of industrial performance.

## License

Software and example scripts are released under the MIT License.

The companion scientific paper should be cited separately using its Zenodo DOI.
