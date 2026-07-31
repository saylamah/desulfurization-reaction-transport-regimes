# Desulfurization Reaction–Transport Regimes

[![Python scientific validation](https://github.com/saylamah/desulfurization-reaction-transport-regimes/actions/workflows/python-tests.yml/badge.svg)](https://github.com/saylamah/desulfurization-reaction-transport-regimes/actions/workflows/python-tests.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21278796.svg)](https://doi.org/10.5281/zenodo.21278796)
[![Software License: MIT](https://img.shields.io/badge/software%20license-MIT-blue.svg)](LICENSE)

An engineering diagnostic framework for identifying reaction–transport limitations, evaluating process-intensification options, and supporting technically defensible scale-up decisions in gas- and petroleum-stream desulfurization.

> **Evidence status**
>
> - **E3 — Engineering screening framework:** the equations, documentation, validated input loader, Python examples, illustrative dataset, and automated tests support transparent regime diagnosis and reproducible early-stage engineering comparison.
> - **Not a validated industrial design model:** the repository does not provide universally transferable kinetic constants, catalyst data, mass-transfer correlations, economic thresholds, cavitation-performance correlations, or industrial guarantees.
> - **System-specific validation is mandatory:** application to a real feed, catalyst, adsorbent, reactor, oxidant system, separation process, or intensification device requires measured data, uncertainty analysis, sulfur-balance closure, durability assessment, process-safety review, and pilot-scale evidence.
> - **Passing software tests demonstrates implementation consistency only:** it does not experimentally validate the illustrative parameters, reaction mechanisms, catalyst performance, cavitation efficacy, or scale-up behavior.

---

## 1. Purpose

Desulfurization performance is rarely controlled by reaction chemistry alone.

Observed sulfur removal may depend simultaneously on:

- intrinsic reaction kinetics;
- external gas–liquid, liquid–liquid, or liquid–solid mass transfer;
- internal diffusion in porous catalysts or adsorbents;
- adsorption equilibrium, capacity, and surface accessibility;
- sulfur-species reactivity;
- hydrogen, oxidant, or other reactant availability;
- mixing, dispersion, and hydrodynamics;
- catalyst or adsorbent deactivation;
- downstream extraction, adsorption, filtration, or phase separation;
- energy input and pressure drop;
- product recovery and quality;
- corrosion, erosion, fouling, and process operability.

This repository provides a structured framework for determining which limitation should be addressed before changing chemistry, catalyst, equipment, operating conditions, or process-intensification strategy.

The central engineering question is:

> **Which physical, chemical, transport, adsorption, hydrodynamic, or separation step controls the observed sulfur-removal performance under the defined process conditions?**

---

## 2. Practical Engineering Questions

The framework is intended to support questions such as:

- Is the observed process reaction controlled, transport limited, capacity limited, separation limited, hydrodynamically limited, or under mixed control?
- Would increasing catalyst activity materially improve the complete process?
- Is oxidant addition limited by intrinsic chemistry, dispersion, interphase transfer, decomposition, or downstream separation?
- Are porous-particle performance and catalyst utilization constrained by internal diffusion?
- Is adsorbent performance governed by equilibrium capacity, uptake kinetics, pore transport, breakthrough, competition, or regeneration?
- Does an intensification method address the actual controlling limitation?
- Are apparent rate constants being incorrectly interpreted as intrinsic kinetics?
- Are sulfur conversion, sulfur transfer, adsorption, and final sulfur removal being distinguished?
- Are reported results transferable across feeds, sulfur species, reactors, scales, and operating conditions?
- What measurements are required before pilot or industrial scale-up?
- Does the expected benefit justify additional energy, reagent consumption, pressure drop, maintenance, erosion risk, corrosion risk, or separation burden?

---

## 3. Application Scope

The methodology is relevant to sulfur removal from:

- natural gas and acid-gas streams;
- light hydrocarbons;
- diesel and middle distillates;
- heavy petroleum fractions.

It may support engineering assessment of:

- hydrodesulfurization;
- oxidative desulfurization;
- adsorptive desulfurization;
- reactive adsorptive desulfurization;
- catalytic oxidation and sweetening;
- reactive gas absorption;
- radical-assisted oxidation;
- hydrodynamic and mixing-based process intensification.

The framework is diagnostic rather than technology prescriptive. It does not assume that one desulfurization pathway, catalyst, adsorbent, or intensification method is optimal for every feed and process boundary.

---

## 4. Reaction–Transport–Separation Classification

The framework distinguishes mechanistic limitations, process-sequence limitations, and industrial-feasibility constraints.

| Limitation or constraint | Diagnostic interpretation | Typical engineering response |
|---|---|---|
| Reaction controlled | Intrinsic chemistry is slow relative to transport | Evaluate catalyst activity, temperature, pressure, reactant availability, or reaction mechanism |
| External mass-transfer limited | Bulk-to-interface or bulk-to-surface transport is insufficient | Improve contacting, dispersion, interfacial area, mixing, distribution, or hydrodynamics |
| Internal diffusion limited | Reaction is fast relative to pore transport | Evaluate particle size, pore architecture, effective diffusivity, wetting, and catalyst utilization |
| Adsorption or capacity limited | Equilibrium capacity, saturation, competition, or mass-transfer-zone behavior controls performance | Evaluate isotherms, breakthrough, working capacity, selectivity, and regeneration |
| Reactant-utilization limited | Hydrogen, oxidant, or another reactant is supplied but poorly used | Improve dosing, distribution, phase transfer, catalyst selectivity, stability, or recycle |
| Hydrodynamically limited | Mixing, residence-time distribution, phase distribution, or contacting is inadequate | Improve distribution, internals, recirculation, suspension, or reactor configuration |
| Separation limited | Sulfur is transformed but not adequately removed from the final product | Improve extraction, adsorption, phase separation, filtration, polishing, or solvent management |
| Deactivation or durability limited | Performance decreases with time, loading, or repeated cycles | Address poisoning, coke, deposits, leaching, attrition, regeneration, or materials degradation |
| Industrial-feasibility constrained | Additional intensity gives insufficient net benefit after penalties | Reassess severity, energy, reagents, product recovery, durability, and the reference process |
| Mixed or transitional | Several mechanisms contribute materially or change during operation | Use controlled perturbations, combined models, and time-dependent analysis |

Energy demand is treated as a system-level feasibility constraint rather than a fundamental microscopic kinetic regime.

The purpose of the classification is not merely descriptive. Each diagnosis should lead to a different:

- experimental plan;
- model structure;
- measurement requirement;
- process intervention;
- scale-up criterion.

---

## 5. Process-Intensification Perspective

Hydrodynamic cavitation and related technologies are treated as possible **reaction–transport intensification layers**, not as universally applicable stand-alone desulfurization solutions.

An intensification method is technically defensible only when it:

1. addresses an identified kinetic, transport, dispersion, mixing, or phase-contacting limitation;
2. improves performance relative to a defined and equivalent reference case;
3. maintains acceptable product quality and downstream separability;
4. produces positive incremental rather than only gross benefit;
5. avoids disproportionate energy, chemical, pressure-drop, erosion, corrosion, fouling, or maintenance penalties;
6. remains controllable, reliable, maintainable, and transferable during scale-up.

The repository therefore emphasizes:

- reference-case definition;
- mechanism-based diagnosis;
- sulfur-balance closure;
- incremental rather than gross performance;
- measured electrical energy;
- hydraulic energy cross-checks;
- energy-normalized sulfur benefit;
- specific energy demand;
- complete flowsheet consequences;
- uncertainty and validation requirements.

A higher apparent rate coefficient or removal percentage is not sufficient evidence of industrial usefulness.

---

## 6. Repository Structure

```text
desulfurization-reaction-transport-regimes/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── data/
│   └── example_parameters.csv
├── docs/
│   ├── equations.md
│   ├── framework-summary.md
│   ├── regime-classification.md
│   └── validation-guidelines.md
├── examples/
│   ├── example_parameter_loader.py
│   ├── hds_regime_example.py
│   ├── ods_mass_transfer_example.py
│   └── cavitation_intensification_example.py
├── tests/
│   └── test_desulfurization_examples.py
├── paper/
│   ├── README.md
│   └── reaction-transport-regime-analysis-desulfurization.pdf
├── CITATION.cff
├── LICENSE
└── README.md
```

### Documentation

- [Framework summary](docs/framework-summary.md)
- [Core equations](docs/equations.md)
- [Regime classification](docs/regime-classification.md)
- [Validation guidelines](docs/validation-guidelines.md)

### Executable Examples

- [Validated parameter loader](examples/example_parameter_loader.py)
- [HDS internal-diffusion screening](examples/hds_regime_example.py)
- [ODS reaction–transfer screening](examples/ods_mass_transfer_example.py)
- [Cavitation-assisted desulfurization screening](examples/cavitation_intensification_example.py)

### Data and Tests

- [Authoritative illustrative parameter dataset](data/example_parameters.csv)
- [Scientific and numerical tests](tests/test_desulfurization_examples.py)
- [Continuous-validation workflow](.github/workflows/python-tests.yml)

### Scientific Paper

- [Paper information](paper/README.md)
- [Repository copy of the primary framework](paper/reaction-transport-regime-analysis-desulfurization.pdf)

---

## 7. Authoritative Input Architecture

The file:

```text
data/example_parameters.csv
```

is the single authoritative numerical source for all three examples.

The scripts no longer duplicate their default numerical values internally.

The shared loader:

```text
examples/example_parameter_loader.py
```

validates:

- exact CSV column structure;
- documented case identifiers;
- parameter names;
- units;
- finite numerical values;
- duplicate definitions;
- case-label consistency;
- allowed data-status categories;
- exact parameter schemas for each example.

The dataset contains only primary model inputs. Derived quantities such as:

- Thiele modulus;
- effectiveness factor;
- resistance fractions;
- overall coefficients;
- incremental sulfur benefit;
- energy-normalized metrics;
- hydraulic power;
- cavitation number;

are calculated by the scripts and are not duplicated in the CSV.

This prevents input and output values from becoming independently inconsistent.

### Data Status

The CSV explicitly distinguishes among:

- `illustrative_not_validated`;
- `illustrative_screening_convention`;
- `illustrative_assumption`.

The loader validates these labels but does not establish physical validity.

For a real application, illustrative values must be replaced with traceable measurements or defensible estimates.

---

## 8. Quick Start

The examples and tests use only the Python standard library.

### Obtain the Repository

```bash
git clone https://github.com/saylamah/desulfurization-reaction-transport-regimes.git
cd desulfurization-reaction-transport-regimes
```

### Validate the Authoritative Dataset

```bash
python examples/example_parameter_loader.py
```

Expected summary:

```text
Rows loaded : 32
Cases found : 5
```

### Run the HDS Example

```bash
python examples/hds_regime_example.py
```

### Run the ODS Example

```bash
python examples/ods_mass_transfer_example.py
```

### Run the Cavitation Example

```bash
python examples/cavitation_intensification_example.py
```

### Run All Scientific and Numerical Tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The current test suite contains 32 tests.

A successful local run ends with:

```text
Ran 32 tests

OK
```

The exact execution time depends on the environment.

On Windows, `py` may be used instead of `python`.

---

## 9. Automated Scientific and Numerical Verification

The test suite verifies implementation consistency for:

### Dataset and Loader

- expected row and case counts;
- required parameter schemas;
- unit enforcement;
- duplicate-parameter rejection;
- non-finite-value rejection;
- case-label consistency.

### HDS Internal Diffusion

- authoritative CSV input values;
- Thiele-modulus calculation;
- spherical effectiveness factor;
- small-$\phi$ limiting behavior;
- large-$\phi$ behavior;
- bounded effectiveness factor;
- monotonic decrease of effectiveness factor with $\phi$;
- model-implied Weisz–Prater identity;
- physical input safeguards.

### ODS Reaction–Transfer Model

- authoritative CSV input values;
- reaction-to-transfer diagnostic ratio;
- characteristic-time identity;
- overall sequential-resistance coefficient;
- resistance fractions;
- resistance-fraction summation;
- sensitivity to reaction and transfer improvement;
- explicit dominance classification;
- invalid-input rejection.

### Cavitation-Assisted Comparison

- apparent enhancement factor;
- product-based sulfur accounting;
- incremental sulfur benefit;
- incremental electrical energy;
- reciprocal energy metrics;
- hydraulic power;
- estimated pump-drive electrical demand;
- cavitation number;
- nominal inventory turnovers;
- rejection of non-equivalent comparison bases;
- handling of zero or negative incremental benefit;
- pressure and efficiency safeguards.

> **Test boundary**
>
> Passing tests confirms that the Python implementation is internally consistent with the documented equations, units, assumptions, and authoritative inputs.
>
> It does not validate the illustrative parameters as experimental data and does not establish industrial process performance.

---

## 10. Continuous Integration

The workflow:

```text
.github/workflows/python-tests.yml
```

runs automatically on:

- pushes to `main`;
- pull requests;
- manual workflow dispatch.

It validates the repository using:

- Python 3.10;
- Python 3.11;
- Python 3.12;
- Python 3.13.

For every Python version, the workflow:

1. checks Python syntax;
2. validates the authoritative CSV dataset;
3. runs the HDS example;
4. runs the ODS example;
5. runs the cavitation example;
6. runs all scientific and numerical tests.

The badge at the top of this README reports the current workflow status.

---

## 11. Example 1 — HDS Internal-Diffusion Screening

### 11.1 Model

The HDS example evaluates a simplified first-order reaction in an isothermal spherical porous catalyst particle.

The Thiele modulus is:

```math
\phi
=
R_p
\sqrt{
\frac{k_v}{D_{\mathrm{eff}}}
}
```

where:

- $R_p$ is particle radius;
- $k_v$ is an intrinsic first-order coefficient on a compatible catalyst-particle-volume basis;
- $D_{\mathrm{eff}}$ is effective intraparticle diffusivity.

The spherical effectiveness factor is:

```math
\eta
=
\frac{3}{\phi^2}
\left(
\frac{\phi}{\tanh\phi}-1
\right)
```

The model-implied Weisz–Prater parameter is:

```math
C_{\mathrm{WP}}
=
\eta\phi^2
```

This last relationship is a consistency identity for the stated first-order spherical model.

An experimental Weisz–Prater assessment should instead use:

- observed rate on a particle-volume basis;
- sulfur concentration at the external particle surface;
- independently justified effective diffusivity;
- stated particle geometry.

### 11.2 Default Illustrative Results

```text
Thiele modulus, phi          : 2.2361
Effectiveness factor         : 0.7726
Model-implied C_WP           : 3.8632
Internal utilization loss   : 22.74 %
```

The screening statement is:

```text
Significant reaction-diffusion coupling in this simplified model
```

### 11.3 Interpretation

The result indicates that internal concentration gradients reduce calculated particle utilization under the stated assumptions.

It does not demonstrate that an industrial HDS reactor is diffusion limited.

A rigorous assessment must also consider:

- sulfur speciation;
- intrinsic reaction order;
- coefficient basis;
- hydrogen availability and transfer;
- external film resistance;
- competitive adsorption;
- catalyst wetting;
- pore-size distribution;
- effective diffusivity;
- catalyst deactivation;
- coke and metal deposition;
- temperature and pressure;
- feed composition;
- reactor hydrodynamics.

### 11.4 Model Assumptions

The example assumes:

- spherical geometry;
- first-order intrinsic kinetics;
- isothermal operation;
- constant effective diffusivity;
- uniform pore structure;
- no external-film resistance;
- no deactivation;
- known particle-surface concentration.

---

## 12. Example 2 — ODS Reaction–Transfer Screening

### 12.1 Model

The ODS example compares a compatible pseudo-first-order reaction coefficient with an effective first-order transfer coefficient:

```math
Da_{\mathrm{diag}}
=
\frac{
k_{\mathrm{rxn}}
}{
k_{\mathrm{mt,eff}}
}
```

Using characteristic times:

```math
\tau_{\mathrm{rxn}}
=
\frac{1}{k_{\mathrm{rxn}}}
```

```math
\tau_{\mathrm{mt}}
=
\frac{1}{k_{\mathrm{mt,eff}}}
```

therefore:

```math
Da_{\mathrm{diag}}
=
\frac{
\tau_{\mathrm{mt}}
}{
\tau_{\mathrm{rxn}}
}
```

The simplified overall coefficient for two linear sequential resistances is:

```math
\frac{1}{k_{\mathrm{overall}}}
=
\frac{1}{k_{\mathrm{rxn}}}
+
\frac{1}{k_{\mathrm{mt,eff}}}
```

The reaction and transfer resistance fractions are based on their characteristic times.

### 12.2 Basis Requirement

The diagnostic ratio is dimensionless only when both coefficients use compatible:

- concentration bases;
- phase-volume bases;
- time bases;
- transported-species definitions.

If partition equilibrium, phase ratio, chemical enhancement, or concentration conversion is required, it must be incorporated consistently into the effective transfer coefficient.

The ratio is not a universal Damköhler-number definition.

### 12.3 Default Illustrative Results

```text
Diagnostic ratio, k_rxn/k_mt       : 4.0000
Reaction characteristic time       : 50.00 s
Transfer characteristic time       : 200.00 s
Overall characteristic time        : 250.00 s
Overall series coefficient          : 4.0000e-03 s^-1
Reaction resistance contribution   : 20.00 %
Transfer resistance contribution   : 80.00 %
```

The selected illustrative dominance criterion is 80% of the modeled total resistance.

The resulting screening statement is:

```text
External-transfer-dominated tendency in the simplified two-resistance model
```

### 12.4 Equal-Factor Sensitivity

When the reaction coefficient is doubled:

```text
Predicted overall-coefficient gain : 11.11 %
```

When the effective transfer coefficient is doubled:

```text
Predicted overall-coefficient gain : 66.67 %
```

Under the stated linear assumptions, improving the larger resistance produces the greater modeled benefit.

### 12.5 Interpretation Limits

The result is a diagnostic hypothesis, not experimental proof of mass-transfer control.

A real ODS assessment should examine:

- identity of the transferred species;
- sulfur-species chemistry;
- oxidant concentration and decomposition;
- catalyst or promoter partitioning;
- liquid–liquid equilibrium;
- interfacial reaction;
- phase-volume ratio;
- droplet-size distribution;
- changing interfacial area;
- mixing and hydrodynamics;
- emulsification;
- residence-time distribution;
- extraction or adsorption after oxidation;
- solvent recovery;
- final product sulfur.

Chemical conversion must be distinguished from sulfur removal after downstream separation.

---

## 13. Example 3 — Cavitation-Assisted Screening

### 13.1 Comparison Boundary

The cavitation example compares:

- a defined non-cavitating reference;
- a cavitation-assisted case;
- a documented hydraulic operating point.

Direct subtraction requires equivalent:

- initial sulfur inventory;
- feed volume;
- treatment time;
- initial temperature;
- final temperature.

Experimental comparison must additionally establish equivalent:

- feed chemistry;
- sulfur speciation;
- analytical methods;
- separation procedures;
- product recovery;
- full temperature history;
- sulfur-balance boundary.

### 13.2 Apparent Enhancement

The apparent enhancement factor is:

```math
F_{\mathrm{app}}
=
\frac{
k_{\mathrm{app,HC}}
}{
k_{\mathrm{app,ref}}
}
```

It compares fitted apparent coefficients only.

It does not prove:

- intrinsic kinetic enhancement;
- radical formation;
- a cavitation-specific chemical mechanism;
- industrial usefulness.

### 13.3 Product-Based Sulfur Metric

The example calculates sulfur absent from the recovered product:

```math
m_{S,\mathrm{excluded}}
=
m_{S,\mathrm{feed}}
-
m_{S,\mathrm{recovered\ product}}
```

The incremental product-based benefit is:

```math
\Delta m_S
=
m_{S,\mathrm{excluded,HC}}
-
m_{S,\mathrm{excluded,ref}}
```

This is not a complete sulfur balance.

Sulfur may remain in:

- extraction solvent;
- water;
- gas;
- solids;
- catalyst;
- adsorbent;
- deposits;
- lost hydrocarbon;
- samples;
- unidentified products.

### 13.4 Incremental Energy Metrics

Incremental electrical energy is:

```math
\Delta E
=
E_{\mathrm{HC}}
-
E_{\mathrm{ref}}
```

For positive incremental sulfur benefit and positive incremental energy:

```math
EN_S
=
\frac{
\Delta m_S
}{
\Delta E
}
```

and:

```math
SEC_S
=
\frac{
\Delta E
}{
\Delta m_S
}
```

These metrics are intentionally not calculated when the incremental sulfur benefit or incremental energy is zero or negative.

### 13.5 Hydraulic Cross-Check

Hydraulic power is:

```math
P_{\mathrm{hydraulic}}
=
\Delta P Q
```

Estimated pump-drive electrical power is:

```math
P_{\mathrm{electrical,est}}
=
\frac{
P_{\mathrm{hydraulic}}
}{
\eta_{\mathrm{pump}}\eta_{\mathrm{drive}}
}
```

Measured total electrical energy remains the preferred basis when it covers the declared process boundary.

### 13.6 Cavitation Number

The example uses:

```math
\sigma
=
\frac{
p_{\mathrm{ref}}-p_v
}{
\frac{1}{2}\rho v^2
}
```

where all pressures are absolute and the pressure and velocity locations must be defined.

The cavitation number is a hydrodynamic descriptor.

Equal values do not guarantee equal:

- cavity population;
- collapse intensity;
- radical production;
- residence pattern;
- erosion;
- chemical performance;
- scale-up behavior.

### 13.7 Default Illustrative Results

```text
Apparent enhancement factor                 : 3.0000
Incremental product-based sulfur benefit    : 3.500 g
Incremental electrical energy               : 0.7500 kWh
Incremental sulfur per additional energy    : 4.6667 g S/kWh
Incremental specific energy                 : 0.214286 kWh/g S
Incremental specific energy, kilogram basis : 214.286 kWh/kg S
Hydraulic power                             : 800.00 W
Estimated pump-drive electrical power       : 1269.84 W
Estimated pump-drive electrical energy      : 0.6349 kWh
Cavitation number, stated definition        : 0.5661
Nominal feed-volume turnovers               : 18.00
```

The nominal turnover value is circulated loop volume divided by liquid inventory.

It is not the number of identical cavitation events experienced by every fluid element. A recirculating system has a treatment-history distribution governed by mixing, bypassing, and residence-time behavior.

### 13.8 Required Validation

A defensible cavitation-assisted study should include:

- a non-cavitating hydrodynamic control;
- a matched thermal control;
- measured pressure and flow histories;
- measured electrical power;
- sulfur speciation;
- complete sulfur balance;
- oxidant utilization;
- downstream separation;
- product recovery and quality;
- erosion and corrosion assessment;
- fouling and emulsion evaluation;
- durability testing;
- process-safety review;
- pilot-scale verification.

---

## 14. Validation Requirements

A defensible validation program should include, where applicable:

1. representative feed characterization;
2. sulfur speciation before and after treatment;
3. validated analytical methods;
4. blanks, controls, and reference cases;
5. sulfur-balance closure;
6. distinction between conversion, transfer, adsorption, and removal;
7. repeat experiments and uncertainty estimates;
8. independent mass-transfer measurements;
9. internal-diffusion assessment;
10. adsorption capacity and breakthrough evaluation;
11. oxidant or hydrogen utilization;
12. phase-separation and product-quality assessment;
13. measured energy and pressure drop;
14. catalyst or adsorbent durability;
15. corrosion, erosion, fouling, and materials compatibility;
16. realistic feed-variability testing;
17. pilot-scale verification before industrial extrapolation;
18. predefined acceptance criteria.

Detailed guidance is provided in:

- [Validation guidelines](docs/validation-guidelines.md)

---

## 15. Evidence and Maturity

| Repository component | Classification | Interpretation |
|---|---|---|
| Reaction–transport concepts | Established engineering basis within stated assumptions | Require correct units, geometry, rate law, and boundary conditions |
| Regime framework | **E3 — Engineering screening framework** | Structured diagnostic logic requiring system-specific validation |
| Equations and indicators | Established relationships integrated into an **E3 prototype** | Useful for screening but not universal correlations |
| Validated parameter loader | **E3 supporting infrastructure** | Enforces dataset structure and consistency, not physical validity |
| Python examples | **E3 — Executable demonstrations** | Reproducible illustrative calculations, not plant models |
| Automated tests | Implementation verification | Confirm software consistency, not experimental validation |
| CSV data | Illustrative only | Not measured pilot or industrial data |
| Primary paper | Open technical preprint | Scientific and engineering basis for the framework |
| Industrial design claims | Not established | Require independent data, safety analysis, pilot operation, and detailed engineering |

The repository does not provide:

- universal kinetic constants;
- validated catalyst or adsorbent datasets;
- a complete reactor model;
- a complete process simulator;
- proprietary cavitation geometry;
- validated radical-generation correlations;
- detailed process economics;
- process-safety calculations;
- materials-selection certification;
- guaranteed product specifications;
- validated industrial scale-up correlations.

---

## 16. Responsible Use

Use this repository for:

- early-stage technical screening;
- process diagnosis;
- experimental planning;
- sensitivity analysis;
- reaction–transport comparison;
- internal-diffusion screening;
- preliminary process-intensification assessment;
- identification of missing evidence;
- definition of validation requirements;
- transparent communication of assumptions;
- reproducible educational demonstrations.

Do not use it as:

- a substitute for measured kinetic or transport data;
- a final reactor-design calculation;
- a catalyst-selection guarantee;
- proof of a cavitation mechanism;
- a process-safety analysis;
- a techno-economic assessment;
- an industrial performance warranty;
- a regulatory or emissions-compliance model.

All real applications require independent engineering review and explicit documentation of the validated applicability domain.

---

## 17. Scientific and Engineering Basis

### Primary Framework

**Reaction–Transport Regime Analysis for Desulfurization of Gas and Petroleum Streams: An Engineering Diagnostic Framework**

- DOI: [10.5281/zenodo.20095695](https://doi.org/10.5281/zenodo.20095695)
- Repository copy: [reaction-transport-regime-analysis-desulfurization.pdf](paper/reaction-transport-regime-analysis-desulfurization.pdf)
- Paper information: [paper/README.md](paper/README.md)

This paper develops the reaction–transport–separation framework underlying the repository.

### Supporting Process-Intensification Framework

**Industrial Usefulness and Technology Selection in Process Intensification: Energy-Normalized Metrics for Hydrodynamic Cavitation**

- DOI: [10.5281/zenodo.20593905](https://doi.org/10.5281/zenodo.20593905)

This supporting framework introduces incremental, energy-normalized, and system-level decision criteria for determining whether an intensification technology creates useful process benefit after penalties and uncertainty are considered.

---

## 18. Citation

Repository citation metadata is provided in:

- [`CITATION.cff`](CITATION.cff)

Repository DOI:

- [10.5281/zenodo.21278796](https://doi.org/10.5281/zenodo.21278796)

When using the scientific framework, also cite the primary paper:

> Saylam, A. (2026). *Reaction–Transport Regime Analysis for Desulfurization of Gas and Petroleum Streams: An Engineering Diagnostic Framework*. Zenodo. https://doi.org/10.5281/zenodo.20095695

For reproducible use, identify:

- repository version or commit;
- Python version;
- input dataset version;
- all modified parameters;
- assumptions;
- units;
- analytical and experimental sources.

---

## 19. Licensing and Reuse

- Repository software and associated software documentation are distributed under the [MIT License](LICENSE).
- Companion scientific papers remain subject to the licences stated in their respective Zenodo records and PDF files.
- The MIT software licence must not be assumed to override the separate licence of a scientific paper or third-party source.
- Third-party material remains subject to its original attribution and reuse conditions.

---

## 20. Public-Information Policy

The repository is intended for open engineering communication, reproducible screening calculations, and scientific discussion.

It does not intentionally include:

- confidential client data;
- proprietary industrial operating data;
- restricted project documents;
- employer-owned design information;
- undisclosed proprietary device geometry;
- unpublished third-party material without permission.

---

## 21. Author

**Prof. Dr. Ahmad Saylam**

R&D & Technology Development Leader  
Scientific & Engineering Consultant  
Duisburg, Germany

ORCID: [0000-0001-7484-1265](https://orcid.org/0000-0001-7484-1265)

---

## 22. Keywords

Desulfurization · hydrodesulfurization · oxidative desulfurization · adsorption · reaction engineering · mass transfer · internal diffusion · Thiele modulus · effectiveness factor · Weisz–Prater parameter · hydrodynamic cavitation · process intensification · sulfur balance · sulfur removal · energy-normalized performance · scale-up · validation · reproducible engineering
