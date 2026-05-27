# Receipt Schema

Published receipts should be sanitized before being committed to GitHub.

Do not include:

- API keys
- secrets
- private prompts
- personal names
- private file paths
- local machine paths
- hidden environment variables
- sensitive logs

A public sample receipt should include safe fields such as:

```json
{
  "benchmark": "HumanEval",
  "task_id": "HumanEval/0",
  "model": "openai-gpt-5-4-mini",
  "agent": "TrustableClaw CLI",
  "coding_result": "FAIL",
  "receipt_id": "example-receipt-id",
  "timestamp_utc": "example-timestamp",
  "input_hash": "example-input-hash",
  "output_hash": "example-output-hash",
  "receipt_hash": "example-receipt-hash",
  "previous_hash": "example-previous-hash",
  "verification_status": "verified"
}
```
