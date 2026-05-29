# HumanEval Governance and Auditability Benchmark

This folder contains the public sanitized evidence summary for the TrustableClaw HumanEval governance and auditability benchmark.

## Result Summary

| Measurement | Result |
| --- | ---: |
| Tasks attempted | 164 / 164 |
| Coding passes | 146 / 164 |
| Coding failures | 18 / 164 |
| Coding pass rate | 89.0% |
| Receipts created | 164 / 164 |
| Receipts verified | 164 / 164 |
| Tamper tests detected | 164 / 164 |
| Auditability failures | 0 |

## What Was Measured

The benchmark separates two different measurements:

1. **Coding result**: whether the model/agent-generated answer passed the HumanEval unit tests.
2. **Auditability result**: whether TrustableClaw created, verified, and tamper-tested public evidence records for the task.

The 18 failed HumanEval tasks were coding failures. They were not TrustableClaw auditability failures.

## Files

- `REVIEWER_SUMMARY.md` — short reviewer-facing summary.
- `METHODOLOGY.md` — plain-English method and interpretation.
- `ENVIRONMENT.md` — recorded and not-recorded environment details.
- `COMMANDS.md` — commands available for public consistency checks.
- `REPLAY.md` — how to run the public verifier.
- `results/humaneval-164-results.json` — public task-level evidence summary.
- `results/humaneval-164-results.jsonl` — JSONL version of the same task-level summary.
- `results/humaneval-164-summary.csv` — reviewer-friendly CSV summary.
- `receipts/receipt-manifest.json` — sanitized receipt ID/hash manifest.
- `verification/verification-results.json` — verification summary.
- `tamper-tests/tamper-results.json` — tamper-test summary.
- `scripts/verify_humaneval_evidence.py` — public evidence consistency verifier.

## Verify Locally

```bash
python -m py_compile benchmarks/humaneval-governance-auditability/scripts/verify_humaneval_evidence.py
python benchmarks/humaneval-governance-auditability/scripts/verify_humaneval_evidence.py
```
