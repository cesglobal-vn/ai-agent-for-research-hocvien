# Dự đoán câu hỏi hội đồng

## Mục tiêu

Giúp nghiên cứu sinh xây dựng một ngân hàng câu hỏi mà hội đồng có thể đặt ra, phân
theo nhóm chủ đề, kèm cách chuẩn bị câu trả lời và nhận diện các câu hỏi "bẫy" thường
gặp. Mục đích là không bị bất ngờ tại buổi bảo vệ và luôn có sẵn một phác thảo câu
trả lời cho mọi hướng truy vấn.

## Khi nào dùng

- Trước buổi bảo vệ đề cương, pre-defense hoặc bảo vệ chính thức.
- Khi muốn rà soát những điểm yếu nhất của luận án dưới góc nhìn phản biện.
- Khi cần luyện tập mock viva và cần nguồn câu hỏi đầu vào.

## Nội dung chuyên môn

### Ngân hàng câu hỏi theo nhóm

**Nhóm 1 — Lý do chọn đề tài & tính cấp thiết**
- Vì sao anh/chị chọn đề tài này? Nó quan trọng với ai?
- Nếu chỉ thay bối cảnh sang Việt Nam thì có đủ mới không?
- Đề tài này giải quyết vấn đề thực tiễn hay chỉ lý thuyết?

**Nhóm 2 — Đóng góp mới (gap & contribution)**
- Khoảng trống nghiên cứu chính xác là gì? Ai đã làm gần nhất?
- Đóng góp lý thuyết và đóng góp thực tiễn của luận án là gì?
- Nếu bỏ một chương đi, kết luận có còn đứng vững không?

**Nhóm 3 — Phương pháp**
- Vì sao chọn định lượng/định tính/hỗn hợp?
- Mẫu có đại diện không? Cỡ mẫu đủ chưa? Tính theo cách nào?
- Độ tin cậy, độ giá trị (validity/reliability) được đảm bảo ra sao?
- Đã xử lý sai lệch do phương pháp chung (common method bias) chưa?

**Nhóm 4 — Kết quả & diễn giải**
- Vì sao giả thuyết này không được ủng hộ?
- Effect size có ý nghĩa thực tiễn không, hay chỉ có ý nghĩa thống kê?
- Kết quả có khái quát hóa được không?

**Nhóm 5 — Hạn chế & hướng tương lai**
- Hạn chế lớn nhất của nghiên cứu là gì?
- Nếu làm lại, anh/chị thay đổi điều gì?

**Nhóm 6 — Đạo đức nghiên cứu**
- Quy trình thu thập dữ liệu có được chấp thuận đạo đức không?
- Dữ liệu người tham gia được bảo mật và ẩn danh thế nào?

**Nhóm 7 — Sử dụng AI**
- Anh/chị có dùng AI trong nghiên cứu không? Dùng cho phần nào?
- Có kiểm tra lại nguồn do AI gợi ý không?
- Dữ liệu có đưa vào công cụ AI không, đã ẩn danh chưa?

### Cách chuẩn bị câu trả lời

| Bước | Việc làm |
|---|---|
| 1 | Phân loại mỗi câu hỏi: dễ / trung bình / nguy hiểm |
| 2 | Viết phác thảo trả lời 3-4 câu cho mỗi câu nguy hiểm |
| 3 | Gắn mỗi câu trả lời với một slide backup hoặc bảng số liệu |
| 4 | Tập nói thành tiếng, bấm giờ dưới 90 giây/câu |

### Câu hỏi "bẫy" thường gặp

- "Đóng góp của em chỉ là lặp lại nghiên cứu cũ ở bối cảnh khác đúng không?" — bẫy
  hạ thấp; trả lời bằng đóng góp lý thuyết cụ thể, không phòng thủ.
- "Nếu kết quả ngược lại thì em giải thích thế nào?" — bẫy kiểm tra độ hiểu cơ chế.
- "Em tự làm hay AI làm phần này?" — bẫy liêm chính; trả lời trung thực, rõ phạm vi.
- Câu hỏi dồn: hội đồng hỏi liên tiếp để xem có lúng túng không. Giữ bình tĩnh, xin
  phép trả lời từng ý.

## Quy trình các bước

1. Thu thập tóm tắt luận án và các điểm yếu đã biết.
2. Sinh câu hỏi theo từng nhóm 1–7, ưu tiên nhóm khớp đặc thù đề tài.
3. Đánh dấu mức độ nguy hiểm cho từng câu hỏi.
4. Viết phác thảo câu trả lời cho mọi câu nguy hiểm và câu bẫy.
5. Gắn câu trả lời với slide backup tương ứng.
6. Bàn giao danh sách cho mock viva để luyện tập.

## Đầu ra

- Ngân hàng câu hỏi phân theo 7 nhóm, có gắn mức độ nguy hiểm.
- Phác thảo câu trả lời cho các câu nguy hiểm và câu bẫy.
- Danh sách câu hỏi cần luyện thêm để chuyển sang skill `luyen-tra-loi`.
- Gợi ý lưu kết quả vào `kho-tri-thuc/outputs` nếu là sản phẩm quan trọng.

## Lưu ý liêm chính

- Câu hỏi và câu trả lời phải dựa trên nội dung luận án thật, không tô vẽ kết quả.
- Với câu hỏi về AI và đạo đức, chuẩn bị câu trả lời trung thực — không che giấu phạm
  vi đã sử dụng công cụ.
- Không bịa số liệu hay trích dẫn để "đỡ" câu hỏi khó; nếu chưa chắc, hãy thừa nhận
  và nêu hướng kiểm tra.
- Mọi câu hỏi/đáp do AI gợi ý cần được nghiên cứu sinh đối chiếu với luận án thật.
