# Chọn mẫu và cỡ mẫu

## Mục tiêu

Giúp học viên chọn phương pháp chọn mẫu phù hợp với tổng thể và khả năng tiếp cận,
xác định cỡ mẫu có căn cứ thống kê (ưu tiên phân tích sức mạnh), và nhận diện các
rủi ro sai lệch để thừa nhận trong luận án.

## Khi nào dùng

- Khi cần quyết định khảo sát/phỏng vấn ai, theo cách chọn nào.
- Khi cần biện luận cỡ mẫu trước hội đồng, không chỉ ghi một con số theo kinh nghiệm.
- Khi dùng SEM (CB-SEM hoặc PLS-SEM) và cần tính cỡ mẫu cho đúng.
- Khi nghiên cứu định tính và cần xác định khi nào dừng thu thập dữ liệu.

## Nội dung chuyên môn

### 1. Phương pháp chọn mẫu

| Nhóm | Phương pháp | Khi dùng | Rủi ro chính |
|---|---|---|---|
| Xác suất | Ngẫu nhiên đơn | Có khung mẫu đầy đủ | Khó có danh sách đầy đủ |
| Xác suất | Hệ thống | Có danh sách sắp xếp, chọn theo bước k | Sai lệch nếu danh sách có chu kỳ |
| Xác suất | Phân tầng | Cần đại diện các nhóm con | Cần biết tỷ lệ từng tầng |
| Xác suất | Cụm | Mẫu theo trường, công ty, vùng | Hiệu ứng thiết kế (design effect) |
| Phi xác suất | Thuận tiện | Khó tiếp cận, nguồn lực hạn chế | Sai lệch cao, hạn chế suy rộng |
| Phi xác suất | Phán đoán (purposive) | Cần đúng nhóm chuyên biệt | Phụ thuộc đánh giá chủ quan |
| Phi xác suất | Quả cầu tuyết | Nhóm khó tiếp cận, ẩn | Sai lệch mạng lưới |
| Phi xác suất | Hạn ngạch (quota) | Cần đủ tỷ lệ theo nhóm nhưng không ngẫu nhiên | Không suy rộng thống kê được |

Chọn mẫu xác suất cho phép suy rộng thống kê; chọn mẫu phi xác suất thì phải thừa
nhận giới hạn về tính đại diện trong phần hạn chế của nghiên cứu.

### 2. Cỡ mẫu cho định lượng

Nguyên tắc: ưu tiên phân tích sức mạnh (power analysis) bằng phần mềm như G\*Power,
khai báo rõ mức ý nghĩa (alpha, thường 0,05), sức mạnh (power, thường 0,80) và cỡ
hiệu ứng (effect size) dự kiến.

| Kỹ thuật phân tích | Cách xác định cỡ mẫu |
|---|---|
| Khảo sát mô tả tổng thể | Công thức Cochran hoặc phân tích sức mạnh |
| Hồi quy bội | G\*Power theo số biến độc lập, alpha, power, effect size |
| ANOVA | G\*Power theo số nhóm và cỡ hiệu ứng |
| CB-SEM | Thường cần N ≥ 200 và mô hình không quá phức tạp |
| PLS-SEM | Dùng phân tích sức mạnh; xem cảnh báo bên dưới |

> Cảnh báo về "quy tắc 10 lần" (10-times rule) trong PLS-SEM: đây chỉ là heuristic
> rất yếu (lấy 10 lần số mũi tên lớn nhất chỉ vào một biến tiềm ẩn). Nó thường ước
> lượng thiếu cỡ mẫu cần thiết. Hãy ưu tiên phân tích sức mạnh thực sự thay vì dựa
> vào quy tắc này.

### 3. Cỡ mẫu cho định tính: bão hòa lý thuyết

Định tính không tính cỡ mẫu bằng công thức thống kê. Dừng thu thập khi đạt bão hòa
lý thuyết (theoretical saturation): khi các cuộc phỏng vấn/quan sát mới không còn
tạo ra mã, chủ đề hay hiểu biết mới. Khoảng tham khảo: phỏng vấn sâu thường 12–30
người tùy độ đồng nhất của mẫu, nhưng phải biện luận bằng bão hòa chứ không bằng con số.

## Quy trình các bước

1. Xác định tổng thể nghiên cứu (population) và khung mẫu (sampling frame) nếu có.
2. Chọn phương pháp chọn mẫu từ bảng trên, ghi rõ lý do và giới hạn tiếp cận.
3. Với định lượng: chạy G\*Power hoặc công thức phù hợp; ghi alpha, power, effect size.
4. Với định tính: đặt tiêu chí bão hòa và khoảng số người tham gia dự kiến.
5. Dự trù tỷ lệ không phản hồi/mất mẫu và cộng thêm vào cỡ mẫu kế hoạch.
6. Liệt kê các rủi ro sai lệch tương ứng để đưa vào phần hạn chế.

## Đầu ra

- Bảng kế hoạch chọn mẫu: phương pháp, tổng thể, tiêu chí chọn.
- Cỡ mẫu có căn cứ (kèm tham số G\*Power hoặc lý do bão hòa).
- Danh sách rủi ro sai lệch và cách giảm thiểu.

## Lưu ý liêm chính

- Không ghi cỡ mẫu theo cảm tính rồi gán lý do sau; căn cứ phải có trước con số.
- Không che giấu chọn mẫu thuận tiện thành "đại diện"; phải thừa nhận giới hạn.
- Không dùng "quy tắc 10 lần" như bằng chứng đủ mẫu; nêu rõ đây là heuristic yếu.
- Đánh dấu mọi con số cần giảng viên hoặc chuyên gia thống kê xác nhận lại.
