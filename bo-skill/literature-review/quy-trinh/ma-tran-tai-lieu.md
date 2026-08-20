# Lập ma trận tổng hợp tài liệu (literature matrix)

## Mục Tiêu

Biến tập bài đã chọn thành một **ma trận** trích xuất có cấu trúc, rồi tổng hợp
(synthesis) theo **chủ đề** thay vì liệt kê từng tác giả. Ma trận vừa là công cụ
đọc có hệ thống, vừa là nguyên liệu để bước sau (`tim-khoang-trong`) phát hiện
khoảng trống.

## Khi Nào Dùng

- Khi đã có danh sách bài "Included" và cần đọc, rút thông tin theo cùng một khung.
- Khi chương tổng quan đang bị viết kiểu "tác giả A nói…, tác giả B nói…" và cần
  chuyển sang tổng hợp theo chủ đề.
- Khi cần một bảng để so sánh lý thuyết, phương pháp, biến, kết quả giữa nhiều bài.

## Nội Dung Chuyên Môn

### 1. Các cột chuẩn của ma trận trích xuất

| Cột | Nội dung rút ra | Mục đích |
|---|---|---|
| Tác giả – năm | Họ tác giả, năm xuất bản | Định danh, trích dẫn |
| Bối cảnh | Quốc gia, ngành, đối tượng | So sánh tính khái quát |
| Lý thuyết | Khung/lý thuyết nền (TAM, SDT, RBV…) | Nhóm theo nền lý thuyết |
| Mẫu | Cỡ mẫu, đặc điểm mẫu | Đánh giá độ mạnh bằng chứng |
| Phương pháp | Định lượng/định tính/hỗn hợp, công cụ, phân tích | So sánh thiết kế |
| Biến / khái niệm | Biến độc lập, phụ thuộc, trung gian, điều tiết | Lập bản đồ biến |
| Kết quả chính | Phát hiện cốt lõi, hướng và độ mạnh quan hệ | Tổng hợp pattern |
| Hạn chế / khoảng trống | Hạn chế tác giả nêu + khoảng trống quan sát được | Nuôi bước tìm gap |

### 2. Mẫu ma trận (điền dữ liệu thật từ bài)

| Tác giả-năm | Bối cảnh | Lý thuyết | Mẫu | Phương pháp | Biến | Kết quả chính | Khoảng trống |
|---|---|---|---|---|---|---|---|
| Nguyen 2023 | VN, ĐH | TAM | 412 SV | Định lượng, SEM | Nhận thức hữu ích → ý định dùng | Quan hệ dương, mạnh | Chưa xét biến điều tiết |
| Smith 2021 | Mỹ, ĐH | SDT | 28 SV | Định tính, phỏng vấn | Động lực tự chủ | Tăng gắn kết | Mẫu nhỏ, 1 trường |

### 3. Từ ma trận → tổng hợp theo chủ đề (synthesis)

Đừng viết theo từng dòng. Hãy **đọc dọc các cột** để rút chủ đề:

- **Nhóm theo cột Lý thuyết**: bao nhiêu bài dùng TAM, SDT, RBV? Khung nào thống trị?
- **Nhóm theo cột Kết quả**: các bài đồng thuận điều gì? Mâu thuẫn ở đâu?
- **Nhóm theo cột Bối cảnh / Phương pháp**: pattern có khác nhau giữa các bối cảnh
  hay thiết kế không?

Mỗi chủ đề viết theo khung 5 ý: (1) pattern chính, (2) bằng chứng ủng hộ (nhiều
nguồn), (3) kết quả mâu thuẫn, (4) điều kiện/bối cảnh làm kết quả đổi, (5) khoảng
trống còn lại.

### 4. Bảng đếm tần suất (concept count) — hỗ trợ synthesis

| Lý thuyết nền | Số bài dùng | Bài tiêu biểu |
|---|---|---|
| TAM | 7 | Nguyen 2023, … |
| SDT | 4 | Smith 2021, … |
| Chưa nêu lý thuyết | 5 | … |

Bảng đếm giúp thấy ngay khung nào bão hòa, khung nào còn ít — đầu vào trực tiếp
cho việc tìm khoảng trống.

## Quy Trình Các Bước

1. Nhận tập bài "Included" từ sub-skill `sang-loc-tai-lieu`.
2. Chốt bộ cột ma trận phù hợp đề tài (thêm/bớt cột nếu cần).
3. Đọc từng bài, rút thông tin vào đúng cột — chỉ ghi điều bài thật sự nói.
4. Đọc dọc các cột để rút chủ đề; lập bảng đếm tần suất lý thuyết/biến/phương pháp.
5. Viết tổng hợp theo chủ đề (mỗi chủ đề theo khung 5 ý), không liệt kê từng tác giả.
6. Đánh dấu các điểm mâu thuẫn và khoảng trống, bàn giao cho `tim-khoang-trong`.

## Đầu Ra

- Ma trận trích xuất đầy đủ các cột, dữ liệu rút từ bài thật.
- Bảng đếm tần suất lý thuyết/biến/phương pháp.
- Dàn ý tổng hợp theo chủ đề (thematic synthesis).
- Danh sách điểm mâu thuẫn và khoảng trống sơ bộ.

## Lưu Ý Liêm Chính

- Chỉ điền vào ma trận điều bài **thật sự** nêu; không suy diễn kết quả tác giả
  không khẳng định, không bịa cỡ mẫu hay biến.
- Tổng hợp theo chủ đề phải dựa trên **nhiều nguồn**; tránh "citation march" (mỗi
  câu một trích dẫn rời rạc mà không có lập luận tổng hợp).
- Giữ truy vết: mỗi ô trong ma trận nên gắn được với trang/đoạn trong bài gốc để
  kiểm tra lại khi cần.
