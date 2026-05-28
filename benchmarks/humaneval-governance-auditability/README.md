# HumanEval Governance & Auditability Benchmark

This benchmark uses HumanEval as a fixed set of coding tasks to show whether TrustableClaw audit evidence was produced across a full AI task run.

## Results

### HumanEval coding result

| Metric | Result |
|---|---:|
| Tasks attempted | 164 / 164 |
| Tasks passed | 146 / 164 |
| Tasks failed | 18 / 164 |
| Coding pass rate | 89.0% |

### TrustableClaw auditability result

| Metric | Result |
|---|---:|
| Receipts created | 164 / 164 |
| Receipts verified | 164 / 164 |
| Tamper tests detected | 164 / 164 |
| Auditability failures | 0 |

The 18 failed tasks were coding failures from the model/agent output. They were not TrustableClaw auditability failures.

TrustableClaw still created and verified receipts for those failed outputs, which is exactly what an auditability layer should do.

## Files

- [`REVIEWER_SUMMARY.md`](REVIEWER_SUMMARY.md) - concise reviewer-facing summary of the eval process and results
- [`humaneval-164-summary.txt`](humaneval-164-summary.txt) - readable task-by-task public summary
- [`results/humaneval-164-results.json`](results/humaneval-164-results.json) - machine-readable public results summary in JSON
- [`results/humaneval-164-results.jsonl`](results/humaneval-164-results.jsonl) - machine-readable public results summary in JSONL
- [`results/humaneval-164-summary.csv`](results/humaneval-164-summary.csv) - reviewer-friendly CSV summary
- [`receipts/receipt-manifest.json`](receipts/receipt-manifest.json) - one sanitized public receipt-manifest entry per task
- [`verification/verification-results.json`](verification/verification-results.json) - public receipt-verification summary
- [`tamper-tests/tamper-results.json`](tamper-tests/tamper-results.json) - public tamper-detection summary
- [`METHODOLOGY.md`](METHODOLOGY.md) - methodology and limitations
- [`ENVIRONMENT.md`](ENVIRONMENT.md) - run environment details and missing-metadata status
- [`COMMANDS.md`](COMMANDS.md) - historical command capture status and public replay commands
- [`REPLAY.md`](REPLAY.md) - independent public evidence consistency-check instructions
- [`scripts/verify_humaneval_evidence.py`](scripts/verify_humaneval_evidence.py) - non-secret public evidence consistency verifier

## Reviewer guidance

A reviewer should check the coding result and auditability result separately.

The coding result answers whether the model-generated code passed HumanEval tests. The auditability result answers whether TrustableClaw reported audit evidence for each task.

## Evidence limits

These public files are sanitized. They do not include private prompts, completions, API keys, secrets, or sensitive local paths.

The included public verifier checks internal consistency across committed evidence files. It is not a substitute for canonical TrustableClaw ledger verification unless canonical public ledger artifacts are added.
