# 📊 Báo Cáo Phân Tích Dữ Liệu Định Lượng

| Thông tin | Chi tiết |
|---|---|
| **Tên nghiên cứu** | Ảnh hưởng của Lãnh đạo số đến Hiệu quả đổi mới trong doanh nghiệp nhỏ và vừa (DNNVV): vai trò trung gian của Chia sẻ tri thức |
| **Tác giả** | [điền họ tên] |
| **Ngày phân tích** | 25/08/2026 |
| **Phần mềm / công cụ** | Claude Code + skill data-analysis, academic-writing |

> Văn phong: khách quan, không nói quá. Dữ liệu cắt ngang nên diễn giải theo hướng liên hệ, không suy nhân quả.

---

## 1. Giới thiệu mẫu & dữ liệu

- **Nguồn dữ liệu:** khảo sát nhân sự tại các doanh nghiệp nhỏ và vừa (DNNVV). Dữ liệu giả lập phục vụ dạy học.
- **Cách thu thập:** bảng hỏi tự báo cáo, thang Likert 5 mức (1 = Hoàn toàn không đồng ý … 5 = Hoàn toàn đồng ý).
- **Cỡ mẫu ban đầu:** 320 quan sát.
- **Các biến chính:**
  - **Lãnh đạo số (DL)** biến độc lập (X), đo bằng 4 item DL1 tới DL4.
  - **Chia sẻ tri thức (KS)** biến trung gian (M), đo bằng 4 item KS1 tới KS4.
  - **Hiệu quả đổi mới (IP)** biến phụ thuộc (Y), đo bằng 4 item IP1 tới IP4.
- **Mô hình giả thuyết:** DL → KS → IP.

---

## 2. Làm sạch dữ liệu

Quy trình làm sạch được ghi lại đầy đủ để bảo đảm khả năng tái lập.

| Loại lỗi | Số lượng phát hiện | Cách xử lý |
|---|---|---|
| Giá trị thiếu (missing) | 14 ô (nằm rải ở 14 dòng, thuộc các item thang đo) | Loại dòng (listwise) |
| Ngoại lai (outlier) vô lý | 4 giá trị: R045 DL3=0; R110 KS1=0; R077 IP2=7; R203 IP4=9 (ngoài thang 1–5) | Coi là lỗi nhập liệu, chuyển thành khuyết rồi loại dòng |
| Giá trị không nhất quán (cột phân loại) | 0 | Không cần xử lý, nhãn đã thống nhất |
| Dòng trùng lặp | 0 | Không cần xử lý |

- **Số dòng bị loại:** 18 (14 do thiếu + 4 do ngoại lai, không có dòng dính cả hai lỗi).
- **Cỡ mẫu sau làm sạch:** **302 quan sát.**

> Tiêu chí loại: một dòng bị loại nếu có bất kỳ item nào bị thiếu hoặc mang giá trị ngoài khoảng hợp lệ 1–5.

---

## 3. Thống kê mô tả

### 3.1. Đặc điểm nhân khẩu (N = 302)

| Biến | Phân nhóm | Tần suất | Phần trăm |
|---|---|---|---|
| Giới tính | Nam | 146 | 48.3% |
| | Nữ | 156 | 51.7% |
| Nhóm tuổi | Dưới 30 | 77 | 25.5% |
| | 30–39 | 107 | 35.4% |
| | 40–49 | 69 | 22.8% |
| | 50 trở lên | 49 | 16.2% |
| Kinh nghiệm | Dưới 3 năm | 81 | 26.8% |
| | 3–5 năm | 95 | 31.5% |
| | 6–10 năm | 65 | 21.5% |
| | Trên 10 năm | 61 | 20.2% |
| Quy mô DN | Siêu nhỏ | 80 | 26.5% |
| | Nhỏ | 135 | 44.7% |
| | Vừa | 87 | 28.8% |
| Ngành | Thương mại-Dịch vụ | 118 | 39.1% |
| | Sản xuất | 82 | 27.2% |
| | Công nghệ thông tin | 58 | 19.2% |
| | Xây dựng | 26 | 8.6% |
| | Khác | 18 | 6.0% |

Mẫu tương đối cân bằng về giới tính, tập trung ở nhóm tuổi 30–39 và ở doanh nghiệp quy mô nhỏ, ngành Thương mại-Dịch vụ.

### 3.2. Biến số (điểm trung bình mỗi thang, N = 302)

| Thang đo | Trung bình | Độ lệch chuẩn | Min | Max |
|---|---|---|---|---|
| Lãnh đạo số (DL) | 3.39 | 0.77 | 1.00 | 5.00 |
| Chia sẻ tri thức (KS) | 3.39 | 0.77 | 1.00 | 5.00 |
| Hiệu quả đổi mới (IP) | 3.43 | 0.80 | 1.00 | 5.00 |

Cả ba thang có điểm trung bình quanh mức 3.4/5, độ phân tán vừa phải.

---

## 4. Kiểm định thang đo (độ tin cậy)

Cronbach's alpha cho từng thang (ngưỡng chấp nhận ≥ 0.70).

| Thang đo | Số item | Alpha tổng | Item nên cân nhắc loại |
|---|---|---|---|
| Lãnh đạo số (DL) | 4 | 0.815 | Không |
| Chia sẻ tri thức (KS) | 4 | 0.805 | Không |
| Hiệu quả đổi mới (IP) | 4 | 0.835 | Không |

- **Nhận xét:** cả ba thang đạt độ tin cậy nội tại tốt (alpha 0.81–0.84). Với cả ba thang, việc loại bất kỳ item nào đều làm alpha giảm, nên giữ nguyên đủ 4 item mỗi thang.

---

## 5. Kiểm định giả thuyết

### 5.1. Tương quan

| Cặp biến | Hệ số tương quan r | p-value |
|---|---|---|
| Lãnh đạo số – Hiệu quả đổi mới | 0.498 | < .001 |

### 5.2. Hồi quy (IP ~ DL, hồi quy tuyến tính đơn)

| Mô hình | Hệ số B | Beta chuẩn hóa | Sai số chuẩn | t | p-value | R² |
|---|---|---|---|---|---|---|
| Hiệu quả đổi mới ~ Lãnh đạo số | 0.517 | 0.498 | 0.052 | 9.94 | < .001 | 0.248 |

Khi điểm Lãnh đạo số tăng 1 đơn vị, điểm Hiệu quả đổi mới tăng trung bình 0.52 đơn vị. Mô hình giải thích khoảng 25% phương sai của Hiệu quả đổi mới.

### 5.3. Trung gian (KS trong quan hệ DL → IP)

- **Đường a** (DL → KS): B = 0.466, β = 0.463, p < .001.
- **Đường b** (KS → IP, kiểm soát DL): B = 0.315, p < .001.
- **Hiệu ứng tổng c** (DL → IP): 0.517; **hiệu ứng trực tiếp c'** (DL → IP, đã có KS): 0.370 (p < .001).
- **Hiệu ứng gián tiếp a×b:** 0.147 (khoảng tin cậy bootstrap 95%: 0.094 – 0.210, 5000 lần lấy mẫu lại, không chứa 0).
- **Kết luận loại trung gian:** trung gian một phần (partial mediation). Chia sẻ tri thức giải thích khoảng 28.5% tổng liên hệ giữa Lãnh đạo số và Hiệu quả đổi mới; phần còn lại là liên hệ trực tiếp.

### 5.4. Tổng hợp kết quả giả thuyết

| Giả thuyết | Nội dung | Kết quả |
|---|---|---|
| H1 | Lãnh đạo số có liên hệ thuận với Hiệu quả đổi mới | Ủng hộ (B = 0.517, p < .001) |
| H2 | Lãnh đạo số có liên hệ thuận với Chia sẻ tri thức | Ủng hộ (B = 0.466, p < .001) |
| H3 | Chia sẻ tri thức có liên hệ thuận với Hiệu quả đổi mới (kiểm soát Lãnh đạo số) | Ủng hộ (B = 0.315, p < .001) |
| H4 | Chia sẻ tri thức trung gian quan hệ Lãnh đạo số → Hiệu quả đổi mới | Ủng hộ, trung gian một phần (a×b = 0.147, 95% CI [0.094; 0.210]) |

---

## 6. Diễn giải

Trong mẫu 302 nhân sự DNNVV, Lãnh đạo số có liên hệ thuận và có ý nghĩa thống kê với Hiệu quả đổi mới (β = 0.50, p < .001); mô hình giải thích khoảng 25% phương sai của Hiệu quả đổi mới (R² = 0.25), cho thấy một liên hệ ở mức đáng kể chứ không chỉ có ý nghĩa về mặt con số.

Kết quả cũng cho thấy Chia sẻ tri thức đóng vai trò trung gian một phần trong quan hệ này. Hiệu ứng gián tiếp Lãnh đạo số → Chia sẻ tri thức → Hiệu quả đổi mới có ý nghĩa (a×b = 0.147, khoảng tin cậy bootstrap 95% [0.094; 0.210], không chứa 0), trong khi đường trực tiếp vẫn còn ý nghĩa (c' = 0.370, p < .001). Điều này gợi ý rằng một phần liên hệ giữa Lãnh đạo số và Hiệu quả đổi mới diễn ra gián tiếp thông qua việc thúc đẩy Chia sẻ tri thức, song Lãnh đạo số vẫn còn liên hệ trực tiếp với Hiệu quả đổi mới ngoài con đường này.

Vì đây là dữ liệu cắt ngang, các kết quả phản ánh mối liên hệ (tương quan) giữa các biến trong mẫu tại thời điểm khảo sát, chưa cho phép khẳng định quan hệ nhân quả. Cần thận trọng khi khái quát các phát hiện ra ngoài bối cảnh và thời điểm nghiên cứu.

---

## 7. Hạn chế

- **Thiết kế cắt ngang.** Dữ liệu được thu tại một thời điểm duy nhất, nên chỉ ghi nhận được sự đồng biến giữa các biến chứ không quan sát được diễn tiến theo thời gian. *Ảnh hưởng tới kết luận:* không thể khẳng định chiều nhân quả; về mặt logic, quan hệ có thể ngược lại (doanh nghiệp có hiệu quả đổi mới cao hơn tạo điều kiện cho lãnh đạo số phát triển) hoặc do một biến thứ ba chưa đo. Vì vậy mọi phát biểu trong báo cáo được giữ ở mức "có liên hệ", không mở rộng thành "làm tăng" hay "gây ra".

- **Cách lấy mẫu và tính khái quát.** Mẫu giới hạn trong nhóm nhân sự DNNVV và mang tính minh họa (dữ liệu giả lập phục vụ dạy học), không dựa trên khung lấy mẫu xác suất đại diện cho tổng thể. *Ảnh hưởng tới kết luận:* các con số (mean, alpha, hệ số hồi quy, tỉ lệ trung gian) chỉ có giá trị trong phạm vi mẫu này; không nên khái quát cho các loại hình doanh nghiệp, ngành hay bối cảnh khác khi chưa có mẫu đại diện và kiểm định lặp lại.

- **Đo lường bằng tự báo cáo.** Cả ba biến (Lãnh đạo số, Chia sẻ tri thức, Hiệu quả đổi mới) đều do cùng một người trả lời tự đánh giá trong cùng một bảng hỏi. *Ảnh hưởng tới kết luận:* độ lớn của các mối liên hệ có thể bị thổi phồng do thiên lệch phương pháp chung (common method bias), và các đánh giá có thể lệch theo hướng mong muốn xã hội. Do đó hệ số liên hệ và tỉ lệ trung gian nên được đọc như ước lượng cận trên; nghiên cứu sau cần thu thêm dữ liệu khách quan hoặc từ nhiều nguồn (đa nguồn thông tin) để kiểm chứng.

---

## 8. Khai báo dùng AI

> Trong quá trình phân tích dữ liệu và viết báo cáo này, tác giả có sử dụng công cụ trí tuệ nhân tạo (Claude Code) để hỗ trợ làm sạch dữ liệu, chạy kiểm định thống kê và chỉnh văn phong. Toàn bộ số liệu, kết quả, lập luận và kết luận đã được tác giả kiểm tra, hiệu chỉnh và chịu trách nhiệm hoàn toàn. Công cụ AI không được liệt kê là tác giả.

> Lưu ý: kiểm tra quy định cụ thể của trường/tạp chí bạn nộp, vì cách diễn đạt yêu cầu có thể khác nhau. Xem thêm mẫu chi tiết trong `MAU_KHAI_BAO_AI.md`.
