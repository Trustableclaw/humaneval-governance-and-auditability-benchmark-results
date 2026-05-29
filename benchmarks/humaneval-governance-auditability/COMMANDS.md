# Commands

## Public Verification Commands

The following commands are available in this repository for public evidence consistency checks:

```bash
python -m py_compile benchmarks/humaneval-governance-auditability/scripts/verify_humaneval_evidence.py
python benchmarks/humaneval-governance-auditability/scripts/verify_humaneval_evidence.py
```

Expected output:

```text
HumanEval public evidence consistency check passed
Tasks: 164; coding passed: 146; coding failed: 18; auditability failures: 0
```

## Historical Benchmark Commands

The exact historical commands used during the original private benchmark run were not recorded in this public evidence package.

Because they were not recorded, this repository does not claim full end-to-end private replay from original inference through private ledger verification. It provides a public sanitized evidence summary and a consistency verifier for the published public files.
