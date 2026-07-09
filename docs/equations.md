# Core Equations for Desulfurization Reaction–Transport Regime Analysis

## Purpose

This document summarizes the principal equations used for engineering diagnosis of desulfurization systems.

The equations are intended to support regime identification, comparison of reaction and transport rates, assessment of porous-catalyst or adsorbent limitations, evaluation of hydrodynamic intensification, and energy-normalized process assessment.

The equations should not be interpreted as universal predictive models. Their applicability depends on the feed composition, sulfur species, phase system, catalyst or adsorbent, reactor configuration, hydrodynamics, operating conditions, and available experimental validation.

---

## 1. Pseudo-First-Order Sulfur Removal

For many desulfurization systems, an apparent pseudo-first-order expression is used:

\[
-r_S = k_{\mathrm{obs}} C_S
\]

where:

- \(r_S\) = sulfur-species removal rate
- \(k_{\mathrm{obs}}\) = observed or apparent rate constant
- \(C_S\) = concentration of the sulfur species

For a batch system with constant volume:

\[
\ln\left(\frac{C_{S,0}}{C_S}\right) = k_{\mathrm{obs}}t
\]

where:

- \(C_{S,0}\) = initial sulfur concentration
- \(C_S\) = sulfur concentration at time \(t\)
- \(t\) = reaction time

### Engineering caution

The measured \(k_{\mathrm{obs}}\) may include contributions from:

- intrinsic reaction kinetics
- interphase mass transfer
- mixing
- catalyst accessibility
- internal diffusion
- adsorption
- oxidant activation
- hydrodynamic intensification

Therefore, an apparent rate constant should not automatically be interpreted as an intrinsic kinetic constant.

---

## 2. Generalized Oxidative Desulfurization Rate

For oxidative desulfurization:

\[
-r_S = k C_S^n C_{\mathrm{ox}}^m
\]

where:

- \(k\) = apparent or intrinsic rate coefficient, depending on the model
- \(C_S\) = sulfur-compound concentration
- \(C_{\mathrm{ox}}\) = oxidant concentration
- \(n\) = apparent reaction order with respect to sulfur species
- \(m\) = apparent reaction order with respect to oxidant

When oxidant concentration remains approximately constant:

\[
-r_S = k_{\mathrm{obs}}C_S
\]

The resulting \(k_{\mathrm{obs}}\) may still depend on catalyst concentration, interfacial area, temperature, phase ratio, mixing, and oxidant utilization.

---

## 3. Arrhenius Temperature Dependence

The temperature dependence of a kinetic coefficient may be represented by:

\[
k = A\exp\left(-\frac{E_a}{RT}\right)
\]

where:

- \(A\) = pre-exponential factor
- \(E_a\) = apparent or intrinsic activation energy
- \(R\) = universal gas constant
- \(T\) = absolute temperature

### Engineering caution

An unusually low apparent activation energy may indicate that the measured process is affected by external mass transfer or internal diffusion rather than controlled solely by intrinsic reaction kinetics.

---

## 4. Interphase Mass Transfer

For gas–liquid, liquid–liquid, or liquid–solid systems:

\[
r_{\mathrm{mt}} = k_La(C^* - C)
\]

where:

- \(r_{\mathrm{mt}}\) = volumetric mass-transfer rate
- \(k_La\) = volumetric liquid-side mass-transfer coefficient
- \(C^*\) = equilibrium concentration corresponding to the interface
- \(C\) = bulk-phase concentration

This equation is particularly relevant to:

- H₂S absorption
- oxygen transfer
- oxidative desulfurization
- multiphase catalytic oxidation
- liquid–liquid extraction-assisted systems

---

## 5. Gas-Side H₂S Transfer

For gas-treatment applications:

\[
N_{H_2S} = k_Ga\left(P_{H_2S} - P_{H_2S}^*\right)
\]

where:

- \(N_{H_2S}\) = volumetric H₂S absorption rate
- \(k_Ga\) = volumetric gas-side mass-transfer coefficient
- \(P_{H_2S}\) = bulk gas-phase partial pressure of H₂S
- \(P_{H_2S}^*\) = equilibrium partial pressure corresponding to the liquid-phase concentration

The observed removal performance may therefore depend on solvent chemistry as well as interfacial area, circulation rate, gas velocity, temperature, pressure, and contactor design.

---

## 6. Reaction-to-Mass-Transfer Damköhler-Type Ratio

A practical diagnostic ratio is:

\[
Da = \frac{k_{\mathrm{rxn}}}{k_La}
\]

Approximate interpretation:

- \(Da \ll 1\): reaction-controlled tendency
- \(Da \approx 1\): coupled reaction–transport regime
- \(Da \gg 1\): mass-transfer-controlled tendency

For reactive H₂S absorption:

\[
Da_{\mathrm{abs}} = \frac{k_{\mathrm{rxn}}}{k_La}
\]

### Important limitation

The exact definition of a Damköhler number depends on the reactor, characteristic time scales, rate law, geometry, and phase system. The above ratio is therefore a diagnostic form and should not be treated as a universal definition for every desulfurization process.

---

## 7. Internal Diffusion and Thiele Modulus

For a first-order reaction in a spherical porous catalyst particle:

\[
\phi = R_p\sqrt{\frac{k}{D_{\mathrm{eff}}}}
\]

where:

- \(\phi\) = Thiele modulus
- \(R_p\) = catalyst-particle radius
- \(k\) = first-order reaction-rate coefficient
- \(D_{\mathrm{eff}}\) = effective diffusivity

Approximate interpretation:

- \(\phi \ll 1\): weak internal diffusion limitation
- \(\phi \approx 1\): reaction and diffusion are coupled
- \(\phi \gg 1\): significant internal diffusion limitation

---

## 8. Effectiveness Factor

The effectiveness factor is:

\[
\eta =
\frac{\text{actual reaction rate inside the porous particle}}
{\text{rate if the entire particle were at the external surface concentration}}
\]

For a first-order reaction in an isothermal spherical particle:

\[
\eta =
\frac{3}{\phi^2}
\left(
\phi\coth\phi - 1
\right)
\]

Approximate interpretation:

- \(\eta \approx 1\): most of the catalyst particle is effectively utilized
- \(\eta \ll 1\): substantial internal diffusion resistance is present

---

## 9. Langmuir Adsorption Isotherm

For adsorption equilibrium:

\[
q_e =
\frac{q_{\max}K_LC_e}
{1 + K_LC_e}
\]

where:

- \(q_e\) = equilibrium adsorption capacity
- \(q_{\max}\) = maximum adsorption capacity
- \(K_L\) = Langmuir affinity constant
- \(C_e\) = equilibrium sulfur concentration

The Langmuir model assumes an idealized homogeneous adsorption surface and finite monolayer capacity.

---

## 10. Freundlich Adsorption Isotherm

An empirical heterogeneous-surface model is:

\[
q_e = K_F C_e^{1/n_F}
\]

where:

- \(K_F\) = Freundlich capacity coefficient
- \(n_F\) = empirical heterogeneity parameter

Model selection should be based on experimental evidence and should not by itself be interpreted as proof of a specific adsorption mechanism.

---

## 11. Pseudo-Second-Order Adsorption Model

A commonly used empirical adsorption-kinetics model is:

\[
\frac{dq}{dt} = k_2(q_e-q)^2
\]

Its integrated form is:

\[
\frac{t}{q_t}
=
\frac{1}{k_2q_e^2}
+
\frac{t}{q_e}
\]

where:

- \(q_t\) = adsorption capacity at time \(t\)
- \(q_e\) = equilibrium adsorption capacity
- \(k_2\) = pseudo-second-order rate coefficient

### Engineering caution

Good agreement with a pseudo-second-order model is not, by itself, proof of chemisorption. Mechanistic interpretation requires complementary evidence.

---

## 12. Overall Reaction–Transport Resistance

For simplified sequential reaction and mass-transfer resistances:

\[
\frac{1}{k_{\mathrm{overall}}}
=
\frac{1}{k_{\mathrm{rxn}}}
+
\frac{1}{k_{\mathrm{mt}}}
\]

where:

- \(k_{\mathrm{overall}}\) = observed overall coefficient
- \(k_{\mathrm{rxn}}\) = reaction-related coefficient
- \(k_{\mathrm{mt}}\) = mass-transfer-related coefficient

This simplified resistance form is useful for conceptual diagnosis but should only be applied when its assumptions are consistent with the actual system.

---

## 13. Cavitation Enhancement Factor

For cavitation-assisted desulfurization, a dimensionless apparent enhancement factor may be defined as:

\[
E_{\mathrm{HC}} =
\frac{k_{\mathrm{app,HC}}}
{k_{\mathrm{app,ref}}}
\]

where:

- \(k_{\mathrm{app,HC}}\) = apparent rate constant under hydrodynamic-cavitation conditions
- \(k_{\mathrm{app,ref}}\) = apparent rate constant for a defined non-HC reference case

Interpretation:

- \(E_{\mathrm{HC}} > 1\): apparent rate enhancement
- \(E_{\mathrm{HC}} = 1\): no apparent rate enhancement
- \(E_{\mathrm{HC}} < 1\): lower apparent performance than the reference

### Important caution

An enhancement factor greater than unity does not prove industrial usefulness. Energy demand, pressure drop, erosion, emulsion formation, oxidant consumption, separation burden, maintenance, and reliability should also be evaluated.

---

## 14. Cavitation Number

For hydrodynamic cavitation:

\[
\sigma =
\frac{p_2-p_v}
{0.5\rho v^2}
\]

where:

- \(p_2\) = representative downstream or recovery pressure
- \(p_v\) = vapor pressure
- \(\rho\) = fluid density
- \(v\) = characteristic velocity

Lower values of \(\sigma\) may indicate stronger cavitation tendencies, but equal cavitation numbers do not guarantee equal process performance because geometry, pressure recovery, flow field, residence pattern, fluid properties, and collapse location may differ.

---

## 15. Energy-Normalized Sulfur Removal

A basic energy-normalized sulfur-removal metric is:

\[
EN_S =
\frac{\Delta m_S}{E}
\]

where:

- \(\Delta m_S\) = sulfur mass removed relative to a defined reference
- \(E\) = additional energy consumed

Possible units include:

\[
\mathrm{mg\ S/kWh}
\]

or:

\[
\mathrm{g\ S/kWh}
\]

depending on scale.

A corresponding specific energy demand may be expressed as:

\[
SEC_S =
\frac{E}{\Delta m_S}
\]

with possible units such as:

\[
\mathrm{kWh/g\ S}
\]

or:

\[
\mathrm{kWh/kg\ S}
\]

---

## 16. Oxidant Utilization Efficiency

For oxidative desulfurization:

\[
\eta_{\mathrm{ox}} =
\frac{\text{useful oxidant consumption associated with target sulfur conversion}}
{\text{total oxidant supplied}}
\]

A rigorous definition should specify:

- oxidant identity
- stoichiometric basis
- target sulfur species
- desired oxidation state
- side reactions
- oxidant decomposition
- residual oxidant

High sulfur conversion with poor oxidant utilization may be technically or economically unattractive.

---

## 17. Separation Performance

For a chemically transformed sulfur species, a simple separation efficiency may be expressed as:

\[
\eta_{\mathrm{sep}} =
\frac{m_{S,\mathrm{removed\ from\ product}}}
{m_{S,\mathrm{available\ for\ separation}}}
\]

The final product sulfur concentration should be measured after the complete reaction and separation sequence.

This distinction is essential because:

> **Sulfur conversion is not necessarily equivalent to sulfur removal.**

---

## 18. Recommended Engineering Interpretation

No single equation should be used in isolation to claim process superiority.

A technically defensible assessment should combine, where relevant:

- sulfur speciation
- reaction kinetics
- interphase mass transfer
- internal diffusion
- adsorption or surface phenomena
- hydrodynamics
- oxidant utilization
- downstream separation
- energy consumption
- catalyst or adsorbent durability
- erosion, corrosion, and fouling
- product quality
- reliability
- scale-up transferability

The primary objective is to determine which mechanism controls overall performance and whether the proposed intervention improves the complete process rather than only one local performance indicator.
