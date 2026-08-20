---
name: literature-review
description: >
  Thực hiện tổng quan tài liệu, systematic review, scoping review, narrative
  review, meta-analysis planning và research synthesis. Sử dụng khi người dùng
  cần tìm bài báo, lập search string, tiêu chí chọn loại, PRISMA flow, data
  extraction matrix, quality appraisal, thematic synthesis hoặc tìm research gap.
---

# Literature Review Skill

## Mục Tiêu

Hỗ trợ người dùng tìm, lọc, đánh giá và tổng hợp tài liệu có hệ thống. Skill này
ưu tiên tính minh bạch: search strategy phải ghi lại được, tiêu chí chọn loại
phải giải thích được, và citation phải kiểm tra được.

## Đầu Vào Tối Thiểu

Hỏi tối đa 3 câu khi thiếu thông tin:

1. Chủ đề, câu hỏi nghiên cứu hoặc mục tiêu review là gì?
2. Lĩnh vực, bối cảnh, giai đoạn năm và ngôn ngữ tài liệu?
3. Người dùng cần narrative review, systematic review, scoping review hay chỉ
   cần tìm tài liệu ban đầu?

## Chọn Loại Review

| Loại review | Khi dùng | Chuẩn hoặc hướng dẫn |
|---|---|---|
| Narrative review | Khám phá rộng, chương 2 luận án | Cấu trúc theo theme |
| Systematic review | Câu hỏi cụ thể, quy trình lặp lại được | PRISMA 2020 |
| Scoping review | Map evidence và xác định khoảng trống | PRISMA-ScR |
| Meta-analysis | Có effect size đủ đồng nhất | PRISMA, GRADE nếu phù hợp |
| Meta-synthesis | Tổng hợp định tính | ENTREQ hoặc hướng dẫn tương đương |

## Quy Trình 6 Bước

### Bước 1: Scoping

Xác định:

- Research question.
- Population, mục tri thức, context hoặc PICO.
- Thời gian xuất bản.
- Loại tài liệu được nhận.
- Database sẽ tìm.
- Ngôn ngữ.

PICO phù hợp y sinh hoặc can thiệp. PCC phù hợp scoping review.

### Bước 2: Search Strategy

Tạo từ khóa theo 4 nhóm:

1. Khái niệm chính.
2. Synonym và thuật ngữ gần nghĩa.
3. Context hoặc population.
4. Outcome hoặc hiện tượng quan tâm.

Ví dụ search string:

```text
("artificial intelligence" OR ChatGPT OR "generative AI")
AND ("higher education" OR university OR student)
AND (learning OR teaching OR assessment)
```

Ghi lại database, ngày tìm kiếm, số kết quả và bộ lọc đã dùng.

### Bước 3: Database Selection

| Lĩnh vực | Database ưu tiên |
|---|---|
| Quản trị, kinh doanh | Scopus, Web of Science, EBSCOhost, ABI/INFORM |
| Giáo dục | ERIC, Scopus, Web of Science, PsycINFO |
| Y tế | PubMed, CINAHL, Cochrane, Embase |
| CNTT, kỹ thuật | IEEE Xplore, ACM Digital Library, Scopus |
| Liên ngành | Scopus, Web of Science, Google Scholar bổ sung |

Google Scholar nên dùng để bổ sung hoặc citation chasing, không nên là nguồn
duy nhất cho systematic review.

### Bước 4: Screening

Tạo tiêu chí inclusion và exclusion trước khi đọc sâu.

| Nhóm tiêu chí | Ví dụ |
|---|---|
| Inclusion | Peer-reviewed, đúng năm, đúng population, đúng RQ |
| Exclusion | Duplicate, không full text, sai context, không empirical nếu cần empirical |
| Boundary | Conference paper có nhận không, preprint có nhận không |

Ghi lý do loại bài ở full-text screening để dùng cho PRISMA flow.

### Bước 5: Extraction Và Quality Appraisal

Data extraction matrix tối thiểu:

| Field | Nội dung cần lấy |
|---|---|
| Study ID | Tác giả, năm |
| Context | Quốc gia, ngành, population |
| Design | Quantitative, qualitative, mixed, review |
| Sample | Cỡ mẫu và đặc điểm mẫu |
| Constructs | Biến hoặc mục tri thức chính |
| Method | Công cụ, thang đo, phân tích |
| Findings | Kết quả chính |
| Limitations | Hạn chế tác giả nêu |
| Quality note | Rủi ro bias hoặc điểm chất lượng |

Công cụ appraisal tham khảo:

- Quantitative observational: Newcastle-Ottawa Scale hoặc JBI checklist.
- RCT: Cochrane RoB 2.
- Qualitative: CASP hoặc COREQ.
- Mixed methods: MMAT.

### Bước 6: Synthesis Và Gap

Tổng hợp theo theme, không theo từng tác giả riêng lẻ. Mỗi theme cần:

- Pattern chính.
- Bằng chứng ủng hộ.
- Kết quả mâu thuẫn.
- Điều kiện hoặc bối cảnh làm kết quả thay đổi.
- Gap còn lại.

Gap taxonomy:

| Loại gap | Câu hỏi kiểm tra |
|---|---|
| Theoretical | Lý thuyết nào chưa được áp dụng hoặc tích hợp? |
| Contextual | Bối cảnh nào chưa được nghiên cứu? |
| Methodological | Phương pháp nào chưa được dùng? |
| Population | Nhóm mẫu nào còn thiếu? |
| Variable | Biến trung gian, điều tiết hoặc outcome nào bị bỏ qua? |
| Temporal | Bối cảnh mới làm kết quả cũ cần kiểm tra lại? |

## PRISMA Flow Text Template

```text
Identification: [N] records from databases, [N] records from other sources.
Screening: [N] records after duplicates removed; [N] excluded by title/abstract.
Eligibility: [N] full-text articles assessed; [N] excluded with reasons.
Included: [N] studies included in synthesis.
```

## Write-Up Structure

1. Mục tiêu review.
2. Search strategy.
3. Inclusion và exclusion criteria.
4. Screening và PRISMA flow.
5. Đặc điểm nghiên cứu được include.
6. Thematic synthesis.
7. Quality appraisal summary.
8. Research gaps và future research.
9. Kết luận.

## Checklist Chất Lượng

- [ ] Search string có thể lặp lại.
- [ ] Database và ngày tìm kiếm được ghi rõ.
- [ ] Inclusion và exclusion không thay đổi tùy tiện sau khi thấy kết quả.
- [ ] Có xử lý duplicate.
- [ ] Có data extraction matrix.
- [ ] Claim tổng hợp dựa trên nhiều nguồn, không citation march.
- [ ] Trích dẫn được kiểm tra bằng DOI hoặc nguồn thật.

## Kết Quả Đề Xuất

- Search strategy.
- Screening criteria.
- PRISMA flow text.
- Data extraction matrix.
- Thematic synthesis outline.
- Research gap statement.
- Các mục tri thức trong `kho-tri-thuc/references`, `kho-tri-thuc/theories` hoặc
  `kho-tri-thuc/constructs`.


## Quy trình chi tiết (đọc khi cần)

Các quy trình con của skill này nằm trong thư mục `quy-trinh/`. Khi làm đến bước tương ứng, mở file để lấy hướng dẫn chi tiết:

- [Lập chuỗi tìm kiếm (search string) cho cơ sở dữ liệu học thuật](quy-trinh/lap-chuoi-tim-kiem.md) - Lập chuỗi tìm kiếm cho cơ sở dữ liệu học thuật.
- [Lập ma trận tổng hợp tài liệu (literature matrix)](quy-trinh/ma-tran-tai-lieu.md) - Tạo ma trận trích xuất tài liệu.
- [Sàng lọc tài liệu theo quy trình PRISMA](quy-trinh/sang-loc-tai-lieu.md) - Sàng lọc tài liệu theo tiêu chí chọn và loại.
- [Sinh từ khóa và từ đồng nghĩa cho tổng quan tài liệu](quy-trinh/tao-tu-khoa.md) - Tạo từ khóa và từ đồng nghĩa cho tổng quan tài liệu.
- [Phát hiện khoảng trống nghiên cứu từ ma trận tài liệu](quy-trinh/tim-khoang-trong.md) - Tìm khoảng trống nghiên cứu có căn cứ.
