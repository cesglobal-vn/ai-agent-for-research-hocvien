# ✅ Kết Quả Mong Đợi (Để Tự Chấm)

> Đây là kết quả tham chiếu khi phân tích [`khao-sat-doi-moi-dnnvv.csv`](khao-sat-doi-moi-dnnvv.csv). Con số của bạn có thể lệch nhẹ tùy cách xử lý dữ liệu thiếu/outlier — điều quan trọng là **đúng quy trình** và **diễn giải đúng**.

## Bước 2 — Làm sạch dữ liệu

| Hạng mục | Kết quả |
|---|---|
| Tổng quan sát ban đầu | 320 |
| Số ô trống (missing) | **14** |
| Số giá trị ngoài thang 1–5 (outlier) | **4** (R045 `DL3`=0; R110 `KS1`=0; R077 `IP2`=7; R203 `IP4`=9) |
| Số dòng bị loại (listwise) | 18 |
| **Quan sát còn lại để phân tích** | **302** |

## Bước 4 — Độ tin cậy (Cronbach's alpha)

| Khái niệm | Số item | Alpha | Nhận xét |
|---|---|---|---|
| Lãnh đạo số (DL) | 4 | **≈ 0.81** | Đạt (≥ 0.70) |
| Chia sẻ tri thức (KS) | 4 | **≈ 0.81** | Đạt |
| Hiệu quả đổi mới (IP) | 4 | **≈ 0.83** | Đạt |

## Bước 5 — Kiểm định giả thuyết

Dùng điểm trung bình từng khái niệm (mean của 4 item) và hồi quy tuyến tính:

| Giả thuyết | Đường | Hệ số (chưa chuẩn hóa) | Kết luận |
|---|---|---|---|
| H2 | Lãnh đạo số → Chia sẻ tri thức (a) | b ≈ **0.48** | Ủng hộ |
| H1 | Lãnh đạo số → Hiệu quả đổi mới — tổng tác động (c) | b ≈ **0.53** (β chuẩn hóa ≈ 0.51), R² ≈ 0.26 | Ủng hộ |
| — | Lãnh đạo số → Hiệu quả đổi mới — trực tiếp (c′) | b ≈ **0.37** | Giảm so với c nhưng vẫn có ý nghĩa |
| H3 | Chia sẻ tri thức → Hiệu quả đổi mới (b) | b ≈ **0.32**, R² mô hình ≈ 0.33 | Ủng hộ |

**Trung gian:** tác động gián tiếp a × b ≈ **0.15**, khoảng tin cậy bootstrap 95% **không chứa 0** → Chia sẻ tri thức là **trung gian một phần** (vì tác động trực tiếp c′ vẫn có ý nghĩa).

## Bước 6 — Mẫu câu diễn giải đúng

> "Trên mẫu 302 nhân sự DNNVV, lãnh đạo số có **liên hệ thuận** với hiệu quả đổi mới (β ≈ 0.51). Một phần liên hệ này diễn ra **gián tiếp qua** chia sẻ tri thức (trung gian một phần). Vì đây là dữ liệu **cắt ngang**, kết quả phản ánh **tương quan**, **chưa thể kết luận nhân quả**."

> ⚠️ Tránh viết "lãnh đạo số **làm tăng / gây ra** hiệu quả đổi mới" — dữ liệu cắt ngang không cho phép khẳng định nhân quả. Xem skill `data-analysis/quy-trinh/dien-giai-ket-qua`.
