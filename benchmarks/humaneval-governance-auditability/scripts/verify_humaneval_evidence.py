#!/usr/bin/env python3
"""Check public HumanEval governance/auditability evidence consistency.

This verifier intentionally uses only sanitized public files. It does not require API
keys and does not expose private prompts or completions.

Important: this is an evidence consistency checker. It validates that the committed
public summaries, CSV, JSONL, manifest, verification summary, and tamper summary all
agree. It does not rerun paid model inference or independently replay private
cryptographic ledger verification unless canonical public ledger artifacts are added.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any

EXPECTED_TASKS = 164
EXPECTED_PASSED = 146
EXPECTED_FAILED = 18
EXPECTED_AUDITABILITY_FAILURES = 0
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
TASK_RE = re.compile(r"^HumanEval/(\d+):")
BENCH_DIR = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")


def require_bool(record: dict[str, Any], key: str, task_id: str) -> None:
    if record.get(key) is not True:
        fail(f"{task_id} {key} must be true")


def validate_task_record(record: dict[str, Any], idx: int) -> None:
    task_id = record.get("task_id")
    if task_id != f"HumanEval/{idx}":
        fail(f"record {idx} has unexpected task_id: {task_id!r}")
    coding_result = record.get("coding_result")
    if coding_result not in {"passed", "failed"}:
        fail(f"{task_id} has invalid coding_result: {coding_result!r}")
    if record.get("status") != coding_result:
        fail(f"{task_id} status must match coding_result")
    if record.get("auditability_result") != "passed":
        fail(f"{task_id} auditability_result must be passed")
    require_bool(record, "receipt_created", task_id)
    require_bool(record, "receipt_verified", task_id)
    require_bool(record, "tamper_test_detected", task_id)
    receipt_id = record.get("receipt_id")
    if not isinstance(receipt_id, str) or not receipt_id:
        fail(f"{task_id} missing receipt_id")
    receipt_hash = record.get("receipt_hash")
    if not isinstance(receipt_hash, str) or not SHA256_RE.fullmatch(receipt_hash):
        fail(f"{task_id} receipt_hash must be a lowercase 64-character sha256 hex string")


def normalize_csv_bool(value: str, field: str, task_id: str) -> bool:
    if value == "True":
        return True
    if value == "False":
        return False
    fail(f"{task_id} CSV field {field} must be True or False, found {value!r}")


def main() -> None:
    results_path = BENCH_DIR / "results" / "humaneval-164-results.json"
    jsonl_path = BENCH_DIR / "results" / "humaneval-164-results.jsonl"
    csv_path = BENCH_DIR / "results" / "humaneval-164-summary.csv"
    summary_path = BENCH_DIR / "humaneval-164-summary.txt"
    manifest_path = BENCH_DIR / "receipts" / "receipt-manifest.json"
    verification_path = BENCH_DIR / "verification" / "verification-results.json"
    tamper_path = BENCH_DIR / "tamper-tests" / "tamper-results.json"

    records = load_json(results_path)
    if not isinstance(records, list):
        fail("results JSON must be a list")
    if len(records) != EXPECTED_TASKS:
        fail(f"expected {EXPECTED_TASKS} result records, found {len(records)}")

    by_task: dict[str, dict[str, Any]] = {}
    passed = failed_count = 0
    for idx, record in enumerate(records):
        if not isinstance(record, dict):
            fail(f"record {idx} must be an object")
        validate_task_record(record, idx)
        task_id = record["task_id"]
        if task_id in by_task:
            fail(f"duplicate task_id: {task_id}")
        by_task[task_id] = record
        if record["coding_result"] == "passed":
            passed += 1
        else:
            failed_count += 1

    if passed != EXPECTED_PASSED:
        fail(f"expected {EXPECTED_PASSED} coding passes, found {passed}")
    if failed_count != EXPECTED_FAILED:
        fail(f"expected {EXPECTED_FAILED} coding failures, found {failed_count}")

    jsonl_records = []
    try:
        for line_no, line in enumerate(jsonl_path.read_text(encoding="utf-8").splitlines(), start=1):
            if line.strip():
                try:
                    item = json.loads(line)
                except json.JSONDecodeError as exc:
                    fail(f"invalid JSONL at line {line_no}: {exc}")
                if not isinstance(item, dict):
                    fail(f"JSONL line {line_no} must be an object")
                jsonl_records.append(item)
    except FileNotFoundError:
        fail(f"missing file: {jsonl_path}")
    if len(jsonl_records) != EXPECTED_TASKS:
        fail(f"expected {EXPECTED_TASKS} JSONL records, found {len(jsonl_records)}")
    for idx, record in enumerate(jsonl_records):
        validate_task_record(record, idx)
        if record != records[idx]:
            fail(f"JSONL record for {record.get('task_id')} does not match JSON results")

    try:
        with csv_path.open(newline="", encoding="utf-8") as f:
            csv_rows = list(csv.DictReader(f))
    except FileNotFoundError:
        fail(f"missing file: {csv_path}")
    if len(csv_rows) != EXPECTED_TASKS:
        fail(f"expected {EXPECTED_TASKS} CSV rows, found {len(csv_rows)}")
    for idx, row in enumerate(csv_rows):
        task_id = row.get("task_id")
        if task_id != f"HumanEval/{idx}":
            fail(f"CSV row {idx} has unexpected task_id: {task_id!r}")
        record = by_task[task_id]
        for field in ["coding_result", "auditability_result", "receipt_id", "receipt_hash"]:
            if row.get(field) != str(record.get(field)):
                fail(f"CSV field {field} for {task_id} does not match JSON results")
        for field in ["receipt_created", "receipt_verified", "tamper_test_detected"]:
            if normalize_csv_bool(row.get(field, ""), field, task_id) is not record[field]:
                fail(f"CSV field {field} for {task_id} does not match JSON results")

    manifest = load_json(manifest_path)
    entries = manifest.get("entries")
    if manifest.get("total_entries") != EXPECTED_TASKS:
        fail("receipt manifest total_entries must be 164")
    if not isinstance(entries, list) or len(entries) != EXPECTED_TASKS:
        fail(f"receipt manifest must contain {EXPECTED_TASKS} entries")
    for idx, entry in enumerate(entries):
        if not isinstance(entry, dict):
            fail(f"manifest entry {idx} must be an object")
        task_id = entry.get("task_id")
        if task_id != f"HumanEval/{idx}":
            fail(f"manifest entry {idx} has unexpected task_id: {task_id!r}")
        record = by_task[task_id]
        if entry.get("receipt_id") != record["receipt_id"]:
            fail(f"manifest receipt_id for {task_id} does not match JSON results")
        if entry.get("receipt_hash") != record["receipt_hash"]:
            fail(f"manifest receipt_hash for {task_id} does not match JSON results")
        if not SHA256_RE.fullmatch(entry.get("receipt_hash", "")):
            fail(f"manifest receipt_hash for {task_id} must be lowercase sha256 hex")
        if entry.get("verified") is not True:
            fail(f"manifest verified for {task_id} must be true")
        if entry.get("tamper_test_detected") is not True:
            fail(f"manifest tamper_test_detected for {task_id} must be true")

    verification = load_json(verification_path)
    if verification.get("receipts_checked") != EXPECTED_TASKS:
        fail("verification receipts_checked must be 164")
    if verification.get("receipts_verified") != EXPECTED_TASKS:
        fail("verification receipts_verified must be 164")
    if verification.get("verification_failures") != EXPECTED_AUDITABILITY_FAILURES:
        fail("verification_failures must be 0")
    if verification.get("all_receipts_verified") is not True:
        fail("all_receipts_verified must be true")

    tamper = load_json(tamper_path)
    if tamper.get("tamper_tests_run") != EXPECTED_TASKS:
        fail("tamper_tests_run must be 164")
    if tamper.get("tamper_tests_detected") != EXPECTED_TASKS:
        fail("tamper_tests_detected must be 164")
    if tamper.get("tamper_detection_failures") != EXPECTED_AUDITABILITY_FAILURES:
        fail("tamper_detection_failures must be 0")
    if tamper.get("all_tamper_tests_detected") is not True:
        fail("all_tamper_tests_detected must be true")

    try:
        summary_lines = summary_path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        fail(f"missing file: {summary_path}")
    task_lines = [line for line in summary_lines if TASK_RE.match(line)]
    if len(task_lines) != EXPECTED_TASKS:
        fail(f"expected {EXPECTED_TASKS} task lines in text summary, found {len(task_lines)}")
    for idx, line in enumerate(task_lines):
        task_id = f"HumanEval/{idx}"
        if not line.startswith(task_id + ":"):
            fail(f"text summary task line {idx} should start with {task_id}")
        expected_phrase = "failed coding test" if by_task[task_id]["coding_result"] == "failed" else "passed"
        if expected_phrase not in line:
            fail(f"text summary for {task_id} does not match coding result")
        for phrase in ["receipt created", "receipt verified", "tamper detected"]:
            if phrase not in line:
                fail(f"text summary for {task_id} missing phrase: {phrase}")

    print("HumanEval public evidence consistency check passed")
    print(f"Tasks: {EXPECTED_TASKS}; coding passed: {passed}; coding failed: {failed_count}; auditability failures: 0")


if __name__ == "__main__":
    main()
