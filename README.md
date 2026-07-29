# Desulfurization Reaction–Transport Regimes

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21278796.svg)](https://doi.org/10.5281/zenodo.21278796)

An engineering diagnostic framework for identifying reaction–transport limitations, evaluating process-intensification options, and supporting scale-up decisions in gas- and petroleum-stream desulfurization.

---

## Purpose

Desulfurization performance is rarely controlled by reaction chemistry alone.

Observed sulfur removal may depend simultaneously on:

- intrinsic reaction kinetics;
- gas–liquid or liquid–solid mass transfer;
- internal pore diffusion;
- adsorption and surface availability;
- mixing and hydrodynamics;
- oxidant or hydrogen utilization;
- downstream separation;
- catalyst or adsorbent durability;
- energy input;
- feed composition and sulfur speciation.

This repository provides a structured framework for distinguishing these effects and determining which limitation should be addressed before modifying chemistry, equipment, operating conditions, or process-intensification strategy.

---

## Practical Engineering Questions

The framework is intended to support questions such as:

- Is the observed process primarily reaction-controlled or transport-limited?
- Would increasing catalyst activity materially improve overall sulfur removal?
- Is oxidant addition limited by chemistry, dispersion, mass transfer, or downstream separation?
- Could adsorption capacity, pore diffusion, or regeneration determine performance?
- Does an intensification method address the actual process bottleneck?
- Are reported removal values transferable across feeds, sulfur species, reactors, and operating conditions?
- What validation evidence is required before pilot or industrial scale-up?
- Does the expected improvement justify additional energy, chemicals, pressure drop, maintenance, or separation burden?

---

## Application Scope

The methodology is relevant to sulfur removal from:

- natural gas and acid-gas streams;
- light hydrocarbons;
- diesel and middle distillates;
- heavy petroleum fractions.

It may support the engineering assessment of:

- hydrodesulfurization;
- oxidative desulfurization;
- adsorptive desulfurization;
- reactive adsorptive desulfurization;
- catalytic oxidation and sweetening;
- radical-assisted oxidation;
- hydrodynamic and mixing-based process intensification.

---

## Reaction–Transport Regimes

The framework considers several possible controlling or interacting regimes:

- reaction-controlled;
- external mass-transfer-limited;
- internal diffusion-limited;
- adsorption- or capacity-limited;
- oxidant- or reactant-utilization-limited;
- mixing- or hydrodynamics-limited;
- downstream-separation-limited;
- mixed or transitional regimes.

The purpose of the classification is not merely descriptive. It is intended to connect the identified regime with appropriate experimental, modelling, design, and scale-up actions.

---

## Process-Intensification Perspective

Hydrodynamic cavitation and related intensification technologies are treated as possible **reaction–transport intensification layers**, not as universal stand-alone desulfurization solutions.

Their usefulness depends on whether they:

1. address an identified kinetic, transport, dispersion, or phase-contacting limitation;
2. improve sulfur removal or process performance relative to a defined reference case;
3. maintain acceptable product quality;
4. avoid disproportionate energy, chemical, pressure-drop, erosion, fouling, or separation penalties;
5. remain technically and economically transferable during scale-up.

This repository therefore emphasizes energy-normalized and system-level assessment rather than removal percentage alone.

---

## Scientific and Engineering Basis

The repository is based on:

### Primary Framework

**Reaction–Transport Regime Analysis for Desulfurization of Gas and Petroleum Streams: An Engineering Diagnostic Framework**

DOI: [10.5281/zenodo.20095695](https://doi.org/10.5281/zenodo.20095695)

### Supporting Process-Intensification Framework

**Industrial Usefulness and Technology Selection in Process Intensification: Energy-Normalized Metrics for Hydrodynamic Cavitation**

DOI: [10.5281/zenodo.20593905](https://doi.org/10.5281/zenodo.20593905)

The supporting work introduces the **Industrial Usefulness Window** and energy-normalized decision metrics for evaluating whether an intensification technology creates transferable industrial value after accounting for energy demand, chemical consumption, pressure drop, separation burden, erosion, fouling, maintenance, product quality, reliability, and scale-up constraints.

---

## Repository Contents

```text
docs/       Technical documentation and framework notes
examples/   Simplified calculation examples
data/       Illustrative parameters and demonstration data
