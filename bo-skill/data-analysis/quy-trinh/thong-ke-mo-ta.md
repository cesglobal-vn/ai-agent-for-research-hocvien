# Tạo thống kê mô tả

## Mục tiêu

Tóm tắt đặc điểm của mẫu và của từng biến bằng các chỉ số mô tả chuẩn (N, trung
bình, độ lệch chuẩn, min, max, skewness, kurtosis) và bảng tần suất nhân khẩu học.
Mục tiêu là cho người đọc bức tranh tổng quát về dữ liệu trước khi vào kiểm định
giả thuyết — đây là phần mở đầu của Chương 4.

## Khi nào dùng

- Cần mô tả đặc điểm mẫu (giới tính, độ tuổi, trình độ, thâm niên...).
- Cần bảng trung bình/độ lệch chuẩn cho các biến/thang đo.
- Quyết định nên báo cáo trung bình hay trung vị cho biến lệch.
- Cần ma trận tương quan sơ bộ giữa các biến chính.

## Nội dung chuyên môn

### 1. Các chỉ số mô tả cốt lõi

| Chỉ số | Ý nghĩa | Dùng cho loại biến |
|---|---|---|
| N | Số quan sát hợp lệ | Mọi biến |
| Mean (trung bình) | Giá trị trung tâm | Định lượng, phân phối cân đối |
| Median (trung vị) | Giá trị giữa, ít bị outlier | Định lượng, phân phối lệch |
| Mode (yếu vị) | Giá trị xuất hiện nhiều nhất | Danh định / thứ bậc |
| SD (độ lệch chuẩn) | Mức phân tán quanh mean | Định lượng |
| Min / Max | Giá trị nhỏ nhất / lớn nhất | Định lượng, kiểm tra range |
| Skewness | Độ lệch của phân phối (±2) | Định lượng |
| Kurtosis | Độ nhọn của phân phối (±2) | Định lượng |

Công thức chính:
- Trung bình: `mean = Σx / N`
- Độ lệch chuẩn mẫu: `SD = √[ Σ(x − mean)² / (N − 1) ]`
- Hệ số biến thiên: `CV = SD / mean` (so sánh phân tán giữa các biến khác đơn vị).

### 2. Trung bình hay trung vị?

| Tình huống | Nên báo cáo |
|---|---|
| Phân phối cân đối, không có outlier mạnh | Mean + SD |
| Phân phối lệch mạnh (skewness ngoài ±2) | Median + IQR |
| Có outlier hợp lệ nhưng đáng kể | Median (kèm Mean để so sánh) |
| Biến danh định (nominal) | Tần suất + tỷ lệ %, không tính mean |
| Biến thứ bậc (ordinal) như Likert đơn | Median/Mode; mean chỉ khi coi như khoảng |

Lưu ý: với thang Likert tổng hợp nhiều item (composite), thông lệ học thuật vẫn
báo cáo mean + SD và coi là biến khoảng.

### 3. Bảng mô tả mẫu (nhân khẩu học)

Trình bày từng đặc điểm thành nhóm, kèm tần suất và tỷ lệ %:

| Đặc điểm | Nhóm | Tần suất (n) | Tỷ lệ (%) |
|---|---|---|---|
| Giới tính | Nam | 142 | 47,3 |
|  | Nữ | 158 | 52,7 |
| Độ tuổi | < 25 | 60 | 20,0 |
|  | 25–34 | 135 | 45,0 |
|  | 35–44 | 75 | 25,0 |
|  | ≥ 45 | 30 | 10,0 |
| Trình độ | Đại học | 210 | 70,0 |
|  | Sau đại học | 90 | 30,0 |
| **Tổng** |  | **300** | **100,0** |

Nguyên tắc: tổng % mỗi đặc điểm = 100%; ghi rõ N tổng; làm tròn % thống nhất (1
chữ số thập phân); nếu có missing thì ghi "valid %".

### 4. Bảng mô tả biến đo lường

| Biến/Thang đo | N | Mean | SD | Min | Max | Skewness | Kurtosis |
|---|---|---|---|---|---|---|---|
| Sự hài lòng (SAT) | 300 | 3,82 | 0,67 | 1,40 | 5,00 | −0,41 | 0,12 |
| Ý định gắn bó (INT) | 300 | 3,55 | 0,74 | 1,00 | 5,00 | −0,18 | −0,33 |

### 5. Ma trận tương quan sơ bộ

Báo cáo hệ số tương quan (Pearson nếu biến khoảng & phân phối chuẩn; Spearman nếu
thứ bậc/lệch) giữa các biến chính, kèm dấu sao mức ý nghĩa (`* p<.05`, `** p<.01`).
Đây là mô tả quan hệ tuyến tính, **chưa phải kiểm định giả thuyết**.

## Quy trình các bước

1. Phân loại biến: danh định, thứ bậc, khoảng, tỷ lệ.
2. Với biến phân loại: lập bảng tần suất + % cho mô tả mẫu.
3. Với biến định lượng: tính N, mean, SD, min, max, skewness, kurtosis.
4. Chọn mean hay median theo phân phối từng biến.
5. Lập ma trận tương quan sơ bộ nếu cần.
6. Trình bày bảng theo chuẩn APA (tiêu đề, ghi chú, đơn vị).

## Đầu ra

- Bảng mô tả mẫu nhân khẩu học (n, %).
- Bảng mô tả biến đo lường (mean, SD, min, max, skewness, kurtosis).
- Ma trận tương quan sơ bộ (nếu phù hợp).
- Đoạn văn mô tả đặc điểm mẫu cho Chương 4.

## Lưu ý

- Thống kê mô tả chỉ **mô tả**, không kiểm định và **không suy ra quan hệ nhân
  quả**. Tương quan trong ma trận mô tả ≠ ảnh hưởng.
- Phân biệt **ý nghĩa thống kê** với **ý nghĩa thực tiễn**: một tương quan r = .12
  có thể có p < .05 với N lớn nhưng độ lớn rất nhỏ.
- Không tính trung bình cho biến danh định (giới tính, ngành...).
- Báo cáo skewness/kurtosis để người đọc đánh giá giả định phân phối cho các bước
  sau.
