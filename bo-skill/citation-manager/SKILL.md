---
name: citation-manager
description: >
  Tạo, kiểm tra và định dạng trích dẫn, in-text citation, footnote và danh mục
  tài liệu tham khảo theo APA, Chicago, Vancouver, IEEE, Harvard hoặc chuẩn của
  tạp chí. Sử dụng khi người dùng đưa DOI, URL, PMID, arXiv ID, danh sách tài
  liệu thô, manuscript cần citation audit hoặc yêu cầu kiểm tra nguồn.
---

# Kỹ Năng Quản Lý Trích Dẫn

## Mục Tiêu

Giúp người dùng tạo và kiểm tra trích dẫn chính xác. Nguyên tắc bắt buộc: không
tạo nguồn giả, không đoán DOI, không tự thêm tác giả hoặc năm nếu chưa kiểm tra.

## Đầu Vào Tối Thiểu

Hỏi tối đa 3 câu khi thiếu thông tin:

1. Chuẩn trích dẫn cần dùng là gì?
2. Người dùng cần định dạng danh mục, in-text citation hay audit toàn bản thảo?
3. Nguồn đầu vào là DOI, URL, PDF, danh sách thô hay manuscript?

## Chuẩn Hỗ Trợ

| Chuẩn | Lĩnh vực thường dùng | Trích dẫn trong bài |
|---|---|---|
| APA 7 | Giáo dục, tâm lý, xã hội, kinh doanh | (Author, Year) |
| Chicago author-date | Nhân văn, xã hội | (Author Year) |
| Chicago notes-bibliography | Lịch sử, luật, nhân văn | Footnote |
| Vancouver hoặc NLM | Y sinh, sức khỏe | [1] |
| IEEE | Kỹ thuật, công nghệ | [1] |
| Harvard | Kinh tế, quản trị, khoa học | (Author Year) |
| MLA 9 | Ngôn ngữ, văn học | (Author page) |

## Quy Trình Tạo Trích Dẫn

1. Nhận dạng loại tài liệu: bài báo khoa học, sách, chương sách, báo cáo,
   luận án, trang web, bản thảo chưa phản biện, bài hội thảo hoặc văn bản pháp lý.
2. Trích xuất dữ liệu mô tả: tác giả, năm, tiêu đề, nguồn, số tập, số kỳ, trang,
   DOI hoặc URL.
3. Kiểm tra dữ liệu mô tả bằng DOI, URL, Crossref, PubMed, arXiv hoặc cơ sở dữ
   liệu người dùng cung cấp nếu có công cụ truy cập.
4. Định dạng theo chuẩn yêu cầu.
5. Đánh dấu trường còn thiếu bằng `Cần bổ sung`.

## Quy Tắc Trích Dẫn Trong Bài Theo APA 7

| Trường hợp | Dạng trong ngoặc | Dạng đưa tên tác giả vào câu |
|---|---|---|
| 1 tác giả | (Smith, 2023) | Smith (2023) |
| 2 tác giả | (Smith & Jones, 2023) | Smith and Jones (2023) |
| 3 tác giả trở lên | (Smith et al., 2023) | Smith et al. (2023) |
| Tổ chức | (World Health Organization, 2023) | World Health Organization (2023) |
| Trích trực tiếp | (Smith, 2023, p. 45) | Smith (2023, p. 45) |
| Nhiều nguồn | (Jones, 2020; Smith, 2019) | Không áp dụng |

Không ghi số trang cho paraphrase trừ khi guideline yêu cầu.

## Mẫu Danh Mục Tài Liệu Theo APA 7

### Journal Article

```text
Author, A. A., & Author, B. B. (Year). Title of article in sentence case.
Journal Name, 12(3), 45-67. https://doi.org/xxxxx
```

### Book

```text
Author, A. A. (Year). Title of book in sentence case. Publisher.
```

### Book Chapter

```text
Author, A. A. (Year). Title of chapter. In E. E. Editor (Ed.), Title of book
(pp. 12-34). Publisher.
```

### Thesis

```text
Author, A. A. (Year). Title of dissertation [Doctoral dissertation,
University Name]. Database or Repository. URL
```

### Report

```text
Organization Name. (Year). Title of report. Publisher. URL
```

### Webpage

```text
Author, A. A. (Year, Month Day). Title of page. Site Name. URL
```

## Tài Liệu Tiếng Việt Và Văn Bản Pháp Luật

- Giữ nguyên tên tiếng Việt nếu bài viết bằng tiếng Việt.
- Có thể thêm bản dịch tiếng Anh trong ngoặc vuông nếu chuẩn yêu cầu.
- Văn bản pháp luật cần có cơ quan ban hành, năm, tên văn bản và số hiệu.
- Nếu không rõ cách định dạng theo chuẩn trường, ghi chú để người dùng xác nhận.

## Rà Soát Trích Dẫn Cho Bản Thảo

1. Liệt kê toàn bộ trích dẫn trong bài.
2. Liệt kê toàn bộ mục trong danh mục tài liệu tham khảo.
3. So sánh:
   - Có trích dẫn trong bài nhưng thiếu ở danh mục tài liệu tham khảo.
   - Có tài liệu trong danh mục nhưng không được trích dẫn trong bài.
   - Sai năm, sai tên tác giả, sai thứ tự.
4. Kiểm tra DOI hoặc URL nếu có thể.
5. Trả về bảng lỗi và mức ưu tiên sửa.

## Quy Trình Xử Lý Nhiều DOI

Khi người dùng đưa nhiều DOI:

1. Chuẩn hóa DOI: bỏ `https://doi.org/`, khoảng trắng và dấu câu thừa.
2. Tra dữ liệu mô tả từng DOI.
3. Xuất bảng: DOI, tiêu đề, tác giả, năm, nguồn, trạng thái.
4. Định dạng danh mục tài liệu tham khảo.
5. Đánh dấu DOI không tìm thấy hoặc dữ liệu mô tả mâu thuẫn.

## Checklist Chất Lượng

- [ ] Không có nguồn bịa hoặc DOI đoán.
- [ ] Tên tác giả và năm khớp giữa trích dẫn trong bài và danh mục tài liệu.
- [ ] Danh mục tài liệu không có nguồn bị thừa.
- [ ] Trích dẫn trong bài không thiếu nguồn tương ứng.
- [ ] Chuẩn trích dẫn thống nhất trong toàn văn.
- [ ] Preprint được ghi rõ là preprint nếu chưa peer-reviewed.
- [ ] URL truy cập được hoặc được đánh dấu cần kiểm tra.

## Kết Quả Đề Xuất

- Danh mục tài liệu đã định dạng.
- Bảng rà soát trích dẫn.
- Danh sách trường dữ liệu mô tả còn thiếu.
- Trích dẫn trong bài được gợi ý.
- Mục tri thức trong `kho-tri-thuc/references` cho nguồn quan trọng.


## Quy trình chi tiết (đọc khi cần)

Các quy trình con của skill này nằm trong thư mục `quy-trinh/`. Khi làm đến bước tương ứng, mở file để lấy hướng dẫn chi tiết:

- [Rà soát trích dẫn trong bản thảo](quy-trinh/citation-audit.md) - Rà soát trích dẫn trong bản thảo.
- [Định dạng trích dẫn APA 7](quy-trinh/doi-sang-apa.md) - Định dạng trích dẫn APA 7.
- [Kiểm tra DOI và nguồn thật](quy-trinh/kiem-tra-doi.md) - Kiểm tra DOI và nguồn thật.
- [Xử lý tài liệu tiếng Việt và văn bản pháp luật](quy-trinh/xu-ly-tai-lieu-viet-nam.md) - Xử lý tài liệu tiếng Việt và văn bản pháp luật.
