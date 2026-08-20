# Lập cấu trúc slide bảo vệ

## Mục tiêu

Giúp nghiên cứu sinh dựng dàn ý bộ slide bảo vệ mạch lạc: đi từ mở đầu, tổng quan,
khoảng trống, câu hỏi nghiên cứu, phương pháp, kết quả, đóng góp đến hạn chế, với số
lượng slide hợp lý theo thời lượng và tuân thủ nguyên tắc một ý một slide. Bộ slide
là công cụ hỗ trợ thị giác, không phải bản thảo để đọc nguyên văn.

## Khi nào dùng

- Khi bắt đầu làm slide bảo vệ từ con số 0.
- Khi đã có slide nhưng bị nhận xét rối, quá nhiều chữ, hoặc lệch thời gian.
- Khi cần quyết định nội dung nào để slide chính, nội dung nào để slide dự phòng.

## Nội dung chuyên môn

### Khung cấu trúc bộ slide

| Phần | Nội dung slide | Số slide gợi ý |
|---|---|---|
| Mở đầu | Tiêu đề, thông tin NCS, dàn ý trình bày | 2 |
| Tổng quan & động cơ | Bối cảnh, vì sao quan trọng | 1–2 |
| Khoảng trống | Tổng quan tài liệu rút gọn → gap | 1–2 |
| Câu hỏi & mục tiêu | Câu hỏi nghiên cứu, mục tiêu, giả thuyết | 1–2 |
| Khung lý thuyết | Mô hình nghiên cứu, biến số | 1–2 |
| Phương pháp | Thiết kế, mẫu, đo lường, phân tích | 2–3 |
| Kết quả | Kết quả chính theo từng câu hỏi | 3–5 |
| Đóng góp & hàm ý | Đóng góp lý thuyết và thực tiễn | 1–2 |
| Hạn chế & tương lai | Hạn chế, hướng nghiên cứu tiếp | 1 |
| Kết luận | Chốt thông điệp, lời cảm ơn | 1 |

### Số slide hợp lý theo thời lượng

Quy tắc thô: trung bình 1–1,5 phút cho mỗi slide nội dung.

| Thời lượng | Tổng số slide chính | Số slide backup |
|---|---|---|
| 15 phút | 12–15 | 5–8 |
| 20 phút | 15–20 | 8–12 |
| 30 phút | 20–28 | 10–15 |

### Nguyên tắc thiết kế

- **Một ý một slide**: mỗi slide chỉ truyền một thông điệp duy nhất.
- Tiêu đề slide viết thành câu khẳng định (thông điệp), không phải nhãn ("Kết quả H1
  được ủng hộ" thay vì "Kết quả").
- Ưu tiên sơ đồ, bảng tóm tắt, biểu đồ hơn là đoạn văn dài.
- Kết quả chính phải có con số, không chỉ mô tả định tính.
- Cỡ chữ đủ lớn để đọc từ cuối phòng; hạn chế dưới 6 dòng/slide.

### Slide dự phòng (backup)

Đặt sau slide kết luận, dùng để trả lời câu hỏi sâu của hội đồng:
- Bảng kết quả đầy đủ, kiểm định độ vững (robustness).
- Chi tiết thang đo, nguồn câu hỏi, quy trình dịch ngược.
- Phê duyệt đạo đức và tuyên bố sử dụng AI.
- Các phân tích phụ chưa đưa vào phần chính.

## Quy trình các bước

1. Xác định thời lượng và tính tổng số slide mục tiêu theo bảng trên.
2. Phân bổ số slide cho từng phần theo khung cấu trúc.
3. Viết tiêu đề dạng thông điệp khẳng định cho mỗi slide.
4. Chọn dạng trình bày (sơ đồ/bảng/biểu đồ) cho từng slide nội dung.
5. Tách phần chi tiết, bảng đầy đủ sang nhóm slide backup.
6. Rà lại nguyên tắc một ý một slide và bấm giờ thử.

## Đầu ra

- Dàn ý bộ slide với tiêu đề từng slide và dạng trình bày đề xuất.
- Bảng phân bổ số slide theo thời lượng.
- Danh sách slide dự phòng kèm mục đích.
- Gợi ý lưu kết quả vào `kho-tri-thuc/outputs` nếu là sản phẩm quan trọng.

## Lưu ý liêm chính

- Biểu đồ và bảng trên slide phải phản ánh đúng dữ liệu thật; không cắt trục hay làm
  đẹp số liệu gây hiểu sai.
- Không che giấu hạn chế bằng cách bỏ slide; hãy có một slide hạn chế trung thực.
- Tuyên bố sử dụng AI nên có sẵn trong slide backup nếu nghiên cứu có dùng công cụ AI.
- Nội dung slide do AI gợi ý cần được NCS kiểm tra lại trước khi trình bày.
