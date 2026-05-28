# Commands and Replay Status

This file separates two things:

1. Historical benchmark commands used during the original run.
2. Public replay commands that reviewers can run against the sanitized evidence committed to this repository.

## Historical command capture status

The exact historical commands for the original benchmark run were not preserved in the public evidence package. Do not invent them.

If the original logs are recovered, replace the `Not recorded` entries below with the exact commands and commit the update through the official TrustableClaw GitHub account.

### 1. Run HumanEval inference

```bash
# Not recorded. Add the exact command used for the original inference run if recovered.
```

### 2. Generate TrustableClaw receipts

```bash
# Not recorded. Add the exact command used to generate TrustableClaw receipts if recovered.
```

### 3. Verify receipts

```bash
# Not recorded. Add the exact TrustableClaw receipt verification command if recovered.
```

### 4. Run tamper tests

```bash
# Not recorded. Add the exact tamper-test command if recovered.
```

### 5. Generate summaries

```bash
# Not recorded. Add the exact summary-generation command if recovered.
```

## Public evidence consistency replay

This command checks the non-secret public evidence included in this repository:

```bash
python -m py_compile benchmarks/humaneval-governance-auditability/scripts/verify_humaneval_evidence.py
python benchmarks/humaneval-governance-auditability/scripts/verify_humaneval_evidence.py
```

Expected output:

```text
HumanEval public evidence consistency check passed
Tasks: 164; coding passed: 146; coding failed: 18; auditability failures: 0
```

## Important limit

The public replay command verifies that the committed public evidence files agree with each other.

It does not rerun paid model inference and does not independently replay private cryptographic ledger verification unless canonical public ledger artifacts are added.
