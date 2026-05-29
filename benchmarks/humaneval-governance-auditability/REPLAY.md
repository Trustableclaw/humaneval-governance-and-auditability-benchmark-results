# Replay and Public Verification

This repository supports public evidence consistency checks. It does not provide full private ledger replay.

## Run the Public Consistency Verifier

From the repository root:

```bash
python -m py_compile benchmarks/humaneval-governance-auditability/scripts/verify_humaneval_evidence.py
python benchmarks/humaneval-governance-auditability/scripts/verify_humaneval_evidence.py
```

Expected output:

```text
HumanEval public evidence consistency check passed
Tasks: 164; coding passed: 146; coding failed: 18; auditability failures: 0
```

## What the Verifier Checks

The verifier checks that:

- 164 task records exist.
- 146 tasks are marked as coding passed.
- 18 tasks are marked as coding failed.
- All 164 records report receipt creation.
- All 164 records report receipt verification.
- All 164 records report tamper-test detection.
- The receipt manifest has 164 entries.
- CSV records match JSON records.
- JSONL records match JSON records.
- Verification and tamper summary files match the task-level records.
- The formatted text summary has one HumanEval task line per task.

## What the Verifier Does Not Check

The verifier does not rerun HumanEval inference, call any private model API, or replay a private TrustableClaw ledger.
