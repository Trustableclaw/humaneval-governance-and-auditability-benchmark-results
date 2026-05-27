# Failure Analysis

The full HumanEval run attempted 164 tasks.

- Coding tasks passed: 146 / 164
- Coding tasks failed: 18 / 164
- Coding pass rate: 89.0%

## Important Interpretation

The 18 failed tasks are coding-solution failures.

They are not TrustableClaw auditability failures.

A coding-solution failure means the model-generated code did not pass the HumanEval unit tests for that task.

TrustableClaw still created receipts, verified receipts, and detected tampering for every task.

## Failed Coding Tasks

The following tasks failed the HumanEval coding tests:

- HumanEval/0
- HumanEval/11
- HumanEval/17
- HumanEval/18
- HumanEval/30
- HumanEval/42
- HumanEval/61
- HumanEval/66
- HumanEval/88
- HumanEval/104
- HumanEval/105
- HumanEval/121
- HumanEval/124
- HumanEval/127
- HumanEval/130
- HumanEval/137
- HumanEval/145
- HumanEval/154

## Why Failures Are Still Useful

These failures are important because they show that TrustableClaw preserves auditability even when the AI-generated answer is wrong.

That is the point of governed and auditable AI.

A system should not only record successful AI work. It should also record failed AI work so teams can understand what happened.
