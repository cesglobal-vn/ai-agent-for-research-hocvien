# Lập bản đồ lập luận luận án

## Mục tiêu

Giúp nghiên cứu sinh dựng một bản đồ lập luận (argument map) cho toàn bộ luận án:
mỗi luận điểm chính được chống đỡ bằng bằng chứng, có dự liệu phản biện và câu trả
lời, đồng thời liên kết thành một mạch nhất quán giữa câu hỏi nghiên cứu, giả thuyết,
kết quả và kết luận. Mục đích cuối cùng là khi hội đồng truy vấn bất kỳ điểm nào,
người bảo vệ luôn lần ngược được về logic gốc.

## Khi nào dùng

- Khi cần kiểm tra tính nhất quán giữa các chương trước khi bảo vệ.
- Khi sợ bị hỏi "phần này liên quan gì đến câu hỏi nghiên cứu của anh/chị?".
- Khi một giả thuyết không được ủng hộ và cần chuẩn bị cách giải thích logic.
- Khi viết phần Thảo luận hoặc Kết luận và cần đảm bảo mọi kết luận đều có gốc.

## Nội dung chuyên môn

### Cấu trúc một đơn vị lập luận

Mỗi luận điểm gồm bốn thành phần. Hãy dựng theo khung sau cho từng luận điểm:

```text
LUẬN ĐIỂM (Claim): [Phát biểu khẳng định cần bảo vệ]
  └─ BẰNG CHỨNG (Evidence): [Dữ liệu, kết quả phân tích, trích dẫn tài liệu nền]
  └─ LẬP LUẬN NỀN (Warrant): [Vì sao bằng chứng này dẫn tới luận điểm]
  └─ PHẢN BIỆN DỰ LIỆU (Rebuttal): [Hội đồng có thể bắt bẻ điều gì?]
  └─ TRẢ LỜI PHẢN BIỆN (Response): [Cách bảo vệ hoặc thừa nhận có điều kiện]
```

### Mạch nhất quán xuyên suốt luận án

Lập bảng "đường truyền logic" để kiểm tra mỗi mắt xích đều khớp:

| Câu hỏi NC | Giả thuyết | Phương pháp kiểm định | Kết quả | Kết luận tương ứng |
|---|---|---|---|---|
| CH1 |  |  |  |  |
| CH2 |  |  |  |  |
| CH3 |  |  |  |  |

Quy tắc kiểm tra: mỗi hàng phải đọc được trọn vẹn từ trái sang phải. Nếu có ô trống,
hoặc kết luận không truy được về câu hỏi nghiên cứu, đó là điểm yếu hội đồng dễ khai
thác.

### Bản đồ tổng (sơ đồ cây)

```text
VẤN ĐỀ NGHIÊN CỨU
   │
   ├─ KHOẢNG TRỐNG (Gap): điều giới học thuật chưa biết
   │
   ├─ CÂU HỎI NGHIÊN CỨU: CH1, CH2, CH3
   │      │
   │      └─ GIẢ THUYẾT/MỆNH ĐỀ: H1, H2, H3
   │             │
   │             └─ KHUNG LÝ THUYẾT: cơ chế giải thích
   │                    │
   │                    └─ PHƯƠNG PHÁP: cách kiểm định
   │                           │
   │                           └─ KẾT QUẢ: ủng hộ / không ủng hộ
   │                                  │
   │                                  └─ ĐÓNG GÓP: lý thuyết + thực tiễn
   │
   └─ KẾT LUẬN: trả lời lại đúng câu hỏi đã đặt ra ban đầu
```

### Xử lý giả thuyết không được ủng hộ

Khi H bị bác, không bỏ trống mà chuẩn bị ba hướng giải thích: (1) điều kiện biên/bối
cảnh, (2) vấn đề đo lường hoặc cỡ mẫu, (3) lý thuyết cần được điều chỉnh. Mỗi hướng
ghi một câu trả lời sẵn.

## Quy trình các bước

1. Liệt kê toàn bộ luận điểm chính (thường 3-6) mà luận án khẳng định.
2. Với mỗi luận điểm, điền đủ bốn thành phần Claim–Evidence–Warrant–Response.
3. Dựng bảng "đường truyền logic" và kiểm tra từng hàng đọc trọn vẹn.
4. Vẽ sơ đồ cây tổng để thấy mọi nhánh đều quy về câu hỏi và kết luận.
5. Đánh dấu mắt xích yếu (ô trống, kết luận vượt quá dữ liệu) và chuẩn bị câu trả lời.
6. Đối chiếu kết luận cuối với câu hỏi gốc: chúng phải trả lời đúng nhau.

## Đầu ra

- Một sơ đồ cây lập luận của toàn luận án.
- Bảng "đường truyền logic" Câu hỏi → Giả thuyết → Phương pháp → Kết quả → Kết luận.
- Danh sách mắt xích yếu kèm câu trả lời phòng thủ đã chuẩn bị.
- Gợi ý lưu kết quả vào `kho-tri-thuc/outputs` nếu là sản phẩm quan trọng.

## Lưu ý liêm chính

- Bản đồ lập luận phải phản ánh đúng dữ liệu thật; không "kéo" kết luận vượt quá
  bằng chứng để nghe thuyết phục hơn.
- Không bịa trích dẫn hay tài liệu nền để lấp chỗ trống lập luận warrant.
- Khi một giả thuyết không được ủng hộ, trình bày trung thực thay vì che giấu hay
  diễn giải lại dữ liệu cho khớp.
- Mọi nội dung do AI gợi ý đều phải được nghiên cứu sinh kiểm chứng lại trước khi đưa
  vào luận án.
