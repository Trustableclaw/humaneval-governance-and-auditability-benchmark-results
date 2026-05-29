# Methodology

## Benchmark Run Details

| Detail             | Value                     |
| ------------------ | ------------------------- |
| Benchmark run date | 2026-05-25 (single run)   |
| Operating system   | Windows 11                |
| Model used         | `gpt-5.4-mini`            |

## Purpose

This benchmark was prepared to show how TrustableClaw records governance and auditability evidence around AI benchmark tasks.

HumanEval was used because it is a widely recognized coding benchmark made up of 164 programming tasks. In this repo, HumanEval is used as a task set around which TrustableClaw auditability evidence is summarized.

## What Was Measured

Two separate outcomes are reported:

1. **Coding performance** — whether the model/agent output passed the HumanEval tests.
2. **TrustableClaw auditability performance** — whether TrustableClaw created and verified auditability evidence for each task and whether tamper tests were detected.

## Coding Pass/Fail

A task is marked `passed` when the generated solution passed the HumanEval evaluation for that task.

A task is marked `failed` when the generated solution did not pass the HumanEval evaluation for that task.

The benchmark recorded 146 coding passes and 18 coding failures.

## Auditability Pass/Fail

A task is marked as an auditability pass when the public summary reports that:

- a receipt was created,
- the receipt was verified,
- a tamper test was detected.

All 164 tasks are reported as auditability passes in the public evidence summary.

## Important Interpretation

This benchmark does not claim that TrustableClaw makes the model better at solving coding problems. The coding pass rate belongs to the model/agent setup used for the run.

This benchmark measures whether TrustableClaw can create, verify, and tamper-test audit evidence for every AI task, including both successful and failed coding outputs.

## Public Evidence Limits

This repository is a sanitized public evidence summary. It does not include private prompts, private completions, API keys, secrets, sensitive local paths, or a full private ledger replay.
