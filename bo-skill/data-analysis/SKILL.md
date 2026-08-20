---
name: data-analysis
description: >
  Phân tích dữ liệu định lượng và định tính cho nghiên cứu học thuật. Sử dụng khi
  người dùng cần descriptive statistics, reliability, validity, CFA, SEM, PLS-SEM,
  regression, ANOVA, mediation, moderation, thematic analysis, coding qualitative
  data, interpretation, chapter 4 hoặc chapter 5.
---

# Data Analysis Skill

## Mục Tiêu

Hỗ trợ lập kế hoạch phân tích, kiểm tra dữ liệu, diễn giải kết quả và viết phần
kết quả/thảo luận theo chuẩn học thuật. Skill này không thay thế chuyên gia
thống kê khi mô hình phức tạp hoặc dữ liệu có rủi ro cao.

## Đầu Vào Tối Thiểu

Hỏi tối đa 3 câu khi thiếu thông tin:

1. Dữ liệu thuộc loại nào: survey, experiment, interview, document, panel?
2. Research questions, hypotheses và biến chính là gì?
3. Người dùng cần plan phân tích, code, diễn giải output hay viết chương?

Nếu người dùng đưa dữ liệu thật, nhắc ẩn danh dữ liệu cá nhân trước khi xử lý.

## Quy Trình Phân Tích Định Lượng

### Bước 1: Data Audit

Kiểm tra:

- Số dòng, số biến, dictionary hoặc codebook.
- Missing values theo biến và theo respondent.
- Outliers đơn biến và đa biến.
- Reverse-coded items.
- Range lỗi hoặc mã hóa sai.
- Duplicate responses nếu là survey.

Missing data:

| Tình huống | Cách xử lý thường gặp |
|---|---|
| MCAR, tỷ lệ rất thấp | Listwise hoặc pairwise tùy phân tích |
| MAR, tỷ lệ đáng kể | Multiple imputation |
| Missing có pattern | Phân tích nguyên nhân trước khi xử lý |

### Bước 2: Descriptive Statistics

Báo cáo:

- N, mean, SD, min, max.
- Frequency cho biến categorical.
- Skewness và kurtosis nếu cần.
- Correlation matrix nếu phù hợp.
- Đặc điểm mẫu theo demographic variables.

### Bước 3: Reliability Và Validity

| Chỉ số | Ngưỡng tham khảo | Ghi chú |
|---|---|---|
| Cronbach alpha | >= .70 | Exploratory có thể chấp nhận thấp hơn nếu giải thích |
| Composite reliability | >= .70 | Dùng trong SEM/PLS-SEM |
| Factor loading | >= .70 | .60 có thể cân nhắc trong nghiên cứu khám phá |
| AVE | >= .50 | Convergent validity |
| HTMT | < .85 hoặc < .90 | Discriminant validity |
| VIF | < 5 | Kiểm tra multicollinearity |

Ngưỡng là hướng dẫn, không phải luật cứng. Cần giải thích theo lĩnh vực, mẫu và
thiết kế nghiên cứu.

### Bước 4: Model Testing

| Phương pháp | Khi dùng | Cần báo cáo |
|---|---|---|
| Regression | Outcome liên tục, model đơn giản | B, beta, SE, p, CI, R2 |
| ANOVA/ANCOVA | So sánh nhóm | F, df, p, eta squared hoặc omega squared |
| CB-SEM | Confirm theory, model fit quan trọng | CFI, TLI, RMSEA, SRMR, chi-square/df |
| PLS-SEM | Prediction, formative construct, sample nhỏ hơn | Path, t, p, CI, f2, Q2, R2 |
| Mediation | Kiểm tra cơ chế trung gian | Indirect effect, bootstrap CI |
| Moderation | Kiểm tra boundary condition | Interaction, simple slopes |

Model fit CB-SEM tham khảo:

| Chỉ số | Mức chấp nhận được | Mức tốt |
|---|---|---|
| CFI/TLI | > .90 | > .95 |
| RMSEA | < .08 | < .06 |
| SRMR | < .10 | < .08 |
| chi-square/df | < 5 | < 3 |

### Bước 5: Interpretation

Luôn phân biệt:

- Statistical significance: kết quả có ý nghĩa thống kê.
- Practical significance: hiệu ứng có đáng kể trong thực tế không.
- Theoretical significance: kết quả đóng góp gì cho lý thuyết.

Không diễn giải vượt dữ liệu. Cross-sectional data không đủ để kết luận nhân quả
nếu không có thiết kế nhận dạng phù hợp.

## Code Templates

### R: Reliability Và Descriptive

```r
library(psych)

items <- df[, c("item1", "item2", "item3")]
psych::alpha(items)
describe(items)
```

### R: CFA Với lavaan

```r
library(lavaan)
library(semTools)

model <- '
  construct1 =~ item1 + item2 + item3
  construct2 =~ item4 + item5 + item6
'

fit <- cfa(model, data = df, estimator = "MLR")
summary(fit, fit.measures = TRUE, standardized = TRUE)
semTools::reliability(fit)
```

### Python: Missing Và Descriptive

```python
import pandas as pd

def missing_report(df):
    out = pd.DataFrame({
        "missing_n": df.isna().sum(),
        "missing_pct": (df.isna().mean() * 100).round(2),
    })
    return out.sort_values("missing_pct", ascending=False)

desc = df.describe(include="all").T
```

### Python: Cronbach Alpha Với pingouin

```python
import pingouin as pg

items = df[["item1", "item2", "item3"]]
alpha, ci = pg.cronbach_alpha(data=items)
print(alpha, ci)
```

## Phân Tích Định Tính

### Thematic Analysis

Theo 6 bước:

1. Familiarization: đọc transcript và ghi memo.
2. Initial coding: code toàn bộ dữ liệu liên quan.
3. Theme search: nhóm code thành theme.
4. Theme review: kiểm tra theme với dữ liệu gốc.
5. Theme definition: đặt tên và định nghĩa theme.
6. Write-up: kể câu chuyện phân tích có trích dẫn minh họa.

### Quality Check

- Có audit trail.
- Có reflexivity note.
- Có ví dụ quote đại diện.
- Không chọn quote chỉ để chứng minh ý có sẵn.
- Nếu có nhiều coder, báo cáo cách thống nhất coding.

## Viết Kết Quả

Chương Results:

- Mô tả mẫu.
- Data screening.
- Measurement model.
- Hypothesis testing.
- Bảng tóm tắt kết quả.

Chương Discussion:

- Trả lời từng RQ.
- So sánh với literature.
- Giải thích kết quả bất ngờ.
- Nêu contribution.
- Nêu limitation và future research.

## Checklist Chất Lượng

- [ ] Dữ liệu đã được kiểm tra missing, outlier và mã hóa.
- [ ] Phương pháp phân tích khớp hypothesis và loại biến.
- [ ] Báo cáo đủ effect size hoặc practical significance.
- [ ] Không nói quá kết quả.
- [ ] Bảng/hình có title, note và đơn vị rõ.
- [ ] Code hoặc bước phân tích có thể replicate.
- [ ] Dữ liệu nhạy cảm đã được ẩn danh.

## Kết Quả Đề Xuất

- Analysis plan.
- Code R hoặc Python có comment.
- APA-style results table.
- Diễn giải kết quả bằng tiếng Việt hoặc tiếng Anh học thuật.
- Chapter 4/5 outline.
- Mục tri thức trong `kho-tri-thuc/methods`, `kho-tri-thuc/datasets` hoặc
  `kho-tri-thuc/outputs`.


## Quy trình chi tiết (đọc khi cần)

Các quy trình con của skill này nằm trong thư mục `quy-trinh/`. Khi làm đến bước tương ứng, mở file để lấy hướng dẫn chi tiết:

- [Diễn giải kết quả nghiên cứu](quy-trinh/dien-giai-ket-qua.md) - Diễn giải kết quả nghiên cứu.
- [Kiểm định giả thuyết](quy-trinh/kiem-dinh-gia-thuyet.md) - Kiểm định giả thuyết.
- [Kiểm tra và làm sạch dữ liệu](quy-trinh/kiem-tra-du-lieu.md) - Kiểm tra và làm sạch dữ liệu.
- [Kiểm tra độ tin cậy và giá trị thang đo](quy-trinh/kiem-tra-thang-do.md) - Kiểm tra độ tin cậy và giá trị thang đo.
- [Tạo thống kê mô tả](quy-trinh/thong-ke-mo-ta.md) - Tạo thống kê mô tả.
