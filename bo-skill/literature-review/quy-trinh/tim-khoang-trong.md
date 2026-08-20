# Phát hiện khoảng trống nghiên cứu từ ma trận tài liệu

## Mục Tiêu

Từ ma trận tổng hợp tài liệu, phát hiện khoảng trống nghiên cứu **có căn cứ**
(không phán đoán mơ hồ) và phát biểu thành gap statement dẫn thẳng tới câu hỏi
nghiên cứu. Sub-skill này tập trung vào tổng hợp **từ ma trận**; nó bổ trợ cho
`critical-review/tim-research-gap` nhưng lấy bằng chứng trực tiếp từ các cột của
ma trận tài liệu.

## Khi Nào Dùng

- Khi đã có ma trận tổng hợp và bảng đếm tần suất, cần rút ra khoảng trống.
- Khi cần biện minh "tại sao đề tài này đáng làm" bằng bằng chứng từ tài liệu.
- Khi cần chuyển khoảng trống thành câu hỏi/mục tiêu nghiên cứu cụ thể.

## Nội Dung Chuyên Môn

### 1. Đọc ma trận theo 6 loại khoảng trống

Mỗi loại gap soi vào một (vài) cột cụ thể của ma trận:

| Loại khoảng trống | Soi cột nào trong ma trận | Câu hỏi kiểm tra |
|---|---|---|
| Lý thuyết | Lý thuyết nền | Khung nào chưa được áp dụng/tích hợp? |
| Bối cảnh | Bối cảnh (quốc gia, ngành) | Bối cảnh VN/ngành cụ thể nào còn thiếu? |
| Phương pháp | Phương pháp, mẫu | Thiết kế nào chưa thử (dọc, hỗn hợp…)? Mẫu nào còn thiếu? |
| Biến | Biến/khái niệm | Biến trung gian/điều tiết/kết quả nào bị bỏ qua? |
| Mâu thuẫn kết quả | Kết quả chính | Các bài cho kết quả trái ngược chưa được giải thích? |
| Thời gian | Bối cảnh + năm | Bối cảnh mới (ví dụ AI tạo sinh) làm kết quả cũ cần kiểm lại? |

### 2. Bốn dấu hiệu khoảng trống đọc được trực tiếp từ ma trận

1. **Ô trống / cột thưa**: một loại bối cảnh, biến hoặc phương pháp gần như không
   xuất hiện trong cột tương ứng → khoảng trống tiềm năng.
2. **Mâu thuẫn kết quả**: cùng quan hệ, bài A dương, bài B âm/không ý nghĩa, chưa
   ai giải thích điều kiện ranh giới → gap về điều tiết/bối cảnh.
3. **Thiếu bối cảnh Việt Nam**: bảng đếm cho thấy phần lớn bằng chứng đến từ bối
   cảnh phương Tây, rất ít hoặc không có dữ liệu VN.
4. **Bão hòa một phía**: một khung lý thuyết hoặc một thiết kế lặp lại quá nhiều,
   các hướng khác chưa được thử.

### 3. Mẫu bảng tổng hợp khoảng trống (bằng chứng → gap)

| Loại gap | Bằng chứng từ ma trận | Phát biểu khoảng trống |
|---|---|---|
| Bối cảnh | 11/12 bài ở Mỹ/EU, 0 bài VN | Chưa có bằng chứng về quan hệ X–Y trong bối cảnh ĐH Việt Nam |
| Biến | Không bài nào xét vai trò điều tiết của Z | Vai trò điều tiết của Z trong quan hệ X–Y chưa được kiểm định |
| Mâu thuẫn | Nguyen 2023 dương, Smith 2021 không ý nghĩa | Điều kiện làm quan hệ X–Y thay đổi chưa được làm rõ |

### 4. Từ gap → câu hỏi nghiên cứu

Mỗi gap statement nên đẻ ra ít nhất một câu hỏi nghiên cứu cụ thể:

```text
Khoảng trống: Vai trò điều tiết của Z trong quan hệ X–Y chưa được kiểm định,
              đặc biệt trong bối cảnh đại học Việt Nam.
→ Câu hỏi NC: Biến Z có điều tiết quan hệ giữa X và Y ở sinh viên đại học
              Việt Nam hay không, và theo chiều nào?
```

### 5. Khung viết đoạn "khoảng trống" trong luận án

1. Tài liệu đã làm được gì (tóm tắt đồng thuận, dẫn nhiều nguồn).
2. Còn thiếu/mâu thuẫn ở đâu (gap, kèm bằng chứng từ ma trận).
3. Vì sao khoảng trống đó quan trọng (đóng góp lý thuyết/thực tiễn).
4. Đề tài này lấp khoảng trống bằng cách nào (câu hỏi/mục tiêu nghiên cứu).

## Quy Trình Các Bước

1. Nhận ma trận, bảng đếm tần suất và danh sách mâu thuẫn từ `ma-tran-tai-lieu`.
2. Soi từng loại trong 6 loại khoảng trống vào cột tương ứng của ma trận.
3. Quét 4 dấu hiệu (ô trống, mâu thuẫn, thiếu bối cảnh VN, bão hòa một phía).
4. Lập bảng tổng hợp khoảng trống: gắn mỗi gap với bằng chứng cụ thể.
5. Chuyển mỗi gap thành câu hỏi/mục tiêu nghiên cứu.
6. Viết đoạn "khoảng trống" theo khung 4 ý cho chương tổng quan.

## Đầu Ra

- Bảng tổng hợp khoảng trống (loại gap, bằng chứng từ ma trận, phát biểu gap).
- Tập câu hỏi/mục tiêu nghiên cứu suy ra từ các gap.
- Đoạn văn "khoảng trống nghiên cứu" cho chương 2.

## Lưu Ý Liêm Chính

- Mỗi khoảng trống phải gắn với **bằng chứng thật** từ ma trận; không phát biểu
  "chưa ai nghiên cứu" nếu thực ra chỉ là chưa tìm thấy do search còn hẹp.
- Phân biệt "thiếu trong tập bài đã chọn" với "thiếu trong toàn bộ y văn"; nếu
  phạm vi tìm kiếm hạn chế, ghi rõ để tránh thổi phồng gap.
- Không biến mong muốn cá nhân thành gap; gap phải đứng vững trước phản biện của
  giảng viên dựa trên tài liệu đã tổng hợp.
