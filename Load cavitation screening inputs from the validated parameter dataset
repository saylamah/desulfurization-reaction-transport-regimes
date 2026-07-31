"""
Automated tests for the desulfurization engineering-screening examples.

The tests verify:

* authoritative CSV loading and schema enforcement;
* dimensional and numerical input safeguards;
* HDS Thiele-modulus and effectiveness-factor calculations;
* limiting behavior of the spherical-particle model;
* ODS reaction-transfer resistance accounting;
* consistency of diagnostic ratios and characteristic times;
* cavitation comparison boundaries;
* incremental sulfur and energy calculations;
* hydraulic and cavitation-number calculations;
* expected results from the documented illustrative cases.

Scientific boundary
-------------------
Passing these tests demonstrates that the repository calculations are
internally consistent with their stated equations and assumptions.

Passing tests does not validate:

* the illustrative parameters as experimental data;
* a reaction mechanism;
* intrinsic kinetics;
* industrial catalyst performance;
* hydrodynamic-cavitation efficacy;
* pilot- or industrial-scale transferability.

Evidence status
---------------
E3 -- automated verification for executable engineering-screening research
prototypes.
"""

from __future__ import annotations

from dataclasses import replace
import math
from pathlib import Path
import sys
import tempfile
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]

if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))


from examples.example_parameter_loader import (  # noqa: E402
    DEFAULT_DATA_PATH,
    ParameterStore,
    load_default_parameter_store,
)
from examples.hds_regime_example import (  # noqa: E402
    HDSInternalDiffusionCase,
    case_from_parameter_store as hds_case_from_parameter_store,
    effectiveness_factor_sphere,
    evaluate_case as evaluate_hds_case,
    model_implied_weisz_prater,
    thiele_modulus,
)
from examples.ods_mass_transfer_example import (  # noqa: E402
    ODSReactionTransferCase,
    case_from_parameter_store as ods_case_from_parameter_store,
    characteristic_time_s,
    classify_regime,
    diagnostic_reaction_to_transfer_ratio,
    evaluate_case as evaluate_ods_case,
    resistance_fractions,
    series_overall_coefficient,
)
from examples.cavitation_intensification_example import (  # noqa: E402
    CavitationOperatingPoint,
    CAVITATION_CASE_ID,
    REFERENCE_CASE_ID,
    compare_cases,
    desulfurization_case_from_store,
    energy_normalized_incremental_sulfur,
    hydraulic_operating_point_from_store,
    incremental_specific_energy,
)


class ParameterDatasetTests(unittest.TestCase):
    """Tests for the authoritative illustrative parameter dataset."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.store = load_default_parameter_store()

    def test_default_dataset_contains_expected_rows_and_cases(self) -> None:
        self.assertEqual(len(self.store.records), 32)
        self.assertEqual(len(self.store.case_keys), 5)

    def test_all_case_labels_are_nonempty(self) -> None:
        for example_id, case_id in self.store.case_keys:
            label = self.store.case_label(
                example_id,
                case_id,
            )

            self.assertTrue(label.strip())

    def test_known_parameter_unit_is_enforced(self) -> None:
        value = self.store.value(
            "hds_internal_diffusion",
            "hds_default",
            "effective_diffusivity_m2_s",
            expected_unit="m^2/s",
        )

        self.assertEqual(value, 1.0e-8)

        with self.assertRaises(ValueError):
            self.store.value(
                "hds_internal_diffusion",
                "hds_default",
                "effective_diffusivity_m2_s",
                expected_unit="cm^2/s",
            )

    def test_duplicate_parameter_definition_is_rejected(self) -> None:
        source_text = DEFAULT_DATA_PATH.read_text(
            encoding="utf-8",
        )
        source_lines = source_text.splitlines()
        duplicated_data_row = source_lines[1]

        corrupted_text = (
            source_text.rstrip()
            + "\n"
            + duplicated_data_row
            + "\n"
        )

        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = (
                Path(temporary_directory)
                / "duplicate_parameter.csv"
            )
            temporary_path.write_text(
                corrupted_text,
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                ValueError,
                "Duplicate parameter definition",
            ):
                ParameterStore.from_csv(
                    temporary_path
                )

    def test_schema_unit_error_is_rejected(self) -> None:
        source_text = DEFAULT_DATA_PATH.read_text(
            encoding="utf-8",
        )

        corrupted_text = source_text.replace(
            "1.0e-8,m^2/s,",
            "1.0e-8,cm^2/s,",
            1,
        )

        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = (
                Path(temporary_directory)
                / "wrong_unit.csv"
            )
            temporary_path.write_text(
                corrupted_text,
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                ValueError,
                "Unit mismatch",
            ):
                ParameterStore.from_csv(
                    temporary_path
                )

    def test_nonfinite_numerical_value_is_rejected(self) -> None:
        source_text = DEFAULT_DATA_PATH.read_text(
            encoding="utf-8",
        )

        corrupted_text = source_text.replace(
            "1.0e-3,m,",
            "nan,m,",
            1,
        )

        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = (
                Path(temporary_directory)
                / "nonfinite_value.csv"
            )
            temporary_path.write_text(
                corrupted_text,
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                ValueError,
                "must be finite",
            ):
                ParameterStore.from_csv(
                    temporary_path
                )


class HDSInternalDiffusionTests(unittest.TestCase):
    """Tests for the spherical HDS reaction-diffusion model."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.store = load_default_parameter_store()
        cls.case = hds_case_from_parameter_store(
            cls.store
        )
        cls.result = evaluate_hds_case(
            cls.case
        )

    def test_authoritative_case_values(self) -> None:
        self.assertEqual(
            self.case.particle_radius_m,
            1.0e-3,
        )
        self.assertEqual(
            self.case.volumetric_rate_constant_s_inv,
            5.0e-2,
        )
        self.assertEqual(
            self.case.effective_diffusivity_m2_s,
            1.0e-8,
        )

    def test_documented_hds_results(self) -> None:
        self.assertAlmostEqual(
            self.result.thiele_modulus,
            math.sqrt(5.0),
            places=12,
        )
        self.assertAlmostEqual(
            self.result.effectiveness_factor,
            0.7726457861442182,
            places=12,
        )
        self.assertAlmostEqual(
            self.result.model_implied_weisz_prater,
            3.8632289307210916,
            places=12,
        )
        self.assertAlmostEqual(
            self.result.internal_utilization_loss_percent,
            22.73542138557818,
            places=10,
        )

    def test_zero_rate_gives_zero_phi_and_unit_effectiveness(self) -> None:
        case = HDSInternalDiffusionCase(
            name="Zero-rate limiting case",
            particle_radius_m=1.0e-3,
            volumetric_rate_constant_s_inv=0.0,
            effective_diffusivity_m2_s=1.0e-8,
        )

        result = evaluate_hds_case(case)

        self.assertEqual(
            result.thiele_modulus,
            0.0,
        )
        self.assertEqual(
            result.effectiveness_factor,
            1.0,
        )
        self.assertEqual(
            result.model_implied_weisz_prater,
            0.0,
        )

    def test_effectiveness_factor_is_bounded(self) -> None:
        for phi in (
            0.0,
            1.0e-8,
            1.0e-4,
            0.1,
            1.0,
            5.0,
            50.0,
            100.0,
        ):
            eta = effectiveness_factor_sphere(phi)

            self.assertGreater(
                eta,
                0.0,
            )
            self.assertLessEqual(
                eta,
                1.0,
            )

    def test_effectiveness_factor_decreases_with_phi(self) -> None:
        phi_values = (
            0.1,
            0.5,
            1.0,
            2.0,
            5.0,
            10.0,
        )

        eta_values = tuple(
            effectiveness_factor_sphere(phi)
            for phi in phi_values
        )

        for earlier, later in zip(
            eta_values,
            eta_values[1:],
        ):
            self.assertGreater(
                earlier,
                later,
            )

    def test_small_phi_series_limit(self) -> None:
        phi = 1.0e-6
        eta = effectiveness_factor_sphere(phi)

        expected = (
            1.0
            - phi**2 / 15.0
            + 2.0 * phi**4 / 315.0
        )

        self.assertAlmostEqual(
            eta,
            expected,
            places=15,
        )

    def test_model_implied_weisz_prater_identity(self) -> None:
        phi = 2.5
        eta = effectiveness_factor_sphere(phi)

        calculated = model_implied_weisz_prater(
            phi,
            eta,
        )

        self.assertAlmostEqual(
            calculated,
            eta * phi**2,
            places=14,
        )

    def test_invalid_hds_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            thiele_modulus(
                particle_radius_m=0.0,
                volumetric_rate_constant_s_inv=0.05,
                effective_diffusivity_m2_s=1.0e-8,
            )

        with self.assertRaises(ValueError):
            thiele_modulus(
                particle_radius_m=1.0e-3,
                volumetric_rate_constant_s_inv=-0.05,
                effective_diffusivity_m2_s=1.0e-8,
            )

        with self.assertRaises(ValueError):
            effectiveness_factor_sphere(-1.0)


class ODSReactionTransferTests(unittest.TestCase):
    """Tests for the simplified ODS sequential-resistance model."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.store = load_default_parameter_store()
        cls.case = ods_case_from_parameter_store(
            cls.store
        )
        cls.result = evaluate_ods_case(
            cls.case
        )

    def test_authoritative_ods_case_values(self) -> None:
        self.assertEqual(
            self.case.reaction_coefficient_s_inv,
            2.0e-2,
        )
        self.assertEqual(
            self.case.effective_transfer_coefficient_s_inv,
            5.0e-3,
        )
        self.assertEqual(
            self.case.dominance_fraction,
            0.8,
        )
        self.assertEqual(
            self.case.sensitivity_factor,
            2.0,
        )

    def test_documented_ods_results(self) -> None:
        self.assertAlmostEqual(
            self.result.diagnostic_ratio,
            4.0,
            places=14,
        )
        self.assertAlmostEqual(
            self.result.reaction_time_s,
            50.0,
            places=14,
        )
        self.assertAlmostEqual(
            self.result.transfer_time_s,
            200.0,
            places=14,
        )
        self.assertAlmostEqual(
            self.result.overall_time_s,
            250.0,
            places=14,
        )
        self.assertAlmostEqual(
            self.result.overall_coefficient_s_inv,
            4.0e-3,
            places=14,
        )
        self.assertAlmostEqual(
            self.result.reaction_resistance_fraction,
            0.2,
            places=14,
        )
        self.assertAlmostEqual(
            self.result.transfer_resistance_fraction,
            0.8,
            places=14,
        )
        self.assertAlmostEqual(
            self.result.reaction_improvement_gain_percent,
            11.111111111111116,
            places=12,
        )
        self.assertAlmostEqual(
            self.result.transfer_improvement_gain_percent,
            66.66666666666666,
            places=12,
        )

    def test_ratio_and_characteristic_time_identity(self) -> None:
        ratio = diagnostic_reaction_to_transfer_ratio(
            reaction_coefficient_s_inv=0.02,
            effective_transfer_coefficient_s_inv=0.005,
        )

        time_ratio = (
            characteristic_time_s(0.005)
            / characteristic_time_s(0.02)
        )

        self.assertAlmostEqual(
            ratio,
            time_ratio,
            places=14,
        )

    def test_overall_coefficient_is_below_both_step_coefficients(
        self,
    ) -> None:
        reaction_coefficient = 0.02
        transfer_coefficient = 0.005

        overall = series_overall_coefficient(
            reaction_coefficient,
            transfer_coefficient,
        )

        self.assertLess(
            overall,
            reaction_coefficient,
        )
        self.assertLess(
            overall,
            transfer_coefficient,
        )

    def test_resistance_fractions_sum_to_one(self) -> None:
        reaction_fraction, transfer_fraction = (
            resistance_fractions(
                reaction_coefficient_s_inv=0.02,
                effective_transfer_coefficient_s_inv=0.005,
            )
        )

        self.assertAlmostEqual(
            reaction_fraction + transfer_fraction,
            1.0,
            places=15,
        )

    def test_swapping_coefficients_swaps_resistance_fractions(
        self,
    ) -> None:
        first_reaction, first_transfer = resistance_fractions(
            reaction_coefficient_s_inv=0.02,
            effective_transfer_coefficient_s_inv=0.005,
        )
        second_reaction, second_transfer = resistance_fractions(
            reaction_coefficient_s_inv=0.005,
            effective_transfer_coefficient_s_inv=0.02,
        )

        self.assertAlmostEqual(
            first_reaction,
            second_transfer,
            places=15,
        )
        self.assertAlmostEqual(
            first_transfer,
            second_reaction,
            places=15,
        )

    def test_classification_uses_explicit_resistance_fraction(
        self,
    ) -> None:
        statement = classify_regime(
            reaction_resistance_fraction=0.2,
            transfer_resistance_fraction=0.8,
            dominance_fraction=0.8,
        )

        self.assertIn(
            "External-transfer-dominated",
            statement,
        )

    def test_invalid_ods_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            diagnostic_reaction_to_transfer_ratio(
                reaction_coefficient_s_inv=0.02,
                effective_transfer_coefficient_s_inv=0.0,
            )

        with self.assertRaises(ValueError):
            ODSReactionTransferCase(
                name="Invalid dominance case",
                reaction_coefficient_s_inv=0.02,
                effective_transfer_coefficient_s_inv=0.005,
                dominance_fraction=1.0,
                sensitivity_factor=2.0,
            )


class CavitationIntensificationTests(unittest.TestCase):
    """Tests for cavitation-assisted process comparison calculations."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.store = load_default_parameter_store()

        cls.reference = desulfurization_case_from_store(
            cls.store,
            REFERENCE_CASE_ID,
        )
        cls.intensified = desulfurization_case_from_store(
            cls.store,
            CAVITATION_CASE_ID,
        )
        cls.hydraulics = hydraulic_operating_point_from_store(
            cls.store
        )
        cls.comparison = compare_cases(
            reference=cls.reference,
            intensified=cls.intensified,
        )

    def test_documented_incremental_comparison_results(self) -> None:
        self.assertAlmostEqual(
            self.comparison.apparent_enhancement_factor,
            3.0,
            places=14,
        )
        self.assertAlmostEqual(
            self.comparison.incremental_sulfur_excluded_from_product_g,
            3.5,
            places=14,
        )
        self.assertAlmostEqual(
            self.comparison.incremental_electrical_energy_kwh,
            0.75,
            places=14,
        )
        self.assertAlmostEqual(
            self.comparison.energy_normalized_incremental_sulfur_g_per_kwh,
            4.666666666666667,
            places=14,
        )
        self.assertAlmostEqual(
            self.comparison.incremental_specific_energy_kwh_per_g_s,
            0.21428571428571427,
            places=14,
        )
        self.assertAlmostEqual(
            self.comparison.incremental_specific_energy_kwh_per_kg_s,
            214.28571428571428,
            places=12,
        )
        self.assertAlmostEqual(
            self.comparison.incremental_energy_intensity_kwh_m3,
            3.75,
            places=14,
        )

    def test_energy_metrics_are_reciprocal(self) -> None:
        energy_normalized = energy_normalized_incremental_sulfur(
            incremental_sulfur_g=3.5,
            incremental_energy_kwh=0.75,
        )
        specific_energy = incremental_specific_energy(
            incremental_energy_kwh=0.75,
            incremental_sulfur_g=3.5,
        )

        self.assertAlmostEqual(
            energy_normalized * specific_energy,
            1.0,
            places=14,
        )

    def test_documented_hydraulic_results(self) -> None:
        self.assertAlmostEqual(
            self.hydraulics.pressure_drop_pa,
            4.0e5,
            places=8,
        )
        self.assertAlmostEqual(
            self.hydraulics.hydraulic_power_w,
            800.0,
            places=10,
        )
        self.assertAlmostEqual(
            self.hydraulics.estimated_electrical_power_w,
            1269.8412698412699,
            places=10,
        )
        self.assertAlmostEqual(
            self.hydraulics.estimated_electrical_energy_kwh,
            0.6349206349206349,
            places=12,
        )
        self.assertAlmostEqual(
            self.hydraulics.cavitation_number,
            0.5660915662650602,
            places=12,
        )
        self.assertAlmostEqual(
            self.hydraulics.nominal_inventory_turnovers(
                self.intensified.feed_volume_m3
            ),
            18.0,
            places=14,
        )

    def test_product_metric_is_not_greater_than_feed_inventory(
        self,
    ) -> None:
        self.assertLessEqual(
            self.reference.sulfur_excluded_from_product_g,
            self.reference.initial_sulfur_in_feed_g,
        )
        self.assertLessEqual(
            self.intensified.sulfur_excluded_from_product_g,
            self.intensified.initial_sulfur_in_feed_g,
        )

    def test_negative_incremental_benefit_has_no_energy_ratio(
        self,
    ) -> None:
        poorer_intensified_case = replace(
            self.intensified,
            sulfur_in_recovered_product_g=4.5,
        )

        result = compare_cases(
            reference=self.reference,
            intensified=poorer_intensified_case,
        )

        self.assertLess(
            result.incremental_sulfur_excluded_from_product_g,
            0.0,
        )
        self.assertIsNone(
            result.energy_normalized_incremental_sulfur_g_per_kwh
        )
        self.assertIsNone(
            result.incremental_specific_energy_kwh_per_g_s
        )
        self.assertIn(
            "No positive incremental",
            result.outcome_statement,
        )

    def test_zero_incremental_energy_has_no_energy_ratio(
        self,
    ) -> None:
        equal_energy_case = replace(
            self.intensified,
            measured_total_electrical_energy_kwh=(
                self.reference.measured_total_electrical_energy_kwh
            ),
        )

        result = compare_cases(
            reference=self.reference,
            intensified=equal_energy_case,
        )

        self.assertEqual(
            result.incremental_electrical_energy_kwh,
            0.0,
        )
        self.assertIsNone(
            result.energy_normalized_incremental_sulfur_g_per_kwh
        )
        self.assertIn(
            "no measured incremental electrical energy",
            result.outcome_statement,
        )

    def test_noncomparable_feed_volume_is_rejected(self) -> None:
        unequal_volume_case = replace(
            self.intensified,
            feed_volume_m3=0.25,
        )

        with self.assertRaisesRegex(
            ValueError,
            "equivalent feed volume",
        ):
            compare_cases(
                reference=self.reference,
                intensified=unequal_volume_case,
            )

    def test_noncomparable_temperature_is_rejected(self) -> None:
        unequal_temperature_case = replace(
            self.intensified,
            final_temperature_k=305.15,
        )

        with self.assertRaisesRegex(
            ValueError,
            "equivalent final temperature",
        ):
            compare_cases(
                reference=self.reference,
                intensified=unequal_temperature_case,
            )

    def test_invalid_pressure_order_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            CavitationOperatingPoint(
                upstream_pressure_abs_pa=1.0e5,
                downstream_reference_pressure_abs_pa=1.5e5,
                vapor_pressure_pa=3.17e3,
                density_kg_m3=830.0,
                characteristic_velocity_m_s=25.0,
                loop_flow_rate_m3_s=2.0e-3,
                operating_time_s=1800.0,
                pump_efficiency=0.70,
                drive_efficiency=0.90,
            )

    def test_reference_pressure_below_vapor_pressure_is_rejected(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            CavitationOperatingPoint(
                upstream_pressure_abs_pa=5.5e5,
                downstream_reference_pressure_abs_pa=2.0e3,
                vapor_pressure_pa=3.17e3,
                density_kg_m3=830.0,
                characteristic_velocity_m_s=25.0,
                loop_flow_rate_m3_s=2.0e-3,
                operating_time_s=1800.0,
                pump_efficiency=0.70,
                drive_efficiency=0.90,
            )


if __name__ == "__main__":
    unittest.main()
