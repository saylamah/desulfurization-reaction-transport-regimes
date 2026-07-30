# Validation Guidelines for Desulfurization Reaction–Transport Regime Analysis

## Purpose

This document defines a scientifically rigorous validation framework for applying reaction–transport regime analysis to desulfurization systems.

The objective is to distinguish genuine process improvement from apparent performance gains caused by:

- incomplete sulfur accounting;
- inadequate sulfur speciation;
- analytical bias or matrix interference;
- uncontrolled mass-transfer effects;
- internal diffusion;
- non-equivalent reference conditions;
- catalyst or adsorbent deactivation;
- reactant depletion or inefficient utilization;
- incomplete downstream separation;
- unmeasured energy input;
- product loss or quality deterioration;
- erosion, corrosion, fouling, or other operability penalties;
- unjustified laboratory-to-pilot or pilot-to-industrial extrapolation.

> **Evidence status**
>
> - This repository provides an **E3 engineering screening framework and executable research prototype**.
> - The validation procedures organize technically defensible evidence but do not replace qualified laboratory practice, process-safety review, pilot testing, or detailed engineering.
> - Acceptance criteria must be defined for the specific feed, process, product specification, analytical uncertainty, and development stage.
> - A high sulfur-conversion value, apparent rate constant, or removal percentage is not sufficient by itself to validate a desulfurization process.

---

## 1. Validation Philosophy

### 1.1 Central Principle

A desulfurization result should be considered technically credible only when the following questions can be answered:

1. What sulfur species entered the process?
2. What sulfur species were transformed?
3. Where did the sulfur go?
4. Which reaction or transport mechanism controlled the observed performance?
5. Was the comparison made against a valid reference?
6. Was the improvement larger than the experimental uncertainty?
7. Was the final sulfur concentration measured after the complete treatment and separation sequence?
8. What energy, reagents, catalyst, adsorbent, solvent, and utilities were consumed?
9. Was product quality preserved?
10. Was performance maintained with time, feed variability, and repeated operation?
11. Can the controlling regime and process benefit be transferred to larger scale?

### 1.2 Validation Is Hierarchical

Validation should proceed through progressively stronger evidence levels.

#### Level A — Analytical Feasibility

Demonstrate that sulfur and relevant process variables can be measured reliably in the selected matrices.

#### Level B — Controlled Laboratory Proof

Demonstrate repeatable performance against appropriate blanks and reference cases.

#### Level C — Mechanistic and Regime Validation

Distinguish intrinsic reaction, mass transfer, internal diffusion, adsorption, hydrodynamics, reactant utilization, separation, and deactivation effects.

#### Level D — Integrated Process Validation

Demonstrate complete sulfur removal, separation performance, energy demand, product quality, and material compatibility.

#### Level E — Pilot-Scale Validation

Demonstrate stable performance at relevant throughput and operating duration using representative feed.

#### Level F — Industrial Qualification

Demonstrate operability, control, safety, reliability, maintenance, economics, and specification compliance under realistic operating variability.

Success at one level does not automatically establish success at the next.

---

## 2. Define the Validation Decision

Before experiments begin, define the engineering decision the validation program is intended to support.

Possible objectives include:

- demonstrating chemical conversion;
- reducing final total sulfur;
- removing specific refractory sulfur compounds;
- comparing catalysts or adsorbents;
- identifying the controlling regime;
- evaluating a process-intensification device;
- reducing temperature or pressure severity;
- reducing hydrogen or oxidant demand;
- improving throughput;
- extending catalyst or adsorbent life;
- validating downstream separation;
- qualifying a process for pilot testing;
- evaluating industrial scale-up.

The validation metrics and acceptance criteria must be aligned with the stated decision.

For example, a study intended to demonstrate oxidation chemistry does not, by itself, validate a complete oxidative-desulfurization process.

---

## 3. Define the System Boundary

A validation study must define the physical and accounting boundaries of the process.

Document:

- feed preparation;
- reaction or contacting stage;
- recirculation loops;
- gas supply;
- oxidant preparation;
- catalyst or adsorbent addition;
- heating and cooling;
- phase separation;
- extraction;
- filtration;
- adsorption polishing;
- solvent recovery;
- purge and vent streams;
- sampling losses;
- product recovery;
- cleaning and regeneration;
- energy measurement boundary.

The boundary determines what may legitimately be described as:

- sulfur conversion;
- sulfur removal;
- process energy;
- chemical consumption;
- product yield;
- waste generation.

A narrow boundary can overstate process performance by excluding separation, recovery, or auxiliary-energy requirements.

---

## 4. Define the Feed and Sulfur Speciation

Before evaluating performance, document the feed as completely as required by the intended application.

### 4.1 Minimum Feed Information

Record:

- feed type;
- feed source;
- sampling date or batch;
- storage conditions;
- total sulfur concentration;
- sulfur-species distribution, where measurable;
- hydrocarbon or gas composition;
- density;
- viscosity;
- water content;
- solids content;
- acidity or relevant acid number;
- nitrogen-containing compounds;
- oxygen-containing compounds;
- metals;
- salts;
- resins and asphaltenes, where relevant;
- other competitive or catalyst-poisoning species.

### 4.2 Sulfur Speciation

Where technically possible, distinguish among:

- hydrogen sulfide;
- mercaptans;
- sulfides;
- disulfides;
- thiophenes;
- benzothiophenes;
- dibenzothiophenes;
- alkyl-substituted refractory sulfur species;
- sulfoxides;
- sulfones;
- sulfate;
- sulfite;
- elemental sulfur;
- sulfur associated with solids or deposits.

Total sulfur alone may conceal major differences in:

- intrinsic reactivity;
- adsorption selectivity;
- molecular diffusivity;
- oxidation pathway;
- extraction behavior;
- catalyst inhibition;
- product-phase distribution.

### 4.3 Feed Representativeness

Validation feed should reflect the intended application with respect to:

- sulfur concentration;
- sulfur-species distribution;
- viscosity;
- density;
- water content;
- competing species;
- contaminants;
- solids;
- feed variability.

Model compounds are useful for mechanism development but should not be treated as full validation of performance with real feeds.

---

## 5. Validate the Analytical Methods

Analytical reliability is a prerequisite for all subsequent conclusions.

### 5.1 Method Suitability

The analytical method should be appropriate for:

- expected sulfur concentration;
- sulfur species of interest;
- feed matrix;
- product matrix;
- aqueous, organic, gas, and solid phases;
- required product specification;
- expected oxidation products;
- required uncertainty.

### 5.2 Calibration

Document:

- calibration standards;
- calibration range;
- number of calibration levels;
- calibration model;
- weighting method, where used;
- calibration frequency;
- blank response;
- quality-control standards;
- acceptance limits;
- recalibration criteria.

Calibration standards should be traceable and matrix-compatible where possible.

### 5.3 Detection and Quantification Limits

Report:

- limit of detection;
- limit of quantification;
- practical reporting limit;
- dilution factor;
- sample mass or volume;
- matrix effects.

Results below the quantification limit should not be treated as accurate numerical concentrations.

A statement such as “not detected” is not equivalent to zero sulfur.

### 5.4 Accuracy and Recovery

Evaluate accuracy using, where appropriate:

- certified reference materials;
- matrix spikes;
- standard additions;
- independent analytical methods;
- interlaboratory comparison;
- known synthetic mixtures.

Spike recovery should be evaluated in the actual matrix when matrix effects are expected.

### 5.5 Precision

Distinguish among:

- instrument repeatability;
- sample-preparation repeatability;
- within-run process repeatability;
- between-day repeatability;
- between-operator reproducibility;
- between-laboratory reproducibility.

Repeated measurement of one prepared sample does not quantify the variability of the complete experiment.

### 5.6 Sampling Integrity

Control:

- sample location;
- sampling time;
- phase homogeneity;
- sample temperature;
- volatile losses;
- adsorption on sampling equipment;
- filtration;
- phase separation before analysis;
- preservation;
- storage duration;
- light exposure;
- oxidation after sampling.

A representative analytical result requires a representative sample.

---

## 6. Use Blanks, Controls, and Reference Experiments

A credible validation program should include controls appropriate to the process.

### 6.1 Analytical Blank

Used to identify contamination from:

- solvents;
- reagents;
- sampling equipment;
- digestion;
- extraction;
- laboratory handling.

### 6.2 Process Blank

Operate the process without the active intervention.

Examples include:

- no catalyst;
- no adsorbent;
- no oxidant;
- no hydrogen;
- no cavitation;
- no ultrasound;
- no plasma;
- no intensification device.

### 6.3 Thermal Control

Operate at the same temperature and duration without the proposed active mechanism.

This is particularly important when pumping, recirculation, cavitation, or mixing causes temperature rise.

### 6.4 Hydrodynamic Control

Match, where possible:

- flow rate;
- residence time;
- pressure drop;
- recirculation;
- temperature;
- mixing power;

while suppressing or altering the proposed intensified mechanism.

### 6.5 Chemical Control

Evaluate possible contributions from:

- oxidant alone;
- catalyst alone;
- solvent alone;
- adsorbent alone;
- pH adjustment alone;
- thermal treatment alone;
- combined catalyst and oxidant.

### 6.6 Positive Control

Use a reference system known to produce a measurable response where appropriate.

### 6.7 Reference Process

Compare the proposed process with a technically relevant baseline, such as:

- conventional stirred treatment;
- conventional hydrodesulfurization conditions;
- non-cavitating flow;
- standard adsorbent;
- standard extraction;
- untreated feed;
- current industrial practice.

The reference must be justified scientifically and practically.

---

## 7. Establish an Equivalent Reference Case

The reference and test cases should be equivalent except for the variable being evaluated.

Control or document:

- feed batch;
- initial sulfur concentration;
- sulfur-species distribution;
- treated feed mass or volume;
- temperature;
- pressure;
- treatment duration;
- residence time;
- catalyst loading;
- adsorbent loading;
- oxidant-to-sulfur ratio;
- hydrogen partial pressure;
- solvent-to-feed ratio;
- phase ratio;
- flow rate;
- recirculation ratio;
- reactor fill level;
- sampling schedule;
- analytical method;
- downstream separation;
- product-recovery basis.

If exact equivalence is impossible, quantify the differences and account for them in the interpretation.

A process-intensification comparison is invalid when the intensified case also receives:

- more oxidant;
- higher temperature;
- longer treatment;
- more catalyst;
- more solvent;
- greater product loss;
- a different separation procedure;

unless those differences are explicitly included in the comparison.

---

## 8. Close the Sulfur Balance

### 8.1 General Sulfur Balance

For a defined process interval:

```math
m_{S,\mathrm{in}}
=
m_{S,\mathrm{product}}
+
m_{S,\mathrm{aqueous}}
+
m_{S,\mathrm{solvent}}
+
m_{S,\mathrm{gas}}
+
m_{S,\mathrm{solid}}
+
m_{S,\mathrm{deposit}}
+
m_{S,\mathrm{sample}}
+
m_{S,\mathrm{unaccounted}}
```

The unaccounted fraction must be reported rather than implicitly described as removed sulfur.

### 8.2 Sulfur-Balance Closure

A dimensionless closure ratio may be written as:

```math
B_S
=
\frac{
\sum m_{S,\mathrm{out}}
+
\sum m_{S,\mathrm{accumulated}}
}{
\sum m_{S,\mathrm{in}}
}
```

The corresponding relative closure error is:

```math
\varepsilon_S
=
\left|
B_S-1
\right|
\times
100\%
```

The acceptable closure error should be defined before testing and justified using:

- analytical uncertainty;
- sampling uncertainty;
- expected sulfur concentration;
- number of phases;
- process complexity;
- material retained in equipment.

### 8.3 Sulfur Locations to Consider

Where relevant, quantify sulfur in:

- untreated feed;
- treated hydrocarbon;
- treated gas;
- aqueous phase;
- extraction solvent;
- wash liquid;
- adsorbent;
- catalyst;
- precipitated solids;
- suspended solids;
- equipment deposits;
- vent gas;
- purge streams;
- recovered elemental sulfur;
- sulfoxides;
- sulfones;
- sulfate;
- other identified sulfur products.

### 8.4 Interpretation

A closed sulfur balance supports consistent accounting.

It does not, by itself, prove:

- a reaction mechanism;
- intrinsic kinetics;
- absence of unmeasured intermediates;
- industrial process usefulness.

---

## 9. Distinguish Conversion, Transfer, Capture, and Removal

For oxidative desulfurization, a simplified pathway may be represented as:

```math
\text{organosulfur compound}
\rightarrow
\text{sulfoxide}
\rightarrow
\text{sulfone}
```

This transformation does not guarantee that sulfur has left the treated hydrocarbon.

Separately report:

- disappearance of the original sulfur compound;
- formation of oxidized sulfur products;
- total sulfur in each phase;
- sulfur transferred to solvent;
- sulfur retained on adsorbent;
- sulfur retained on catalyst;
- sulfur recovered as solid;
- final total sulfur in the product;
- hydrocarbon product recovery.

### 9.1 Apparent Conversion

For a constant-volume batch system:

```math
X_S
=
\frac{
C_{S,0}-C_S
}{
C_{S,0}
}
```

This expression is meaningful only when:

- concentration basis is unchanged;
- dilution is accounted for;
- phase transfer is understood;
- sampling losses are corrected;
- the measured species is clearly defined.

### 9.2 Separation Efficiency

For transformed sulfur entering a downstream separation step:

```math
\eta_{\mathrm{sep}}
=
\frac{
m_{S,\mathrm{removed\ from\ product}}
}{
m_{S,\mathrm{available\ for\ separation}}
}
```

### 9.3 Product-Based Performance

The primary industrial metric is generally the final sulfur concentration in the recovered product, not only the conversion of one starting compound.

---

## 10. Validate Apparent Kinetics

### 10.1 Apparent Rate Expression

A pseudo-first-order model may be written as:

```math
-r_S
=
k_{\mathrm{obs}}C_S
```

For a constant-volume batch system:

```math
\ln\left(
\frac{C_{S,0}}{C_S}
\right)
=
k_{\mathrm{obs}}t
```

The fitted value of $k_{\mathrm{obs}}$ may contain contributions from:

- intrinsic reaction;
- external mass transfer;
- internal diffusion;
- adsorption;
- catalyst accessibility;
- oxidant transfer;
- mixing;
- phase ratio;
- hydrodynamics;
- deactivation;
- simultaneous separation.

It should not automatically be described as an intrinsic kinetic constant.

### 10.2 Model Adequacy

Evaluate:

- residual plots;
- parameter uncertainty;
- goodness of fit;
- sensitivity to the fitted time interval;
- alternative kinetic models;
- initial-condition uncertainty;
- conversion range;
- catalyst deactivation;
- oxidant depletion;
- equilibrium approach;
- mass-transfer variation.

A high coefficient of determination alone does not validate the mechanism.

### 10.3 Initial-Rate Analysis

Initial-rate measurements can reduce complications from:

- reactant depletion;
- product inhibition;
- changing phase composition;
- catalyst deactivation;
- changing oxidant concentration;
- equilibrium approach.

However, early-time data may be affected by:

- mixing transients;
- heating transients;
- sampling delay;
- catalyst wetting;
- instrument response.

### 10.4 Temperature Dependence

An Arrhenius-type relationship is:

```math
k
=
A
\exp\left(
-\frac{E_a}{RT}
\right)
```

Temperature studies should control or account for simultaneous changes in:

- viscosity;
- diffusivity;
- vapor pressure;
- gas solubility;
- phase equilibrium;
- interfacial area;
- catalyst state;
- oxidant stability;
- mass transfer.

An apparent activation energy is not necessarily an intrinsic activation energy.

---

## 11. Discriminate Reaction and External Mass Transfer

### 11.1 Diagnostic Ratio

For compatible first-order coefficients:

```math
Da_{\mathrm{diag}}
=
\frac{
k_{\mathrm{rxn}}
}{
k_La
}
```

Approximate tendencies are:

- $Da_{\mathrm{diag}}\ll1$: reaction-controlled tendency;
- $Da_{\mathrm{diag}}\approx1$: coupled reaction–transfer behavior;
- $Da_{\mathrm{diag}}\gg1$: mass-transfer-controlled tendency.

The ratio is dimensionless only when the coefficients use compatible bases.

### 11.2 Controlled Perturbations

Vary, where appropriate:

- agitation rate;
- recirculation rate;
- gas velocity;
- liquid velocity;
- flow rate;
- phase ratio;
- droplet size;
- bubble size;
- viscosity;
- reactor geometry;
- static-mixer configuration;
- distributor configuration.

### 11.3 Interpretation

A rate increase with greater mixing can indicate:

- improved external mass transfer;
- increased interfacial area;
- reduced concentration gradients;
- improved catalyst suspension;
- improved phase distribution.

It can also be confounded by:

- increased temperature;
- emulsion formation;
- changed residence-time distribution;
- improved solids suspension;
- increased oxygen ingress;
- different sampling behavior.

### 11.4 Independent Measurements

Where possible, measure or estimate independently:

- $k_La$;
- $k_Ga$;
- interfacial area;
- gas holdup;
- droplet-size distribution;
- bubble-size distribution;
- mixing time;
- residence-time distribution;
- phase distribution.

Independent transport measurements substantially strengthen the regime diagnosis.

---

## 12. Evaluate Internal Diffusion

### 12.1 Relevant Properties

For porous catalysts and adsorbents, characterize:

- particle size;
- particle shape;
- pore-size distribution;
- porosity;
- tortuosity;
- surface area;
- pore volume;
- effective diffusivity;
- wetting;
- molecular size of relevant sulfur species;
- deposition and pore blockage.

### 12.2 Thiele Modulus

For a first-order reaction in an isothermal spherical particle:

```math
\phi
=
R_p
\sqrt{
\frac{k_v}{D_{\mathrm{eff}}}
}
```

The coefficient $k_v$ must be defined on a compatible volumetric basis.

### 12.3 Effectiveness Factor

For a first-order isothermal spherical particle:

```math
\eta
=
\frac{3}{\phi^2}
\left(
\phi\coth\phi-1
\right)
```

### 12.4 Weisz–Prater Screening

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

The interpretation depends on:

- rate basis;
- geometry;
- reaction order;
- surface concentration;
- effective diffusivity;
- thermal effects.

### 12.5 Particle-Size Testing

Reducing particle size can provide evidence of internal diffusion when the apparent rate increases under otherwise equivalent conditions.

Control possible confounding changes in:

- external surface area;
- bed packing;
- pressure drop;
- catalyst suspension;
- attrition;
- hydrodynamics;
- wetting;
- catalyst loss.

### 12.6 Heavy Feeds

For heavy petroleum fractions, internal transport may be affected by:

- high viscosity;
- large sulfur molecules;
- resins;
- asphaltenes;
- pore blockage;
- coke;
- metal deposition;
- competitive adsorption.

Diffusivity values derived from light model systems should not be transferred without justification.

---

## 13. Validate Adsorption Performance

### 13.1 Equilibrium Is Not Sufficient

Adsorptive desulfurization should be validated through both equilibrium and dynamic performance.

Report, where relevant:

- equilibrium isotherms;
- adsorption kinetics;
- breakthrough curves;
- breakthrough capacity;
- working capacity;
- saturation capacity;
- treated bed volumes;
- mass-transfer-zone length;
- bed utilization;
- pressure drop;
- regeneration efficiency;
- capacity retention;
- selectivity;
- competitive adsorption.

### 13.2 Isotherm Evaluation

For a Langmuir-type model:

```math
q_e
=
\frac{
q_{\max}K_LC_e
}{
1+K_LC_e
}
```

Model fitting should include:

- parameter uncertainty;
- residual analysis;
- concentration range;
- temperature;
- feed matrix;
- competing species;
- replicate measurements.

Agreement with an isotherm does not prove a particular adsorption mechanism.

### 13.3 Breakthrough Validation

For fixed-bed systems, document:

- bed dimensions;
- adsorbent mass;
- particle-size distribution;
- superficial velocity;
- residence time;
- inlet concentration;
- outlet sampling frequency;
- breakthrough criterion;
- saturation criterion;
- pressure drop;
- temperature;
- regeneration history.

### 13.4 Real-Feed Validation

Test competitive effects from:

- aromatic compounds;
- nitrogen compounds;
- oxygenates;
- moisture;
- salts;
- metals;
- particulate matter;
- other sulfur compounds.

Capacity measured with one model sulfur compound may substantially overestimate real-feed performance.

---

## 14. Validate Hydrogen, Oxidant, and Reactant Utilization

### 14.1 Reactant Accounting

Report:

- reactant identity;
- purity;
- concentration;
- total amount supplied;
- feed-to-reactant ratio;
- stoichiometric basis;
- residual concentration;
- decomposition;
- side reactions;
- recycle;
- vent losses;
- reaction products.

### 14.2 Oxidant Utilization

A stoichiometric oxidant-utilization efficiency may be defined as:

```math
\eta_{\mathrm{ox}}
=
\frac{
n_{\mathrm{ox,stoich,target}}
}{
n_{\mathrm{ox,supplied}}
}
```

The target oxidation state and stoichiometric coefficient must be defined.

### 14.3 Hydrogen Utilization

For hydrogen-based processes, evaluate:

- hydrogen feed rate;
- hydrogen purity;
- partial pressure;
- dissolved hydrogen availability;
- recycle;
- purge;
- hydrogen consumption;
- hydrogen sulfide formation;
- competing hydrogenation reactions;
- product saturation changes.

### 14.4 Staged Addition and Distribution

Test whether performance changes with:

- staged oxidant addition;
- staged hydrogen addition;
- improved gas distribution;
- improved liquid distribution;
- recycle;
- mixing;
- feed injection location.

High reactant dosage may mask poor utilization.

---

## 15. Validate Hydrodynamics

### 15.1 Relevant Hydrodynamic Quantities

Where applicable, characterize:

- flow rate;
- superficial velocity;
- recirculation rate;
- residence time;
- residence-time distribution;
- mixing time;
- gas holdup;
- liquid holdup;
- solids suspension;
- pressure distribution;
- bypassing;
- channeling;
- stagnant volume;
- phase maldistribution.

### 15.2 Residence-Time Distribution

Tracer testing can help identify:

- bypassing;
- dead volume;
- short-circuiting;
- broad residence-time distribution;
- recirculation;
- non-ideal flow.

Equal nominal residence time does not guarantee equivalent exposure history.

### 15.3 Local Versus Global Behavior

Local measurements may be required because:

- concentration varies along the reactor;
- pressure varies through restrictions;
- gas holdup is nonuniform;
- catalyst wetting is incomplete;
- local cavitation intensity varies;
- recirculation creates multiple passes.

A global average can conceal local controlling regimes.

---

## 16. Validate Hydrodynamic Cavitation

### 16.1 Verify Cavitation Rather Than Assume It

A device should not be considered validated as a hydrodynamic-cavitation reactor solely because it contains an orifice, venturi, rotor, constriction, or pressure drop.

Characterize:

- upstream absolute pressure;
- throat or minimum-pressure region, where measurable;
- downstream absolute pressure;
- recovery pressure;
- fluid temperature;
- vapor pressure;
- density;
- viscosity;
- flow rate;
- characteristic velocity;
- pressure drop;
- device geometry;
- number of passes;
- recirculation ratio;
- treated throughput;
- residence-time distribution.

### 16.2 Cavitation Number

A commonly used form is:

```math
\sigma
=
\frac{
p_{\mathrm{ref}}-p_v
}{
\frac{1}{2}\rho v^2
}
```

Every reported value should define:

- pressure location;
- absolute or gauge basis;
- velocity definition;
- flow area;
- fluid temperature;
- vapor-pressure source;
- fluid density.

Equal cavitation number does not guarantee equal:

- cavity population;
- collapse intensity;
- collapse location;
- residence time;
- erosion;
- chemical effect;
- scale-up behavior.

### 16.3 Additional Diagnostic Methods

Where technically justified, consider:

- pressure-fluctuation measurements;
- acoustic measurements;
- high-speed imaging;
- visualization;
- erosion mapping;
- computational fluid dynamics;
- non-cavitating controls;
- dissolved-gas measurement;
- temperature-rise measurement.

### 16.4 Thermal Confounding

Cavitation and recirculation can increase temperature.

A thermal control should reproduce the temperature history without cavitation, where possible.

Performance improvement must not be attributed to cavitation when it can be explained by heating alone.

### 16.5 Multiple-Pass Systems

For recirculating systems, report:

- tank volume;
- loop flow rate;
- nominal passes;
- residence-time distribution;
- total treatment time;
- sampling position;
- temperature history;
- changing feed composition.

The number of nominal passes is not equivalent to identical treatment of every fluid element.

---

## 17. Quantify Energy Input

### 17.1 Energy Boundary

State whether the reported energy includes:

- hydraulic pumping;
- motor losses;
- recirculation;
- heating;
- cooling;
- gas compression;
- hydrogen supply;
- oxidant production;
- ultrasound;
- solvent circulation;
- separation;
- filtration;
- adsorption regeneration;
- auxiliary equipment.

### 17.2 Hydraulic Power

For an incompressible pumped stream:

```math
P_{\mathrm{hydraulic}}
=
\Delta P Q
```

where:

- $\Delta P$ is pressure drop;
- $Q$ is volumetric flow rate.

### 17.3 Electrical Power

Hydraulic power is not equivalent to electrical input.

Where applicable:

```math
P_{\mathrm{electrical}}
=
\frac{
P_{\mathrm{hydraulic}}
}{
\eta_{\mathrm{pump}}\eta_{\mathrm{drive}}
}
```

Measured electrical input is preferable to assuming nameplate power.

### 17.4 Energy Consumption

For time-dependent power:

```math
E
=
\int_0^{t_f}
P(t)\,dt
```

If power is approximately constant:

```math
E
=
Pt
```

### 17.5 Energy-Normalized Sulfur Removal

Incremental sulfur removal relative to a reference is:

```math
\Delta m_S
=
m_{S,\mathrm{removed,int}}
-
m_{S,\mathrm{removed,ref}}
```

Incremental energy is:

```math
\Delta E
=
E_{\mathrm{int}}
-
E_{\mathrm{ref}}
```

For positive incremental energy:

```math
EN_S
=
\frac{
\Delta m_S
}{
\Delta E
}
```

The reciprocal metric is:

```math
SEC_S
=
\frac{
\Delta E
}{
\Delta m_S
}
```

Report units explicitly, such as:

- $\mathrm{kWh\,m^{-3}}$;
- $\mathrm{kWh\,t^{-1}\ feed}$;
- $\mathrm{g\ S\,kWh^{-1}}$;
- $\mathrm{kWh\,kg^{-1}\ S}$.

### 17.6 Interpretation

Energy-normalized results require:

- equivalent reference cases;
- identical product boundaries;
- positive incremental benefit;
- defined energy boundaries;
- uncertainty analysis.

Gross sulfur removal should not be divided by intensified-system energy when the objective is to quantify incremental intensification benefit.

---

## 18. Validate Downstream Separation

For oxidative, extractive, adsorptive, and multiphase systems, characterize the complete separation sequence.

Report:

- phase-separation time;
- extraction efficiency;
- solvent-to-feed ratio;
- number of extraction stages;
- solvent selectivity;
- solvent recovery;
- solvent loss;
- emulsion stability;
- hydrocarbon loss;
- water carryover;
- residual oxidant;
- catalyst separation;
- adsorbent requirement;
- filtration performance;
- solid waste;
- liquid waste;
- final product sulfur.

### 18.1 Complete Process Comparison

An intensified reaction stage may:

- increase emulsion formation;
- increase solvent demand;
- decrease phase-separation rate;
- increase product loss;
- create fine solids;
- increase filtration burden;
- increase residual oxidant.

The total flowsheet should be compared, not only the reactor.

---

## 19. Assess Catalyst and Adsorbent Durability

### 19.1 Time-on-Stream Performance

Evaluate:

- initial activity;
- stabilized activity;
- activity decline;
- selectivity decline;
- capacity decline;
- pressure-drop increase;
- product-quality change;
- regeneration response.

### 19.2 Relative Activity

A normalized activity may be written as:

```math
a(t)
=
\frac{
r_{\mathrm{obs}}(t)
}{
r_{\mathrm{obs}}(0)
}
```

The rates must be compared at equivalent conditions.

### 19.3 Deactivation Mechanisms

Investigate, where relevant:

- poisoning;
- coking;
- sulfur deposition;
- metal deposition;
- pore blockage;
- active-phase oxidation or reduction;
- sintering;
- active-component leaching;
- attrition;
- mechanical fragmentation;
- surface-area loss;
- pore-volume loss;
- structural transformation.

### 19.4 Regeneration

Document:

- regeneration method;
- temperature;
- gas or solvent;
- duration;
- chemical consumption;
- capacity recovery;
- activity recovery;
- selectivity recovery;
- material loss;
- number of cycles.

Single-cycle performance is insufficient for industrial qualification.

---

## 20. Assess Materials Compatibility and Operability

Evaluate risks associated with:

- corrosion;
- erosion;
- cavitation damage;
- vibration;
- noise;
- seal failure;
- pump damage;
- valve damage;
- fouling;
- plugging;
- solids accumulation;
- catalyst attrition;
- thermal excursions;
- oxidant decomposition;
- peroxide incompatibility;
- gas release;
- pressure excursions;
- unstable emulsions;
- static electricity;
- flammability;
- oxygen enrichment;
- hydrogen service;
- hydrogen sulfide exposure.

### 20.1 Materials Evidence

Where applicable, use:

- material coupons;
- wall-thickness monitoring;
- erosion mapping;
- corrosion-rate measurement;
- particle-size monitoring;
- solids analysis;
- surface inspection;
- microscopy;
- chemical analysis of leached metals.

### 20.2 Operability

Assess:

- start-up;
- shutdown;
- upset response;
- cleaning;
- draining;
- sampling;
- isolation;
- pressure control;
- temperature control;
- flow control;
- level control;
- safe reagent addition;
- maintenance access.

Scientific performance must be compatible with safe and stable operation.

---

## 21. Evaluate Product Quality

Desulfurization should not compromise other required product properties.

Depending on the feed and product, evaluate:

- hydrocarbon recovery;
- gas recovery;
- boiling range;
- viscosity;
- density;
- acidity;
- water content;
- oxidation stability;
- color;
- odor;
- sediment;
- particulate content;
- storage stability;
- flash point;
- cetane-related properties;
- octane-related properties;
- lubricity;
- aromatic content;
- olefin content;
- dissolved metals;
- residual solvent;
- residual oxidant;
- catalyst carryover;
- adsorbent fines.

A lower sulfur concentration does not establish a superior process when product yield or quality deteriorates.

---

## 22. Establish Repeatability, Reproducibility, and Uncertainty

### 22.1 Independent Replicates

Replicates should repeat the complete experimental sequence, including:

- feed preparation;
- reactor charging;
- treatment;
- sampling;
- phase separation;
- sample preparation;
- analysis.

Repeated analysis of one sample is not an independent process replicate.

### 22.2 Statistical Reporting

Report:

- number of independent experiments;
- mean;
- standard deviation;
- confidence interval, where appropriate;
- individual data points;
- outlier policy;
- missing-data treatment;
- analytical uncertainty;
- process variability.

Three or more independent replicates are generally preferable for preliminary comparisons, but sample size should be justified by:

- expected variability;
- expected effect size;
- required confidence;
- cost and safety constraints.

### 22.3 Difference Versus Uncertainty

An observed improvement should not be considered meaningful when it is comparable to:

- analytical uncertainty;
- feed variability;
- replicate variability;
- sampling uncertainty;
- sulfur-balance error.

### 22.4 Uncertainty Propagation

For a ratio:

```math
y
=
\frac{a}{b}
```

with independent standard uncertainties $u_a$ and $u_b$:

```math
\left(
\frac{u_y}{y}
\right)^2
\approx
\left(
\frac{u_a}{a}
\right)^2
+
\left(
\frac{u_b}{b}
\right)^2
```

This linear approximation may be unsuitable when:

- the denominator approaches zero;
- uncertainties are large;
- quantities are correlated;
- the result depends on the difference between similar values;
- distributions are non-normal.

Monte Carlo propagation or another appropriate method should then be considered.

### 22.5 Incremental Metrics

Metrics based on differences require special caution:

```math
\Delta m_S
=
m_{S,\mathrm{removed,int}}
-
m_{S,\mathrm{removed,ref}}
```

When two similar values are subtracted, relative uncertainty can become large even if each value is individually precise.

---

## 23. Predefine Acceptance Criteria

Acceptance criteria should be established before interpreting results.

Possible criteria include:

- final total sulfur specification;
- sulfur-species conversion;
- sulfur-balance closure;
- minimum product recovery;
- maximum solvent loss;
- minimum oxidant utilization;
- maximum energy consumption;
- minimum energy-normalized benefit;
- maximum pressure drop;
- maximum erosion or corrosion rate;
- minimum catalyst activity retention;
- minimum adsorbent capacity retention;
- maximum emulsion-separation time;
- minimum replicate precision;
- minimum operating duration;
- acceptable product-quality changes.

Avoid selecting thresholds after reviewing the results unless the change is documented and justified.

### 23.1 Criterion Categories

Each criterion should state whether it is:

- analytical;
- scientific;
- engineering;
- safety-related;
- economic;
- regulatory;
- project-specific.

### 23.2 Pass, Conditional Pass, and Fail

A structured decision may use:

- **Pass:** all critical criteria satisfied;
- **Conditional pass:** promising result with defined unresolved validation requirements;
- **Fail:** one or more critical criteria not satisfied;
- **Inconclusive:** evidence insufficient or uncertainty too large.

“Inconclusive” is scientifically preferable to an unsupported positive claim.

---

## 24. Data Integrity and Reproducibility

Record sufficient information to reproduce the work.

### 24.1 Raw Data

Preserve:

- raw instrument files;
- calibration files;
- process data;
- pressure and temperature histories;
- flow records;
- power measurements;
- sampling times;
- sample identifiers;
- analyst notes;
- deviations;
- failed experiments.

### 24.2 Data Processing

Document:

- baseline correction;
- blank subtraction;
- dilution correction;
- integration method;
- calibration model;
- unit conversions;
- excluded data;
- smoothing;
- interpolation;
- fitted equations;
- software version;
- code version.

### 24.3 Version Control

For computational analysis, record:

- repository commit;
- script version;
- input data;
- parameter file;
- execution environment;
- package versions;
- output files.

### 24.4 Traceability

Every reported result should be traceable to:

- feed batch;
- experiment;
- sample;
- analytical run;
- calculation;
- figure;
- table.

---

## 25. Pilot-Scale Validation

Laboratory validation should be followed by pilot testing when industrial extrapolation is intended.

### 25.1 Pilot Objectives

A pilot should test:

- representative feed;
- realistic throughput;
- continuous or intended operating mode;
- realistic residence time;
- feed variability;
- process control;
- heat removal;
- mass transfer;
- catalyst wetting;
- adsorbent breakthrough;
- phase separation;
- energy demand;
- cleaning;
- maintenance;
- materials compatibility;
- sustained operation.

### 25.2 Pilot Duration

Pilot duration should be sufficient to observe:

- stabilization;
- feed variation;
- catalyst deactivation;
- adsorbent saturation;
- fouling;
- pressure-drop change;
- erosion;
- corrosion;
- solvent accumulation;
- waste generation;
- control performance.

A brief demonstration may establish operability but not long-term durability.

### 25.3 Sampling Plan

Pilot sampling should cover:

- start-up;
- steady operation;
- feed changes;
- operating-severity changes;
- shutdown;
- regeneration;
- cleaning;
- upset conditions, where safely possible.

---

## 26. Scale-Up Validation

Geometric similarity alone does not guarantee dynamic, kinetic, transport, or process similarity.

### 26.1 Reaction-Controlled Systems

Evaluate preservation of:

- temperature;
- pressure;
- reactant concentration;
- catalyst-to-feed ratio;
- residence time;
- catalyst state.

Transport limitations may emerge at larger scale even if absent in laboratory equipment.

### 26.2 External Mass-Transfer-Controlled Systems

Evaluate:

- $k_La$;
- interfacial area;
- phase holdup;
- mixing time;
- superficial velocity;
- distributor performance;
- flow regime;
- power input;
- pressure drop.

Equal power per unit volume does not automatically guarantee equal mass transfer.

### 26.3 Internal Diffusion-Controlled Systems

Preserve or evaluate:

- catalyst geometry;
- particle size;
- pore structure;
- effective diffusivity;
- wetting;
- temperature;
- deposition tendency.

### 26.4 Adsorption Systems

Evaluate:

- bed dimensions;
- superficial velocity;
- mass-transfer-zone length;
- breakthrough;
- pressure drop;
- heat effects;
- regeneration;
- cycle stability.

### 26.5 Hydrodynamic Systems

Evaluate:

- residence-time distribution;
- bypassing;
- channeling;
- local velocity;
- recirculation topology;
- phase distribution;
- gas or liquid holdup;
- mixing time.

### 26.6 Hydrodynamic Cavitation

Scale-up should consider:

- device geometry;
- pressure boundary conditions;
- pressure recovery;
- flow rate;
- characteristic velocity;
- cavitation number;
- number of devices;
- parallel versus series operation;
- recirculation;
- pass distribution;
- energy;
- erosion location;
- fluid properties;
- vapor pressure;
- dissolved gas.

One dimensionless number is not sufficient to guarantee similar cavitation behavior.

### 26.7 Separation Scale-Up

Evaluate:

- phase-settling area;
- separator residence time;
- emulsion stability;
- solvent inventory;
- extraction staging;
- filtration area;
- adsorbent demand;
- solvent recovery;
- waste handling.

---

## 27. Evidence Grading

Validation evidence may be classified as follows.

| Grade | Description | Typical evidence |
|---|---|---|
| **E1 — Validated performance** | Independently supported performance within a defined applicability domain | Representative feed, complete balance, uncertainty, sustained pilot or industrial evidence |
| **E2 — Reconstructed or benchmarked evidence** | Results reproduced or benchmarked against traceable external data | Independent dataset, benchmark model, repeatable reconstruction |
| **E3 — Research prototype or engineering screening** | Transparent calculations or controlled experimental evidence with remaining validation gaps | Laboratory data, diagnostic equations, executable examples, defined assumptions |
| **E4 — Hypothesis** | Mechanistic or technological proposition not yet adequately validated | Conceptual mechanism, preliminary observation, proposed model |
| **R — Restricted** | Evidence exists but cannot be disclosed sufficiently for independent assessment | Confidential client, employer, or proprietary information |

### 27.1 Evidence Boundaries

The evidence grade should specify:

- the exact claim being graded;
- feed and operating range;
- scale;
- duration;
- analytical method;
- uncertainty;
- missing validation steps.

A repository may contain different evidence grades for different components.

For example:

- classical transport equations may be established;
- repository scripts may be E3;
- default parameters may be illustrative;
- industrial performance claims may remain unvalidated.

---

## 28. Minimum Recommended Validation Matrix

| Category | Minimum validation question |
|---|---|
| Objective | What engineering decision is the study intended to support? |
| System boundary | Which reaction, separation, recovery, and auxiliary steps are included? |
| Feed | Is the feed chemically and physically characterized? |
| Sulfur chemistry | Which sulfur species are present, transformed, and removed? |
| Analytical method | Are calibration, recovery, precision, and quantification limits established? |
| Controls | Are blank, thermal, chemical, hydrodynamic, and reference cases included? |
| Sulfur balance | Is sulfur accounted for across all relevant phases and deposits? |
| Conversion | Is chemical transformation distinguished from final removal? |
| Kinetics | Is the reported rate intrinsic or apparent? |
| External transfer | Could interphase transport control the observed rate? |
| Internal diffusion | Are porous-particle limitations evaluated? |
| Adsorption | Are capacity, breakthrough, competition, and regeneration known? |
| Reactant utilization | Are hydrogen or oxidant use and losses quantified? |
| Hydrodynamics | Are mixing, distribution, and residence-time behavior characterized? |
| Cavitation | Is cavitation characterized rather than assumed? |
| Energy | Is actual incremental energy measured within a defined boundary? |
| Separation | Are transformed sulfur products removed from the final product? |
| Durability | Is performance maintained over time and repeated cycles? |
| Materials | Are erosion, corrosion, fouling, and plugging acceptable? |
| Product quality | Does treatment preserve required product properties and yield? |
| Statistics | Are independent replicates and uncertainty reported? |
| Data integrity | Are raw data, calculations, and versions traceable? |
| Pilot scale | Is sustained performance demonstrated using representative feed? |
| Scale-up | Are controlling regimes and process penalties transferable? |
| Acceptance | Were criteria defined before interpreting the results? |

---

## 29. Validation Reporting Checklist

A technical report should include:

### Feed and Materials

- feed identification;
- sulfur concentration;
- sulfur speciation;
- physical properties;
- catalyst or adsorbent characterization;
- reagent specifications.

### Equipment

- process flow diagram;
- reactor geometry;
- device dimensions;
- instrumentation;
- sampling points;
- energy boundary;
- separation equipment.

### Procedure

- operating sequence;
- temperature;
- pressure;
- flow rates;
- residence time;
- recirculation;
- catalyst loading;
- oxidant or hydrogen dose;
- solvent ratio;
- sampling schedule.

### Analytical Information

- methods;
- calibration;
- detection and quantification limits;
- recovery;
- precision;
- sample preparation;
- quality controls.

### Results

- individual measurements;
- mean and variability;
- sulfur balance;
- sulfur distribution;
- final product sulfur;
- product recovery;
- energy;
- reagent consumption;
- separation performance;
- durability.

### Interpretation

- controlling regime;
- alternative explanations;
- uncertainty;
- applicability domain;
- unresolved questions;
- scale-up implications;
- evidence grade.

### Deviations

- failed runs;
- anomalies;
- equipment problems;
- analytical deviations;
- excluded results;
- protocol changes.

---

## 30. Core Validation Principles

> **Do not interpret a concentration decrease in one phase as total sulfur removal without a sulfur balance.**

> **Do not describe an apparent rate constant as intrinsic kinetics without excluding transport, diffusion, deactivation, and hydrodynamic effects.**

> **Do not claim process-intensification benefit without an equivalent reference case.**

> **Do not evaluate an intensified reactor independently of downstream separation, energy, product recovery, and materials effects.**

> **Do not use nominal equipment power when measured process energy is available.**

> **Do not infer industrial performance from one short laboratory experiment.**

> **Do not treat differences smaller than experimental uncertainty as meaningful improvement.**

> **Do not extrapolate beyond the validated feed, operating range, scale, or duration without explicitly stating the uncertainty.**

---

## 31. Related Repository Resources

- [Repository README](../README.md)
- [Framework summary](framework-summary.md)
- [Core equations](equations.md)
- [Regime classification](regime-classification.md)
- [HDS internal-diffusion example](../examples/hds_regime_example.py)
- [ODS reaction–mass-transfer example](../examples/ods_mass_transfer_example.py)
- [Cavitation-intensification example](../examples/cavitation_intensification_example.py)
- [Illustrative parameter table](../data/example_parameters.csv)

---

## 32. Summary

A technically defensible validation program must integrate:

- feed characterization;
- sulfur speciation;
- analytical-method validation;
- blanks and controls;
- equivalent reference cases;
- sulfur-balance closure;
- kinetic and transport discrimination;
- internal-diffusion analysis;
- adsorption and breakthrough testing;
- reactant-utilization assessment;
- hydrodynamic characterization;
- cavitation verification;
- measured energy consumption;
- downstream separation;
- catalyst and adsorbent durability;
- materials compatibility;
- product-quality assessment;
- independent replication;
- uncertainty analysis;
- pilot-scale testing;
- scale-up validation.

The present repository provides an **E3 engineering screening framework** for organizing this evidence.

It does not replace validated analytical practice, detailed reactor design, process-safety analysis, pilot operation, techno-economic assessment, or independent engineering review.
