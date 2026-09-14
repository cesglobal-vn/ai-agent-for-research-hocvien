# 📝 Đề Bài — Phân Tích Dữ Liệu Khảo Sát (Buổi 3)

> Dữ liệu: [`khao-sat-doi-moi-dnnvv.csv`](khao-sat-doi-moi-dnnvv.csv) · Mô tả biến: [bảng mô tả dữ liệu](bang-mo-ta-du-lieu.md)

## Bối cảnh

Bạn nhận một bộ dữ liệu khảo sát **320 nhân sự** tại các doanh nghiệp nhỏ và vừa (DNNVV). Câu hỏi nghiên cứu:

> **Lãnh đạo số** có làm tăng **Hiệu quả đổi mới** không, và **Chia sẻ tri thức** có đóng vai trò trung gian không?

## Nhiệm vụ

Mở Claude Code trong VS Code, nạp skill `data-analysis`, rồi đi lần lượt:

1. **Nạp & xem dữ liệu:** đọc file CSV, in 5 dòng đầu, liệt kê tên biến.
2. **Làm sạch dữ liệu:** đếm số ô trống (missing); phát hiện giá trị ngoài thang 1–5 (outlier); quyết định cách xử lý và cho biết còn bao nhiêu quan sát sau làm sạch.
3. **Thống kê mô tả:** lập bảng nhân khẩu học (tần suất, %); tính mean/SD cho từng item.
4. **Kiểm định thang đo:** tính Cronbach's alpha cho 3 khái niệm (DL, KS, IP); nhận xét độ tin cậy (ngưỡng ≥ 0.70).
5. **Kiểm định giả thuyết:**
   - H1: Lãnh đạo số → Hiệu quả đổi mới (hồi quy đơn).
   - H2: Lãnh đạo số → Chia sẻ tri thức.
   - H3: Chia sẻ tri thức → Hiệu quả đổi mới (khi đã có Lãnh đạo số).
   - Kiểm định **vai trò trung gian** của Chia sẻ tri thức bằng **khoảng tin cậy bootstrap 95%** (Preacher–Hayes), kết luận trung gian một phần hay toàn phần.
6. **Diễn giải:** viết 3–5 câu kết luận, **không suy nhân quả** vượt quá dữ liệu cắt ngang.

## Yêu cầu nộp

- Một báo cáo ngắn theo [mẫu báo cáo phân tích dữ liệu](../tai-lieu-mau/MAU_BAO_CAO_PHAN_TICH_DU_LIEU.md).
- Một dòng **khai báo sử dụng AI** (xem [mẫu khai báo](../tai-lieu-mau/MAU_KHAI_BAO_AI.md)).

> ✅ Làm xong, đối chiếu với [kết quả mong đợi](ket-qua-mong-doi.md) để tự chấm. Con số của bạn có thể lệch nhẹ tùy cách xử lý outlier — quan trọng là **đúng quy trình và đúng cách diễn giải**.

> ⚠️ **Liêm chính:** đây là dữ liệu giả lập để luyện tập. Khi làm đề tài thật, không bịa số liệu, không bịa nguồn, và phải khai báo việc dùng AI theo quy định của trường/tạp chí.
