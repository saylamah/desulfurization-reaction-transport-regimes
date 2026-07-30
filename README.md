# Desulfurization Reaction–Transport Regimes

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21278796.svg)](https://doi.org/10.5281/zenodo.21278796)
[![Software License: MIT](https://img.shields.io/badge/software%20license-MIT-blue.svg)](LICENSE)

An engineering diagnostic framework for identifying reaction–transport limitations, evaluating process-intensification options, and supporting technically defensible scale-up decisions in gas- and petroleum-stream desulfurization.

> **Evidence status**
>
> - **E3 — Engineering screening framework:** the equations, documentation, Python examples, and illustrative dataset support transparent regime diagnosis and early-stage engineering comparison.
> - **Not a validated design model:** the repository does not provide universally transferable kinetic constants, catalyst data, mass-transfer correlations, economic thresholds, or industrial performance guarantees.
> - **System-specific validation is mandatory:** application to a real feed, catalyst, adsorbent, reactor, oxidant system, or intensification device requires measured data, uncertainty analysis, sulfur closure, durability assessment, and pilot-scale evidence.

---

## 1. Purpose

Desulfurization performance is rarely controlled by reaction chemistry alone.

Observed sulfur removal may depend simultaneously on:

- intrinsic reaction kinetics;
- external gas–liquid or liquid–solid mass transfer;
- internal diffusion in porous catalysts or adsorbents;
- adsorption capacity and surface accessibility;
- sulfur-species reactivity;
- hydrogen or oxidant availability;
- mixing, dispersion, and hydrodynamics;
- catalyst or adsorbent deactivation;
- downstream extraction, adsorption, or phase separation;
- energy input and pressure drop;
- product quality and process operability.

This repository provides a structured framework for determining which limitation should be addressed before changing chemistry, equipment, operating conditions, or process-intensification strategy.

The central engineering question is:

> **Which physical, chemical, or separation step controls the observed sulfur-removal performance under the defined process conditions?**

---

## 2. Practical Engineering Questions

The framework is intended to support questions such as:

- Is the observed process reaction-controlled, transport-limited, capacity-limited, separation-limited, or mixed?
- Would increasing catalyst activity materially improve overall sulfur removal?
- Is oxidant addition limited by reaction chemistry, dispersion, interphase transfer, or downstream separation?
- Are porous-particle performance and catalyst utilization constrained by internal diffusion?
- Is adsorbent performance governed by equilibrium capacity, kinetics, pore transport, or regeneration?
- Does an intensification method address the actual process bottleneck?
- Are reported removal values transferable across feeds, sulfur species, reactors, and operating conditions?
- What measurements are required before pilot or industrial scale-up?
- Does the expected benefit justify additional energy, chemicals, pressure drop, maintenance, erosion risk, or separation burden?

---

## 3. Application Scope

The methodology is relevant to sulfur removal from:

- natural gas and acid-gas streams;
- light hydrocarbons;
- diesel and middle distillates;
- heavy petroleum fractions.

It may support the engineering assessment of:

- hydrodesulfurization (HDS);
- oxidative desulfurization (ODS);
- adsorptive desulfurization;
- reactive adsorptive desulfurization;
- catalytic oxidation and sweetening;
- radical-assisted oxidation;
- hydrodynamic and mixing-based process intensification.

The framework is diagnostic rather than technology-prescriptive. It does not assume that one desulfurization pathway or intensification method is optimal for all feeds and process boundaries.

---

## 4. Reaction–Transport–Separation Regimes

The framework considers several possible controlling or interacting regimes.

| Regime | Diagnostic interpretation | Typical engineering response |
|---|---|---|
| Reaction-controlled | Intrinsic chemistry is slow relative to transport | Evaluate catalyst activity, temperature, pressure, reactive-species availability, or mechanism |
| External mass-transfer-limited | Bulk-to-interface transport is insufficient | Improve contacting, dispersion, interfacial area, mixing, or hydrodynamics |
| Internal diffusion-limited | Reaction is fast relative to pore transport | Evaluate particle size, pore architecture, effective diffusivity, and catalyst utilization |
| Adsorption- or capacity-limited | Surface saturation, competition, or finite capacity controls performance | Evaluate equilibrium, breakthrough, regeneration, and adsorbent selectivity |
| Reactant-utilization-limited | Hydrogen, oxidant, or another reactive species is poorly used | Improve dosing, distribution, phase transfer, selectivity, or recycle |
| Hydrodynamics-limited | Mixing, residence-time distribution, or phase contacting is inadequate | Redesign contacting or reactor hydrodynamics |
| Separation-limited | Sulfur is transformed but not adequately removed from the product stream | Improve extraction, adsorption, phase separation, polishing, or solvent management |
| Energy- or intensification-limited | Additional process intensity gives insufficient benefit per unit penalty | Reassess operating severity, device selection, and the reference process |
| Mixed or transitional | Several resistances contribute materially | Use combined experiments and models; avoid single-factor interpretation |

The purpose of this classification is not merely descriptive. Each regime should lead to a different validation plan, model structure, and scale-up decision.

---

## 5. Process-Intensification Perspective

Hydrodynamic cavitation and related technologies are treated as possible **reaction–transport intensification layers**, not as universal stand-alone desulfurization solutions.

An intensification method is technically defensible only when it:

1. addresses an identified kinetic, transport, dispersion, or phase-contacting limitation;
2. improves performance relative to a defined reference case;
3. maintains acceptable product quality and downstream separability;
4. avoids disproportionate energy, chemical, pressure-drop, erosion, fouling, or maintenance penalties;
5. remains controllable, reliable, and transferable during scale-up.

The repository therefore emphasizes:

- reference-case definition;
- mechanism-based diagnosis;
- incremental rather than gross performance;
- energy-normalized sulfur removal;
- specific energy demand;
- complete flowsheet consequences;
- uncertainty and validation requirements.

A higher apparent rate or removal percentage is not sufficient evidence of industrial usefulness.

---

## 6. Repository Structure

```text
desulfurization-reaction-transport-regimes/
├── data/
│   └── example_parameters.csv
├── docs/
│   ├── equations.md
│   ├── framework-summary.md
│   ├── regime-classification.md
│   └── validation-guidelines.md
├── examples/
│   ├── cavitation_intensification_example.py
│   ├── hds_regime_example.py
│   └── ods_mass_transfer_example.py
├── paper/
│   ├── README.md
│   └── reaction-transport-regime-analysis-desulfurization.pdf
├── CITATION.cff
├── LICENSE
└── README.md
```

### Documentation

- [Framework summary](docs/framework-summary.md)
- [Model equations](docs/equations.md)
- [Regime classification](docs/regime-classification.md)
- [Validation guidelines](docs/validation-guidelines.md)

### Executable Examples

- [HDS internal-diffusion screening](examples/hds_regime_example.py)
- [ODS reaction–mass-transfer screening](examples/ods_mass_transfer_example.py)
- [Cavitation-assisted desulfurization screening](examples/cavitation_intensification_example.py)

### Illustrative Data

- [Example parameter table](data/example_parameters.csv)

The CSV file documents the default illustrative values used across the examples. The current scripts define their demonstration values internally and do not yet load the CSV directly.

---

## 7. Quick Start

The three current examples use only the Python standard library.

### Obtain the Repository

Download the ZIP archive from GitHub or clone the repository:

```bash
git clone https://github.com/saylamah/desulfurization-reaction-transport-regimes.git
cd desulfurization-reaction-transport-regimes
```

### Run the HDS Example

```bash
python examples/hds_regime_example.py
```

The script calculates:

- the Thiele modulus;
- the spherical-particle effectiveness factor;
- a qualitative internal-diffusion screening classification.

### Run the ODS Example

```bash
python examples/ods_mass_transfer_example.py
```

The script calculates:

- a reaction-to-mass-transfer diagnostic ratio;
- a qualitative reaction–mass-transfer regime classification.

### Run the Cavitation Example

```bash
python examples/cavitation_intensification_example.py
```

The script compares a cavitation-assisted case with a reference case using:

- apparent-rate enhancement;
- incremental sulfur removal;
- energy-normalized sulfur removal;
- specific energy demand;
- a qualitative screening statement.

On Windows, `py` may be used instead of `python`.

---

## 8. Example 1 — HDS Internal-Diffusion Screening

The HDS example uses a simplified first-order reaction in a spherical porous catalyst particle.

The Thiele modulus is represented as:

```text
phi = R_p * sqrt(k / D_eff)
```

where:

- `R_p` is particle radius;
- `k` is a simplified first-order rate constant;
- `D_eff` is effective diffusivity.

The spherical effectiveness factor is represented as:

```text
eta = (3 / phi^2) * (phi / tanh(phi) - 1)
```

The default illustrative case gives approximately:

```text
Thiele modulus, phi  = 2.2361
Effectiveness factor = 0.7726
```

This indicates significant reaction–diffusion coupling within the simplified screening model.

A rigorous HDS assessment must also consider:

- sulfur speciation;
- competitive adsorption;
- hydrogen availability;
- catalyst deactivation;
- external mass transfer;
- pore structure;
- temperature and pressure;
- feed composition;
- reactor hydrodynamics.

---

## 9. Example 2 — ODS Reaction–Mass-Transfer Screening

The ODS example compares an apparent reaction-rate constant with a volumetric mass-transfer coefficient:

```text
Da_diagnostic = k_obs / kLa
```

where:

- `k_obs` is an apparent reaction-rate constant;
- `kLa` is a volumetric mass-transfer coefficient.

The default illustrative case gives:

```text
Da_diagnostic = 4.000
```

and is classified as a mixed reaction–mass-transfer regime.

This diagnostic ratio is a screening indicator, not a universal Damköhler-number definition. A real ODS assessment should additionally consider:

- sulfur-species chemistry;
- oxidant utilization;
- catalyst or promoter effects;
- liquid–liquid equilibrium;
- interfacial area;
- mixing and droplet-size distribution;
- extraction and phase separation;
- solvent and oxidant recovery;
- product stability.

---

## 10. Example 3 — Cavitation-Assisted Screening

The cavitation example compares a defined reference case with a hydrodynamic-cavitation-assisted case.

The apparent enhancement factor is:

```text
F_app = k_app,HC / k_app,ref
```

The incremental energy-normalized sulfur removal is:

```text
EN_S = delta_m_S / E_HC
```

The corresponding specific energy demand is:

```text
SEC_S = E_HC / delta_m_S
```

where:

- `delta_m_S` is the incremental sulfur removed relative to the reference case;
- `E_HC` is the additional cavitation energy input.

The default illustrative case gives:

```text
Apparent enhancement factor = 3.000
Energy-normalized removal   = 4.667 g S/kWh
Specific energy demand      = 0.214 kWh/g S
```

These values are demonstration outputs only. The qualitative thresholds in the script are illustrative and must be replaced by project-specific technical, economic, environmental, and reliability criteria.

A complete evaluation should also include:

- oxidant and reagent consumption;
- pressure drop and pumping efficiency;
- erosion and material compatibility;
- emulsion formation;
- downstream separation;
- product quality;
- fouling and cleaning;
- operating stability;
- maintenance;
- uncertainty;
- scale-up transferability.

---

## 11. Data and Parameter Use

The file:

```text
data/example_parameters.csv
```

contains illustrative parameters for:

- HDS internal-diffusion screening;
- ODS reaction–mass-transfer screening;
- cavitation-assisted desulfurization screening.

The values are not validated design data.

For a real case, replace them with traceable measurements or defensible estimates and document:

- feed composition and sulfur speciation;
- temperature and pressure;
- catalyst or adsorbent properties;
- reactor geometry and operating mode;
- phase flow rates;
- mixing and mass-transfer measurements;
- oxidant or hydrogen dosage;
- analytical methods and detection limits;
- sulfur balance;
- uncertainty;
- reference-case definition.

---

## 12. Validation Requirements

A defensible validation program should include, as applicable:

1. sulfur speciation before and after treatment;
2. a closed sulfur balance;
3. repeat experiments and uncertainty estimates;
4. independent measurements of mass-transfer behavior;
5. catalyst or adsorbent durability;
6. oxidant or hydrogen utilization;
7. phase-separation and product-quality assessment;
8. energy and pressure-drop measurements;
9. materials compatibility and erosion assessment;
10. testing with realistic feed variability;
11. comparison with an appropriate reference process;
12. pilot-scale verification before industrial extrapolation.

Detailed guidance is provided in:

- [Validation guidelines](docs/validation-guidelines.md)

---

## 13. Evidence and Maturity

| Repository component | Classification | Interpretation |
|---|---|---|
| Regime framework | **E3 — Engineering screening framework** | Structured diagnostic logic based on established reaction and transport concepts |
| Equations and regime indicators | **E3 — Research prototype** | Useful for transparent screening; require case-specific parameterization |
| Python examples | **E3 — Executable demonstrations** | Reproducible illustrative calculations, not validated plant models |
| Example CSV data | **Illustrative only** | Not measured pilot or industrial data |
| Companion paper | **Open technical preprint** | Scientific and engineering basis for the framework |
| Industrial design claims | **Not established** | Require independent data, validation, safety analysis, and scale-up evidence |

The repository does not currently provide:

- universal kinetic constants;
- validated catalyst or adsorbent datasets;
- a complete reactor model;
- a process simulator;
- detailed economics;
- process-safety calculations;
- materials-selection certification;
- guaranteed emissions or product specifications;
- validated scale-up correlations for a specific device.

---

## 14. Responsible Use

Use this repository for:

- early-stage technical screening;
- process diagnosis;
- experimental planning;
- sensitivity analysis;
- comparison of reaction and transport resistances;
- preliminary process-intensification assessment;
- definition of validation requirements;
- transparent communication of assumptions.

Do not use the current repository as:

- a substitute for measured kinetic or transport data;
- a final reactor-design calculation;
- a catalyst-selection guarantee;
- a process-safety analysis;
- a techno-economic assessment;
- an industrial performance warranty;
- a regulatory or emissions-compliance model.

All real applications require independent engineering review and explicit documentation of the applicability domain.

---

## 15. Scientific and Engineering Basis

### Primary Framework

**Reaction–Transport Regime Analysis for Desulfurization of Gas and Petroleum Streams: An Engineering Diagnostic Framework**

- DOI: [10.5281/zenodo.20095695](https://doi.org/10.5281/zenodo.20095695)
- Repository copy: [reaction-transport-regime-analysis-desulfurization.pdf](paper/reaction-transport-regime-analysis-desulfurization.pdf)
- Paper information: [paper/README.md](paper/README.md)

This paper develops the reaction–transport–separation framework underlying the repository.

### Supporting Process-Intensification Framework

**Industrial Usefulness and Technology Selection in Process Intensification: Energy-Normalized Metrics for Hydrodynamic Cavitation**

- DOI: [10.5281/zenodo.20593905](https://doi.org/10.5281/zenodo.20593905)

This supporting framework introduces energy-normalized and system-level decision criteria for determining whether an intensification technology creates useful process benefit after penalties and uncertainty are considered.

---

## 16. Citation

Repository citation metadata is provided in:

- [`CITATION.cff`](CITATION.cff)

Repository DOI:

- [10.5281/zenodo.21278796](https://doi.org/10.5281/zenodo.21278796)

When using the scientific framework, also cite the primary paper:

> Saylam, A. (2026). *Reaction–Transport Regime Analysis for Desulfurization of Gas and Petroleum Streams: An Engineering Diagnostic Framework*. Zenodo. https://doi.org/10.5281/zenodo.20095695

For reproducible use, identify the repository version or commit and document all modified parameters.

---

## 17. Licensing and Reuse

- The repository software and associated software documentation are distributed under the [MIT License](LICENSE).
- The companion scientific papers remain subject to the licences stated in their respective Zenodo records and PDF files.
- The MIT software licence must not be assumed to override the separate licence of a scientific paper or third-party source.
- Third-party material remains subject to its original attribution and reuse conditions.

---

## 18. Public-Information Policy

The repository is intended for open engineering communication, reproducible screening calculations, and scientific discussion.

It does not intentionally include:

- confidential client data;
- proprietary industrial operating data;
- restricted project documents;
- employer-owned design information;
- unpublished third-party material without permission.

---

## 19. Author

**Prof. Dr. Ahmad Saylam**

R&D & Technology Development Leader  
Scientific & Engineering Consultant  
Duisburg, Germany

ORCID: [0000-0001-7484-1265](https://orcid.org/0000-0001-7484-1265)

---

## 20. Keywords

Desulfurization · hydrodesulfurization · oxidative desulfurization · adsorption · reaction engineering · mass transfer · internal diffusion · Thiele modulus · effectiveness factor · hydrodynamic cavitation · process intensification · sulfur removal · energy-normalized performance · scale-up · validation
