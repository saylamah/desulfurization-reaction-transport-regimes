# Core Equations for Desulfurization Reaction–Transport Regime Analysis

## Purpose

This document summarizes the principal equations used for engineering diagnosis of desulfurization systems.

The equations support:

- identification of reaction-, transport-, diffusion-, adsorption-, hydrodynamic-, and separation-limited behavior;
- comparison of intrinsic and apparent rates;
- screening of porous-catalyst or adsorbent limitations;
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
- rates are expressed as positive removal rates;
- time is expressed in seconds or another explicitly stated unit;
- absolute temperature is used in kinetic expressions;
- absolute pressure is used in vapor-pressure and cavitation calculations;
- all quantities in a dimensionless ratio must use compatible units and bases.

A symbol such as $k$ is meaningful only when its basis is specified. Depending on the model, it may be:

- a first-order volumetric rate coefficient, $\mathrm{s^{-1}}$;
- a surface-based coefficient;
- a catalyst-mass-based coefficient;
- a higher-order kinetic coefficient with concentration-dependent units;
- an overall apparent coefficient incorporating reaction and transport effects.

Coefficients on different bases must not be combined without conversion.

### 1.2 Representative Symbols

| Symbol | Meaning | Representative unit |
|---|---|---|
| $C_S$ | sulfur-species concentration | $\mathrm{mol\,m^{-3}}$ or $\mathrm{kg\,m^{-3}}$ |
| $C_{\mathrm{ox}}$ | oxidant concentration | same concentration basis used in the rate law |
| $r_S$ | volumetric sulfur-removal rate | concentration per time |
| $k_{\mathrm{obs}}$ | apparent pseudo-first-order coefficient | $\mathrm{s^{-1}}$ |
| $k_L$ | liquid-side mass-transfer coefficient | $\mathrm{m\,s^{-1}}$ |
| $a$ | interfacial area per reactor volume | $\mathrm{m^2\,m^{-3}} = \mathrm{m^{-1}}$ |
| $k_La$ | volumetric mass-transfer coefficient | $\mathrm{s^{-1}}$ |
| $R_p$ | porous-particle radius | $\mathrm{m}$ |
| $D_{\mathrm{eff}}$ | effective diffusivity | $\mathrm{m^2\,s^{-1}}$ |
| $\phi$ | Thiele modulus | dimensionless |
| $\eta$ | internal effectiveness factor | dimensionless |
| $E$ | energy | $\mathrm{kWh}$, $\mathrm{J}$, or another stated unit |
| $m_S$ | sulfur mass | $\mathrm{g}$, $\mathrm{kg}$, or another stated unit |

---

## 2. Sulfur Conversion and Removal

For a constant-volume batch system, an apparent sulfur conversion may be written as:

$$
X_S
=
\frac{C_{S,0}-C_S}{C_{S,0}}
$$

where:

- $C_{S,0}$ is the initial sulfur concentration;
- $C_S$ is the sulfur concentration at the specified time;
- $X_S$ is dimensionless.

For a continuous system or a process with changing phase volume, use sulfur molar or mass flow rather than concentration alone:

$$
X_S
=
\frac{\dot n_{S,\mathrm{in}}-\dot n_{S,\mathrm{out}}}
{\dot n_{S,\mathrm{in}}}
$$

or an equivalent mass-flow expression.

### Engineering Caution

A decrease in sulfur concentration in one measured phase can result from:

- chemical conversion;
- transfer to another phase;
- adsorption;
- precipitation;
- sampling bias;
- dilution;
- analytical loss.

Therefore:

> **A concentration decrease is not automatically equivalent to complete sulfur removal.**

---

## 3. Pseudo-First-Order Sulfur Removal

For many screening calculations, sulfur disappearance is represented by:

$$
-r_S = k_{\mathrm{obs}} C_S
$$

where:

- $r_S$ is the volumetric sulfur-species removal rate;
- $k_{\mathrm{obs}}$ is an observed or apparent first-order coefficient;
- $C_S$ is the sulfur-species concentration.

Dimensional consistency requires:

$$
[k_{\mathrm{obs}}] = \mathrm{time^{-1}}
$$

For a constant-volume batch system with constant $k_{\mathrm{obs}}$:

$$
\frac{dC_S}{dt} = -k_{\mathrm{obs}}C_S
$$

and integration gives:

$$
\ln\left(\frac{C_{S,0}}{C_S}\right)
=
k_{\mathrm{obs}}t
$$

or:

$$
C_S
=
C_{S,0}\exp(-k_{\mathrm{obs}}t)
$$

The corresponding conversion is:

$$
X_S
=
1-\exp(-k_{\mathrm{obs}}t)
$$

### Assumptions

This integrated form assumes:

- constant volume;
- no sulfur inflow or outflow during the batch interval;
- one apparent first-order coefficient over the fitted interval;
- no unmodeled phase transfer or sampling-volume correction;
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
- downstream removal occurring during the measurement interval.

It must not automatically be interpreted as an intrinsic kinetic coefficient.

---

## 4. Generalized Oxidative Desulfurization Rate

A generalized oxidative-desulfurization rate may be represented as:

$$
-r_S
=
k C_S^n C_{\mathrm{ox}}^m
$$

where:

- $k$ is the kinetic or apparent rate coefficient;
- $C_S$ is sulfur-compound concentration;
- $C_{\mathrm{ox}}$ is oxidant concentration;
- $n$ is the apparent order with respect to sulfur species;
- $m$ is the apparent order with respect to oxidant.

If $r_S$ is expressed as concentration per time, dimensional consistency requires:

$$
[k]
=
[\mathrm{concentration}]^{\,1-n-m}
[\mathrm{time}]^{-1}
$$

When oxidant concentration remains approximately constant:

$$
k_{\mathrm{obs}}
=
k C_{\mathrm{ox}}^m
$$

and, only when $n=1$:

$$
-r_S
=
k_{\mathrm{obs}}C_S
$$

The resulting $k_{\mathrm{obs}}$ may still depend on:

- catalyst concentration;
- phase ratio;
- interfacial area;
- temperature;
- mixing;
- oxidant decomposition;
- oxidant utilization;
- sulfur speciation.

### Applicability Boundary

The pseudo-first-order reduction is not justified when oxidant concentration changes materially, reaction order changes, catalyst activity changes, or mass transfer evolves during the fitted interval.

---

## 5. Arrhenius Temperature Dependence

The temperature dependence of a kinetic coefficient may be represented by:

$$
k
=
A\exp\left(-\frac{E_a}{RT}\right)
$$

where:

- $A$ is the pre-exponential factor and has the same units as $k$;
- $E_a$ is activation energy, typically $\mathrm{J\,mol^{-1}}$;
- $R$ is the universal gas constant, $8.314462618\ \mathrm{J\,mol^{-1}\,K^{-1}}$;
- $T$ is absolute temperature in kelvin.

The linearized form is:

$$
\ln k
=
\ln A
-
\frac{E_a}{R}
\frac{1}{T}
$$

### Engineering Caution

An apparent activation energy can be distorted by:

- external mass transfer;
- internal diffusion;
- adsorption equilibrium;
- catalyst deactivation;
- changes in phase behavior;
- temperature-dependent mixing or viscosity;
- analytical or fitting limitations.

A low apparent activation energy may indicate transport influence, but it is not conclusive proof of a specific limitation.

---

## 6. Interphase Mass Transfer

For gas–liquid or liquid–liquid transfer on a liquid concentration basis:

$$
r_{\mathrm{mt}}
=
k_La\left(C^*-C\right)
$$

where:

- $r_{\mathrm{mt}}$ is the volumetric transfer rate;
- $k_L$ is the liquid-side mass-transfer coefficient;
- $a$ is interfacial area per reactor volume;
- $k_La$ is the volumetric mass-transfer coefficient;
- $C^*$ is the equilibrium concentration corresponding to the interfacial condition;
- $C$ is the bulk-phase concentration.

Dimensional consistency requires:

$$
[k_La]
=
\mathrm{time^{-1}}
$$

when $r_{\mathrm{mt}}$ and $C$ are expressed on the same volumetric concentration basis.

This relationship is relevant to:

- hydrogen sulfide absorption;
- oxygen or oxidant transfer;
- oxidative desulfurization;
- multiphase catalytic oxidation;
- liquid–liquid extraction-assisted systems.

### Engineering Caution

The notation $k_La$ can hide changes in both:

- local transfer coefficient, $k_L$;
- interfacial area, $a$.

An observed increase in $k_La$ does not by itself identify which contribution changed.

---

## 7. Gas-Side Hydrogen-Sulfide Transfer

For a pressure-based gas-side driving force:

$$
N_{H_2S}
=
K_Ga
\left(
P_{H_2S}-P_{H_2S}^*
\right)
$$

where:

- $N_{H_2S}$ is the volumetric hydrogen-sulfide transfer rate;
- $K_Ga$ is an overall volumetric gas-side transfer coefficient;
- $P_{H_2S}$ is bulk gas-phase hydrogen-sulfide partial pressure;
- $P_{H_2S}^*$ is the equilibrium partial pressure corresponding to the liquid-side condition.

If $N_{H_2S}$ is expressed in $\mathrm{mol\,m^{-3}\,s^{-1}}$ and pressure in pascals:

$$
[K_Ga]
=
\mathrm{mol\,m^{-3}\,s^{-1}\,Pa^{-1}}
$$

The observed performance can depend on:

- solvent chemistry;
- chemical enhancement;
- interfacial area;
- circulation rate;
- gas velocity;
- temperature;
- total pressure;
- contactor geometry;
- equilibrium representation.

### Basis Requirement

Do not combine pressure-based and concentration-based transfer coefficients without an explicit equilibrium relation and unit conversion.

---

## 8. Reaction-to-Mass-Transfer Diagnostic Ratio

When both reaction and mass transfer can be represented by first-order coefficients on the same time basis, a diagnostic ratio is:

$$
Da_{\mathrm{diag}}
=
\frac{k_{\mathrm{rxn}}}{k_La}
$$

where both $k_{\mathrm{rxn}}$ and $k_La$ have units of $\mathrm{time^{-1}}$.

Approximate screening interpretation:

- $Da_{\mathrm{diag}} \ll 1$: reaction-controlled tendency;
- $Da_{\mathrm{diag}} \approx 1$: coupled reaction–transport tendency;
- $Da_{\mathrm{diag}} \gg 1$: mass-transfer-controlled tendency.

Equivalently, using characteristic times:

$$
Da_{\mathrm{diag}}
=
\frac{\tau_{\mathrm{mt}}}{\tau_{\mathrm{rxn}}}
$$

with:

$$
\tau_{\mathrm{rxn}}
=
\frac{1}{k_{\mathrm{rxn}}}
$$

and:

$$
\tau_{\mathrm{mt}}
=
\frac{1}{k_La}
$$

### Important Limitation

The ratio $k_{\mathrm{rxn}}/k_La$ is dimensionless only when both coefficients use compatible first-order bases.

For higher-order kinetics, complex reactor models, reactive absorption, or changing interfacial area, construct the Damköhler number from consistent characteristic rates or timescales. The exact definition depends on:

- reactor type;
- rate law;
- characteristic length;
- phase system;
- geometry;
- selected concentration basis.

The repository example therefore uses this quantity as an **illustrative diagnostic ratio**, not as a universal Damköhler-number definition.

---

## 9. Internal Diffusion and the Thiele Modulus

For an isothermal spherical porous particle with a first-order volumetric reaction:

$$
\phi
=
R_p
\sqrt{
\frac{k_v}{D_{\mathrm{eff}}}
}
$$

where:

- $\phi$ is the Thiele modulus;
- $R_p$ is particle radius;
- $k_v$ is a first-order reaction coefficient on a catalyst-pore-volume basis;
- $D_{\mathrm{eff}}$ is effective diffusivity.

Dimensional consistency is:

$$
[\phi]
=
[\mathrm{m}]
\sqrt{
\frac{\mathrm{s^{-1}}}
{\mathrm{m^2\,s^{-1}}}
}
=
1
$$

### Basis Requirement

If the kinetic rate is expressed per:

- catalyst mass;
- external surface area;
- active-site inventory;

it must be converted to a compatible volumetric basis before use in this expression.

### Approximate Interpretation

- $\phi \ll 1$: weak internal diffusion influence;
- $\phi \approx 1$: reaction and diffusion are coupled;
- $\phi \gg 1$: substantial internal diffusion influence.

These are qualitative screening statements. The practical threshold depends on acceptable catalyst utilization and uncertainty.

### Assumptions

The expression assumes:

- spherical geometry;
- first-order reaction;
- constant effective diffusivity;
- isothermal behavior;
- uniform porous structure;
- no concentration-dependent reaction coefficient;
- a defined external particle concentration.

---

## 10. Spherical-Particle Effectiveness Factor

The internal effectiveness factor is:

$$
\eta
=
\frac{
\text{actual total reaction rate inside the porous particle}
}{
\text{rate if the entire particle were at the external surface concentration}
}
$$

For a first-order reaction in an isothermal spherical particle:

$$
\eta
=
\frac{3}{\phi^2}
\left(
\phi\coth\phi-1
\right)
$$

An equivalent computational form is:

$$
\eta
=
\frac{3}{\phi^2}
\left(
\frac{\phi}{\tanh\phi}-1
\right)
$$

### Limiting Cases

As $\phi \rightarrow 0$:

$$
\eta
\rightarrow
1
$$

A numerically stable small-$\phi$ expansion is:

$$
\eta
\approx
1
-
\frac{\phi^2}{15}
+
\frac{2\phi^4}{315}
$$

For large $\phi$:

$$
\eta
\approx
\frac{3}{\phi}
-
\frac{3}{\phi^2}
$$

and the leading behavior is:

$$
\eta
\sim
\frac{3}{\phi}
$$

### Approximate Interpretation

- $\eta \approx 1$: most of the particle is effectively utilized;
- $0<\eta<1$: internal gradients reduce utilization;
- $\eta \ll 1$: substantial internal diffusion resistance.

### Numerical Safeguards

A computational implementation should:

- reject negative $\phi$;
- return $\eta=1$ at $\phi=0$;
- use a series expansion for very small $\phi$;
- avoid direct evaluation of expressions that subtract nearly equal numbers;
- verify that $0<\eta\leq1$ for the stated model.

---

## 11. Langmuir Adsorption Isotherm

For idealized finite-capacity adsorption:

$$
q_e
=
\frac{
q_{\max}K_LC_e
}{
1+K_LC_e
}
$$

where:

- $q_e$ is equilibrium adsorption capacity;
- $q_{\max}$ is maximum monolayer capacity;
- $K_L$ is the Langmuir affinity coefficient;
- $C_e$ is equilibrium sulfur concentration.

Dimensional consistency requires:

$$
[K_L]
=
[\mathrm{concentration}]^{-1}
$$

so that $K_LC_e$ is dimensionless.

### Limiting Cases

When $K_LC_e \ll 1$:

$$
q_e
\approx
q_{\max}K_LC_e
$$

When $K_LC_e \gg 1$:

$$
q_e
\rightarrow
q_{\max}
$$

### Assumptions and Limits

The Langmuir model assumes an idealized homogeneous surface, finite equivalent sites, and monolayer adsorption without interaction among adsorbed species.

Agreement with the equation does not prove that these assumptions describe the actual adsorption mechanism.

---

## 12. Freundlich Adsorption Isotherm

An empirical heterogeneous-surface relation is:

$$
q_e
=
K_F C_e^{1/n_F}
$$

where:

- $K_F$ is the Freundlich capacity coefficient;
- $n_F$ is an empirical heterogeneity parameter.

The units of $K_F$ depend on:

- the units of $q_e$;
- the units of $C_e$;
- the value of $1/n_F$.

Therefore, $K_F$ values cannot be compared unless concentration and loading bases are identical.

### Engineering Caution

The Freundlich relation has no finite saturation capacity. Extrapolation beyond the fitted concentration range can therefore become physically unrealistic.

Model agreement alone is not proof of a specific adsorption mechanism.

---

## 13. Pseudo-Second-Order Adsorption Model

A commonly used empirical adsorption-kinetics expression is:

$$
\frac{dq}{dt}
=
k_2(q_e-q)^2
$$

where:

- $q$ is loading at time $t$;
- $q_e$ is fitted equilibrium loading;
- $k_2$ is the pseudo-second-order coefficient.

If $q$ is expressed as mass of adsorbate per mass of adsorbent:

$$
[k_2]
=
[q]^{-1}
[\mathrm{time}]^{-1}
$$

For $q(0)=0$, integration gives:

$$
\frac{t}{q_t}
=
\frac{1}{k_2q_e^2}
+
\frac{t}{q_e}
$$

### Engineering Caution

Good agreement with this model is not, by itself, proof of chemisorption.

Mechanistic interpretation requires complementary evidence such as:

- equilibrium measurements;
- temperature dependence;
- spectroscopy;
- diffusion analysis;
- competitive-adsorption tests;
- regeneration behavior.

---

## 14. Simplified Overall Reaction–Transfer Resistance

For two linear sequential resistances expressed on a common coefficient basis:

$$
\frac{1}{k_{\mathrm{overall}}}
=
\frac{1}{k_{\mathrm{rxn}}}
+
\frac{1}{k_{\mathrm{mt}}}
$$

where all coefficients must have compatible units and driving-force definitions.

This gives:

$$
k_{\mathrm{overall}}
=
\frac{
k_{\mathrm{rxn}}k_{\mathrm{mt}}
}{
k_{\mathrm{rxn}}+k_{\mathrm{mt}}
}
$$

### Limiting Cases

If:

$$
k_{\mathrm{rxn}}
\ll
k_{\mathrm{mt}}
$$

then:

$$
k_{\mathrm{overall}}
\approx
k_{\mathrm{rxn}}
$$

If:

$$
k_{\mathrm{mt}}
\ll
k_{\mathrm{rxn}}
$$

then:

$$
k_{\mathrm{overall}}
\approx
k_{\mathrm{mt}}
$$

### Applicability Boundary

This additive-resistance form is valid only when:

- the resistances are sequential;
- the model is linear or appropriately linearized;
- coefficients use the same basis;
- driving forces are consistently defined;
- no strong coupling invalidates independent resistance addition.

It is a conceptual screening relation, not a universal reactor equation.

---

## 15. Apparent Cavitation Enhancement Factor

For hydrodynamic-cavitation-assisted desulfurization, define:

$$
F_{\mathrm{app}}
=
\frac{
k_{\mathrm{app,HC}}
}{
k_{\mathrm{app,ref}}
}
$$

where:

- $k_{\mathrm{app,HC}}$ is the apparent coefficient under hydrodynamic-cavitation conditions;
- $k_{\mathrm{app,ref}}$ is the apparent coefficient for a defined reference case.

Interpretation:

- $F_{\mathrm{app}}>1$: higher apparent rate than the reference;
- $F_{\mathrm{app}}=1$: no apparent rate difference;
- $F_{\mathrm{app}}<1$: lower apparent rate than the reference.

### Comparability Requirements

The two coefficients should be obtained using comparable:

- feed and sulfur speciation;
- temperature;
- pressure;
- oxidant or hydrogen dose;
- catalyst or adsorbent loading;
- phase ratio;
- analytical method;
- fitting interval;
- product and separation basis.

### Important Caution

A value above unity does not prove industrial usefulness. Evaluate:

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

$$
\sigma
=
\frac{
p_{\mathrm{ref}}-p_v
}{
\frac{1}{2}\rho v^2
}
$$

where:

- $p_{\mathrm{ref}}$ is a stated downstream, recovery, or reference absolute pressure;
- $p_v$ is vapor pressure at the local fluid temperature;
- $\rho$ is fluid density;
- $v$ is the stated characteristic velocity.

Dimensional consistency is:

$$
[\sigma]
=
\frac{\mathrm{Pa}}{\mathrm{Pa}}
=
1
$$

### Definition Requirement

Every reported value should identify:

- the pressure measurement location;
- whether the pressure is absolute;
- the velocity definition and area;
- fluid temperature;
- density;
- vapor-pressure basis;
- device geometry;
- flow rate.

### Engineering Caution

Lower $\sigma$ may correspond to stronger cavitation tendency within a defined setup, but equal values do not guarantee equal:

- cavity dynamics;
- collapse intensity;
- residence pattern;
- erosion risk;
- chemical effect;
- scale-up performance.

The cavitation number is a hydrodynamic descriptor, not a universal performance correlation.

---

## 17. Incremental Sulfur Removal

For comparison with a reference case:

$$
\Delta m_S
=
m_{S,\mathrm{removed,HC}}
-
m_{S,\mathrm{removed,ref}}
$$

where both sulfur-removal quantities use the same:

- feed basis;
- throughput;
- treatment duration;
- product boundary;
- analytical method.

Interpretation:

- $\Delta m_S>0$: positive incremental removal;
- $\Delta m_S=0$: no incremental removal;
- $\Delta m_S<0$: poorer removal than the reference.

Gross removal in the intensified case must not be substituted for incremental removal when the objective is to quantify the benefit attributable to intensification.

---

## 18. Additional Energy Input

Define the incremental energy associated with intensification as:

$$
\Delta E
=
E_{\mathrm{HC}}
-
E_{\mathrm{ref}}
$$

where the energy boundary should specify, as applicable:

- pump input;
- motor electrical input;
- heating or cooling;
- oxidant generation;
- recirculation;
- separation;
- auxiliary equipment.

For electrical devices, state whether energy is based on:

- nameplate power;
- measured electrical input;
- shaft power;
- hydraulic power.

These are not interchangeable.

---

## 19. Energy-Normalized Sulfur Removal

For a positive incremental energy input:

$$
EN_S
=
\frac{
\Delta m_S
}{
\Delta E
}
$$

where:

- $\Delta m_S$ is incremental sulfur removed relative to the reference;
- $\Delta E$ is additional energy consumed relative to the reference.

Representative units include:

$$
\mathrm{g\ S\,kWh^{-1}}
$$

or:

$$
\mathrm{kg\ S\,kWh^{-1}}
$$

The reciprocal specific energy demand is:

$$
SEC_S
=
\frac{
\Delta E
}{
\Delta m_S
}
$$

with representative units such as:

$$
\mathrm{kWh\,g^{-1}\ S}
$$

or:

$$
\mathrm{kWh\,kg^{-1}\ S}
$$

For positive finite values:

$$
EN_S
\cdot
SEC_S
=
1
$$

provided reciprocal units are used consistently.

### Numerical and Interpretive Safeguards

- If $\Delta E=0$, $EN_S$ is undefined.
- If $\Delta m_S=0$, $SEC_S$ is undefined.
- If $\Delta m_S<0$, the intensified case has a negative incremental sulfur-removal benefit.
- If $\Delta E<0$, the comparison requires explicit interpretation because the intensified configuration uses less energy than the reference.
- Report uncertainty when either numerator is obtained by subtracting similar measured quantities.

A large numerical value is not sufficient evidence of usefulness unless product quality, separation, reliability, and scale-up constraints are also acceptable.

---

## 20. Oxidant Utilization Efficiency

A stoichiometric oxidant-utilization efficiency may be defined as:

$$
\eta_{\mathrm{ox}}
=
\frac{
n_{\mathrm{ox,stoich,target}}
}{
n_{\mathrm{ox,supplied}}
}
$$

with:

$$
n_{\mathrm{ox,stoich,target}}
=
\nu_{\mathrm{ox}}
n_{S,\mathrm{converted,target}}
$$

where:

- $n_{\mathrm{ox,supplied}}$ is oxidant supplied on a molar or equivalent basis;
- $n_{S,\mathrm{converted,target}}$ is moles of target sulfur converted to the specified oxidation state;
- $\nu_{\mathrm{ox}}$ is the stoichiometric oxidant requirement per mole of target sulfur conversion.

A rigorous definition must state:

- oxidant identity;
- concentration or purity;
- stoichiometric basis;
- target sulfur species;
- target oxidation state;
- side reactions;
- decomposition;
- residual oxidant;
- analytical uncertainty.

For a consistent closed basis:

$$
0
\leq
\eta_{\mathrm{ox}}
\leq
1
$$

A calculated value above unity indicates that the basis, stoichiometry, sulfur analysis, oxidant analysis, or assumed reaction pathway requires review.

---

## 21. Separation Efficiency

For transformed sulfur entering a downstream separation step:

$$
\eta_{\mathrm{sep}}
=
\frac{
m_{S,\mathrm{removed\ from\ product}}
}{
m_{S,\mathrm{available\ for\ separation}}
}
$$

where:

- the numerator is sulfur actually removed from the final product phase;
- the denominator is transformed sulfur entering the defined separation boundary.

For a consistent nonnegative basis:

$$
0
\leq
\eta_{\mathrm{sep}}
\leq
1
$$

The final product sulfur concentration should be measured after the complete reaction and separation sequence.

This distinction is essential:

> **Sulfur conversion is not necessarily equivalent to sulfur removal.**

---

## 22. Sulfur-Balance Closure

For a batch or continuous process over a defined accounting interval:

$$
B_S
=
\frac{
\sum m_{S,\mathrm{out}}
+
\sum m_{S,\mathrm{accumulated}}
}{
\sum m_{S,\mathrm{in}}
}
$$

For a closed batch system without external sulfur input or output after charging:

$$
B_S
=
\frac{
\sum m_{S,\mathrm{recovered}}
}{
m_{S,0}
}
$$

A relative closure error may be reported as:

$$
\varepsilon_S
=
\left|
B_S-1
\right|
\times
100\%
$$

The balance should include, where relevant:

- treated hydrocarbon or gas;
- aqueous phase;
- extractant or solvent;
- adsorbent or catalyst deposits;
- precipitated solids;
- purge or vent streams;
- sampling losses;
- identified sulfur products.

### Engineering Caution

A numerically closed total-sulfur balance does not establish reaction mechanism. It establishes consistency of sulfur accounting within the analytical uncertainty and defined boundary.

---

## 23. Uncertainty Propagation for Ratios

For a ratio:

$$
y
=
\frac{a}{b}
$$

with independent uncertainties $u_a$ and $u_b$, a first-order relative uncertainty estimate is:

$$
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
$$

This approximation is relevant to:

- apparent enhancement factors;
- energy-normalized removal;
- specific energy demand;
- utilization efficiencies;
- separation efficiencies.

### Important Limitation

This linearized relation may become unreliable when:

- the denominator is near zero;
- uncertainty is large;
- variables are correlated;
- distributions are strongly non-normal;
- numerator or denominator is obtained from a small difference between large quantities.

In such cases, use a more appropriate uncertainty method, such as Monte Carlo propagation, and report the assumptions.

---

## 24. Recommended Engineering Interpretation

No single equation should be used in isolation to claim process superiority.

A technically defensible assessment should combine, where relevant:

- sulfur speciation;
- total sulfur balance;
- intrinsic and apparent kinetics;
- interphase mass transfer;
- internal diffusion;
- adsorption or surface phenomena;
- hydrodynamics;
- oxidant or hydrogen utilization;
- downstream separation;
- energy consumption;
- catalyst or adsorbent durability;
- erosion, corrosion, and fouling;
- product quality;
- uncertainty;
- reliability;
- scale-up transferability.

The primary objective is to determine:

1. which mechanism controls overall performance;
2. which secondary limitations remain relevant;
3. whether the proposed intervention addresses the controlling limitation;
4. whether the complete process improves relative to a defined reference.

---

## 25. Numerical Implementation Requirements

Executable implementations should:

- validate that required inputs are finite;
- reject nonphysical negative concentrations, diffusivities, radii, energies, and times;
- reject zero denominators before evaluating ratios;
- document every unit and basis;
- use numerically stable limiting expressions;
- distinguish warnings from fatal input errors;
- preserve significant digits appropriate to data uncertainty;
- test representative, boundary, and failure cases;
- reproduce published demonstration outputs from version-controlled inputs.

The repository examples are screening demonstrations. They should not silently replace missing plant or pilot data with assumed values.

---

## 26. Evidence, Applicability, and Responsible Use

| Element | Status | Interpretation |
|---|---|---|
| Individual classical equations | Established within stated assumptions | Require correct geometry, rate law, units, and boundary conditions |
| Repository integration and examples | **E3 — Engineering screening framework** | Transparent research prototype for diagnosis and comparison |
| Default parameter values | Illustrative | Not validated design or industrial data |
| Regime thresholds | Screening guidance | Must be justified for the specific decision |
| Industrial performance prediction | Not established | Requires independent validation and scale-up evidence |

Use these equations for:

- transparent screening;
- dimensional checks;
- sensitivity analysis;
- experimental planning;
- regime diagnosis;
- comparison with a defined reference;
- identification of missing evidence.

Do not use them as:

- universal kinetic correlations;
- final reactor-design calculations;
- guaranteed catalyst or adsorbent performance;
- complete process-safety analysis;
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
- defined system and energy boundaries;
- sulfur-balance closure;
- uncertainty assessment;
- comparison with an appropriate reference;
- system-specific validation.

The present repository implements these relationships as an **E3 engineering screening framework and executable research prototype**, not as a universally validated industrial design model.
