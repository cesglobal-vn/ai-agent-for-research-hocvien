# Sàng lọc tài liệu theo quy trình PRISMA

## Mục Tiêu

Đưa tập kết quả tìm kiếm thô đi qua quy trình sàng lọc PRISMA 2020 minh bạch:
xây tiêu chí chọn/loại trước, sàng lọc 2 vòng (tiêu đề–abstract rồi full-text),
ghi lý do loại, và lập sơ đồ PRISMA flow để chứng minh số bài đưa vào tổng hợp.

## Khi Nào Dùng

- Khi đã có số kết quả từ các CSDL và cần lọc xuống tập bài cuối cùng để đọc sâu.
- Khi cần xây bộ tiêu chí inclusion/exclusion trước khi sàng lọc.
- Khi cần dựng PRISMA flow diagram cho luận án hoặc bài báo systematic/scoping review.

## Nội Dung Chuyên Môn

### 1. Bốn giai đoạn PRISMA 2020

| Giai đoạn | Việc làm | Số cần ghi |
|---|---|---|
| Identification | Gom records từ CSDL + nguồn khác; gỡ trùng | N tìm được, N trùng đã gỡ |
| Screening | Đọc tiêu đề + abstract theo tiêu chí | N sàng lọc, N loại ở vòng 1 |
| Eligibility | Đọc full-text theo tiêu chí | N đọc full-text, N loại kèm lý do |
| Included | Bài đưa vào tổng hợp | N cuối cùng |

### 2. Bảng tiêu chí Include / Exclude (lập TRƯỚC khi sàng lọc)

| Chiều | Include | Exclude |
|---|---|---|
| Loại tài liệu | Bài peer-reviewed, có phản biện | Bài báo phổ thông, blog, không phản biện |
| Thời gian | Trong khung năm đã định (ví dụ 2015–2026) | Ngoài khung năm |
| Population | Đúng đối tượng (ví dụ sinh viên đại học) | Sai đối tượng (học sinh phổ thông) |
| Thiết kế | Có dữ liệu thực nghiệm/empirical nếu RQ cần | Quan điểm cá nhân, không dữ liệu |
| Ngôn ngữ | Tiếng Anh, tiếng Việt | Ngôn ngữ ngoài năng lực đọc |
| Khả dụng | Có full-text | Chỉ có abstract, không lấy được toàn văn |
| Liên quan RQ | Trả lời trực tiếp câu hỏi nghiên cứu | Lệch chủ đề, chỉ nhắc thoáng qua |

Tiêu chí phải **cố định trước**, không đổi tùy tiện sau khi đã thấy kết quả.

### 3. Sàng lọc 2 vòng

**Vòng 1 — Tiêu đề và abstract.** Đọc nhanh, áp tiêu chí dễ kiểm (năm, loại tài
liệu, đối tượng, chủ đề). Khi phân vân thì **giữ lại** để xét tiếp ở vòng 2.

**Vòng 2 — Full-text.** Đọc toàn văn, áp tiêu chí chặt. Mỗi bài bị loại phải ghi
**một** lý do duy nhất, rõ ràng.

| Mã lý do loại (full-text) | Diễn giải |
|---|---|
| L1 | Sai đối tượng/population |
| L2 | Không có dữ liệu thực nghiệm |
| L3 | Sai bối cảnh |
| L4 | Không lấy được full-text |
| L5 | Trùng lặp/cùng bộ dữ liệu đã có bài khác |
| L6 | Lệch câu hỏi nghiên cứu |

### 4. Mẫu bảng quyết định sàng lọc

| ID | Tác giả-năm | Vòng 1 (giữ/loại) | Vòng 2 (giữ/loại) | Mã lý do loại |
|---|---|---|---|---|
| 001 | Nguyen 2023 | Giữ | Giữ | — |
| 002 | Smith 2020 | Giữ | Loại | L2 |
| 003 | Tran 2019 | Loại | — | Sai năm |

### 5. PRISMA flow — mẫu văn bản điền số

```text
Identification: [N] records từ CSDL, [N] records từ nguồn khác.
                [N] trùng lặp đã gỡ.
Screening:      [N] records sàng lọc tiêu đề/abstract; [N] loại.
Eligibility:    [N] full-text được đánh giá; [N] loại kèm lý do
                (L1=…, L2=…, L3=…, L4=…, L5=…, L6=…).
Included:       [N] nghiên cứu đưa vào tổng hợp.
```

## Quy Trình Các Bước

1. Nhận số kết quả thô từ sub-skill `lap-chuoi-tim-kiem`.
2. Gộp kết quả các CSDL, gỡ trùng (Identification), ghi số trùng đã gỡ.
3. Lập bảng tiêu chí Include/Exclude trước khi đọc bất kỳ bài nào.
4. Sàng lọc vòng 1 (tiêu đề + abstract), ghi giữ/loại.
5. Sàng lọc vòng 2 (full-text), ghi giữ/loại kèm mã lý do.
6. Tổng hợp số liệu vào PRISMA flow và bàn giao tập bài "Included" cho `ma-tran-tai-lieu`.

## Đầu Ra

- Bảng tiêu chí Include/Exclude.
- Bảng quyết định sàng lọc 2 vòng kèm mã lý do loại.
- PRISMA flow đã điền số.
- Danh sách bài cuối cùng đưa vào tổng hợp.

## Lưu Ý Liêm Chính

- Không đổi tiêu chí sau khi đã thấy kết quả để "ép" số bài theo ý muốn.
- Mỗi bài loại ở full-text phải có lý do ghi lại được; con số trong PRISMA flow
  phải cộng đúng (số vào trừ số loại bằng số ra).
- Khi đôi người sàng lọc, ghi lại mức đồng thuận; với luận án nên có người thứ hai
  rà soát ít nhất mẫu ngẫu nhiên để giảm thiên lệch.
