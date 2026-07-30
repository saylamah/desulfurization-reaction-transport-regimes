# Desulfurization Regime Classification and Diagnostic Protocol

## Purpose

This document provides a structured engineering procedure for identifying the dominant and interacting limitations in desulfurization processes.

Measured sulfur removal may reflect the combined effects of:

- intrinsic reaction kinetics;
- external mass transfer;
- internal pore diffusion;
- adsorption equilibrium and capacity;
- reactant availability and utilization;
- hydrodynamics and residence-time distribution;
- downstream separation;
- catalyst or adsorbent deactivation;
- fouling, deposition, and materials effects;
- energy input and other process-intensification penalties.

A high apparent removal rate does not necessarily demonstrate fast intrinsic chemistry. Conversely, moderate intrinsic kinetics may produce strong overall performance when transport, contacting, reactor configuration, catalyst utilization, and separation are properly designed.

> **Evidence status**
>
> - This repository provides an **E3 engineering screening framework and executable research prototype**.
> - The regime classifications are diagnostic interpretations, not universally validated design rules.
> - A defensible classification requires compatible parameter bases, controlled perturbation experiments, sulfur-balance closure, uncertainty analysis, and system-specific validation.
> - A single sulfur-removal percentage or apparent rate constant is insufficient to establish the controlling regime.

---

## 1. Classification Philosophy

### 1.1 Three Levels of Limitation

For scientific clarity, the framework separates three different classes of limitation.

#### A. Mechanistic Reaction–Transport Limitations

These directly affect the rate at which sulfur species reach and react at an active interface:

- intrinsic reaction limitation;
- external mass-transfer limitation;
- internal diffusion limitation;
- adsorption or surface-accessibility limitation;
- hydrogen-, oxidant-, or reactant-utilization limitation.

#### B. Reactor and Process-Sequence Limitations

These arise from the way the complete process is configured and operated:

- hydrodynamic or residence-time-distribution limitation;
- phase maldistribution;
- separation limitation;
- catalyst or adsorbent deactivation;
- fouling, deposition, plugging, or emulsion formation.

#### C. Industrial Feasibility Constraints

These do not necessarily control the microscopic reaction rate but may determine whether an intensified process is technically useful:

- excessive energy demand;
- excessive reagent consumption;
- unacceptable pressure drop;
- erosion or corrosion;
- difficult maintenance;
- poor reliability;
- unfavorable scale-up behavior.

An energy penalty should therefore not be described as a fundamental kinetic regime. It is a **system-level feasibility constraint** that must be evaluated together with the mechanistic regime.

---

## 2. Prerequisites for Regime Classification

Before assigning a regime, define the system boundary and confirm the quality of the underlying data.

At minimum, document:

- feed identity and origin;
- total sulfur concentration;
- sulfur-species distribution;
- hydrocarbon or gas composition;
- viscosity, density, and relevant phase properties;
- temperature and pressure;
- reactor or contactor geometry;
- catalyst or adsorbent identity;
- particle size and pore characteristics;
- catalyst or adsorbent loading;
- hydrogen, oxidant, solvent, or reagent dose;
- phase ratio;
- flow rates;
- residence time or space velocity;
- mixing or recirculation conditions;
- downstream separation sequence;
- product sulfur specification;
- analytical method and detection limit;
- replicate variability;
- energy and pressure-drop boundary;
- reference-case definition.

A regime classification is unreliable when the process boundary, analytical basis, or reference condition is not defined.

---

## 3. Sulfur Conversion, Transfer, and Removal

Sulfur conversion and sulfur removal are not necessarily equivalent.

For a constant-volume batch system, apparent sulfur conversion may be expressed as:

```math
X_S
=
\frac{C_{S,0}-C_S}{C_{S,0}}
```

However, a decrease in sulfur concentration in one phase may result from:

- chemical transformation;
- transfer to another liquid phase;
- adsorption;
- precipitation;
- deposition on equipment;
- dilution;
- sampling loss;
- analytical interference.

A complete assessment should distinguish among:

1. **chemical conversion** of the original sulfur compound;
2. **phase transfer** of sulfur-containing material;
3. **temporary adsorption**;
4. **irreversible or recoverable removal**;
5. **final sulfur concentration in the treated product**.

The sulfur balance should include all accessible phases and deposits.

> **A reduction in one measured sulfur species or phase is not sufficient evidence of total sulfur removal.**

---

## 4. Reaction-Controlled Regime

### 4.1 Definition

A process is approximately reaction controlled when intrinsic chemical transformation is substantially slower than the relevant transport processes.

For a pseudo-first-order multiphase system, a diagnostic ratio may be written as:

```math
Da_{\mathrm{diag}}
=
\frac{k_{\mathrm{rxn}}}{k_La}
```

where:

- $k_{\mathrm{rxn}}$ is a reaction-related first-order coefficient;
- $k_La$ is a volumetric mass-transfer coefficient;
- both coefficients must use compatible time and concentration bases.

A reaction-controlled tendency corresponds approximately to:

```math
Da_{\mathrm{diag}}
\ll
1
```

This diagnostic expression is not a universal Damköhler-number definition. It is valid only when the two coefficients represent compatible characteristic times.

### 4.2 Expected Experimental Indicators

A reaction-controlled process may show:

- weak sensitivity to mixing intensity;
- weak sensitivity to interfacial area;
- weak sensitivity to catalyst-particle size when internal diffusion is absent;
- significant sensitivity to temperature;
- significant sensitivity to catalyst activity;
- significant sensitivity to catalyst loading at low conversion;
- sensitivity to hydrogen or oxidant concentration when included in the rate law;
- an apparent activation energy reasonably consistent with the proposed chemistry.

No single indicator is sufficient. Temperature also affects viscosity, diffusivity, equilibrium, and mass transfer.

### 4.3 Potential Improvement Strategies

Depending on the chemistry, appropriate strategies may include:

- increasing catalyst activity;
- increasing active-site accessibility;
- improving catalyst selectivity;
- increasing temperature within safe and product-quality limits;
- increasing hydrogen partial pressure;
- improving oxidant activation;
- increasing reactive-species availability;
- optimizing catalyst loading;
- changing solvent or reaction medium;
- modifying reaction chemistry.

Increasing mixing intensity is unlikely to provide a large benefit when intrinsic chemistry remains controlling.

### 4.4 Validation Requirements

A reaction-controlled interpretation should be supported by:

- mixing-independence tests;
- particle-size-independence tests where porous solids are used;
- repeatable kinetic data;
- a suitable rate law;
- an appropriate temperature range;
- confirmation that catalyst deactivation is negligible during the fitted interval;
- absence of significant phase-transfer or separation artifacts.

---

## 5. External Mass-Transfer-Limited Regime

### 5.1 Definition

External mass-transfer limitation occurs when transport from a bulk phase to an interface, catalyst surface, adsorbent surface, droplet, bubble, or reactive phase is slow relative to chemical reaction.

For a compatible pseudo-first-order system:

```math
Da_{\mathrm{diag}}
=
\frac{k_{\mathrm{rxn}}}{k_La}
```

A mass-transfer-controlled tendency corresponds approximately to:

```math
Da_{\mathrm{diag}}
\gg
1
```

For gas–liquid or liquid–liquid transfer:

```math
r_{\mathrm{mt}}
=
k_La
\left(
C^*-C
\right)
```

where:

- $k_La$ is the volumetric mass-transfer coefficient;
- $C^*$ is the equilibrium concentration corresponding to the interface;
- $C$ is the bulk concentration.

### 5.2 Expected Experimental Indicators

External transfer limitation may be indicated by:

- increasing rate with increasing agitation speed;
- increasing rate with increasing superficial gas or liquid velocity;
- increasing rate with increasing interfacial area;
- sensitivity to droplet or bubble size;
- sensitivity to viscosity;
- sensitivity to phase ratio;
- weak response to additional intrinsic catalyst activity;
- convergence toward a mixing-independent plateau at sufficiently high contacting intensity.

A plateau should not automatically be interpreted as intrinsic kinetics. It may also result from:

- reactant depletion;
- equilibrium;
- catalyst deactivation;
- oxidant exhaustion;
- downstream separation limitation;
- analytical limitations.

### 5.3 Diagnostic Methods

Useful methods include:

- agitation-speed variation;
- recirculation-rate variation;
- gas-velocity variation;
- interfacial-area measurement or estimation;
- droplet- or bubble-size characterization;
- independent measurement of $k_La$;
- comparison with Mears-type external transport criteria for porous catalysts;
- computational fluid dynamics where geometry and flow distribution are important.

Mears-type criteria must use internally consistent definitions of:

- observed rate;
- reaction order;
- particle size;
- external transfer coefficient;
- catalyst density;
- bulk concentration.

A threshold taken from the literature should not be used without checking the original variable basis and assumptions.

### 5.4 Potential Improvement Strategies

Potential responses include:

- increasing effective interfacial area;
- improving phase dispersion;
- improving bulk mixing;
- modifying reactor internals;
- improving gas–liquid or liquid–liquid contacting;
- reducing viscosity where technically acceptable;
- improving feed distribution;
- increasing recirculation;
- applying a suitable process-intensification device.

Increasing intrinsic catalyst activity alone may provide little benefit while external transfer remains controlling.

---

## 6. Internal Diffusion-Limited Regime

### 6.1 Definition

Internal diffusion limitation occurs when reactants cannot penetrate a porous catalyst or adsorbent sufficiently rapidly relative to reaction or adsorption.

For an isothermal spherical particle with a first-order volumetric reaction:

```math
\phi
=
R_p
\sqrt{
\frac{k_v}{D_{\mathrm{eff}}}
}
```

where:

- $\phi$ is the Thiele modulus;
- $R_p$ is particle radius;
- $k_v$ is a first-order coefficient on a compatible volumetric basis;
- $D_{\mathrm{eff}}$ is effective diffusivity.

The internal effectiveness factor is:

```math
\eta
=
\frac{
\text{actual total reaction rate in the porous particle}
}{
\text{rate if the complete particle were at the surface concentration}
}
```

For a first-order reaction in an isothermal sphere:

```math
\eta
=
\frac{3}{\phi^2}
\left(
\phi\coth\phi-1
\right)
```

### 6.2 Approximate Interpretation

```math
\phi
\ll
1
\quad\Rightarrow\quad
\eta
\approx
1
```

This indicates weak internal concentration gradients.

```math
\phi
\approx
1
```

This indicates coupled reaction and diffusion.

```math
\phi
\gg
1
\quad\Rightarrow\quad
\eta
\ll
1
```

This indicates substantial internal diffusion influence.

These are qualitative tendencies rather than universal thresholds.

### 6.3 Weisz–Prater Screening

A Weisz–Prater-type parameter may be expressed as:

```math
C_{\mathrm{WP}}
=
\frac{
r_{S,\mathrm{obs}}R_p^2
}{
C_{S,s}D_{\mathrm{eff}}
}
```

where:

- $r_{S,\mathrm{obs}}$ is the observed volumetric rate on a particle-volume basis;
- $C_{S,s}$ is sulfur-species concentration at the external particle surface;
- $R_p$ is particle radius;
- $D_{\mathrm{eff}}$ is effective diffusivity.

For a first-order spherical-particle model:

```math
C_{\mathrm{WP}}
=
\eta\phi^2
```

Values well below unity support weak internal diffusion influence. Values approaching or exceeding unity require more detailed analysis.

The interpretation is not universal because it depends on:

- rate basis;
- particle geometry;
- reaction order;
- surface concentration;
- effective diffusivity;
- non-isothermal effects.

Using bulk concentration in place of the surface concentration may be misleading when external film resistance is significant.

### 6.4 Expected Experimental Indicators

Internal diffusion may be indicated by:

- increasing observed rate as particle size decreases;
- effectiveness factor below unity;
- sublinear response to increased intrinsic catalyst activity;
- lower apparent activation energy than expected for intrinsic kinetics;
- sensitivity to pore structure;
- sensitivity to effective diffusivity;
- stronger limitation for larger or more highly substituted sulfur compounds;
- improved utilization with thinner catalyst layers or more accessible pore networks.

Particle-size variation must be interpreted carefully because it can also alter:

- external surface area;
- packing;
- pressure drop;
- wetting;
- attrition;
- hydrodynamics.

### 6.5 Potential Improvement Strategies

Potential responses include:

- reducing particle size;
- reducing diffusion length;
- increasing pore accessibility;
- optimizing pore-size distribution;
- increasing effective diffusivity;
- improving catalyst wetting;
- selecting hierarchical or structured porosity;
- reducing deposit formation;
- using catalyst structures compatible with the molecular size of the feed components.

For heavy petroleum fractions, diffusional behavior may be influenced by:

- large refractory sulfur compounds;
- high viscosity;
- resin and asphaltene content;
- pore blocking;
- coke or deposit formation;
- competitive adsorption.

---

## 7. Adsorption-, Capacity-, or Breakthrough-Limited Regime

### 7.1 Definition

Adsorptive desulfurization may be limited by several distinct phenomena:

- equilibrium capacity;
- adsorption kinetics;
- external film transfer;
- pore diffusion;
- competitive adsorption;
- mass-transfer-zone propagation;
- finite bed capacity;
- incomplete regeneration;
- irreversible fouling.

These phenomena should not be grouped under a single adsorption label without further discrimination.

### 7.2 Equilibrium Capacity

An idealized Langmuir isotherm is:

```math
q_e
=
\frac{
q_{\max}K_LC_e
}{
1+K_LC_e
}
```

where:

- $q_e$ is equilibrium loading;
- $q_{\max}$ is maximum monolayer capacity;
- $K_L$ is the Langmuir affinity coefficient;
- $C_e$ is equilibrium sulfur concentration.

Agreement with a Langmuir model does not prove:

- a homogeneous surface;
- monolayer adsorption;
- absence of competitive adsorption;
- a specific chemical mechanism.

### 7.3 Dynamic Bed Performance

Industrial adsorbent performance should be evaluated using:

- breakthrough concentration;
- breakthrough time;
- treated bed volumes;
- working capacity;
- mass-transfer-zone length;
- bed utilization;
- pressure drop;
- cycle duration;
- regeneration efficiency;
- capacity retention over repeated cycles.

A high equilibrium capacity measured in a batch test does not guarantee a long breakthrough time in a fixed bed.

### 7.4 Diagnostic Indicators

Capacity limitation may be indicated by:

- rapid initial removal followed by saturation;
- predictable breakthrough at a finite sulfur loading;
- weak response to additional contact time after equilibrium;
- improved performance with greater adsorbent inventory.

Kinetic or transport limitation may be indicated by:

- strong sensitivity to particle size;
- strong sensitivity to flow rate;
- long time to equilibrium;
- broad mass-transfer zones;
- poor use of nominal equilibrium capacity.

Competitive adsorption may be indicated by:

- lower sulfur capacity in real feed than in model compounds;
- sensitivity to aromatics, nitrogen compounds, water, oxygenates, or metals;
- changing sulfur selectivity with feed composition.

### 7.5 Potential Improvement Strategies

Potential responses include:

- increasing working capacity;
- improving sulfur selectivity;
- improving pore accessibility;
- optimizing particle size;
- improving regeneration;
- using staged beds;
- using guard beds;
- improving feed pretreatment;
- reducing competitive species;
- controlling breakthrough rather than relying only on equilibrium data.

---

## 8. Reactant-Utilization-Limited Regime

### 8.1 Definition

Hydrogen, oxidant, oxygen, promoter, or another reactive species may be supplied to the process but not used effectively for the target sulfur transformation.

Poor utilization may result from:

- inadequate distribution;
- interphase transfer resistance;
- local depletion;
- decomposition;
- non-selective side reactions;
- insufficient stoichiometric dose;
- excessive dose with poor selectivity;
- catalyst deactivation;
- poor recycle;
- nonuniform residence time.

### 8.2 Oxidant Utilization

A stoichiometric oxidant-utilization efficiency may be expressed as:

```math
\eta_{\mathrm{ox}}
=
\frac{
n_{\mathrm{ox,stoich,target}}
}{
n_{\mathrm{ox,supplied}}
}
```

where the stoichiometric target must specify:

- sulfur species;
- desired oxidation state;
- oxidant identity;
- oxidant purity;
- side reactions;
- residual oxidant;
- decomposition.

High sulfur conversion with low oxidant utilization may be technically or economically unfavorable.

### 8.3 Diagnostic Indicators

Reactant-utilization limitation may be indicated by:

- strong response to improved reactant distribution;
- strong response to staged dosing;
- residual untreated zones despite overall excess dose;
- high residual oxidant without corresponding sulfur conversion;
- significant oxidant decomposition;
- non-selective hydrogen consumption;
- sensitivity to gas–liquid contacting;
- local concentration gradients;
- improvement with recycle or redistribution.

### 8.4 Potential Improvement Strategies

Potential responses include:

- staged addition;
- improved distributor design;
- better phase contacting;
- optimized stoichiometry;
- improved catalyst selectivity;
- improved oxidant stability;
- reactant recycle;
- better residence-time control;
- reduction of side reactions.

---

## 9. Hydrodynamic- or Residence-Time-Distribution-Limited Regime

### 9.1 Definition

Hydrodynamic limitations occur when the reactor does not expose all material to the intended reaction or contact conditions.

Relevant phenomena include:

- bypassing;
- channeling;
- short-circuiting;
- stagnant zones;
- phase maldistribution;
- incomplete suspension;
- poor wetting;
- gas or liquid holdup variation;
- nonuniform shear;
- broad residence-time distribution;
- insufficient recirculation.

### 9.2 Diagnostic Indicators

Hydrodynamic limitation may be indicated by:

- strong dependence on geometry;
- strong dependence on flow regime;
- inconsistent results at equal nominal residence time;
- incomplete catalyst suspension;
- nonuniform temperature or concentration;
- poor scale-up based on volume alone;
- improvement after redistribution or internal modification;
- tracer evidence of bypassing or dead volume;
- dependence on orientation or liquid level.

### 9.3 Diagnostic Methods

Useful methods include:

- tracer residence-time-distribution testing;
- local pressure measurement;
- velocity or flow visualization;
- phase-holdup measurement;
- droplet- or bubble-size characterization;
- mixing-time measurement;
- computational fluid dynamics;
- scale-model experiments;
- local sampling where practical.

### 9.4 Potential Improvement Strategies

Potential responses include:

- improved feed distribution;
- revised reactor internals;
- modified recirculation;
- staged contacting;
- improved suspension;
- reduced bypassing;
- improved phase disengagement;
- hydrodynamically similar scale-up criteria.

Matching nominal residence time alone does not guarantee hydrodynamic similarity.

---

## 10. Separation-Limited Process

### 10.1 Definition

A process is separation limited when sulfur compounds are chemically transformed but the sulfur-containing products are not adequately removed from the treated stream.

This distinction is particularly important in oxidative desulfurization, where sulfides may be transformed to more polar sulfoxides or sulfones.

The oxidized products may still remain in the hydrocarbon phase unless they are removed by:

- solvent extraction;
- adsorption;
- precipitation;
- filtration;
- phase separation;
- membrane treatment;
- crystallization;
- polishing treatment.

### 10.2 Separation Efficiency

A separation efficiency may be expressed as:

```math
\eta_{\mathrm{sep}}
=
\frac{
m_{S,\mathrm{removed\ from\ product}}
}{
m_{S,\mathrm{available\ for\ separation}}
}
```

The final product sulfur concentration should be measured after the complete reaction and separation sequence.

### 10.3 Diagnostic Indicators

A separation-limited process may show:

- high conversion of the original sulfur species;
- limited reduction in final total sulfur;
- accumulation of sulfoxides or sulfones in the product;
- improved final sulfur after changing only the separation step;
- emulsion formation;
- poor phase disengagement;
- high solvent requirement;
- adsorbent saturation;
- loss of hydrocarbons into the extract phase;
- difficult solvent recovery.

### 10.4 Potential Improvement Strategies

Potential responses include:

- improved solvent selection;
- optimized solvent-to-feed ratio;
- staged extraction;
- improved phase disengagement;
- reduced emulsion formation;
- adsorption polishing;
- improved filtration;
- solvent recovery and recycle;
- improved sulfur-product recovery;
- integration of oxidation and separation boundaries.

A chemically successful oxidation stage is not sufficient when downstream sulfur removal is inadequate.

---

## 11. Deactivation-, Fouling-, or Durability-Limited Operation

### 11.1 Definition

A process may perform well initially but lose performance because the active material or equipment condition changes with time.

Potential causes include:

- catalyst poisoning;
- coke formation;
- sulfur or metal deposition;
- pore blockage;
- adsorbent saturation;
- active-phase leaching;
- oxidation-state changes;
- attrition;
- erosion;
- corrosion;
- fouling;
- plugging;
- emulsion accumulation.

### 11.2 Relative Activity

A normalized activity may be expressed as:

```math
a(t)
=
\frac{
r_{\mathrm{obs}}(t)
}{
r_{\mathrm{obs}}(0)
}
```

The rates must be compared under equivalent:

- feed conditions;
- temperature;
- pressure;
- reactant concentration;
- hydrodynamics;
- conversion basis.

### 11.3 Diagnostic Indicators

Deactivation or durability limitation may be indicated by:

- declining rate with time on stream;
- reduced capacity after regeneration;
- increasing pressure drop;
- changing product selectivity;
- increasing energy demand;
- increasing fouling or deposit mass;
- changes in catalyst composition;
- active-component leaching;
- poor repeatability between cycles.

### 11.4 Potential Improvement Strategies

Potential responses include:

- improved feed pretreatment;
- guard beds;
- regeneration optimization;
- improved materials selection;
- reduced operating severity;
- improved cleaning;
- anti-fouling design;
- better solids management;
- improved catalyst retention;
- revised maintenance intervals.

A steady-state regime classification is incomplete when performance changes materially with time.

---

## 12. Energy and Process-Intensification Feasibility

### 12.1 Scientific Classification

Energy demand is not itself a molecular kinetic regime.

It is a system-level constraint used to determine whether an intervention that improves local reaction or transport performance produces a useful net process benefit.

### 12.2 Incremental Sulfur Removal

The incremental sulfur removed relative to a defined reference is:

```math
\Delta m_S
=
m_{S,\mathrm{removed,int}}
-
m_{S,\mathrm{removed,ref}}
```

### 12.3 Incremental Energy Input

The additional energy input is:

```math
\Delta E
=
E_{\mathrm{int}}
-
E_{\mathrm{ref}}
```

### 12.4 Energy-Normalized Benefit

For positive incremental energy input:

```math
EN_S
=
\frac{
\Delta m_S
}{
\Delta E
}
```

The reciprocal specific energy demand is:

```math
SEC_S
=
\frac{
\Delta E
}{
\Delta m_S
}
```

Representative units include:

```math
[EN_S]
=
\mathrm{g\ S\,kWh^{-1}}
```

and:

```math
[SEC_S]
=
\mathrm{kWh\,g^{-1}\ S}
```

### 12.5 Complete Process Penalties

An intensified process should be assessed for:

- electrical energy;
- pumping duty;
- pressure drop;
- heating and cooling;
- oxidant production;
- solvent circulation;
- catalyst or adsorbent consumption;
- erosion;
- corrosion;
- fouling;
- emulsion formation;
- downstream separation;
- cleaning;
- maintenance;
- reliability;
- product yield and quality.

Higher apparent conversion does not automatically imply higher industrial usefulness.

---

## 13. Mixed and Transitional Regimes

### 13.1 Nature of Mixed Control

Real desulfurization systems frequently operate under mixed control.

Examples include:

- reaction plus liquid–liquid mass transfer in ODS;
- reaction plus internal diffusion in HDS;
- adsorption equilibrium plus pore diffusion;
- gas–liquid transfer plus reactive absorption of hydrogen sulfide;
- oxidation plus downstream separation;
- hydrodynamic maldistribution plus reactant-utilization limitation;
- transport improvement followed by catalyst deactivation.

### 13.2 Regime Changes During Operation

The controlling limitation may change with:

- time;
- conversion;
- temperature;
- pressure;
- catalyst age;
- particle size;
- feed composition;
- sulfur concentration;
- oxidant concentration;
- flow rate;
- scale.

Examples include:

- reaction control at low temperature changing to diffusion control at high temperature;
- kinetic control early in a batch changing to reactant depletion later;
- fresh-catalyst reaction control changing to pore blockage after deposition;
- oxidation control changing to separation control as sulfones accumulate.

### 13.3 Local and Global Regimes

Different parts of one reactor may operate in different regimes.

For example:

- inlet zones may experience reactant excess and rapid reaction;
- downstream zones may experience hydrogen or oxidant depletion;
- some particles may be externally well contacted while others remain poorly wetted;
- recirculation loops may contain different phase distributions;
- local cavitation intensity may vary strongly with geometry.

A single global rate coefficient can conceal these local differences.

### 13.4 Engineering Interpretation

For mixed regimes:

- avoid forcing the system into a single label;
- quantify the relative contribution of major resistances;
- report the operating range over which the classification applies;
- identify the regime most relevant to the engineering decision;
- design experiments that distinguish competing explanations.

---

## 14. Experimental Discrimination Matrix

The following perturbations can help distinguish regimes.

| Controlled perturbation | Primary observation | Possible interpretation | Important confounding factors |
|---|---|---|---|
| Increase agitation or recirculation | Rate increases | External transfer or hydrodynamic influence | Temperature rise, changing interfacial area, emulsion formation |
| Increase gas or liquid superficial velocity | Rate increases | Improved transfer or distribution | Residence-time change, pressure drop |
| Decrease catalyst-particle size | Rate increases | Internal diffusion influence | External area, packing, attrition, pressure drop |
| Increase catalyst loading | Linear rate increase | Kinetic or active-site dependence | Mixing, suspension, opacity, heat release |
| Increase temperature | Strong rate increase | Reaction sensitivity | Viscosity, equilibrium, diffusivity, deactivation |
| Increase hydrogen or oxidant supply | Rate increases | Reactant availability or kinetic dependence | Transfer, decomposition, selectivity |
| Improve distribution without changing chemistry | Performance increases | Hydrodynamic or utilization limitation | Residence-time changes |
| Improve only the separation step | Final sulfur decreases | Separation limitation | Dilution or product loss |
| Increase adsorbent inventory | Breakthrough delayed | Capacity limitation | Flow and mass-transfer-zone changes |
| Decrease adsorbent particle size | Faster uptake or sharper breakthrough | Pore or film transfer influence | Pressure drop |
| Repeat operating cycles | Performance declines | Deactivation, fouling, or regeneration limitation | Feed variability |
| Increase intensification severity | Rate increases but energy-normalized benefit declines | Diminishing industrial usefulness | Incorrect energy boundary |

No perturbation should be interpreted in isolation.

---

## 15. Practical Diagnostic Sequence

A defensible assessment should proceed in the following order.

### Step 1 — Define the Decision

Specify whether the objective is to:

- increase conversion;
- reduce final total sulfur;
- improve refractory sulfur removal;
- extend catalyst life;
- reduce energy;
- reduce chemical consumption;
- improve throughput;
- improve product quality;
- improve scale-up reliability.

### Step 2 — Define the Reference Case

Document:

- feed;
- sulfur species;
- operating conditions;
- reactor configuration;
- catalyst or adsorbent;
- analytical method;
- energy input;
- separation sequence;
- baseline performance.

### Step 3 — Establish Sulfur Speciation and Balance

Measure, where possible:

- initial sulfur species;
- transformed sulfur species;
- sulfur in all phases;
- sulfur on solids;
- sulfur in deposits;
- final product sulfur.

### Step 4 — Check Analytical Reliability

Confirm:

- calibration;
- detection limits;
- sampling consistency;
- phase homogeneity;
- replicate variability;
- recovery;
- matrix effects.

### Step 5 — Evaluate Time Dependence

Determine whether performance is:

- stable;
- transient;
- deactivating;
- capacity limited;
- affected by accumulation.

### Step 6 — Test Hydrodynamic Sensitivity

Vary, where appropriate:

- agitation;
- recirculation;
- superficial velocity;
- gas flow;
- phase ratio;
- distribution conditions.

### Step 7 — Test Particle-Scale Transport

Evaluate:

- particle-size effects;
- Thiele modulus;
- effectiveness factor;
- Weisz–Prater parameter;
- Mears-type external transfer screening;
- pore accessibility.

### Step 8 — Test Kinetic Sensitivity

Evaluate:

- temperature;
- catalyst loading;
- reactant concentration;
- hydrogen partial pressure;
- oxidant concentration;
- reaction time.

### Step 9 — Evaluate Adsorption and Capacity

Measure:

- equilibrium loading;
- uptake kinetics;
- breakthrough;
- working capacity;
- regeneration;
- cycle stability.

### Step 10 — Evaluate Separation

Measure:

- sulfur conversion;
- sulfur distribution;
- extraction efficiency;
- adsorption polishing;
- phase disengagement;
- solvent recovery;
- final product sulfur.

### Step 11 — Quantify Process Penalties

Measure or estimate:

- energy;
- pressure drop;
- chemical consumption;
- catalyst or adsorbent consumption;
- erosion;
- corrosion;
- fouling;
- maintenance;
- product loss.

### Step 12 — Assign a Regime with Confidence Level

Report:

- dominant limitation;
- secondary limitations;
- evidence supporting each classification;
- conflicting evidence;
- operating range;
- confidence level;
- required next experiment.

### Step 13 — Modify the Controlling Limitation

Select the intervention most directly related to the diagnosed bottleneck.

### Step 14 — Reassess the Complete Process

After modification, repeat:

- sulfur balance;
- product-quality assessment;
- energy assessment;
- separation assessment;
- durability assessment;
- uncertainty analysis.

---

## 16. Confidence in the Regime Assignment

A regime classification should include a confidence statement.

### High Confidence

A high-confidence classification generally requires:

- multiple independent diagnostic tests;
- reproducible data;
- compatible trends;
- closed or adequately reconciled sulfur balance;
- consistent transport and kinetic calculations;
- uncertainty small enough to distinguish competing regimes.

### Moderate Confidence

A moderate-confidence classification may be based on:

- limited but consistent perturbation testing;
- incomplete direct transport measurements;
- acceptable repeatability;
- some remaining alternative explanations.

### Low Confidence

A low-confidence classification results when:

- only one conversion value is available;
- only an apparent rate constant is available;
- sulfur speciation is incomplete;
- sulfur balance is missing;
- mass-transfer parameters are assumed;
- no controlled perturbation tests have been performed;
- analytical uncertainty is comparable to the observed effect.

Low-confidence classifications should be described as hypotheses rather than conclusions.

---

## 17. Scale-Up Implications

### Reaction-Controlled Systems

Scale-up should preserve:

- temperature;
- pressure;
- catalyst-to-feed ratio;
- reactive-species concentration;
- residence time;
- catalyst state.

However, transport limitations may emerge at larger scale even when absent in the laboratory.

### External Transfer-Controlled Systems

Scale-up should preserve or predict:

- interfacial area;
- mass-transfer coefficient;
- phase holdup;
- velocity;
- mixing power;
- contactor geometry;
- distribution quality.

Equal power per unit volume does not automatically guarantee equal $k_La$ or equal phase behavior.

### Internal Diffusion-Controlled Systems

Scale-up must preserve:

- particle size;
- pore structure;
- wetting;
- effective diffusivity;
- temperature;
- catalyst history.

Changing pellet size or catalyst geometry can change effectiveness factor and pressure drop simultaneously.

### Adsorption Systems

Scale-up should address:

- breakthrough behavior;
- mass-transfer-zone length;
- bed geometry;
- superficial velocity;
- pressure drop;
- heat effects;
- regeneration;
- cycle stability.

### Hydrodynamically Limited Systems

Scale-up requires attention to:

- residence-time distribution;
- bypassing;
- distribution;
- mixing time;
- phase segregation;
- local shear;
- recirculation topology.

### Separation-Limited Systems

Scale-up must include:

- phase disengagement;
- solvent inventory;
- extraction staging;
- adsorbent demand;
- product recovery;
- solvent recovery;
- waste handling.

### Intensified Systems

Scale-up should not rely on one descriptor alone.

For hydrodynamic cavitation, relevant parameters may include:

- pressure boundary conditions;
- pressure recovery;
- characteristic velocity;
- cavitation number;
- geometry;
- flow rate;
- fluid properties;
- number of passes;
- residence pattern;
- specific energy;
- erosion location.

Equal cavitation number does not guarantee equal cavity dynamics or equal chemical performance.

---

## 18. Evidence and Responsible Use

| Classification element | Evidence status | Required caution |
|---|---|---|
| Reaction–transport concepts | Established engineering basis | Must be applied using compatible assumptions and units |
| Thiele modulus and effectiveness factor | Established for defined reaction and geometry assumptions | Not universally transferable to arbitrary kinetics or geometries |
| Weisz–Prater and Mears-type screening | Established diagnostic approaches | Variable basis and threshold assumptions must be verified |
| Repository regime framework | **E3 — Engineering screening framework** | Requires system-specific validation |
| Default thresholds | Qualitative screening guidance | Not universal industrial acceptance criteria |
| Example data | Illustrative | Not pilot or industrial design data |
| Scale-up conclusions | Not established by the repository alone | Require experimental and engineering validation |

Use this framework for:

- process diagnosis;
- experimental design;
- identification of missing data;
- sensitivity analysis;
- comparison of alternative interventions;
- preliminary process-intensification assessment;
- transparent communication of assumptions.

Do not use it as:

- a final reactor-design model;
- a catalyst-selection guarantee;
- a universal regime map;
- an industrial performance warranty;
- a process-safety analysis;
- an emissions-compliance model;
- a substitute for pilot testing.

---

## 19. Core Decision Principles

> **Do not intensify a process before identifying what limits it.**

> **Do not describe conversion in one phase as total sulfur removal without a sulfur balance.**

> **Do not combine kinetic and transport coefficients unless their dimensions and bases are compatible.**

> **Do not infer intrinsic kinetics from an apparent rate constant without excluding transport, deactivation, and separation effects.**

> **Do not select a technology using removal percentage alone; evaluate the complete process and its penalties.**

The preferred engineering solution is the one that removes or reduces the controlling bottleneck while maintaining acceptable:

- product quality;
- energy demand;
- reagent consumption;
- separation performance;
- materials compatibility;
- operability;
- reliability;
- maintainability;
- safety;
- scale-up transferability.

---

## 20. Related Repository Resources

- [Repository README](../README.md)
- [Framework summary](framework-summary.md)
- [Core equations](equations.md)
- [Validation guidelines](validation-guidelines.md)
- [HDS internal-diffusion example](../examples/hds_regime_example.py)
- [ODS reaction–mass-transfer example](../examples/ods_mass_transfer_example.py)
- [Cavitation-intensification example](../examples/cavitation_intensification_example.py)
- [Illustrative parameter table](../data/example_parameters.csv)

---

## 21. Selected Technical References

1. Mears, D. E. *Tests for Transport Limitations in Experimental Catalytic Reactors*. Industrial & Engineering Chemistry Process Design and Development, 1971. DOI: `10.1021/i260040a020`.

2. *Phenomena Affecting Catalytic Reactions at Solid–Liquid Interfaces*. ACS Catalysis, 2017. DOI: `10.1021/acscatal.6b02532`.

3. Sampanthar, J. T.; Xiao, H.; Dou, J.; Nah, T. Y.; Rong, X.; Kwan, W. P. *A Novel Oxidative Desulfurization Process to Remove Refractory Sulfur Compounds from Diesel Fuel*. Applied Catalysis B: Environmental, 2006. DOI: `10.1016/j.apcatb.2005.09.007`.

4. *Removal of Sulfone Compounds Formed in Oxidative Desulfurization of Middle Distillate*. Fuel, 2017. DOI: `10.1016/j.fuel.2017.01.003`.

5. Saylam, A. *Reaction–Transport Regime Analysis for Desulfurization of Gas and Petroleum Streams: An Engineering Diagnostic Framework*. Zenodo, 2026. DOI: `10.5281/zenodo.20095695`.

---

## 22. Summary

Desulfurization performance should be interpreted as the result of coupled chemistry, transport, adsorption, hydrodynamics, separation, durability, and process penalties.

A technically defensible regime classification requires:

- a defined system boundary;
- sulfur speciation;
- sulfur-balance closure;
- compatible units and coefficient bases;
- controlled perturbation testing;
- time-dependent performance assessment;
- uncertainty analysis;
- a stated confidence level;
- system-specific validation.

The present repository provides an **E3 engineering screening framework** for organizing this diagnosis. It does not replace detailed kinetic analysis, pilot testing, process safety, or industrial design.
