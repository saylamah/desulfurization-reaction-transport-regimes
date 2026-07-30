# Core Equations for Desulfurization Reaction–Transport Regime Analysis

## Purpose

This document summarizes the principal equations used for engineering diagnosis of desulfurization systems.

The equations support:

- identification of reaction-, transport-, diffusion-, adsorption-, hydrodynamic-, and separation-limited behavior;
- comparison of intrinsic and apparent rates;
- screening of porous-catalyst and adsorbent limitations;
- assessment of hydrodynamic process intensification;
- sulfur-balance evaluation;
- energy-normalized comparison with a defined reference case;
- planning of system-specific validation.

> **Evidence status**
>
> - The individual equations are established engineering relationships when used within their stated assumptions.
> - Their integration, parameterization, threshold selection, and use in this repository constitute an **E3 engineering screening framework and executable research prototype**.
> - The equations are not a universally validated industrial design model. Real applications require traceable data, dimensional consistency, uncertainty analysis, sulfur closure, and independent validation.

---

## 1. Notation, Basis, and Unit Discipline

### 1.1 General Conventions

Unless otherwise stated:

- concentrations are expressed on a consistent molar or mass basis;
- rates are expressed as positive sulfur-removal rates;
- time is expressed in seconds or another explicitly stated unit;
- absolute temperature is used in kinetic expressions;
- absolute pressure is used in vapor-pressure and cavitation calculations;
- all quantities forming a dimensionless ratio must use compatible units and bases.

A symbol such as $k$ is meaningful only when its basis is specified. Depending on the model, it may represent:

- a first-order volumetric rate coefficient, $\mathrm{s^{-1}}$;
- a surface-based coefficient;
- a catalyst-mass-based coefficient;
- a higher-order kinetic coefficient with concentration-dependent units;
- an overall apparent coefficient incorporating reaction and transport effects.

Coefficients defined on different bases must not be combined without conversion.

### 1.2 Representative Symbols

| Symbol | Meaning | Representative unit |
|---|---|---|
| $C_S$ | sulfur-species concentration | $\mathrm{mol\,m^{-3}}$ or $\mathrm{kg\,m^{-3}}$ |
| $C_{\mathrm{ox}}$ | oxidant concentration | consistent concentration basis |
| $r_S$ | volumetric sulfur-removal rate | concentration per time |
| $k_{\mathrm{obs}}$ | apparent pseudo-first-order coefficient | $\mathrm{s^{-1}}$ |
| $k_L$ | liquid-side mass-transfer coefficient | $\mathrm{m\,s^{-1}}$ |
| $a$ | interfacial area per reactor volume | $\mathrm{m^{-1}}$ |
| $k_La$ | volumetric mass-transfer coefficient | $\mathrm{s^{-1}}$ |
| $R_p$ | porous-particle radius | $\mathrm{m}$ |
| $D_{\mathrm{eff}}$ | effective diffusivity | $\mathrm{m^2\,s^{-1}}$ |
| $\phi$ | Thiele modulus | dimensionless |
| $\eta$ | internal effectiveness factor | dimensionless |
| $E$ | energy | $\mathrm{kWh}$ or $\mathrm{J}$ |
| $m_S$ | sulfur mass | $\mathrm{g}$ or $\mathrm{kg}$ |

---

## 2. Sulfur Conversion and Removal

For a constant-volume batch system, sulfur conversion may be expressed as:

$$ X_S=\frac{C_{S,0}-C_S}{C_{S,0}} $$

where:

- $C_{S,0}$ is the initial sulfur concentration;
- $C_S$ is the sulfur concentration at the specified time;
- $X_S$ is dimensionless.

For a continuous system, sulfur conversion should normally be defined using molar or mass flow:

$$ X_S=\frac{\dot n_{S,\mathrm{in}}-\dot n_{S,\mathrm{out}}}{\dot n_{S,\mathrm{in}}} $$

An equivalent mass-flow expression may also be used.

### Engineering Caution

A decrease in sulfur concentration in one measured phase can result from:

- chemical conversion;
- transfer to another phase;
- adsorption;
- precipitation;
- sampling bias;
- dilution;
- analytical loss.

> **A concentration decrease in one phase is not automatically equivalent to complete sulfur removal.**

---

## 3. Pseudo-First-Order Sulfur Removal

For many screening calculations, sulfur disappearance is represented by:

$$ -r_S=k_{\mathrm{obs}}C_S $$

where:

- $r_S$ is the volumetric sulfur-species removal rate;
- $k_{\mathrm{obs}}$ is an observed or apparent first-order coefficient;
- $C_S$ is the sulfur-species concentration.

Dimensional consistency requires:

$$ [k_{\mathrm{obs}}]=\mathrm{time^{-1}} $$

For a constant-volume batch system with constant $k_{\mathrm{obs}}$:

$$ \frac{dC_S}{dt}=-k_{\mathrm{obs}}C_S $$

Integration gives:

$$ \ln\left(\frac{C_{S,0}}{C_S}\right)=k_{\mathrm{obs}}t $$

The concentration profile is:

$$ C_S=C_{S,0}\exp\left(-k_{\mathrm{obs}}t\right) $$

The corresponding conversion is:

$$ X_S=1-\exp\left(-k_{\mathrm{obs}}t\right) $$

### Assumptions

This integrated form assumes:

- constant system volume;
- no sulfur inflow or outflow during the batch interval;
- constant apparent rate coefficient;
- no unmodeled phase transfer;
- no significant sampling-volume correction;
- a consistent analytical basis.

### Engineering Caution

The fitted $k_{\mathrm{obs}}$ may include contributions from:

- intrinsic reaction kinetics;
- external mass transfer;
- internal diffusion;
- mixing;
- catalyst accessibility;
- adsorption;
- oxidant activation;
- hydrodynamic intensification;
- simultaneous downstream removal.

It must not automatically be interpreted as an intrinsic kinetic coefficient.

---

## 4. Generalized Oxidative Desulfurization Rate

A generalized oxidative-desulfurization rate may be represented as:

$$ -r_S=kC_S^nC_{\mathrm{ox}}^m $$

where:

- $k$ is the intrinsic or apparent rate coefficient;
- $C_S$ is sulfur-compound concentration;
- $C_{\mathrm{ox}}$ is oxidant concentration;
- $n$ is the apparent order with respect to sulfur;
- $m$ is the apparent order with respect to oxidant.

If $r_S$ is expressed as concentration per time, dimensional consistency requires:

$$ [k]=[\mathrm{concentration}]^{1-n-m}[\mathrm{time}]^{-1} $$

When oxidant concentration remains approximately constant:

$$ k_{\mathrm{obs}}=kC_{\mathrm{ox}}^m $$

Only when $n=1$ does the expression reduce to:

$$ -r_S=k_{\mathrm{obs}}C_S $$

The apparent coefficient may still depend on:

- catalyst concentration;
- phase ratio;
- interfacial area;
- temperature;
- mixing;
- oxidant decomposition;
- oxidant utilization;
- sulfur speciation.

### Applicability Boundary

The pseudo-first-order reduction is not justified when oxidant concentration changes materially, catalyst activity changes, mass transfer evolves, or the reaction order varies during the fitted interval.

---

## 5. Arrhenius Temperature Dependence

The temperature dependence of a kinetic coefficient may be represented by:

$$ k=A\exp\left(-\frac{E_a}{RT}\right) $$

where:

- $A$ is the pre-exponential factor;
- $E_a$ is the apparent or intrinsic activation energy;
- $R$ is the universal gas constant;
- $T$ is absolute temperature.

The linearized form is:

$$ \ln k=\ln A-\frac{E_a}{R}\frac{1}{T} $$

The units of $A$ must be the same as the units of $k$.

### Engineering Caution

An apparent activation energy can be affected by:

- external mass transfer;
- internal diffusion;
- adsorption equilibrium;
- catalyst deactivation;
- changing phase behavior;
- temperature-dependent viscosity;
- temperature-dependent mixing;
- analytical and fitting limitations.

A low apparent activation energy may indicate transport influence, but it is not conclusive proof of a specific limitation.

---

## 6. Interphase Mass Transfer

For gas–liquid or liquid–liquid transfer on a liquid concentration basis:

$$ r_{\mathrm{mt}}=k_La\left(C^*-C\right) $$

where:

- $r_{\mathrm{mt}}$ is the volumetric transfer rate;
- $k_L$ is the liquid-side mass-transfer coefficient;
- $a$ is interfacial area per reactor volume;
- $k_La$ is the volumetric mass-transfer coefficient;
- $C^*$ is the equilibrium concentration corresponding to the interfacial condition;
- $C$ is the bulk-phase concentration.

Dimensional consistency requires:

$$ [k_La]=\mathrm{time^{-1}} $$

This relationship is relevant to:

- hydrogen-sulfide absorption;
- oxygen or oxidant transfer;
- oxidative desulfurization;
- multiphase catalytic oxidation;
- liquid–liquid extraction-assisted systems.

### Engineering Caution

The quantity $k_La$ combines two contributions:

$$ k_La=k_L\,a $$

An observed change in $k_La$ does not by itself identify whether the local transfer coefficient, the interfacial area, or both have changed.

---

## 7. Gas-Side Hydrogen-Sulfide Transfer

For a pressure-based gas-side driving force:

$$ N_{H_2S}=K_Ga\left(P_{H_2S}-P_{H_2S}^*\right) $$

where:

- $N_{H_2S}$ is the volumetric hydrogen-sulfide transfer rate;
- $K_Ga$ is an overall volumetric gas-side transfer coefficient;
- $P_{H_2S}$ is the bulk gas-phase partial pressure;
- $P_{H_2S}^*$ is the equilibrium partial pressure corresponding to the liquid-side condition.

When the transfer rate is expressed in $\mathrm{mol\,m^{-3}\,s^{-1}}$ and pressure is expressed in pascals:

$$ [K_Ga]=\mathrm{mol\,m^{-3}\,s^{-1}\,Pa^{-1}} $$

Observed performance may depend on:

- solvent chemistry;
- chemical enhancement;
- interfacial area;
- circulation rate;
- gas velocity;
- temperature;
- total pressure;
- contactor geometry;
- equilibrium representation.

Pressure-based and concentration-based coefficients must not be combined without an explicit equilibrium relation and unit conversion.

---

## 8. Reaction-to-Mass-Transfer Diagnostic Ratio

When reaction and mass transfer can both be represented by compatible first-order coefficients:

$$ Da_{\mathrm{diag}}=\frac{k_{\mathrm{rxn}}}{k_La} $$

Approximate screening interpretation:

- $Da_{\mathrm{diag}}\ll1$: reaction-controlled tendency;
- $Da_{\mathrm{diag}}\approx1$: coupled reaction–transport tendency;
- $Da_{\mathrm{diag}}\gg1$: mass-transfer-controlled tendency.

Using characteristic times:

$$ \tau_{\mathrm{rxn}}=\frac{1}{k_{\mathrm{rxn}}} $$

$$ \tau_{\mathrm{mt}}=\frac{1}{k_La} $$

Therefore:

$$ Da_{\mathrm{diag}}=\frac{\tau_{\mathrm{mt}}}{\tau_{\mathrm{rxn}}} $$

### Important Limitation

The ratio is dimensionless only when $k_{\mathrm{rxn}}$ and $k_La$ use compatible first-order bases.

For higher-order kinetics, complex reactor models, reactive absorption, or changing interfacial area, the Damköhler number must be constructed from consistent characteristic rates or timescales.

The exact definition depends on:

- reactor type;
- rate law;
- characteristic length;
- phase system;
- geometry;
- concentration basis.

This repository therefore uses the ratio as an **illustrative diagnostic quantity**, not as a universal Damköhler-number definition.

---

## 9. Internal Diffusion and the Thiele Modulus

For an isothermal spherical porous particle with a first-order volumetric reaction:

$$ \phi=R_p\sqrt{\frac{k_v}{D_{\mathrm{eff}}}} $$

where:

- $\phi$ is the Thiele modulus;
- $R_p$ is particle radius;
- $k_v$ is a first-order coefficient on a compatible volumetric catalyst basis;
- $D_{\mathrm{eff}}$ is effective diffusivity.

Dimensional consistency is:

$$ [\phi]=[\mathrm{m}]\sqrt{\frac{\mathrm{s^{-1}}}{\mathrm{m^2\,s^{-1}}}}=1 $$

### Basis Requirement

If the rate coefficient is expressed per catalyst mass, external surface area, or active-site inventory, it must be converted to a compatible volumetric basis before use.

### Approximate Interpretation

- $\phi\ll1$: weak internal diffusion influence;
- $\phi\approx1$: reaction and diffusion are coupled;
- $\phi\gg1$: substantial internal diffusion influence.

### Assumptions

The expression assumes:

- spherical particle geometry;
- first-order reaction;
- constant effective diffusivity;
- isothermal behavior;
- uniform porous structure;
- a defined external particle concentration.

---

## 10. Spherical-Particle Effectiveness Factor

The internal effectiveness factor is defined as:

$$ \eta=\frac{\text{actual total reaction rate in the particle}}{\text{rate if the whole particle were at the surface concentration}} $$

For a first-order reaction in an isothermal spherical particle:

$$ \eta=\frac{3}{\phi^2}\left(\phi\coth\phi-1\right) $$

An equivalent computational form is:

$$ \eta=\frac{3}{\phi^2}\left(\frac{\phi}{\tanh\phi}-1\right) $$

### Limiting Cases

As $\phi\rightarrow0$:

$$ \eta\rightarrow1 $$

A numerically stable small-$\phi$ expansion is:

$$ \eta\approx1-\frac{\phi^2}{15}+\frac{2\phi^4}{315} $$

For large $\phi$:

$$ \eta\approx\frac{3}{\phi}-\frac{3}{\phi^2} $$

The leading large-$\phi$ behavior is:

$$ \eta\sim\frac{3}{\phi} $$

### Approximate Interpretation

- $\eta\approx1$: most of the particle is effectively utilized;
- $0<\eta<1$: internal gradients reduce catalyst utilization;
- $\eta\ll1$: substantial internal diffusion resistance is present.

### Numerical Safeguards

A computational implementation should:

- reject negative $\phi$;
- return $\eta=1$ at $\phi=0$;
- use the series expansion for sufficiently small $\phi$;
- avoid subtracting nearly equal floating-point quantities;
- verify that $0<\eta\leq1$ for the stated model.

---

## 11. Langmuir Adsorption Isotherm

For idealized finite-capacity adsorption:

$$ q_e=\frac{q_{\max}K_LC_e}{1+K_LC_e} $$

where:

- $q_e$ is equilibrium adsorption capacity;
- $q_{\max}$ is maximum monolayer capacity;
- $K_L$ is the Langmuir affinity coefficient;
- $C_e$ is equilibrium sulfur concentration.

Dimensional consistency requires:

$$ [K_L]=[\mathrm{concentration}]^{-1} $$

Therefore, $K_LC_e$ is dimensionless.

### Limiting Cases

When $K_LC_e\ll1$:

$$ q_e\approx q_{\max}K_LC_e $$

When $K_LC_e\gg1$:

$$ q_e\rightarrow q_{\max} $$

### Assumptions and Limits

The Langmuir model assumes:

- a homogeneous adsorption surface;
- finite equivalent adsorption sites;
- monolayer adsorption;
- no interaction among adsorbed species.

Agreement with the equation does not prove that these assumptions describe the actual adsorption mechanism.

---

## 12. Freundlich Adsorption Isotherm

An empirical heterogeneous-surface relation is:

$$ q_e=K_FC_e^{1/n_F} $$

where:

- $K_F$ is the Freundlich capacity coefficient;
- $n_F$ is an empirical heterogeneity parameter.

The units of $K_F$ depend on:

- the units of $q_e$;
- the units of $C_e$;
- the value of $1/n_F$.

Values of $K_F$ cannot be compared unless concentration and loading bases are identical.

### Engineering Caution

The Freundlich equation has no finite saturation capacity. Extrapolation outside the fitted concentration range may therefore become physically unrealistic.

Agreement with the model is not proof of a specific adsorption mechanism.

---

## 13. Pseudo-Second-Order Adsorption Model

A commonly used empirical adsorption-kinetics expression is:

$$ \frac{dq}{dt}=k_2(q_e-q)^2 $$

where:

- $q$ is loading at time $t$;
- $q_e$ is the fitted equilibrium loading;
- $k_2$ is the pseudo-second-order coefficient.

If $q$ is expressed as mass of adsorbate per mass of adsorbent:

$$ [k_2]=[q]^{-1}[\mathrm{time}]^{-1} $$

For $q(0)=0$, integration gives:

$$ \frac{t}{q_t}=\frac{1}{k_2q_e^2}+\frac{t}{q_e} $$

### Engineering Caution

Good agreement with this model is not, by itself, proof of chemisorption.

Mechanistic interpretation requires complementary evidence such as:

- equilibrium measurements;
- temperature dependence;
- spectroscopy;
- diffusion analysis;
- competitive adsorption;
- regeneration behavior.

---

## 14. Simplified Overall Reaction–Transfer Resistance

For two linear sequential resistances expressed on a common basis:

$$ \frac{1}{k_{\mathrm{overall}}}=\frac{1}{k_{\mathrm{rxn}}}+\frac{1}{k_{\mathrm{mt}}} $$

The equivalent overall coefficient is:

$$ k_{\mathrm{overall}}=\frac{k_{\mathrm{rxn}}k_{\mathrm{mt}}}{k_{\mathrm{rxn}}+k_{\mathrm{mt}}} $$

When reaction is much slower than mass transfer:

$$ k_{\mathrm{rxn}}\ll k_{\mathrm{mt}}\quad\Rightarrow\quad k_{\mathrm{overall}}\approx k_{\mathrm{rxn}} $$

When mass transfer is much slower than reaction:

$$ k_{\mathrm{mt}}\ll k_{\mathrm{rxn}}\quad\Rightarrow\quad k_{\mathrm{overall}}\approx k_{\mathrm{mt}} $$

### Applicability Boundary

The additive-resistance form is appropriate only when:

- the resistances are sequential;
- the model is linear or suitably linearized;
- coefficients use compatible units;
- driving forces are consistently defined;
- strong coupling does not invalidate independent resistance addition.

It is a conceptual screening relation, not a universal reactor equation.

---

## 15. Apparent Cavitation Enhancement Factor

For hydrodynamic-cavitation-assisted desulfurization:

$$ F_{\mathrm{app}}=\frac{k_{\mathrm{app,HC}}}{k_{\mathrm{app,ref}}} $$

where:

- $k_{\mathrm{app,HC}}$ is the apparent coefficient under cavitation-assisted conditions;
- $k_{\mathrm{app,ref}}$ is the apparent coefficient for a defined reference case.

Interpretation:

- $F_{\mathrm{app}}>1$: higher apparent rate than the reference;
- $F_{\mathrm{app}}=1$: no apparent rate difference;
- $F_{\mathrm{app}}<1$: lower apparent rate than the reference.

### Comparability Requirements

The two coefficients should be obtained using comparable:

- feeds and sulfur speciation;
- temperature;
- pressure;
- oxidant or hydrogen dose;
- catalyst or adsorbent loading;
- phase ratio;
- analytical method;
- fitting interval;
- product and separation boundary.

### Important Caution

An enhancement factor greater than one does not prove industrial usefulness. The assessment must also consider:

- additional energy;
- pressure drop;
- oxidant consumption;
- erosion;
- corrosion;
- fouling;
- emulsion formation;
- downstream separation;
- product quality;
- reliability;
- maintenance;
- scale-up transferability.

---

## 16. Cavitation Number

A commonly used hydrodynamic cavitation number is:

$$ \sigma=\frac{p_{\mathrm{ref}}-p_v}{\frac{1}{2}\rho v^2} $$

where:

- $p_{\mathrm{ref}}$ is a stated downstream, recovery, or reference absolute pressure;
- $p_v$ is vapor pressure at the local fluid temperature;
- $\rho$ is fluid density;
- $v$ is the stated characteristic velocity.

Dimensional consistency is:

$$ [\sigma]=\frac{\mathrm{Pa}}{\mathrm{Pa}}=1 $$

### Definition Requirement

Every reported value should identify:

- the pressure-measurement location;
- whether pressure is absolute;
- the velocity definition;
- the flow area;
- fluid temperature;
- density;
- vapor-pressure basis;
- device geometry;
- flow rate.

### Engineering Caution

A lower cavitation number may indicate stronger cavitation tendency within a defined setup, but equal values do not guarantee equal:

- cavity dynamics;
- collapse intensity;
- residence pattern;
- erosion risk;
- chemical effect;
- scale-up performance.

The cavitation number is a hydrodynamic descriptor, not a universal process-performance correlation.

---

## 17. Incremental Sulfur Removal

For comparison with a defined reference case:

$$ \Delta m_S=m_{S,\mathrm{removed,HC}}-m_{S,\mathrm{removed,ref}} $$

Interpretation:

- $\Delta m_S>0$: positive incremental removal;
- $\Delta m_S=0$: no incremental removal;
- $\Delta m_S<0$: poorer removal than the reference.

Both removal quantities must use the same:

- feed basis;
- throughput;
- treatment duration;
- product boundary;
- analytical method.

Gross removal in the intensified case must not be substituted for incremental removal when evaluating the benefit attributable to intensification.

---

## 18. Incremental Energy Input

The incremental energy associated with intensification may be defined as:

$$ \Delta E=E_{\mathrm{HC}}-E_{\mathrm{ref}} $$

The energy boundary should specify, as applicable:

- pump energy;
- measured motor input;
- heating;
- cooling;
- oxidant generation;
- recirculation;
- separation;
- auxiliary equipment.

The following quantities are not interchangeable:

- nameplate power;
- measured electrical input;
- shaft power;
- hydraulic power.

---

## 19. Energy-Normalized Sulfur Removal

For positive incremental energy input:

$$ EN_S=\frac{\Delta m_S}{\Delta E} $$

Representative units include:

$$ [EN_S]=\mathrm{g\ S\,kWh^{-1}} $$

or:

$$ [EN_S]=\mathrm{kg\ S\,kWh^{-1}} $$

The reciprocal specific energy demand is:

$$ SEC_S=\frac{\Delta E}{\Delta m_S} $$

Representative units include:

$$ [SEC_S]=\mathrm{kWh\,g^{-1}\ S} $$

or:

$$ [SEC_S]=\mathrm{kWh\,kg^{-1}\ S} $$

For positive finite quantities expressed in reciprocal units:

$$ EN_S\cdot SEC_S=1 $$

### Numerical and Interpretive Safeguards

- If $\Delta E=0$, $EN_S$ is undefined.
- If $\Delta m_S=0$, $SEC_S$ is undefined.
- If $\Delta m_S<0$, the intensified case provides negative incremental benefit.
- If $\Delta E<0$, the comparison requires explicit interpretation.
- Uncertainty should be reported when either numerator is calculated by subtracting similar measured values.

A high value of $EN_S$ does not by itself establish industrial usefulness.

---

## 20. Oxidant Utilization Efficiency

A stoichiometric oxidant-utilization efficiency may be defined as:

$$ \eta_{\mathrm{ox}}=\frac{n_{\mathrm{ox,stoich,target}}}{n_{\mathrm{ox,supplied}}} $$

The stoichiometric oxidant requirement is:

$$ n_{\mathrm{ox,stoich,target}}=\nu_{\mathrm{ox}}n_{S,\mathrm{converted,target}} $$

where:

- $n_{\mathrm{ox,supplied}}$ is the supplied oxidant quantity;
- $n_{S,\mathrm{converted,target}}$ is the quantity of target sulfur converted;
- $\nu_{\mathrm{ox}}$ is the stoichiometric oxidant requirement per mole of target sulfur.

A rigorous definition must specify:

- oxidant identity;
- oxidant purity;
- stoichiometric basis;
- target sulfur species;
- target oxidation state;
- side reactions;
- decomposition;
- residual oxidant;
- analytical uncertainty.

For a consistent closed basis:

$$ 0\leq\eta_{\mathrm{ox}}\leq1 $$

A calculated value above one indicates that the stoichiometric basis, sulfur analysis, oxidant analysis, or assumed reaction pathway requires review.

---

## 21. Separation Efficiency

For transformed sulfur entering a downstream separation step:

$$ \eta_{\mathrm{sep}}=\frac{m_{S,\mathrm{removed\ from\ product}}}{m_{S,\mathrm{available\ for\ separation}}} $$

For a consistent nonnegative basis:

$$ 0\leq\eta_{\mathrm{sep}}\leq1 $$

The numerator represents sulfur actually removed from the final product phase.

The denominator represents transformed sulfur entering the defined separation boundary.

The final product sulfur concentration should be measured after the complete reaction and separation sequence.

> **Sulfur conversion is not necessarily equivalent to sulfur removal.**

---

## 22. Sulfur-Balance Closure

For a process evaluated over a defined accounting interval:

$$ B_S=\frac{\sum m_{S,\mathrm{out}}+\sum m_{S,\mathrm{accumulated}}}{\sum m_{S,\mathrm{in}}} $$

For a closed batch system:

$$ B_S=\frac{\sum m_{S,\mathrm{recovered}}}{m_{S,0}} $$

A relative sulfur-balance closure error may be expressed as:

$$ \varepsilon_S=\left|B_S-1\right|\times100\% $$

The sulfur balance should include, where relevant:

- treated hydrocarbon or gas;
- aqueous phase;
- extractant or solvent;
- adsorbent;
- catalyst deposits;
- precipitated solids;
- purge and vent streams;
- sampling losses;
- identified sulfur products.

### Engineering Caution

A closed sulfur balance demonstrates consistency of sulfur accounting within the defined boundary and analytical uncertainty. It does not establish a reaction mechanism.

---

## 23. Uncertainty Propagation for Ratios

For a ratio:

$$ y=\frac{a}{b} $$

with independent standard uncertainties $u_a$ and $u_b$, a first-order relative uncertainty estimate is:

$$ \left(\frac{u_y}{y}\right)^2\approx\left(\frac{u_a}{a}\right)^2+\left(\frac{u_b}{b}\right)^2 $$

This approximation may be used for:

- apparent enhancement factors;
- energy-normalized removal;
- specific energy demand;
- oxidant-utilization efficiency;
- separation efficiency.

### Important Limitation

The linearized relation may become unreliable when:

- the denominator approaches zero;
- uncertainty is large;
- variables are correlated;
- distributions are strongly non-normal;
- the numerator or denominator is obtained from a small difference between large quantities.

In such cases, a more appropriate propagation method, such as Monte Carlo analysis, should be considered.

---

## 24. Recommended Engineering Interpretation

No single equation should be used in isolation to claim process superiority.

A technically defensible assessment should combine, where relevant:

- sulfur speciation;
- sulfur-balance closure;
- intrinsic and apparent kinetics;
- interphase mass transfer;
- internal diffusion;
- adsorption and surface phenomena;
- hydrodynamics;
- oxidant or hydrogen utilization;
- downstream separation;
- energy consumption;
- catalyst or adsorbent durability;
- erosion;
- corrosion;
- fouling;
- product quality;
- uncertainty;
- reliability;
- scale-up transferability.

The analysis should determine:

1. which mechanism controls overall performance;
2. which secondary limitations remain important;
3. whether the proposed intervention addresses the controlling limitation;
4. whether the complete process improves relative to a defined reference.

---

## 25. Numerical Implementation Requirements

Executable implementations should:

- validate that required inputs are finite;
- reject negative concentrations, diffusivities, radii, energies, and times;
- reject zero denominators before evaluating ratios;
- document every unit and coefficient basis;
- use numerically stable limiting expressions;
- distinguish warnings from fatal input errors;
- preserve significant digits consistent with data uncertainty;
- test representative, boundary, and failure cases;
- reproduce published demonstration outputs from version-controlled inputs.

The repository examples are screening demonstrations. They should not silently replace missing pilot or industrial data with assumed values.

---

## 26. Evidence, Applicability, and Responsible Use

| Element | Status | Interpretation |
|---|---|---|
| Individual classical equations | Established within stated assumptions | Require correct geometry, units, rate law, and boundary conditions |
| Repository integration | **E3 — Engineering screening framework** | Research prototype for transparent diagnosis and comparison |
| Python examples | **E3 — Executable demonstrations** | Illustrative calculations, not validated industrial models |
| Default parameter values | Illustrative | Not measured pilot or industrial design data |
| Regime thresholds | Screening guidance | Must be justified for the specific system |
| Industrial prediction | Not established | Requires independent validation and scale-up evidence |

Use the equations for:

- transparent engineering screening;
- dimensional checks;
- sensitivity analysis;
- experimental planning;
- regime diagnosis;
- reference-case comparison;
- identification of missing evidence.

Do not use them as:

- universal kinetic correlations;
- final reactor-design calculations;
- guaranteed catalyst or adsorbent performance;
- process-safety calculations;
- emissions-compliance predictions;
- industrial performance warranties.

---

## 27. Related Repository Resources

- [Repository README](../README.md)
- [Framework summary](framework-summary.md)
- [Regime classification](regime-classification.md)
- [Validation guidelines](validation-guidelines.md)
- [HDS internal-diffusion example](../examples/hds_regime_example.py)
- [ODS reaction–mass-transfer example](../examples/ods_mass_transfer_example.py)
- [Cavitation-intensification example](../examples/cavitation_intensification_example.py)
- [Illustrative parameter table](../data/example_parameters.csv)

---

## 28. Summary

The equations in this document provide a structured basis for diagnosing coupled desulfurization phenomena.

Their responsible use requires:

- compatible units and coefficient bases;
- explicit assumptions;
- defined system boundaries;
- defined energy boundaries;
- sulfur-balance closure;
- uncertainty assessment;
- comparison with an appropriate reference;
- system-specific validation.

The repository implements these relationships as an **E3 engineering screening framework and executable research prototype**, not as a universally validated industrial design model.
