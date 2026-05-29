#!/usr/bin/env python3
"""Check public HumanEval governance/auditability evidence consistency.

This verifier checks only the public sanitized evidence files in this repo.
It does not replay private TrustableClaw ledger data or rerun HumanEval inference.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "benchmarks" / "humaneval-governance-auditability"
RESULTS_JSON = BASE / "results" / "humaneval-164-results.json"
RESULTS_JSONL = BASE / "results" / "humaneval-164-results.jsonl"
SUMMARY_CSV = BASE / "results" / "humaneval-164-summary.csv"
SUMMARY_TXT = BASE / "humaneval-164-summary.txt"
MANIFEST_JSON = BASE / "receipts" / "receipt-manifest.json"
VERIFICATION_JSON = BASE / "verification" / "verification-results.json"
TAMPER_JSON = BASE / "tamper-tests" / "tamper-results.json"

EXPECTED_TASKS = 164
EXPECTED_PASSED = 146
EXPECTED_FAILED = 18
EXPECTED_AUDITABILITY_FAILURES = 0
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def canonical_task_key(row: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(row["task_id"]),
        str(row["coding_result"]),
        str(row["receipt_id"]),
        str(row["receipt_hash"]),
    )


def main() -> None:
    results = load_json(RESULTS_JSON)
    assert_true(isinstance(results, list), "results JSON must be a list")
    assert_true(len(results) == EXPECTED_TASKS, f"expected {EXPECTED_TASKS} task records")

    task_ids = {r["task_id"] for r in results}
    assert_true(len(task_ids) == EXPECTED_TASKS, "task IDs must be unique")
    assert_true(task_ids == {f"HumanEval/{i}" for i in range(EXPECTED_TASKS)}, "task IDs must cover HumanEval/0..HumanEval/163")

    passed = [r for r in results if r["coding_result"] == "passed"]
    failed = [r for r in results if r["coding_result"] == "failed"]
    assert_true(len(passed) == EXPECTED_PASSED, f"expected {EXPECTED_PASSED} coding passes")
    assert_true(len(failed) == EXPECTED_FAILED, f"expected {EXPECTED_FAILED} coding failures")

    for r in results:
        assert_true(r.get("auditability_result") == "passed", f"auditability did not pass for {r['task_id']}")
        assert_true(r.get("receipt_created") is True, f"receipt_created not true for {r['task_id']}")
        assert_true(r.get("receipt_verified") is True, f"receipt_verified not true for {r['task_id']}")
        assert_true(r.get("tamper_test_detected") is True, f"tamper_test_detected not true for {r['task_id']}")
        assert_true(SHA256_RE.match(r.get("receipt_hash", "")) is not None, f"invalid receipt hash for {r['task_id']}")

    with RESULTS_JSONL.open("r", encoding="utf-8") as f:
        jsonl_rows = [json.loads(line) for line in f if line.strip()]
    assert_true(len(jsonl_rows) == EXPECTED_TASKS, "JSONL row count mismatch")
    assert_true([canonical_task_key(r) for r in jsonl_rows] == [canonical_task_key(r) for r in results], "JSONL rows do not match JSON results")

    with SUMMARY_CSV.open("r", encoding="utf-8", newline="") as f:
        csv_rows = list(csv.DictReader(f))
    assert_true(len(csv_rows) == EXPECTED_TASKS, "CSV row count mismatch")
    csv_keys = [(r["task_id"], r["coding_result"], r["receipt_id"], r["receipt_hash"]) for r in csv_rows]
    json_keys = [canonical_task_key(r) for r in results]
    assert_true(csv_keys == json_keys, "CSV rows do not match JSON results")

    manifest = load_json(MANIFEST_JSON)
    assert_true(isinstance(manifest, list), "receipt manifest must be a list")
    assert_true(len(manifest) == EXPECTED_TASKS, "receipt manifest row count mismatch")
    manifest_by_task = {r["task_id"]: r for r in manifest}
    assert_true(set(manifest_by_task) == task_ids, "receipt manifest task IDs mismatch")
    for r in results:
        m = manifest_by_task[r["task_id"]]
        assert_true(m["receipt_id"] == r["receipt_id"], f"receipt ID mismatch for {r['task_id']}")
        assert_true(m["receipt_hash"] == r["receipt_hash"], f"receipt hash mismatch for {r['task_id']}")
        assert_true(m["verified"] is True, f"manifest verified not true for {r['task_id']}")
        assert_true(m["tamper_test_detected"] is True, f"manifest tamper not true for {r['task_id']}")

    verification = load_json(VERIFICATION_JSON)
    assert_true(verification["tasks_checked"] == EXPECTED_TASKS, "verification tasks_checked mismatch")
    assert_true(verification["receipts_expected"] == EXPECTED_TASKS, "verification receipts_expected mismatch")
    assert_true(verification["receipts_verified"] == EXPECTED_TASKS, "verification receipts_verified mismatch")
    assert_true(verification["verification_failures"] == EXPECTED_AUDITABILITY_FAILURES, "verification failures mismatch")

    tamper = load_json(TAMPER_JSON)
    assert_true(tamper["tasks_checked"] == EXPECTED_TASKS, "tamper tasks_checked mismatch")
    assert_true(tamper["tamper_tests_run"] == EXPECTED_TASKS, "tamper_tests_run mismatch")
    assert_true(tamper["tamper_tests_detected"] == EXPECTED_TASKS, "tamper_tests_detected mismatch")
    assert_true(tamper["tamper_test_failures"] == EXPECTED_AUDITABILITY_FAILURES, "tamper failures mismatch")

    summary_lines = SUMMARY_TXT.read_text(encoding="utf-8").splitlines()
    humaneval_lines = [line for line in summary_lines if line.startswith("HumanEval/")]
    assert_true(len(humaneval_lines) == EXPECTED_TASKS, "text summary must have one task line per task")

    print("HumanEval public evidence consistency check passed")
    print(f"Tasks: {EXPECTED_TASKS}; coding passed: {EXPECTED_PASSED}; coding failed: {EXPECTED_FAILED}; auditability failures: {EXPECTED_AUDITABILITY_FAILURES}")


if __name__ == "__main__":
    main()
