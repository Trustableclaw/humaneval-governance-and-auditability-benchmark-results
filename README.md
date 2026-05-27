# HumanEval Governance & Auditability Benchmark Results

TrustableClaw completed the full 164-task HumanEval benchmark with 100% reported auditability coverage in the public evidence summary.

## Headline Results

### HumanEval coding result

- Tasks attempted: 164 / 164
- Tasks passed: 146 / 164
- Tasks failed: 18 / 164
- Coding pass rate: 89.0%

### TrustableClaw auditability result

- Receipts created: 164 / 164
- Receipts verified: 164 / 164
- Tamper tests detected: 164 / 164
- Auditability failures: 0

The 18 failed tasks were coding failures from the model/agent output. They were not TrustableClaw auditability failures. TrustableClaw still created and verified receipts for those failed outputs, which is exactly what an auditability layer should do.

## What this repo is meant to show

This repository is not claiming that TrustableClaw made the model better at HumanEval coding tasks. The coding pass rate belongs to the model/agent setup used for the run.

This repository packages public, sanitized benchmark evidence showing that TrustableClaw audit evidence was reported for every task in the benchmark, including both successful and failed coding outputs.

## Evidence included

- Machine-readable 164-task public results summary JSON and JSONL
- Readable 164-task summary text
- CSV summary for reviewers
- Sanitized receipt manifest with one entry per task
- Public verification-results summary
- Public tamper-test summary
- Methodology and limitations
- Environment notes
- Historical command capture status and replay command documentation
- GitHub Actions public-evidence consistency check

See: [`benchmarks/humaneval-governance-auditability`](benchmarks/humaneval-governance-auditability)

## Important limits

The public files are sanitized. They do not include private prompts, private completions, API keys, secrets, or sensitive local paths.

The included receipt IDs and hashes are labeled as sanitized public linkage values unless they are later replaced with canonical public TrustableClaw ledger values. The GitHub Action verifies that the public evidence files are internally consistent. It does not rerun paid model inference or independently replay private cryptographic ledger verification.

All commits that publish or update this evidence should be pushed through the official TrustableClaw GitHub account.
