# Rà soát trích dẫn trong bản thảo

## Mục tiêu

Rà soát toàn bộ hệ thống trích dẫn của một bản thảo: đối chiếu in-text với danh mục
tài liệu (phát hiện thừa/thiếu), kiểm tra tính nhất quán định dạng, và phát hiện
nguồn không tồn tại hoặc do AI bịa. Trả về báo cáo lỗi có mức ưu tiên sửa.

## Khi nào dùng

- Người dùng có bản thảo hoàn chỉnh cần kiểm tra trước khi nộp.
- Cần đối chiếu in-text citation với reference list ở quy mô lớn.
- Nghi ngờ bản thảo chứa nguồn bịa (đặc biệt bản viết có hỗ trợ AI).

## Nội dung chuyên môn

### 1. Bốn loại lỗi đối chiếu in-text ↔ danh mục

| Loại lỗi | Mô tả | Cách phát hiện |
|---|---|---|
| Thiếu trong danh mục (orphan citation) | Trích trong bài nhưng không có mục tương ứng | Mỗi (Tác giả, Năm) phải tìm thấy ở danh mục |
| Thừa trong danh mục (uncited reference) | Có trong danh mục nhưng không trích trong bài | Mỗi mục danh mục phải xuất hiện ≥1 lần trong bài |
| Lệch tên/năm | Họ tác giả hoặc năm khác nhau giữa hai nơi | So khớp chính xác họ + năm |
| Trùng/mơ hồ | Cùng tác giả cùng năm chưa phân biệt a/b/c | Kiểm tra hậu tố năm khi có nhiều bài |

### 2. Quy trình đối chiếu hai chiều

1. Quét toàn văn, lập **danh sách A** = mọi in-text citation (chuẩn hóa về dạng
   `Họ + Năm`, gộp `et al.`).
2. Lập **danh sách B** = mọi mục trong reference list.
3. `A \ B` = trích dẫn thiếu mục danh mục (lỗi nghiêm trọng — phải sửa).
4. `B \ A` = mục danh mục không được trích (cân nhắc xóa hoặc bổ sung trích dẫn).
5. Với phần giao A ∩ B: kiểm tra khớp năm, chính tả tên, hậu tố a/b/c.

### 3. Kiểm tra nhất quán định dạng

- Một chuẩn duy nhất trong toàn văn (APA / Chicago / Vancouver...), không trộn lẫn.
- Dấu `&` vs "và"/"and" dùng nhất quán theo chuẩn.
- Cách viết hoa tiêu đề (sentence case / title case) nhất quán theo loại tài liệu.
- In nghiêng tên tạp chí/sách áp dụng đồng đều.
- Định dạng DOI thống nhất (`https://doi.org/...`).
- Thứ tự sắp xếp danh mục: đúng bảng chữ cái theo họ tác giả.

### 4. Phát hiện nguồn bịa / không tồn tại

Cờ đỏ cần kiểm tra kỹ:

- DOI không phân giải được (chuyển sang sub-skill `kiem-tra-doi`).
- Trang/tập/số không hợp lý (ví dụ tạp chí chỉ có 4 số/năm nhưng ghi số 11).
- Tổ hợp tác giả + tạp chí + năm không tra được trên Crossref/Google Scholar.
- Tiêu đề "quá khớp" với câu trong bài thảo — dấu hiệu AI tự chế.
- Tên tạp chí gần giống nhưng không tồn tại (biến thể của tạp chí thật).

### 5. Bảng checklist audit

| Hạng mục | Kết quả | Mức ưu tiên |
|---|---|---|
| Trích dẫn thiếu mục danh mục | __ trường hợp | Cao |
| Mục danh mục không được trích | __ trường hợp | Trung bình |
| Lệch tên/năm in-text vs danh mục | __ trường hợp | Cao |
| Sai/trộn chuẩn định dạng | __ trường hợp | Trung bình |
| DOI không xác minh được | __ trường hợp | Cao |
| Nguồn nghi bịa | __ trường hợp | Cao nhất |
| Thiếu hậu tố a/b/c khi trùng | __ trường hợp | Thấp |

## Quy trình các bước

1. Nhận bản thảo + danh mục; xác nhận chuẩn trích dẫn áp dụng.
2. Trích danh sách A (in-text) và danh sách B (danh mục).
3. Đối chiếu hai chiều, lập bảng thừa/thiếu/lệch.
4. Kiểm tra nhất quán định dạng theo mục 3.
5. Quét cờ đỏ nguồn bịa; chuyển DOI nghi ngờ sang `kiem-tra-doi`.
6. Tổng hợp báo cáo audit + mức ưu tiên sửa.

## Đầu ra

- Bảng đối chiếu in-text ↔ danh mục (thừa/thiếu/lệch).
- Báo cáo lỗi định dạng và đề xuất chuẩn hóa.
- Danh sách nguồn nghi bịa kèm lý do và bước xác minh.
- Checklist audit đã điền số liệu, sắp theo mức ưu tiên.

## Lưu ý liêm chính

- Không tự "vá" lỗi bằng cách bịa thêm mục danh mục hay đoán năm/tác giả.
- Mọi nguồn nghi bịa phải được nêu rõ, không âm thầm bỏ qua hay hợp thức hóa.
- Phân biệt rõ "lỗi chắc chắn" và "điểm cần người dùng/giảng viên xác nhận".
- Kết quả audit dùng tiếp được trong skill chính `citation-manager`.
