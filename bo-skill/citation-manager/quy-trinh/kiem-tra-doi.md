# Kiểm tra DOI và nguồn thật

## Mục tiêu

Xác minh một DOI/nguồn có thật hay không, đối chiếu dữ liệu thư mục (tác giả, năm,
tiêu đề, tạp chí) với bản ghi chính thức, và phát hiện DOI giả/sai định dạng — đặc
biệt DOI do AI bịa. Nguyên tắc cốt lõi: **không bao giờ đoán DOI**.

## Khi nào dùng

- Có DOI cần kiểm tra trước khi đưa vào danh mục.
- Nghi ngờ một nguồn không tồn tại hoặc dữ liệu thư mục mâu thuẫn.
- Nhận danh sách tài liệu từ nguồn không rõ ràng (AI sinh, chép tay, tổng hợp).

## Nội dung chuyên môn

### 1. Cấu trúc DOI hợp lệ

DOI có dạng: `10.<prefix>/<suffix>`

- Luôn bắt đầu bằng `10.`
- **Prefix**: ít nhất 4 chữ số sau `10.` (ví dụ `10.1108`, `10.1016`), định danh
  nhà xuất bản đăng ký với Crossref/DataCite.
- **Suffix**: chuỗi do nhà xuất bản đặt, phân biệt hoa thường, có thể chứa chữ, số,
  dấu chấm, gạch ngang.
- URL phân giải chuẩn: `https://doi.org/10.xxxx/xxxxx`

### 2. Cách tra DOI thật

| Cách | Thao tác | Dùng để |
|---|---|---|
| doi.org | Mở `https://doi.org/<DOI>` — phải chuyển tới trang bài thật | Xác nhận DOI phân giải được |
| Crossref API | `https://api.crossref.org/works/<DOI>` trả về JSON metadata | Lấy/đối chiếu tác giả, năm, tiêu đề, tạp chí |
| Crossref search | `https://search.crossref.org` tìm theo tiêu đề | Tìm DOI khi chỉ có tiêu đề |
| DataCite | `https://api.datacite.org/dois/<DOI>` | DOI của dataset, kho dữ liệu |

Khi có công cụ truy cập web, gọi Crossref và **so từng trường** trả về với dữ liệu
người dùng cung cấp. Nếu không có công cụ, **không tự khẳng định** DOI đúng — đánh
dấu `[Cần người dùng tự mở doi.org để xác minh]`.

### 3. Dấu hiệu DOI giả / nghi bịa

- Không phân giải được khi mở `https://doi.org/<DOI>` (lỗi "DOI Not Found").
- Sai định dạng: không bắt đầu bằng `10.`, prefix dưới 4 chữ số, có khoảng trắng.
- Suffix "đẹp bất thường": trùng khít tiêu đề bằng tiếng Anh, đánh số tuần tự
  `.001`, `.002` do AI chế ra.
- Metadata Crossref trả về tiêu đề/tác giả/năm **khác hẳn** nguồn người dùng đưa.
- DOI gắn với nhà xuất bản không khớp tạp chí (ví dụ tạp chí Elsevier nhưng prefix
  của nhà xuất bản khác).

### 4. Quy tắc "không đoán DOI"

- Tuyệt đối không tự sinh DOI từ tiêu đề, tên tạp chí hay năm.
- Không "sửa" DOI lỗi bằng cách suy đoán; chỉ tra lại từ Crossref/doi.org.
- Nếu không tìm thấy DOI, để trống và ghi `[Không có DOI / chưa xác minh được]`,
  giữ phần còn lại của trích dẫn.

### 5. Checklist xác minh một nguồn

| Mục kiểm tra | Đạt? |
|---|---|
| DOI bắt đầu bằng `10.` và đúng cấu trúc prefix/suffix | ☐ |
| `https://doi.org/<DOI>` phân giải tới đúng bài | ☐ |
| Tác giả khớp metadata Crossref | ☐ |
| Năm xuất bản khớp | ☐ |
| Tiêu đề khớp (không lệch nghĩa) | ☐ |
| Tên tạp chí / nhà xuất bản khớp | ☐ |
| Không có dấu hiệu DOI bịa | ☐ |

## Quy trình các bước

1. Chuẩn hóa DOI: bỏ tiền tố `https://doi.org/`, khoảng trắng, dấu câu thừa.
2. Kiểm tra cấu trúc định dạng (`10.` + prefix ≥ 4 số + suffix).
3. Phân giải qua doi.org; nếu lỗi → đánh dấu nghi giả.
4. Lấy metadata Crossref, đối chiếu từng trường với dữ liệu người dùng.
5. Ghi trạng thái: `Đã xác minh` / `Lệch dữ liệu` / `Không tìm thấy` / `Sai định dạng`.
6. Trả bảng kết quả; với nguồn nghi bịa, đề xuất tìm nguồn thay thế đáng tin.

## Đầu ra

- Bảng xác minh: DOI | tiêu đề | tác giả | năm | nguồn | trạng thái.
- Danh sách DOI nghi giả/sai định dạng kèm lý do.
- Đề xuất bước tiếp theo (tìm bản gốc, thay nguồn, để trống có ghi chú).

## Lưu ý liêm chính

- Không đoán, không bịa, không "đánh bóng" DOI cho đủ bộ.
- Khi không có công cụ truy cập, nói rõ giới hạn và yêu cầu người dùng tự xác minh.
- Một nguồn không xác minh được vẫn phải được đánh dấu, không âm thầm đưa vào danh mục.
- Cảnh báo người dùng về rủi ro nguồn do AI bịa trong các bản thảo tổng hợp tự động.
