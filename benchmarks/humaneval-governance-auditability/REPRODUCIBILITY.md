# Reproducibility Notes

This file explains how the TrustableClaw HumanEval Governance & Auditability Benchmark was run and how the results should be interpreted.

## Benchmark

The benchmark used HumanEval coding tasks.

The full run attempted 164 / 164 tasks.

## Model and Agent

- Model: openai-gpt-5-4-mini
- Agent: TrustableClaw CLI

## What Was Evaluated

This benchmark evaluated two separate layers:

1. Coding performance
2. TrustableClaw governance and auditability

Coding performance measures whether the generated code passed the HumanEval tests.

Governance and auditability measure whether TrustableClaw created receipts, verified receipts, and detected tampering.

## Full Run Result

```text
Tasks attempted: 164 / 164
Coding tasks passed: 146 / 164
Coding tasks failed: 18 / 164
Coding pass rate: 89.0%

Receipts created: 164 / 164
Receipts verified: 164 / 164
Tamper tests detected: 164 / 164
```
