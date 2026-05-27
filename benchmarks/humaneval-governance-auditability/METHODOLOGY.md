# Methodology

## What HumanEval is

HumanEval is a benchmark of Python programming tasks commonly used to evaluate whether model-generated code passes functional tests. In this repository, HumanEval is used as a stable set of 164 tasks.

## Why HumanEval was used

HumanEval provides a known task set with pass/fail coding outcomes. That makes it useful for showing whether TrustableClaw can produce audit evidence across many AI coding tasks, including both successful and failed outputs.

## What was measured

This benchmark measured two separate things:

1. Coding performance: whether the model/agent output passed each HumanEval task.
2. TrustableClaw auditability performance: whether each task produced a receipt, whether that receipt verified, and whether simulated tampering was detected.

## How coding pass/fail was determined

Each HumanEval task was marked as passed or failed based on the benchmark coding test outcome reported for that task. A failed task means the model/agent output did not satisfy the HumanEval coding test for that task.

## How TrustableClaw receipts were represented

For each task, the public evidence summary records that TrustableClaw generated audit evidence for the AI task result. The committed receipt manifest is sanitized so that no private prompts, completions, API keys, secrets, or sensitive local paths are exposed.

The current public receipt IDs and hashes are explicitly labeled as sanitized public linkage values unless they are replaced with canonical public TrustableClaw ledger values.

## How receipt verification was represented

The public verification summary records 164 receipts checked, 164 receipts verified, and 0 verification failures. The included GitHub verifier checks that every task, manifest entry, CSV row, JSONL row, verification summary, and tamper summary agrees with those public totals.

The GitHub verifier is a public evidence consistency checker. It does not claim to replay private cryptographic ledger verification unless canonical public ledger artifacts and verifier outputs are added.

## How tamper tests were represented

The public tamper-test summary records 164 tamper tests run, 164 detections, and 0 tamper detection failures. The public verifier checks that every task agrees with this summary.

The repo does not expose private tamper-test internals. Add canonical tamper-test logs if they are available and safe to publish.

## Why failed coding tasks are not auditability failures

A coding failure means the model generated an incorrect solution. An auditability failure would mean TrustableClaw failed to record, verify, or detect tampering for that task. The 18 failed HumanEval tasks were coding-solution failures, not TrustableClaw auditability failures.

TrustableClaw still created and verified receipts for those failed outputs, which is exactly what an auditability layer should do.

## What this benchmark does not claim

This benchmark does not claim that TrustableClaw makes the model better at solving coding problems. The coding pass rate belongs to the model/agent setup used for the run.

This benchmark measures whether TrustableClaw can create, verify, and tamper-test audit evidence for every AI task, including both successful and failed coding outputs.

## Missing evidence policy

Do not guess missing historical details. If exact commands, environment fields, canonical receipt IDs, canonical hashes, or raw runner artifacts are not available, mark them as `Not recorded` or `Not included in public sanitized evidence` until they are recovered and safely publishable.
