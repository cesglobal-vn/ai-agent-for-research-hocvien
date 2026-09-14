# 📊 Mẫu Báo Cáo Phân Tích Dữ Liệu Định Lượng

> ✏️ **Đây là template mẫu, hãy sao chép và chỉnh theo đề tài của bạn.** Mọi chỗ ghi `[điền số]` hoặc `[điền …]` là chỗ bạn điền kết quả thật; xóa phần hướng dẫn trong ngoặc khi nộp.

| Thông tin | Chi tiết |
|---|---|
| **Tên nghiên cứu** | [điền tên đề tài] |
| **Tác giả** | [điền họ tên] |
| **Ngày phân tích** | [điền ngày/tháng/năm] |
| **Phần mềm / công cụ** | [ví dụ: Claude Code + skill data-analysis] |

> 📌 **Văn phong:** khách quan, **KHÔNG nói quá**. Ưu tiên "cho thấy", "có liên hệ"; tránh "chứng minh", "nhân quả" khi chưa có thiết kế phù hợp.

---

## 1. Giới thiệu mẫu & dữ liệu

- **Nguồn dữ liệu:** [điền nguồn — khảo sát trực tuyến, dữ liệu thứ cấp…].
- **Cách thu thập:** [điền cách lấy mẫu — thuận tiện, ngẫu nhiên…].
- **Cỡ mẫu ban đầu:** `[điền số]` quan sát.
- **Các biến chính:** [điền — ví dụ: DL (biến độc lập), KS (biến trung gian), IP (biến phụ thuộc)].

---

## 2. Làm sạch dữ liệu

Ghi lại trung thực mọi thao tác làm sạch (đây là nền tảng của kết quả đáng tin).

| Loại lỗi | Số lượng phát hiện | Cách xử lý |
|---|---|---|
| Giá trị thiếu | `[điền số]` ô | [điền — loại dòng / điền giá trị thay thế…] |
| Ngoại lai (outlier) vô lý | `[điền số]` giá trị | [điền — ví dụ tuổi 199 → loại] |
| Giá trị không nhất quán (cột phân loại) | `[điền số]` | [điền — chuẩn hóa nhãn giới tính…] |
| Dòng trùng lặp | `[điền số]` dòng | [điền — xóa bản trùng] |

- **Cỡ mẫu sau làm sạch:** `[điền số]` quan sát.

> ℹ️ Nêu rõ tiêu chí loại từng dòng để người đọc tái lập được.

---

## 3. Thống kê mô tả

### 3.1. Đặc điểm nhân khẩu

| Biến | Phân nhóm | Tần suất | Phần trăm |
|---|---|---|---|
| Giới tính | [điền] | `[điền số]` | `[điền số]`% |
| Độ tuổi | [điền nhóm] | `[điền số]` | `[điền số]`% |
| [biến khác] | [điền] | `[điền số]` | `[điền số]`% |

### 3.2. Biến số (thang đo)

| Biến / Thang đo | Trung bình | Độ lệch chuẩn | Min | Max |
|---|---|---|---|---|
| [thang 1] | `[điền số]` | `[điền số]` | `[điền số]` | `[điền số]` |
| [thang 2] | `[điền số]` | `[điền số]` | `[điền số]` | `[điền số]` |
| [thang 3] | `[điền số]` | `[điền số]` | `[điền số]` | `[điền số]` |

---

## 4. Kiểm định thang đo (độ tin cậy)

Cronbach's alpha cho từng thang (thường yêu cầu **alpha ≥ 0.7**).

| Thang đo | Số item | Alpha tổng | Item nên cân nhắc loại |
|---|---|---|---|
| [thang 1] | `[điền số]` | `[điền số]` | [điền hoặc "không"] |
| [thang 2] | `[điền số]` | `[điền số]` | [điền hoặc "không"] |
| [thang 3] | `[điền số]` | `[điền số]` | [điền hoặc "không"] |

- **Nhận xét:** [điền — các thang có đạt độ tin cậy không].

---

## 5. Kiểm định giả thuyết

### 5.1. Tương quan

| Cặp biến | Hệ số tương quan r | p-value |
|---|---|---|
| [biến A] – [biến B] | `[điền số]` | `[điền số]` |

### 5.2. Hồi quy

| Mô hình | Hệ số β | Sai số chuẩn | t | p-value | R² |
|---|---|---|---|---|---|
| [biến phụ thuộc] ~ [biến độc lập] | `[điền số]` | `[điền số]` | `[điền số]` | `[điền số]` | `[điền số]` |

### 5.3. Trung gian / điều tiết (nếu có)

- Đường a ([X] → [M]): β = `[điền số]`, p = `[điền số]`.
- Đường b ([M] → [Y]): β = `[điền số]`, p = `[điền số]`.
- Hiệu ứng tổng c: `[điền số]`; hiệu ứng trực tiếp c': `[điền số]`.
- Hiệu ứng gián tiếp a×b: `[điền số]` (khoảng tin cậy bootstrap 95%: `[điền số]` – `[điền số]`).
- **Kết luận loại trung gian:** [điền — toàn phần / một phần / không có].

### 5.4. Tổng hợp kết quả giả thuyết

| Giả thuyết | Nội dung | Kết quả |
|---|---|---|
| H1 | [điền] | [ủng hộ / không ủng hộ] |
| H2 | [điền] | [ủng hộ / không ủng hộ] |
| H3 | [điền] | [ủng hộ / không ủng hộ] |

---

## 6. Diễn giải

[điền 1–3 đoạn diễn giải kết quả, gắn với từng giả thuyết. Phân biệt rõ "có liên hệ" với "nhân quả". Không phóng đại. Nêu ý nghĩa thực tiễn nếu phù hợp.]

---

## 7. Hạn chế

- [điền — ví dụ: dữ liệu cắt ngang nên không khẳng định nhân quả].
- [điền — ví dụ: mẫu thuận tiện nên hạn chế tính khái quát].
- [điền — ví dụ: đo lường bằng tự báo cáo].

---

## 8. Khai báo dùng AI

> Trong quá trình phân tích dữ liệu và viết báo cáo này, tác giả có sử dụng công cụ trí tuệ nhân tạo ([điền tên công cụ]) để hỗ trợ [làm sạch dữ liệu / chạy kiểm định / chỉnh văn phong]. Toàn bộ số liệu, kết quả, lập luận và kết luận đã được tác giả kiểm tra, hiệu chỉnh và **chịu trách nhiệm hoàn toàn**. Công cụ AI **không** được liệt kê là tác giả.

> ℹ️ **Lưu ý:** kiểm tra quy định **cụ thể** của trường/tạp chí bạn nộp, vì cách diễn đạt yêu cầu có thể khác nhau. Xem thêm mẫu chi tiết trong `MAU_KHAI_BAO_AI.md`.
