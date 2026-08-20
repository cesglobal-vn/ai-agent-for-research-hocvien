# Lập chuỗi tìm kiếm (search string) cho cơ sở dữ liệu học thuật

## Mục Tiêu

**Ghép** kho từ khóa đã sinh ở bước trước thành một search string hoàn chỉnh, có
thể chạy được trên từng cơ sở dữ liệu, dùng toán tử Boolean, dấu ngoặc, ký tự đại
diện và field tags. Đây là bước **GHÉP CHUỖI**, không sinh thêm từ khóa mới (việc
đó thuộc sub-skill `tao-tu-khoa`).

## Khi Nào Dùng

- Khi đã có bảng nhóm khái niệm → từ khóa và cần biến thành chuỗi chạy được.
- Khi cần chuyển một chuỗi đã viết cho Scopus sang cú pháp Web of Science, PubMed
  hay Google Scholar.
- Khi chuỗi cho ra quá nhiều/quá ít kết quả và cần tinh chỉnh toán tử, ngoặc, tag.

## Nội Dung Chuyên Môn

### 1. Logic ghép: OR trong nhóm, AND giữa các nhóm

Nguyên tắc bất biến của search string:

- **OR** nối các từ đồng nghĩa trong **cùng một** nhóm khái niệm.
- **AND** nối **các nhóm** khái niệm khác nhau (mỗi AND thu hẹp kết quả).
- **NOT** loại chủ đề gây nhiễu — dùng dè dặt vì dễ loại nhầm bài hợp lệ.
- **Dấu ngoặc đơn** `( )` bắt buộc bao quanh mỗi khối OR để giữ đúng thứ tự ưu tiên.

```text
(nhóm 1: A OR B OR C) AND (nhóm 2: D OR E) AND (nhóm 3: F OR G)
```

### 2. Ký tự đại diện và toán tử lân cận

| Ký hiệu | Ý nghĩa | Ví dụ |
|---|---|---|
| `*` | Cắt đuôi (truncation) | `educat*` → education, educational, educator |
| `?` hoặc `$` | Thay 1 ký tự | `behavio?r` → behavior, behaviour |
| `" "` | Tìm chính xác cụm | `"higher education"` |
| `W/n`, `NEAR/n`, `ADJn` | Lân cận n từ | `student NEAR/3 motivation` |

Lưu ý cú pháp truncation và lân cận **khác nhau giữa các CSDL** (xem mục 4).

### 3. Field tags — giới hạn nơi tìm

| Tag | Phạm vi | Scopus | Web of Science | PubMed |
|---|---|---|---|---|
| Tiêu đề | Title | `TITLE( )` | `TI=( )` | `[Title]` |
| Tiêu đề + abstract + từ khóa | — | `TITLE-ABS-KEY( )` | `TS=( )` | — |
| Abstract | — | `ABS( )` | `AB=( )` | `[Title/Abstract]` |
| MeSH | — | — | — | `[MeSH Terms]` |

Bắt đầu rộng (TITLE-ABS-KEY / TS) rồi thu hẹp về Title nếu nhiễu quá nhiều.

### 4. Ví dụ chuỗi hoàn chỉnh theo từng CSDL

Cùng một ý tưởng (AI tạo sinh × sinh viên đại học × kết quả học tập):

**Scopus**
```text
TITLE-ABS-KEY(("generative AI" OR "GenAI" OR ChatGPT OR "large language model" OR LLM)
AND (universit* OR undergraduate OR "higher education")
AND ("learning outcome*" OR "academic performance" OR achievement))
AND PUBYEAR > 2021
AND (LIMIT-TO(LANGUAGE,"English"))
```

**Web of Science (Core Collection)**
```text
TS=(("generative AI" OR GenAI OR ChatGPT OR "large language model" OR LLM)
AND (universit* OR undergraduate OR "higher education")
AND ("learning outcome*" OR "academic performance" OR achievement))
```
Lọc năm và ngôn ngữ bằng bộ lọc giao diện (Publication Years, Languages).

**PubMed**
```text
(("Artificial Intelligence"[MeSH] OR "generative AI"[Title/Abstract] OR ChatGPT[Title/Abstract])
AND ("Students"[MeSH] OR undergraduate[Title/Abstract])
AND ("learning outcome*"[Title/Abstract] OR "academic performance"[Title/Abstract]))
```

**Google Scholar** (không hỗ trợ truncation `*`, ngoặc lồng hạn chế; giữ chuỗi ngắn)
```text
"generative AI" OR ChatGPT "higher education" "learning outcomes"
```
Dùng Google Scholar để bổ sung và truy vết trích dẫn, không làm nguồn chính cho
systematic review.

### 5. Bảng ghi lại chiến lược tìm kiếm (bắt buộc để lặp lại)

| CSDL | Ngày tìm | Chuỗi đã dùng | Bộ lọc (năm, ngôn ngữ, loại) | Số kết quả |
|---|---|---|---|---|
| Scopus | 2026-06-16 | (như trên) | 2022– , English, article+review | … |
| Web of Science | 2026-06-16 | (như trên) | 2022– , English | … |

## Quy Trình Các Bước

1. Nhận bảng nhóm khái niệm → từ khóa từ sub-skill `tao-tu-khoa`.
2. Ghép OR trong từng nhóm, bọc ngoặc, rồi nối các nhóm bằng AND.
3. Thêm truncation `*`, cụm `" "` và toán tử lân cận khi cần.
4. Gắn field tags phù hợp; chọn bắt đầu rộng (TS / TITLE-ABS-KEY).
5. Viết phiên bản chuỗi cho từng CSDL theo đúng cú pháp riêng.
6. Chạy thử, đếm kết quả, tinh chỉnh; ghi lại toàn bộ vào bảng chiến lược tìm kiếm.

## Đầu Ra

- Search string hoàn chỉnh cho từng CSDL (Scopus, WoS, PubMed, Google Scholar…).
- Bảng ghi lại chiến lược tìm kiếm (CSDL, ngày, chuỗi, bộ lọc, số kết quả).
- Bàn giao số kết quả cho sub-skill `sang-loc-tai-lieu`.

## Lưu Ý Liêm Chính

- Cú pháp khác nhau giữa các CSDL: không bê nguyên chuỗi Scopus sang PubMed mà
  chưa chuyển đổi — sẽ ra kết quả sai mà trông như đúng.
- Phải ghi lại chuỗi và ngày tìm chính xác; chiến lược tìm kiếm không lặp lại được
  là vi phạm chuẩn PRISMA về tính minh bạch.
- Không tự bịa số lượng kết quả; nếu chưa chạy thật, ghi rõ là chuỗi đề xuất cần
  người dùng chạy và điền số liệu.
