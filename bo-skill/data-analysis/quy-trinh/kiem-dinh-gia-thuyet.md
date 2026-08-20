# Kiểm định giả thuyết

## Mục tiêu

Chọn đúng phép kiểm định thống kê cho từng giả thuyết dựa trên loại biến và thiết
kế, chạy kiểm định, và báo cáo đầy đủ thống kê kiểm định, mức ý nghĩa (p) và độ
lớn hiệu ứng (effect size). Bao gồm cả kiểm định trung gian (mediation) và điều
tiết (moderation).

## Khi nào dùng

- Có giả thuyết H1, H2... cần kiểm định bằng dữ liệu.
- Cần chọn giữa t-test, ANOVA, chi-square, tương quan, hồi quy.
- Kiểm định cơ chế trung gian hoặc biên điều tiết.
- Cần báo cáo effect size, không chỉ p-value.

## Nội dung chuyên môn

### 1. Bảng chọn kiểm định theo loại biến

| Biến độc lập (X) | Biến phụ thuộc (Y) | Phép kiểm định | Thống kê & effect size |
|---|---|---|---|
| Nhị phân (2 nhóm) | Liên tục | Independent t-test | t, df, p, Cohen's d |
| Cùng đối tượng, 2 thời điểm | Liên tục | Paired t-test | t, df, p, Cohen's d |
| Phân loại (≥ 3 nhóm) | Liên tục | One-way ANOVA | F, df, p, η² (eta bình phương) |
| ≥ 2 yếu tố phân loại | Liên tục | Two-way ANOVA | F, p, η², kiểm tra interaction |
| Phân loại + hiệp biến | Liên tục | ANCOVA | F, p, η² hiệu chỉnh |
| Phân loại | Phân loại | Chi-square (χ²) | χ², df, p, Cramér's V |
| Liên tục (chuẩn) | Liên tục (chuẩn) | Tương quan Pearson | r, p |
| Thứ bậc / lệch | Liên tục / thứ bậc | Tương quan Spearman (ρ) | ρ, p |
| Một biến liên tục | Liên tục | Hồi quy tuyến tính đơn | β, R², t, p |
| Nhiều biến | Liên tục | Hồi quy đa biến (OLS) | β, R², R² hiệu chỉnh, F, t, p, VIF |
| Nhiều biến | Nhị phân | Hồi quy logistic | OR (Exp(B)), Wald, p |
| Hệ nhiều quan hệ + biến tiềm ẩn | — | SEM / PLS-SEM | path coef., t, p, R², f², Q² |

Giả định cần kiểm tra: t-test/ANOVA cần chuẩn & đồng nhất phương sai (Levene); hồi
quy OLS cần tuyến tính, độc lập phần dư, phương sai sai số không đổi
(homoscedasticity), phần dư chuẩn, không đa cộng tuyến (**VIF < 5**, lý tưởng < 3).

### 2. Mức ý nghĩa và độ lớn hiệu ứng

Quy ước: **p < .05** (đôi khi .01 hoặc .001). Nhưng p chỉ cho biết "có/không"
ý nghĩa thống kê — phải báo cáo **effect size** để biết độ lớn:

| Effect size | Nhỏ | Trung bình | Lớn |
|---|---|---|---|
| Cohen's d (t-test) | 0,20 | 0,50 | 0,80 |
| η² (ANOVA) | 0,01 | 0,06 | 0,14 |
| r (tương quan) | 0,10 | 0,30 | 0,50 |
| f² (hồi quy/SEM) | 0,02 | 0,15 | 0,35 |
| R² (hồi quy) | tùy lĩnh vực — báo cáo cùng adjusted R² | | |

Công thức: `Cohen's d = (mean1 − mean2) / SD_gộp`; `η² = SS_giữa / SS_tổng`;
`f² = R² / (1 − R²)`.

### 3. Kiểm định trung gian (mediation)

X → M → Y. **Khuyến nghị hiện nay: dùng bootstrap khoảng tin cậy 95% cho hiệu ứng
gián tiếp** (phương pháp Preacher & Hayes, macro PROCESS / gói `mediation`),
**thay cho** quy trình 4 bước Baron & Kenny (1986) đã lỗi thời.

- Hiệu ứng gián tiếp (indirect effect) = a × b (a: X→M, b: M→Y).
- Lấy ~5.000 mẫu bootstrap, dựng **95% CI** của a×b.
- **Kết luận có trung gian khi khoảng tin cậy không chứa 0** (bias-corrected CI),
  không dựa vào test Sobel vốn giả định phân phối chuẩn.
- Trung gian **toàn phần (full)**: a×b có ý nghĩa và đường trực tiếp c' không còn
  ý nghĩa. Trung gian **một phần (partial)**: cả a×b và c' đều có ý nghĩa.

### 4. Kiểm định điều tiết (moderation)

X × W → Y: thêm **biến tương tác (interaction term)** = X·W vào mô hình hồi quy.

- **Mean-center** (hoặc chuẩn hóa) X và W trước khi tạo tích để giảm đa cộng tuyến.
- Hệ số của số hạng tương tác (β_XW) có ý nghĩa (p < .05) ⇒ có điều tiết.
- Vẽ **simple slopes** (dốc tại W thấp / trung bình / cao, thường ±1 SD) để diễn
  giải hướng và độ mạnh điều tiết.

### Ví dụ minh họa

Giả thuyết: "Lãnh đạo chuyển đổi (X) tác động đến gắn kết (Y) qua hài lòng (M)".
Chạy PROCESS model 4, 5.000 bootstrap: indirect = a×b = .21, 95% CI [.12, .31].
CI không chứa 0 ⇒ **có trung gian**. Đường trực tiếp c' = .15, p = .03 (vẫn có ý
nghĩa) ⇒ **trung gian một phần**.

## Quy trình các bước

1. Phân loại biến của từng giả thuyết (X, Y, M, W; loại thang đo).
2. Chọn phép kiểm định theo bảng ở trên.
3. Kiểm tra giả định (chuẩn, phương sai, VIF, tuyến tính).
4. Chạy kiểm định; ghi thống kê, df, p.
5. Tính và báo cáo effect size tương ứng.
6. Với trung gian: bootstrap CI 95% cho hiệu ứng gián tiếp.
7. Với điều tiết: mean-center, đưa interaction term, vẽ simple slopes.
8. Lập bảng tổng hợp: giả thuyết → kết quả → ủng hộ/bác bỏ.

## Đầu ra

- Bảng tổng hợp kiểm định giả thuyết (β/t/F/χ², p, effect size, kết luận).
- Bảng hồi quy đầy đủ (β chuẩn hóa, R², adjusted R², VIF).
- Bảng trung gian (a, b, a×b, bootstrap CI, loại trung gian).
- Đồ thị simple slopes cho điều tiết (nếu có).

## Lưu ý

- **p < .05 không đồng nghĩa quan trọng**: với N lớn, hiệu ứng rất nhỏ vẫn "có ý
  nghĩa". Luôn báo cáo và diễn giải effect size (ý nghĩa thực tiễn) bên cạnh p.
- Tương quan/hồi quy trên dữ liệu **cắt ngang (cross-sectional)** chỉ cho thấy
  **liên hệ**, **không** chứng minh nhân quả; tránh viết "X gây ra Y" khi chưa có
  thiết kế dọc/thực nghiệm hoặc chiến lược nhận dạng phù hợp.
- Ưu tiên bootstrap CI (Preacher-Hayes) cho trung gian; tránh Baron & Kenny và
  Sobel test cũ.
- Kiểm tra giả định trước khi tin vào p-value; vi phạm nặng cần đổi sang kiểm định
  phi tham số hoặc estimator robust.
