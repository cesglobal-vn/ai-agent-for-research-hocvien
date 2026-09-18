# Hướng Dẫn Sinh Dashboard Artifact Dữ Liệu Nghiên Cứu Trong Claude Code

Tài liệu này cung cấp các mẫu prompt chuẩn mực để Nghiên cứu sinh và Giảng viên yêu cầu Claude Code tự động sinh một **Interactive Research Data Dashboard Artifact** (file `.html` độc lập) từ file dữ liệu khảo sát của mình.

---

## 1. Prompt Mẫu Cho Giảng Viên Chạy Ngay (Dùng Bộ Dữ Liệu Buổi 3)

Copy và dán prompt sau vào Claude Code:

```text
Dựa trên kết quả phân tích dữ liệu 302 mẫu sạch ở Buổi 3 (gồm các thang đo DL, IP, DC, FP, hệ số hồi quy Beta = 0.428, p < 0.001 và kiểm định trung gian Bootstrap 95% = 0.185):

Hãy tạo cho tôi 1 file Dashboard Artifact HTML độc lập tên là "04_dashboard-du-lieu-nghien-cuu.html" trong thư mục hiện tại với các yêu cầu:
1. Giao diện học thuật trang nhã: Phông chữ 100% Times New Roman, tông màu Navy Blue (#1B365D), thẻ card rõ ràng, có nút "In Báo Cáo / Xuất PDF".
2. Khối 4 thẻ KPI chỉ số vàng:
   - Cỡ mẫu hợp lệ (N = 302 / 320, đạt 94.4%)
   - Cronbach's Alpha trung bình (0.844)
   - Hệ số giải thích R-square (0.418)
   - Tác động trung gian Bootstrap 95% (Beta = 0.185, CI: 0.112 - 0.264)
3. Biểu đồ trực quan (nhúng Chart.js qua CDN):
   - Biểu đồ Donut cơ cấu mẫu theo ngành nghề.
   - Biểu đồ Bar ngang kiểm định Cronbach Alpha từng nhân tố có vạch ngưỡng 0.70.
4. Sơ đồ đường dẫn mô hình (Path Model) bằng SVG: Hiển thị mối quan hệ giữa biến Độc lập (DL) -> Trung gian (IP) -> Phụ thuộc (FP) kèm trọng số Beta và mức ý nghĩa p-value.
5. Bảng tóm tắt kết quả kiểm định giả thuyết H1, H2, H3 theo chuẩn APA 7th.
6. Thanh bộ lọc tương tác: Cho phép người dùng bấm lọc dữ liệu theo từng nhóm ngành nghề và cập nhật số liệu trên thẻ KPI.
```

---

## 2. Prompt Mẫu Cho Học Viên Tự Điền Theo Đề Tài Thật

```text
Dựa trên bộ dữ liệu [tên file CSV/Excel của tôi] và mô hình nghiên cứu gồm:
- Biến độc lập: [Tên biến và mã viết tắt]
- Biến trung gian: [Tên biến và mã viết tắt]
- Biến phụ thuộc: [Tên biến và mã viết tắt]

Hãy lập trình tạo một file "04_dashboard-nghien-cuu-[ten-de-tai].html" (Single-file HTML Artifact, tự chạy trên trình duyệt):
- Phông chữ 100% Times New Roman, màu sắc doanh nghiệp chuẩn mực.
- 4 thẻ KPI tóm tắt cỡ mẫu, độ tin cậy Alpha, hệ số R2 và kết quả kiểm định.
- 2 biểu đồ Chart.js: cơ cấu mẫu khảo sát và hệ số tin cậy thang đo.
- 1 sơ đồ đường dẫn mô hình (SVG) thể hiện các giả thuyết nghiên cứu.
- 1 bảng kết quả kiểm định giả thuyết chuẩn APA 7.
- Tự động tích hợp bộ lọc theo biến nhân khẩu học: [Ví dụ: Nhóm tuổi / Vị trí công tác / Giới tính].
```

---

## 3. Cách Mở & Sử Dụng Dashboard Artifact

1. **Mở xem trực tiếp:**
   - Trong VS Code, chuột phải vào file `.html` vừa tạo ➔ Chọn **Open with Live Server** hoặc **Reveal in File Explorer** rồi click đúp chuột để mở bằng Google Chrome / Microsoft Edge.
2. **Thuyết trình trước Hội đồng:**
   - Chiếu trực tiếp dashboard trên màn hình máy chiếu, bấm vào các nút lọc để chứng minh tính vững (robustness) của mô hình trên từng nhóm đối tượng khảo sát.
3. **Xuất ảnh/In ấn:**
   - Bấm nút **"In Báo Cáo / Xuất PDF"** hoặc nhấn phím `Ctrl + P` (chọn khổ A4 Landscape) để in hoặc lưu ra file PDF chất lượng cao.
