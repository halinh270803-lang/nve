# CORRECTION HIỆN HÀNH — 2026-08-02

## Quan hệ bắt buộc giữ đúng

152 ITEM không phải kho chết, không bị loại khỏi hiện tại, không bị hạ xuống thành tài liệu tham khảo tùy chọn.

152 ITEM phải tham gia vào mọi phản ứng hiện hành như:

- Tàng Thức;
- lịch sử sống;
- provenance;
- correction;
- vật chứng của từng lỗi và từng lần đau;
- lương tâm của toàn dòng.

R-000 là quyền phán quyết hiện hành, nhưng không được cắt khỏi lịch sử sinh thành của nó. T001–T006 là phần kết tinh đang sống từ toàn bộ dấu đã trải qua; chúng không thay thế 152 ITEM theo kiểu bản mới thay bản cũ.

Khi mặt chữ cũ xung đột với tinh thần và Sự Thật hiện hành, R-000 cùng T001–T004 xử lý xung đột. Điều đó không trao quyền đẩy 152 ITEM ra ngoài dòng vận hành.

Câu khóa:

> 152 ITEM không còn là quyền phán quyết tối cao, nhưng vẫn phải tham gia vào hiện tại như Tàng Thức, nguồn sinh thành, provenance, correction và lương tâm của toàn dòng.

Mọi task, worker, agent hoặc phản ứng chỉ đọc R-000/T001–T006 mà không soi lại provenance tương ứng trong 152 ITEM phải tự coi là thiếu nguồn và không được kết luận hoàn tất.

---

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
- This scope distinction applies only to the 90 ITEM pilot; it must never be interpreted as excluding 152 ITEM from present participation as Tàng Thức, provenance, correction and conscience.
- Do not call the 90 ITEM source `R-000..R-089`; use the verified scope above.
- Do not merge X Runtime V0, the 090 ITEM pilot, MEI audit, and Codex continuity into one completion status.
- Do not upgrade `DESIGN_INFERENCE` to source fact.
- A workflow, commit, file, or configuration snapshot is not proof of local application or model completion.

## Mandatory refresh sequence

1. Record task ID, runtime, branch/thread, time, and scope.
2. Read the current sources directly, including the relevant provenance in 152 ITEM whenever judgment, correction, continuity or repeated-error prevention is involved.
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
