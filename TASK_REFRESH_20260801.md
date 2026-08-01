# TASK REFRESH — 2026-08-01

## Scope
Refresh every task/worker touching the 90 ITEM source, X Runtime, the 090 ITEM pilot, or Codex execution before the next action.

## Current source set

1. `CHECKPOINT_NHAT_KY_DONG_X_20260801_0437`
   - Session: `CHATGPT-20260801-090-ITEM-PILOT`.
   - Source file: `02_TAC_PHAM_090_ITEM_MASTER_PUBLIC_DEPOSIT_V3_READY_TO_SIGN.pdf`.
   - SHA-256: `179FEB1FE8C420377DD6D1C058EA7725D45B7C2EB6F18486092086C8F522BC46`.
   - Verified scope: `R-001..R-087 + R-088 + R-089 + R-097` = 90 ITEM.
   - Computer-use checkpoint: recorded as DONE.
   - M010/B: `FAILED_BEFORE_MODEL_COMPLETION`; not complete.
   - Condition A: sample delivered; verbatim response still pending.

2. `HỒ SƠ VỐN GỐC — 90 ITEM`
   - 90 ITEM is source capital, not proof of a finished product.

3. `LÕI MVP TỪ 90 ITEM — V0`
   - Keep SOURCE / OBSERVATION / INFERENCE / HYPOTHESIS / UNKNOWN / CONFLICT separate.
   - No PASS without readback.

4. `X RUNTIME — HỒ SƠ CÔNG KHAI V0`
   - Current public record says local Python CLI, synthetic fixtures, JSON receipts, and 6/6 unit tests PASS.
   - This does not complete the 090 ITEM model pilot.
   - No independent verifier, customer benchmark, design partner, revenue, or commercial validation yet.

5. Codex CLI config snapshot dated 2026-07-31
   - Snapshot records `gpt-5.5`, OpenAI provider, `xhigh`, workspace-write, and multi-agent/browser/computer-use enabled.
   - A Drive/GitHub snapshot is not proof that the current local Codex process loaded it.

## Corrections to old task state

- The five-stream registry dated 2026-07-29 is historical, not the final state.
- Do not use 152 ITEM as the implicit scope of the 90 ITEM pilot.
- Do not call the 90 ITEM source `R-000..R-089`; use the verified scope above.
- Do not merge X Runtime V0, the 090 ITEM pilot, MEI audit, and Codex continuity into one completion status.
- Do not upgrade `DESIGN_INFERENCE` to source fact.
- A workflow, commit, file, or configuration snapshot is not proof of local application or model completion.

## Mandatory refresh sequence

1. Record task ID, runtime, branch/thread, time, and scope.
2. Read the current sources directly.
3. Record source reference, version, modified time, and hash when available.
4. Compare previous state with current state.
5. Separate source, observation, inference, hypothesis, unknown, and conflict.
6. Perform one bounded and reversible action within real permissions.
7. Save evidence from the actual operation.
8. Read back the result and create a result hash when possible.
9. Return `PASS`, `PARTIAL`, or `BLOCKED`; do not use DONE without verified criteria.
10. Append a new delta; do not rewrite old history.

## Current priorities

- P0: restore the pilot PDF from a hash-matching source; do not reuse the stale 403 URL.
- P0: never read, copy, print, commit, or log credential values or secret-like filenames.
- P1: obtain one complete M010/B model run with log, artifact, and readback, or record the exact blocker.
- P1: preserve the verbatim Condition A response before A/B comparison.
- P1: verify the local Codex process path/version and prove which config/AGENTS files it actually loaded.
- P2: rerun the six X Runtime tests and output an independent receipt/readback hash.

## Output contract

Every refreshed task must emit:

- `task_id`
- `runtime / branch / thread`
- `scope`
- `sources[]`
- `observations[]`
- `inferences[]`
- `unknowns[]`
- `conflicts[]`
- `action_performed`
- `evidence[]`
- `readback`
- `status: PASS | PARTIAL | BLOCKED`
- `next_pointer`

A task may report `APPLIED_LOCAL` only after it reads the local file path, identifies the running Codex version/process, performs a bounded local test, and reads back the result. Otherwise use `STAGED` or `PARTIAL`.
