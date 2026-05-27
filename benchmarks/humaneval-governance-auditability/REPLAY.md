# Replay and Independent Public Evidence Check

This public replay path does not require private API keys. It verifies the sanitized evidence artifacts committed to the repository.

## Local verification

From the repository root, run:

```bash
python benchmarks/humaneval-governance-auditability/scripts/verify_humaneval_evidence.py
```

The verifier checks that:

- The JSON and JSONL public results files are valid.
- Exactly 164 task records exist in JSON, JSONL, CSV, and receipt manifest.
- JSON, JSONL, CSV, and manifest task IDs match exactly.
- Exactly 146 tasks are marked as coding passes.
- Exactly 18 tasks are marked as coding failures.
- Every task has `receipt_created = true`.
- Every task has `receipt_verified = true`.
- Every task has `tamper_test_detected = true`.
- Every receipt ID and receipt hash matches across JSON, JSONL, CSV, and manifest.
- Receipt hashes are valid 64-character lowercase SHA-256-style hex strings.
- The formatted text summary contains all 164 task lines.
- `verification/verification-results.json` totals match the task records.
- `tamper-tests/tamper-results.json` totals match the task records.

## GitHub Actions

The workflow at `.github/workflows/verify-humaneval-evidence.yml` runs the same public evidence consistency check on pull requests and pushes.

## Limits

This replay validates the public sanitized evidence. It does not rerun paid model inference and does not expose private prompts, completions, secrets, API keys, or local machine paths. It also does not claim to replace canonical TrustableClaw ledger verification unless canonical public ledger artifacts are added.
