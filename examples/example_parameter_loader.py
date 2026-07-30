"""
Validated loader for the repository's illustrative parameter dataset.

The authoritative numerical inputs for the executable examples are stored in:

    data/example_parameters.csv

This module provides:

* deterministic repository-relative path resolution;
* strict CSV-header validation;
* finite numerical-value validation;
* duplicate-parameter detection;
* unit validation;
* case-label consistency checks;
* exact schema validation for the documented HDS, ODS, and cavitation cases.

Scientific scope
----------------
The loader validates data structure, traceability, units, and numerical
integrity. It does not establish that the illustrative values are physically
validated for a real catalyst, feed, reactor, or industrial process.

Physical-domain validation remains the responsibility of the model-specific
dataclasses and calculation functions.

Evidence status
---------------
E3 -- supporting infrastructure for executable engineering-screening
research prototypes.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
import math
from pathlib import Path
from typing import Final


REQUIRED_COLUMNS: Final[tuple[str, ...]] = (
    "example_id",
    "case_id",
    "case_label",
    "parameter",
    "symbol",
    "value",
    "unit",
    "description",
    "data_status",
)

ALLOWED_DATA_STATUSES: Final[frozenset[str]] = frozenset(
    {
        "illustrative_not_validated",
        "illustrative_screening_convention",
        "illustrative_assumption",
    }
)

DEFAULT_DATA_PATH: Final[Path] = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "example_parameters.csv"
)

CaseKey = tuple[str, str]


KNOWN_CASE_SCHEMAS: Final[
    dict[CaseKey, dict[str, str]]
] = {
    (
        "hds_internal_diffusion",
        "hds_default",
    ): {
        "particle_radius_m": "m",
        "volumetric_rate_constant_s_inv": "s^-1",
        "effective_diffusivity_m2_s": "m^2/s",
    },
    (
        "ods_reaction_transfer",
        "ods_default",
    ): {
        "reaction_coefficient_s_inv": "s^-1",
        "effective_transfer_coefficient_s_inv": "s^-1",
        "dominance_fraction": "dimensionless",
        "sensitivity_factor": "dimensionless",
    },
    (
        "cavitation_comparison",
        "reference_case",
    ): {
        "apparent_rate_coefficient_s_inv": "s^-1",
        "initial_sulfur_in_feed_g": "g",
        "sulfur_in_recovered_product_g": "g",
        "feed_volume_m3": "m^3",
        "treatment_time_s": "s",
        "measured_total_electrical_energy_kwh": "kWh",
        "initial_temperature_k": "K",
        "final_temperature_k": "K",
    },
    (
        "cavitation_comparison",
        "cavitation_case",
    ): {
        "apparent_rate_coefficient_s_inv": "s^-1",
        "initial_sulfur_in_feed_g": "g",
        "sulfur_in_recovered_product_g": "g",
        "feed_volume_m3": "m^3",
        "treatment_time_s": "s",
        "measured_total_electrical_energy_kwh": "kWh",
        "initial_temperature_k": "K",
        "final_temperature_k": "K",
    },
    (
        "cavitation_hydraulics",
        "hc_operating_point",
    ): {
        "upstream_pressure_abs_pa": "Pa",
        "downstream_reference_pressure_abs_pa": "Pa",
        "vapor_pressure_pa": "Pa",
        "density_kg_m3": "kg/m^3",
        "characteristic_velocity_m_s": "m/s",
        "loop_flow_rate_m3_s": "m^3/s",
        "operating_time_s": "s",
        "pump_efficiency": "dimensionless",
        "drive_efficiency": "dimensionless",
    },
}


@dataclass(frozen=True, slots=True)
class ParameterRecord:
    """One validated row from the illustrative parameter dataset."""

    example_id: str
    case_id: str
    case_label: str
    parameter: str
    symbol: str
    value: float
    unit: str
    description: str
    data_status: str
    source_line: int

    @property
    def case_key(self) -> CaseKey:
        """Return the compound case identifier."""
        return self.example_id, self.case_id


class ParameterStore:
    """Validated in-memory representation of the parameter dataset."""

    def __init__(
        self,
        records: tuple[ParameterRecord, ...],
        source_path: Path,
    ) -> None:
        if not records:
            raise ValueError(
                "The parameter dataset must contain at least one record."
            )

        self._records = records
        self._source_path = source_path

        records_by_key: dict[
            tuple[str, str, str],
            ParameterRecord,
        ] = {}

        records_by_case: dict[
            CaseKey,
            list[ParameterRecord],
        ] = {}

        for record in records:
            parameter_key = (
                record.example_id,
                record.case_id,
                record.parameter,
            )

            if parameter_key in records_by_key:
                previous = records_by_key[parameter_key]

                raise ValueError(
                    "Duplicate parameter definition for "
                    f"{parameter_key!r} at CSV lines "
                    f"{previous.source_line} and {record.source_line}."
                )

            records_by_key[parameter_key] = record
            records_by_case.setdefault(
                record.case_key,
                [],
            ).append(record)

        self._records_by_key = records_by_key
        self._records_by_case = {
            key: tuple(case_records)
            for key, case_records in records_by_case.items()
        }

        self._validate_case_label_consistency()

    @classmethod
    def from_csv(
        cls,
        path: str | Path,
    ) -> "ParameterStore":
        """Load and validate a parameter dataset from CSV."""
        source_path = Path(path).expanduser().resolve()

        if not source_path.exists():
            raise FileNotFoundError(
                f"Parameter dataset not found: {source_path}"
            )

        if not source_path.is_file():
            raise ValueError(
                f"Parameter dataset path is not a file: {source_path}"
            )

        records: list[ParameterRecord] = []

        with source_path.open(
            mode="r",
            encoding="utf-8-sig",
            newline="",
        ) as csv_file:
            reader = csv.DictReader(csv_file)

            if reader.fieldnames is None:
                raise ValueError(
                    "The parameter CSV does not contain a header."
                )

            normalized_header = tuple(
                field.strip()
                for field in reader.fieldnames
            )

            if normalized_header != REQUIRED_COLUMNS:
                raise ValueError(
                    "Unexpected CSV header.\n"
                    f"Expected: {REQUIRED_COLUMNS}\n"
                    f"Found:    {normalized_header}"
                )

            for row in reader:
                source_line = reader.line_num

                if row is None:
                    continue

                normalized_row = {
                    key.strip(): (
                        value.strip()
                        if value is not None
                        else ""
                    )
                    for key, value in row.items()
                }

                if not any(normalized_row.values()):
                    continue

                records.append(
                    _parse_record(
                        row=normalized_row,
                        source_line=source_line,
                    )
                )

        store = cls(
            records=tuple(records),
            source_path=source_path,
        )

        store.validate_known_case_schemas()

        return store

    @property
    def source_path(self) -> Path:
        """Return the absolute source CSV path."""
        return self._source_path

    @property
    def records(self) -> tuple[ParameterRecord, ...]:
        """Return all validated records."""
        return self._records

    @property
    def case_keys(self) -> tuple[CaseKey, ...]:
        """Return all available case identifiers."""
        return tuple(sorted(self._records_by_case))

    def records_for_case(
        self,
        example_id: str,
        case_id: str,
    ) -> tuple[ParameterRecord, ...]:
        """Return all records belonging to one case."""
        key = _normalized_case_key(
            example_id=example_id,
            case_id=case_id,
        )

        try:
            return self._records_by_case[key]
        except KeyError as error:
            available = ", ".join(
                f"{item[0]}/{item[1]}"
                for item in self.case_keys
            )

            raise KeyError(
                f"Unknown parameter case {key!r}. "
                f"Available cases: {available}"
            ) from error

    def case_label(
        self,
        example_id: str,
        case_id: str,
    ) -> str:
        """Return the unique human-readable label for one case."""
        case_records = self.records_for_case(
            example_id=example_id,
            case_id=case_id,
        )

        return case_records[0].case_label

    def record(
        self,
        example_id: str,
        case_id: str,
        parameter: str,
    ) -> ParameterRecord:
        """Return one parameter record."""
        normalized_parameter = parameter.strip()

        if not normalized_parameter:
            raise ValueError(
                "Parameter name must not be empty."
            )

        key = (
            example_id.strip(),
            case_id.strip(),
            normalized_parameter,
        )

        try:
            return self._records_by_key[key]
        except KeyError as error:
            available = ", ".join(
                record.parameter
                for record in self.records_for_case(
                    example_id=example_id,
                    case_id=case_id,
                )
            )

            raise KeyError(
                f"Parameter {normalized_parameter!r} was not found "
                f"for case {key[0]!r}/{key[1]!r}. "
                f"Available parameters: {available}"
            ) from error

    def value(
        self,
        example_id: str,
        case_id: str,
        parameter: str,
        *,
        expected_unit: str | None = None,
    ) -> float:
        """Return one numerical value with optional unit validation."""
        record = self.record(
            example_id=example_id,
            case_id=case_id,
            parameter=parameter,
        )

        if (
            expected_unit is not None
            and record.unit != expected_unit
        ):
            raise ValueError(
                f"Unit mismatch for "
                f"{record.example_id}/{record.case_id}/"
                f"{record.parameter}: expected "
                f"{expected_unit!r}, found {record.unit!r} "
                f"at CSV line {record.source_line}."
            )

        return record.value

    def values_for_case(
        self,
        example_id: str,
        case_id: str,
    ) -> dict[str, float]:
        """Return a parameter-to-value mapping for one case."""
        return {
            record.parameter: record.value
            for record in self.records_for_case(
                example_id=example_id,
                case_id=case_id,
            )
        }

    def validate_known_case_schemas(self) -> None:
        """Validate exact parameter names and units for documented cases."""
        for case_key, expected_schema in KNOWN_CASE_SCHEMAS.items():
            example_id, case_id = case_key

            case_records = self.records_for_case(
                example_id=example_id,
                case_id=case_id,
            )

            actual_schema = {
                record.parameter: record.unit
                for record in case_records
            }

            expected_parameters = set(expected_schema)
            actual_parameters = set(actual_schema)

            missing_parameters = sorted(
                expected_parameters - actual_parameters
            )
            unexpected_parameters = sorted(
                actual_parameters - expected_parameters
            )

            if missing_parameters or unexpected_parameters:
                messages: list[str] = []

                if missing_parameters:
                    messages.append(
                        "missing parameters: "
                        + ", ".join(missing_parameters)
                    )

                if unexpected_parameters:
                    messages.append(
                        "unexpected parameters: "
                        + ", ".join(unexpected_parameters)
                    )

                raise ValueError(
                    f"Schema mismatch for "
                    f"{example_id}/{case_id}: "
                    + "; ".join(messages)
                    + "."
                )

            for parameter, expected_unit in expected_schema.items():
                actual_unit = actual_schema[parameter]

                if actual_unit != expected_unit:
                    record = self.record(
                        example_id=example_id,
                        case_id=case_id,
                        parameter=parameter,
                    )

                    raise ValueError(
                        f"Unit mismatch for "
                        f"{example_id}/{case_id}/{parameter}: "
                        f"expected {expected_unit!r}, "
                        f"found {actual_unit!r} at "
                        f"CSV line {record.source_line}."
                    )

    def _validate_case_label_consistency(self) -> None:
        """Require one case label for every example/case combination."""
        for case_key, case_records in self._records_by_case.items():
            labels = {
                record.case_label
                for record in case_records
            }

            if len(labels) != 1:
                formatted_labels = ", ".join(
                    repr(label)
                    for label in sorted(labels)
                )

                raise ValueError(
                    f"Inconsistent case labels for "
                    f"{case_key[0]}/{case_key[1]}: "
                    f"{formatted_labels}."
                )


def _parse_record(
    row: dict[str, str],
    source_line: int,
) -> ParameterRecord:
    """Parse and validate one normalized CSV row."""
    for field_name in REQUIRED_COLUMNS:
        if not row.get(field_name, ""):
            raise ValueError(
                f"Missing value in column {field_name!r} "
                f"at CSV line {source_line}."
            )

    try:
        numerical_value = float(row["value"])
    except ValueError as error:
        raise ValueError(
            f"Invalid numerical value {row['value']!r} "
            f"at CSV line {source_line}."
        ) from error

    if not math.isfinite(numerical_value):
        raise ValueError(
            f"Numerical value must be finite at "
            f"CSV line {source_line}: {row['value']!r}."
        )

    data_status = row["data_status"]

    if data_status not in ALLOWED_DATA_STATUSES:
        allowed = ", ".join(
            sorted(ALLOWED_DATA_STATUSES)
        )

        raise ValueError(
            f"Unsupported data status {data_status!r} "
            f"at CSV line {source_line}. "
            f"Allowed values: {allowed}."
        )

    return ParameterRecord(
        example_id=row["example_id"],
        case_id=row["case_id"],
        case_label=row["case_label"],
        parameter=row["parameter"],
        symbol=row["symbol"],
        value=numerical_value,
        unit=row["unit"],
        description=row["description"],
        data_status=data_status,
        source_line=source_line,
    )


def _normalized_case_key(
    example_id: str,
    case_id: str,
) -> CaseKey:
    """Validate and normalize a compound case key."""
    normalized_example_id = example_id.strip()
    normalized_case_id = case_id.strip()

    if not normalized_example_id:
        raise ValueError(
            "example_id must not be empty."
        )

    if not normalized_case_id:
        raise ValueError(
            "case_id must not be empty."
        )

    return normalized_example_id, normalized_case_id


def load_default_parameter_store() -> ParameterStore:
    """Load the authoritative repository parameter dataset."""
    return ParameterStore.from_csv(DEFAULT_DATA_PATH)


def render_validation_summary(
    store: ParameterStore,
) -> str:
    """Return a concise dataset-validation report."""
    lines = [
        "ILLUSTRATIVE PARAMETER DATASET VALIDATION",
        "=" * 48,
        f"Source file : {store.source_path}",
        f"Rows loaded : {len(store.records)}",
        f"Cases found : {len(store.case_keys)}",
        "",
        "Validated cases:",
    ]

    for example_id, case_id in store.case_keys:
        case_records = store.records_for_case(
            example_id=example_id,
            case_id=case_id,
        )

        lines.append(
            f"- {example_id}/{case_id}: "
            f"{store.case_label(example_id, case_id)} "
            f"({len(case_records)} parameters)"
        )

    lines.extend(
        [
            "",
            "Dataset status:",
            (
                "Structural, numerical, unit, duplicate, and documented "
                "case-schema checks passed."
            ),
            (
                "The values remain illustrative and are not validated "
                "design or industrial-performance data."
            ),
        ]
    )

    return "\n".join(lines)


def main() -> None:
    """Validate the authoritative CSV and print a summary."""
    store = load_default_parameter_store()

    print(render_validation_summary(store))


if __name__ == "__main__":
    main()
