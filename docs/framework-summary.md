# Framework Summary

## Reaction–Transport Regime Analysis for Desulfurization

Desulfurization performance is governed not only by reaction chemistry, but by the coupling of:

- intrinsic chemical kinetics;
- external mass transfer;
- internal diffusion;
- adsorption and surface accessibility;
- hydrodynamics and phase contacting;
- reactant utilization;
- catalyst or adsorbent durability;
- downstream separation;
- energy input;
- feed composition and sulfur speciation.

This framework provides a structured engineering methodology for diagnosing the controlling or interacting regime in sulfur-removal processes and identifying the most defensible direction for process improvement.

> **Evidence status**
>
> - **E3 — Engineering screening framework:** the regime logic, equations, Python examples, and illustrative data support transparent diagnosis and early-stage comparison.
> - **Not a validated industrial model:** the framework does not provide universally transferable kinetic constants, catalyst data, mass-transfer correlations, design guarantees, or economic thresholds.
> - **System-specific validation is required:** real applications require measured data, uncertainty analysis, sulfur closure, durability assessment, and pilot-scale evidence.

---

## 1. Core Engineering Principle

A desulfurization process should not be optimized solely by increasing:

- catalyst activity;
- oxidant dosage;
- hydrogen partial pressure;
- temperature;
- pressure;
- mixing intensity;
- residence time;
- process-intensification severity.

The first engineering question is:

> **Which physical, chemical, or separation step actually controls the observed sulfur-removal performance under the defined operating conditions?**

Improving a non-controlling step may increase cost or complexity without materially improving overall performance.

---

## 2. System Boundary

A defensible regime analysis begins by defining the process boundary.

At minimum, document:

- feed type and sulfur concentration;
- sulfur-species distribution;
- temperature and pressure;
- phase configuration;
- reactor or contactor type;
- catalyst, adsorbent, solvent, oxidant, or hydrogen system;
- residence time or space velocity;
- mixing and hydrodynamic conditions;
- product-quality targets;
- downstream separation steps;
- reference process;
- energy and chemical inputs;
- analytical methods;
- uncertainty and detection limits.

Without a defined boundary, apparent performance improvements may not be transferable or comparable.

---

## 3. Representative Desulfurization Pathways

The framework can be applied to:

- hydrodesulfurization (HDS);
- oxidative desulfurization (ODS);
- adsorptive desulfurization;
- reactive adsorptive desulfurization;
- catalytic oxidation and sweetening;
- radical-assisted oxidation;
- gas-stream sulfur removal;
- hydrodynamic-cavitation-assisted treatment;
- mixing- and dispersion-based process intensification.

The framework is diagnostic rather than technology-prescriptive. It does not assume that one pathway is superior for all feeds, sulfur species, reactor configurations, or scale-up constraints.

---

## 4. Diagnostic Quantities

Depending on the system, useful engineering quantities may include:

- apparent and intrinsic reaction-rate constants;
- external mass-transfer coefficients;
- interfacial area;
- volumetric mass-transfer coefficients;
- effective diffusivity;
- particle radius;
- Thiele modulus;
- effectiveness factor;
- Damköhler-type ratios;
- adsorption capacity;
- breakthrough time;
- oxidant or hydrogen utilization;
- sulfur conversion;
- sulfur selectivity;
- sulfur balance closure;
- specific energy consumption;
- energy-normalized sulfur removal;
- pressure drop;
- catalyst or adsorbent deactivation rate.

These quantities should be interpreted together rather than as isolated performance indicators.

Detailed equations are provided in:

- [Model equations](equations.md)

---

## 5. Reaction–Transport–Separation Regimes

### 5.1 Reaction-Controlled Regime

A process is reaction controlled when intrinsic chemical transformation is slow relative to relevant transport steps.

Typical indicators may include:

- strong sensitivity to temperature;
- strong sensitivity to catalyst activity;
- weak sensitivity to mixing or particle size;
- low utilization of available residence time;
- no clear evidence of interphase or pore-transport limitation.

Potential engineering responses include:

- improved catalyst activity or selectivity;
- increased reactive-species availability;
- adjusted temperature or pressure;
- revised catalyst formulation;
- improved reaction pathway or promoter selection.

Increasing mixing intensity is unlikely to provide a large benefit if intrinsic chemistry remains controlling.

---

### 5.2 External Mass-Transfer-Limited Regime

External mass-transfer limitation occurs when transport from the bulk phase to an interface or reactive surface is too slow.

Typical indicators may include:

- strong sensitivity to agitation, gas velocity, or dispersion;
- strong sensitivity to interfacial area;
- dependence on droplet or bubble size;
- weak response to increased intrinsic catalyst activity;
- concentration gradients between bulk and interface.

Potential engineering responses include:

- improved mixing;
- increased interfacial area;
- better phase dispersion;
- improved gas–liquid or liquid–solid contacting;
- redesigned reactor internals;
- hydrodynamic optimization.

---

### 5.3 Internal Diffusion-Limited Regime

Internal diffusion limitation occurs when reaction within a porous catalyst or adsorbent is faster than transport through the pore network.

Relevant diagnostic quantities include:

- Thiele modulus;
- effectiveness factor;
- effective diffusivity;
- particle radius;
- pore structure;
- intrinsic reaction rate.

Typical indicators may include:

- reduced catalyst utilization;
- strong particle-size sensitivity;
- weak response to additional external mixing;
- apparent activation behavior lower than the intrinsic reaction behavior;
- performance dependence on pore architecture.

Potential engineering responses include:

- reduced particle size;
- improved pore structure;
- higher effective diffusivity;
- adjusted catalyst geometry;
- moderated reaction severity;
- improved wetting or phase access.

---

### 5.4 Adsorption- or Capacity-Limited Regime

Adsorption or finite capacity may control when sulfur removal depends on surface occupancy, competitive adsorption, breakthrough, or regeneration.

Typical indicators may include:

- rapid initial removal followed by saturation;
- sensitivity to competing species;
- limited working capacity;
- regeneration-dependent performance;
- strong dependence on feed composition;
- incomplete reversibility.

Potential engineering responses include:

- improved adsorbent selectivity;
- greater working capacity;
- optimized regeneration;
- staged or guard-bed operation;
- feed pretreatment;
- better breakthrough management.

---

### 5.5 Reactant-Utilization-Limited Regime

Hydrogen, oxidant, or another reactive species may be present but poorly utilized.

Typical causes include:

- poor distribution;
- insufficient interphase transfer;
- decomposition or side reactions;
- non-selective consumption;
- local depletion;
- inadequate recycle;
- poor stoichiometric control.

Potential engineering responses include:

- improved dosing and distribution;
- better phase contacting;
- optimized stoichiometry;
- controlled addition;
- improved catalyst selectivity;
- recycle or staged addition.

---

### 5.6 Hydrodynamics-Limited Regime

Hydrodynamics may control when residence-time distribution, mixing, bypassing, channeling, or phase contacting prevents effective use of the available chemistry.

Typical indicators may include:

- strong geometry dependence;
- sensitivity to flow regime;
- broad or non-ideal residence-time distribution;
- phase maldistribution;
- stagnant zones;
- inconsistent scale-up performance.

Potential engineering responses include:

- reactor redesign;
- modified internals;
- improved distribution;
- recirculation;
- staged contacting;
- validated hydrodynamic scaling.

---

### 5.7 Separation-Limited Regime

A process may convert sulfur species without adequately removing the transformed sulfur from the treated stream.

This is especially important in oxidation-based systems.

Typical indicators may include:

- high chemical conversion but modest final sulfur removal;
- persistent oxidized sulfur in the product phase;
- emulsion formation;
- difficult solvent recovery;
- poor phase disengagement;
- adsorbent or polishing-bed overload.

Potential engineering responses include:

- improved extraction;
- optimized solvent selection;
- adsorption polishing;
- phase-separation improvement;
- reduced emulsion formation;
- revised product-recovery strategy.

A chemically successful step is not industrially useful when downstream separation is inadequate.

---

### 5.8 Energy- or Intensification-Limited Regime

An intensified process may increase apparent rate or removal while producing insufficient benefit relative to energy and operating penalties.

Relevant indicators include:

- incremental sulfur removed;
- additional energy demand;
- specific energy consumption;
- pressure drop;
- chemical consumption;
- erosion risk;
- maintenance burden;
- separation penalties.

Potential engineering responses include:

- lower severity;
- alternative device selection;
- improved reference-case definition;
- process integration;
- revised performance target;
- rejection of the intensification option.

---

### 5.9 Mixed or Transitional Regime

Several resistances may contribute materially at the same time.

Typical examples include:

- reaction and external mass transfer;
- reaction and internal diffusion;
- oxidation and downstream separation;
- hydrodynamics and oxidant utilization;
- transport improvement followed by catalyst deactivation.

Mixed regimes require combined experiments and models. Single-factor interpretation is usually insufficient.

Detailed regime logic is provided in:

- [Regime classification](regime-classification.md)

---

## 6. Diagnostic Workflow

A practical analysis can be organized into the following sequence.

### Step 1 — Define the Reference Case

Specify:

- feed;
- sulfur species;
- operating conditions;
- reactor configuration;
- catalyst or adsorbent;
- residence time;
- analytical method;
- energy input;
- downstream separation;
- baseline performance.

### Step 2 — Confirm the Sulfur Balance

Distinguish among:

- sulfur conversion;
- sulfur transfer between phases;
- adsorption;
- irreversible removal;
- analytical loss;
- unmeasured sulfur products.

A reported reduction in one phase is not automatically equivalent to total sulfur removal.

### Step 3 — Test Kinetic Sensitivity

Evaluate the response to:

- temperature;
- catalyst loading;
- catalyst activity;
- hydrogen or oxidant availability;
- reaction time.

### Step 4 — Test Transport Sensitivity

Evaluate the response to:

- mixing intensity;
- gas or liquid velocity;
- droplet or bubble size;
- interfacial area;
- catalyst-particle size;
- effective diffusivity;
- viscosity;
- flow regime.

### Step 5 — Evaluate Separation

Measure:

- phase disengagement;
- extraction efficiency;
- adsorbent loading;
- solvent recovery;
- product quality;
- sulfur distribution after treatment.

### Step 6 — Quantify Energy and Penalties

Document:

- electrical energy;
- pumping duty;
- pressure drop;
- heating duty;
- reagent consumption;
- erosion;
- fouling;
- cleaning;
- maintenance;
- reliability.

### Step 7 — Classify the Regime

Use the combined evidence to identify:

- dominant limitation;
- secondary limitations;
- mixed or transitional behavior;
- uncertainty in the classification.

### Step 8 — Design the Next Validation Experiment

Select the experiment that most clearly distinguishes among competing explanations.

---

## 7. Process-Intensification Perspective

Hydrodynamic cavitation and related intensification methods should be treated as enabling transport or reaction–transport layers rather than universal solutions.

Their value depends on whether they improve:

- interfacial renewal;
- mixing;
- dispersion;
- local mass transfer;
- oxidant utilization;
- radical generation, where chemically relevant;
- apparent reaction rate;
- sulfur removal per unit energy input.

An intensified process should be evaluated against a defined baseline using both technical benefit and process penalties.

Useful quantities include:

```text
F_app = k_app,intensified / k_app,reference
```

```text
EN_S = incremental sulfur removed / additional energy input
```

```text
SEC_S = additional energy input / incremental sulfur removed
```

These metrics are meaningful only when:

- the reference case is comparable;
- the sulfur balance is closed;
- product quality is maintained;
- downstream separation is included;
- energy boundaries are defined;
- uncertainty is reported.

---

## 8. Engineering Usefulness

The practical objective is not simply to maximize sulfur conversion under laboratory conditions.

A proposed improvement should be evaluated by asking whether it:

- addresses the actual controlling resistance;
- remains effective at relevant throughput;
- improves energy-normalized performance;
- reduces or justifies chemical consumption;
- maintains product quality;
- is compatible with downstream separation;
- remains controllable and reliable;
- avoids unacceptable erosion, fouling, or maintenance;
- retains value under feed variability;
- remains technically credible during scale-up.

A process improvement is not transferable merely because it produces a high removal percentage in a small laboratory system.

---

## 9. Validation Requirements

A defensible validation program should include, as applicable:

1. sulfur speciation before and after treatment;
2. a closed sulfur balance;
3. repeat experiments;
4. uncertainty estimates;
5. mass-transfer characterization;
6. catalyst or adsorbent durability;
7. oxidant or hydrogen utilization;
8. product-quality assessment;
9. downstream-separation performance;
10. energy and pressure-drop measurements;
11. materials-compatibility and erosion assessment;
12. realistic feed variability;
13. comparison with an appropriate reference process;
14. pilot-scale verification before industrial extrapolation.

Detailed guidance is provided in:

- [Validation guidelines](validation-guidelines.md)

---

## 10. Evidence and Maturity

| Component | Classification | Current interpretation |
|---|---|---|
| Regime-analysis methodology | **E3 — Engineering screening framework** | Structured diagnostic logic based on established reaction and transport concepts |
| Dimensionless and rate-based indicators | **E3 — Research prototype** | Useful for transparent comparison; require system-specific parameterization |
| Python examples | **E3 — Executable demonstrations** | Reproducible illustrative calculations, not validated plant models |
| Example parameter data | **Illustrative only** | Not measured pilot or industrial data |
| Industrial design claims | **Not established** | Require independent validation, safety analysis, and scale-up evidence |

The framework does not currently provide:

- universal kinetic constants;
- validated catalyst or adsorbent datasets;
- complete reactor hydrodynamics;
- a process simulator;
- validated economic thresholds;
- process-safety calculations;
- guaranteed product specifications;
- emissions-compliance predictions;
- device-specific industrial scale-up correlations.

---

## 11. Intended Application

The framework is intended for:

- early-stage technical screening;
- process diagnosis;
- comparative technology assessment;
- model development;
- experimental planning;
- sensitivity analysis;
- preliminary scale-up evaluation;
- identification of missing evidence;
- communication of assumptions and limitations.

It is not a substitute for:

- validated kinetic data;
- pilot-scale testing;
- detailed reactor design;
- materials compatibility assessment;
- process-safety analysis;
- techno-economic evaluation;
- regulatory review;
- independent engineering judgment.

---

## 12. Responsible Use

Use the framework to:

- organize technical evidence;
- identify likely controlling regimes;
- select discriminating experiments;
- compare improvement strategies;
- quantify incremental benefit;
- define validation requirements;
- support transparent engineering decisions.

Do not use it as:

- a final design calculation;
- a catalyst-selection guarantee;
- a universal correlation;
- an industrial performance warranty;
- an emissions-compliance model;
- a substitute for measured data.

All real applications require explicit documentation of:

- the system boundary;
- data sources;
- assumptions;
- uncertainties;
- applicability domain;
- validation status.

---

## 13. Related Repository Resources

- [Repository README](../README.md)
- [Model equations](equations.md)
- [Regime classification](regime-classification.md)
- [Validation guidelines](validation-guidelines.md)

The executable examples are located in:

```text
examples/
```

The illustrative parameter table is located at:

```text
data/example_parameters.csv
```

---

## 14. Summary

The framework is built around one central engineering principle:

> **Improve the controlling limitation, not merely the most visible process variable.**

Desulfurization performance should be interpreted as the result of coupled reaction, transport, adsorption, hydrodynamic, separation, and energy effects.

The present repository provides an **E3 engineering screening framework** for diagnosing these effects and planning validation. It does not replace system-specific data, pilot testing, or detailed engineering design.
