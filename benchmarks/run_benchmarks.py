from __future__ import annotations

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "02_Data"
RESULTS = ROOT / "04_Results"


def effectiveness_factor_sphere(phi: float) -> float:
    if not math.isfinite(phi) or phi < 0:
        raise ValueError("phi must be finite and non-negative")
    if phi == 0:
        return 1.0
    if phi < 1.0e-4:
        p2 = phi * phi
        eta = 1.0 - p2 / 15.0 + 2.0 * p2 * p2 / 315.0
    elif phi > 50.0:
        eta = 3.0 / phi - 3.0 / (phi * phi)
    else:
        eta = 3.0 / (phi * phi) * (phi / math.tanh(phi) - 1.0)
    return min(1.0, max(0.0, eta))


def classify_hds(eta: float) -> str:
    if eta >= 0.95:
        return "weak_internal_diffusion"
    if eta >= 0.80:
        return "mild_reaction_diffusion_coupling"
    if eta >= 0.50:
        return "significant_reaction_diffusion_coupling"
    return "strong_internal_diffusion"


def classify_ods(rxn_fraction: float, transfer_fraction: float, dominance: float) -> str:
    if rxn_fraction >= dominance:
        return "reaction_dominated"
    if transfer_fraction >= dominance:
        return "external_transfer_dominated"
    return "mixed_or_transitional"


def run_hds() -> list[dict[str, object]]:
    rows = []
    with (DATA / "hds_benchmark_inputs.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rp = float(r["particle_radius_m"])
            kv = float(r["volumetric_rate_constant_s_inv"])
            de = float(r["effective_diffusivity_m2_s"])
            phi = rp * math.sqrt(kv / de)
            eta = effectiveness_factor_sphere(phi)
            rows.append({
                "case_id": r["case_id"],
                "case_label": r["case_label"],
                "thiele_modulus": phi,
                "effectiveness_factor": eta,
                "model_implied_weisz_prater": eta * phi * phi,
                "internal_utilization_loss_percent": (1.0 - eta) * 100.0,
                "classification": classify_hds(eta),
                "evidence_status": "illustrative_not_validated",
            })
    return rows


def run_ods() -> list[dict[str, object]]:
    rows = []
    with (DATA / "ods_benchmark_inputs.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            kr = float(r["reaction_coefficient_s_inv"])
            km = float(r["effective_transfer_coefficient_s_inv"])
            dom = float(r["dominance_fraction"])
            sf = float(r["sensitivity_factor"])
            tr = 1.0 / kr
            tm = 1.0 / km
            total = tr + tm
            rf = tr / total
            mf = tm / total
            ko = 1.0 / total
            ko_rxn = 1.0 / (1.0 / (kr * sf) + 1.0 / km)
            ko_mt = 1.0 / (1.0 / kr + 1.0 / (km * sf))
            rows.append({
                "case_id": r["case_id"],
                "case_label": r["case_label"],
                "diagnostic_ratio": kr / km,
                "reaction_resistance_fraction": rf,
                "transfer_resistance_fraction": mf,
                "overall_coefficient_s_inv": ko,
                "reaction_improvement_gain_percent": (ko_rxn / ko - 1.0) * 100.0,
                "transfer_improvement_gain_percent": (ko_mt / ko - 1.0) * 100.0,
                "classification": classify_ods(rf, mf, dom),
                "evidence_status": "illustrative_not_validated",
            })
    return rows


def read_cavitation() -> dict[tuple[str, str], float]:
    out = {}
    with (DATA / "cavitation_benchmark_inputs.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out[(r["case_id"], r["parameter"])] = float(r["value"])
    return out


def run_cavitation() -> list[dict[str, object]]:
    p = read_cavitation()
    ref = "reference_case"
    hc = "cavitation_case"
    h = "hydraulics"

    removed_ref = p[(ref, "initial_sulfur_in_feed_g")] - p[(ref, "sulfur_in_recovered_product_g")]
    removed_hc = p[(hc, "initial_sulfur_in_feed_g")] - p[(hc, "sulfur_in_recovered_product_g")]
    incremental_sulfur = removed_hc - removed_ref
    incremental_energy = (
        p[(hc, "measured_total_electrical_energy_kwh")]
        - p[(ref, "measured_total_electrical_energy_kwh")]
    )
    dp = p[(h, "upstream_pressure_abs_pa")] - p[(h, "downstream_reference_pressure_abs_pa")]
    hydraulic_power_w = dp * p[(h, "loop_flow_rate_m3_s")]
    estimated_drive_kwh = (
        hydraulic_power_w
        / (p[(h, "pump_efficiency")] * p[(h, "drive_efficiency")])
        * p[(h, "operating_time_s")]
        / 3.6e6
    )
    sigma = (
        p[(h, "downstream_reference_pressure_abs_pa")] - p[(h, "vapor_pressure_pa")]
    ) / (
        0.5 * p[(h, "density_kg_m3")] * p[(h, "characteristic_velocity_m_s")] ** 2
    )
    turnovers = (
        p[(h, "loop_flow_rate_m3_s")] * p[(h, "operating_time_s")]
        / p[(hc, "feed_volume_m3")]
    )

    return [{
        "case_id": "C1",
        "apparent_rate_enhancement": (
            p[(hc, "apparent_rate_coefficient_s_inv")]
            / p[(ref, "apparent_rate_coefficient_s_inv")]
        ),
        "incremental_sulfur_removed_g": incremental_sulfur,
        "incremental_electrical_energy_kwh": incremental_energy,
        "incremental_sulfur_g_per_kwh": incremental_sulfur / incremental_energy,
        "incremental_energy_kwh_per_g_sulfur": incremental_energy / incremental_sulfur,
        "hydraulic_power_w": hydraulic_power_w,
        "estimated_drive_energy_kwh": estimated_drive_kwh,
        "cavitation_number": sigma,
        "nominal_inventory_turnovers": turnovers,
        "classification": "industrial_feasibility_screening_only",
        "evidence_status": "illustrative_not_validated",
    }]


def write_csv(name: str, rows: list[dict[str, object]]) -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    with (RESULTS / name).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    write_csv("hds_benchmark_results.csv", run_hds())
    write_csv("ods_benchmark_results.csv", run_ods())
    write_csv("cavitation_benchmark_results.csv", run_cavitation())
    print("DP-02 benchmark calculations completed.")


if __name__ == "__main__":
    main()
