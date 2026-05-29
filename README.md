# TrustableClaw HumanEval Governance and Auditability Benchmark Results

This repository publishes a sanitized public evidence summary for TrustableClaw's HumanEval governance and auditability benchmark.

The benchmark measured two separate things:

1. **HumanEval coding performance** from the gpt-5.4-mini model/agent setup.
2. **TrustableClaw governance and auditability coverage** around each benchmark task.

## Headline Results

| Category | Result |
| --- | ---: |
| HumanEval tasks attempted | 164 / 164 |
| HumanEval coding passes | 146 / 164 |
| HumanEval coding failures | 18 / 164 |
| Coding pass rate | 89.0% |
| TrustableClaw receipts created | 164 / 164 |
| TrustableClaw receipts verified | 164 / 164 |
| TrustableClaw tamper tests detected | 164 / 164 |
| Reported auditability failures | 0 |

## Important Interpretation

The 18 failed tasks were **coding failures from the gpt-5.4-mini model/agent output**. They were not TrustableClaw auditability failures.

TrustableClaw still created and verified auditability evidence for those failed outputs. That is the expected behavior for an auditability layer: it should record both successful and failed AI work.

## What This Repository Claims

This repository shows that TrustableClaw wrapped all 164 HumanEval benchmark tasks with public auditability evidence summaries:

- 164 / 164 receipts reported created.
- 164 / 164 receipts reported verified.
- 164 / 164 tamper tests reported detected.
- 0 reported auditability failures.

## What This Repository Does Not Claim

This repository does **not** claim that TrustableClaw made the gpt-5.4-mini model better at solving coding tasks.

This repository also does **not** claim to provide full private ledger replay from the original TrustableClaw environment. The public evidence here is sanitized and does not include private prompts, private completions, API keys, secrets, or sensitive local paths.

## Reviewer Starting Points

- [Reviewer Summary](benchmarks/humaneval-governance-auditability/REVIEWER_SUMMARY.md)
- [Benchmark README](benchmarks/humaneval-governance-auditability/README.md)
- [Methodology](benchmarks/humaneval-governance-auditability/METHODOLOGY.md)
- [Replay / Verification Instructions](benchmarks/humaneval-governance-auditability/REPLAY.md)
- [Environment Notes](benchmarks/humaneval-governance-auditability/ENVIRONMENT.md)
- [Commands Notes](benchmarks/humaneval-governance-auditability/COMMANDS.md)
- [Public Results JSON](benchmarks/humaneval-governance-auditability/results/humaneval-164-results.json)
- [Receipt Manifest](benchmarks/humaneval-governance-auditability/receipts/receipt-manifest.json)

## Public Evidence Consistency Check

Run this from the repository root:

```bash
python -m py_compile benchmarks/humaneval-governance-auditability/scripts/verify_humaneval_evidence.py
python benchmarks/humaneval-governance-auditability/scripts/verify_humaneval_evidence.py
```

Expected output:

```text
HumanEval public evidence consistency check passed
Tasks: 164; coding passed: 146; coding failed: 18; auditability failures: 0
```
