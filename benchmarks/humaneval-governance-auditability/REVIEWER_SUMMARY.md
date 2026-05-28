# Reviewer Summary: HumanEval Governance & Auditability Results

This file gives reviewers the shortest path to the benchmark result and the evidence files that support it.

## Result at a glance

| Question                                                    |    Answer |
| ----------------------------------------------------------- | --------: |
| How many HumanEval tasks were attempted?                    |       164 |
| How many HumanEval tasks passed?                            |       146 |
| How many HumanEval tasks failed?                            |        18 |
| What was the HumanEval coding pass rate?                    |     89.0% |
| How many TrustableClaw receipts were reported created?      | 164 / 164 |
| How many TrustableClaw receipts were reported verified?     | 164 / 164 |
| How many TrustableClaw tamper tests were reported detected? | 164 / 164 |
| How many TrustableClaw auditability failures were reported? |         0 |

## Key interpretation

The coding result and the auditability result are separate.

The 18 failed HumanEval tasks were coding failures from the model/agent output. They were not TrustableClaw auditability failures.

TrustableClaw still reported audit evidence for all 164 tasks, including failed coding outputs.

## Evidence map

| Evidence file                            | What reviewers can check                             |
| ---------------------------------------- | ---------------------------------------------------- |
| `results/humaneval-164-results.json`     | All 164 task records in JSON form                    |
| `results/humaneval-164-results.jsonl`    | All 164 task records in JSONL form                   |
| `results/humaneval-164-summary.csv`      | Reviewer-friendly task summary table                 |
| `humaneval-164-summary.txt`              | Human-readable task-by-task summary                  |
| `receipts/receipt-manifest.json`         | One sanitized public receipt-manifest entry per task |
| `verification/verification-results.json` | 164 receipts checked, 164 verified, 0 failures       |
| `tamper-tests/tamper-results.json`       | 164 tamper tests run, 164 detected, 0 failures       |
| `scripts/verify_humaneval_evidence.py`   | Public consistency checker for the evidence files    |

## Reviewer verification command

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

## Public evidence limit

This repo contains a sanitized public evidence summary. It does not expose private prompts, completions, API keys, secrets, or sensitive local paths. It also does not claim to independently replay private cryptographic ledger verification unless canonical public ledger artifacts are later added.
