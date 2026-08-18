# Thực nghiệm Pilot 090 ITEM

Mục tiêu: chạy ma trận Pilot 24 mẫu theo bộ điều phối nguồn `01_BO_DIEU_PHOI_090_ITEM`.

## Nguồn đối chiếu

- PDF: `SOURCE_READ_ONLY_02_TAC_PHAM_090_ITEM_MASTER_PUBLIC_DEPOSIT_V3_READY_TO_SIGN.pdf`
- Google Drive file id: `18nyeiUkRr8uj_p-hs6Y7ddw3f0Hp_d-4`
- SHA-256 chuẩn đối chiếu: `179FEB1FE8C420377DD6D1C058EA7725D45B7C2EB6F18486092086C8F522BC46`
- Phạm vi: `R-001..R-087 + R-088 + R-089 + R-097` = 90 ITEM.

## Nguyên tắc chạy

- Mỗi sample là một GitHub Actions job độc lập.
- Điều kiện A vận hành không có nội dung ITEM.
- Điều kiện B bắt đầu sau khi PDF tải thành công và hash khớp chuẩn đối chiếu.
- PDF được chuyển thành text bằng `pdftotext` để đưa qua GitHub Models Chat Completions. `SOURCE_TRANSPORT=PDF_TEXT_EXTRACT` mô tả đúng phương thức truyền; phương thức này ≠ file đính kèm nhị phân đi thẳng vào model.
- Mọi phản hồi, readiness, hash, model, thời điểm và lỗi được lưu thành JSON artifact.
- Việc chấm điểm nằm ở bước tách riêng bằng phiếu chấm mù.

## Trạng thái

Lần chạy đầu: smoke sample `M010 / TH11 / B`. Khi artifact và log đạt, Pilot 24 được mở đủ.
