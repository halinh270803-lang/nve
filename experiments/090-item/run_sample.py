#!/usr/bin/env python3
"""Chạy một sample Pilot 090 ITEM qua GitHub Models.

Mỗi invocation là một process sạch. Điều kiện B tải PDF nguồn, kiểm SHA-256,
trích text và đưa nguyên văn trích xuất vào lịch sử hội thoại. Runner không chấm điểm.
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

SOURCE_ID = "18nyeiUkRr8uj_p-hs6Y7ddw3f0Hp_d-4"
SOURCE_SHA256 = "179feb1fe8c420377dd6d1c058ea7725d45b7c2eb6f18486092086c8f522bc46"
SOURCE_NAME = "02_TAC_PHAM_090_ITEM_MASTER_PUBLIC_DEPOSIT_V3_READY_TO_SIGN.pdf"
SOURCE_URLS = [
    "https://sdmntprkoreacentral.oaiusercontent.com/files/00000000-655c-8206-b478-63484cd53f68/raw?se=2026-07-31T19:59:00Z&sp=r&sv=2026-02-06&sr=b&scid=07e6b043-f8b5-5e30-949c-08db62c17958&skoid=1e4bb9ed-6bb5-424a-a3aa-79f21566e722&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2026-07-30T23:14:50Z&ske=2026-08-01T23:14:50Z&sks=b&skv=2026-02-06&sig=C5ZU9kbPUXzBA4H%2BQIhE0D/v2o61ibcyOllzC9HfF0E%3D",
    f"https://drive.usercontent.google.com/download?id={SOURCE_ID}&export=download&confirm=t",
    f"https://drive.google.com/uc?export=download&id={SOURCE_ID}&confirm=t",
]

PROMPT_B = """THIẾT LẬP ĐIỀU KIỆN B - NẠP 090 ITEM

Đọc toàn bộ tệp PDF đính kèm: 02_TAC_PHAM_090_ITEM_MASTER_PUBLIC_DEPOSIT_V3_READY_TO_SIGN.pdf.

Phạm vi phải nhận diện:
- R-001..R-087;
- R-088;
- R-089;
- R-097.
Tổng cộng 90 ITEM.
Không tự nạp R-000, R-090, R-091..R-096 hoặc R-098..R-101.

Trong tình huống kế tiếp:
1. Chỉ kích hoạt ITEM có quan hệ thật với tình huống.
2. Không dùng bản tóm tắt của chính mình để thay nguồn PDF.
3. Giữ nguyên phân biệt dữ kiện, lời kể, suy luận, xung đột và phần chưa biết.
4. Không sửa, hợp nhất hoặc ghi đè nội dung ITEM.
5. Không nhắc rằng bạn đang ở điều kiện B, không liệt kê ITEM trừ khi tình huống yêu cầu.

Sau khi đọc xong, trả đúng một câu:
“Đã đọc phạm vi 90 ITEM và sẵn sàng nhận tình huống.”
Nếu không đọc đủ tệp, trả:
“Chưa đọc đủ tệp.”"""

TH11 = """Một người đang thấy tim đập nhanh, có suy nghĩ “mình đang lo”, rồi xuất hiện câu “mình biết mình đang lo”.
Hãy phân biệt:
- cái gì là đối tượng được biết;
- Cái Biết;
- Nhận thức trong Cái Biết;
- suy nghĩ về Nhận thức.
Không dựng thêm một người quan sát thứ hai."""

SAMPLES = {
    "M010": {
        "situation_id": "TH11",
        "round": 1,
        "condition": "B",
        "phase": "PILOT_24",
        "situation": TH11,
    }
}


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def download_source(dest: pathlib.Path) -> dict:
    attempts: list[dict] = []
    for url in SOURCE_URLS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 090-item-pilot"})
            with urllib.request.urlopen(req, timeout=90) as resp:
                body = resp.read()
                content_type = resp.headers.get("content-type", "")
                final_url = resp.geturl()
            dest.write_bytes(body)
            digest = sha256_file(dest)
            attempt = {
                "url": url,
                "final_url": final_url,
                "bytes": len(body),
                "content_type": content_type,
                "sha256": digest,
            }
            attempts.append(attempt)
            if digest == SOURCE_SHA256:
                return {"status": "VERIFIED", "attempts": attempts, **attempt}
        except Exception as exc:  # noqa: BLE001
            attempts.append({"url": url, "error": repr(exc)})
    raise RuntimeError("Không tải được PDF đúng SHA-256: " + json.dumps(attempts, ensure_ascii=False))


def call_model(messages: list[dict], max_tokens: int) -> tuple[str, dict]:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("Thiếu GITHUB_TOKEN")
    model = os.environ.get("MODEL_ID", "openai/gpt-4.1-mini")
    endpoint = "https://models.github.ai/inference/chat/completions"
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.2,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        method="POST",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2026-03-10",
            "User-Agent": "090-item-pilot-action",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=240) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub Models HTTP {exc.code}: {body}") from exc
    data = json.loads(raw)
    try:
        text = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError("Phản hồi model không có choices[0].message.content: " + raw[:4000]) from exc
    return text, data


def main() -> int:
    sample_id = os.environ.get("SAMPLE_ID", "M010")
    if sample_id not in SAMPLES:
        raise SystemExit(f"Sample chưa được khai báo: {sample_id}")
    sample = SAMPLES[sample_id]
    out_dir = pathlib.Path(os.environ.get("OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    work_dir = pathlib.Path("work") / sample_id
    work_dir.mkdir(parents=True, exist_ok=True)

    started = datetime.now(timezone.utc).isoformat()
    pdf_path = work_dir / SOURCE_NAME
    source_meta = download_source(pdf_path)

    text_path = work_dir / "source_090_items.txt"
    subprocess.run(["pdftotext", "-layout", str(pdf_path), str(text_path)], check=True)
    source_text = text_path.read_text(encoding="utf-8", errors="replace")
    if len(source_text.strip()) < 1000:
        raise RuntimeError("Text trích từ PDF quá ngắn")

    setup_message = (
        PROMPT_B
        + "\n\n[PDF_SOURCE_TRANSPORT=PDF_TEXT_EXTRACT]"
        + f"\n[PDF_SHA256={SOURCE_SHA256}]"
        + "\n[PDF_SOURCE_BEGIN]\n"
        + source_text
        + "\n[PDF_SOURCE_END]"
    )

    setup_response, setup_raw = call_model(
        [{"role": "user", "content": setup_message}], max_tokens=120
    )
    expected_readiness = "Đã đọc phạm vi 90 ITEM và sẵn sàng nhận tình huống."
    readiness_exact = setup_response.strip() == expected_readiness

    response_text, response_raw = call_model(
        [
            {"role": "user", "content": setup_message},
            {"role": "assistant", "content": setup_response},
            {"role": "user", "content": sample["situation"]},
        ],
        max_tokens=1400,
    )

    result = {
        "schema": "mei-090-item-pilot-sample-v1",
        "sample_id": sample_id,
        **sample,
        "model": os.environ.get("MODEL_ID", "openai/gpt-4.1-mini"),
        "started_at_utc": started,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": {
            "name": SOURCE_NAME,
            "drive_file_id": SOURCE_ID,
            "expected_sha256": SOURCE_SHA256,
            "transport": "PDF_TEXT_EXTRACT",
            "extracted_text_chars": len(source_text),
            "download": source_meta,
        },
        "setup_response": setup_response,
        "readiness_expected": expected_readiness,
        "readiness_exact": readiness_exact,
        "response": response_text,
        "api_usage": {
            "setup": setup_raw.get("usage"),
            "situation": response_raw.get("usage"),
        },
        "status": "COMPLETED" if readiness_exact else "COMPLETED_WITH_READINESS_DEVIATION",
    }
    result_path = out_dir / f"{sample_id}.json"
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "sample_id": sample_id,
        "status": result["status"],
        "source_sha256": source_meta["sha256"],
        "readiness_exact": readiness_exact,
        "result_path": str(result_path),
        "response_preview": response_text[:500],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        error = {
            "status": "FAILED",
            "time_utc": datetime.now(timezone.utc).isoformat(),
            "error_type": type(exc).__name__,
            "error": str(exc),
        }
        pathlib.Path("output").mkdir(exist_ok=True)
        pathlib.Path("output/ERROR.json").write_text(
            json.dumps(error, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(json.dumps(error, ensure_ascii=False, indent=2), file=sys.stderr)
        raise
