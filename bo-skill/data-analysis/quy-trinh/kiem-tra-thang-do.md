# Kiểm tra độ tin cậy và giá trị thang đo

## Mục tiêu

Đánh giá chất lượng đo lường (measurement model) của các thang đo trước khi kiểm
định giả thuyết: độ tin cậy (reliability), độ giá trị hội tụ (convergent validity)
và độ giá trị phân biệt (discriminant validity), thông qua EFA và/hoặc CFA. Nếu
thang đo không đạt, mọi kết quả kiểm định sau đều không đáng tin.

## Khi nào dùng

- Sau khi làm sạch dữ liệu, trước khi chạy hồi quy/SEM.
- Cần báo cáo Cronbach alpha, CR, AVE, HTMT, factor loading.
- Cần chạy EFA (khám phá cấu trúc) hoặc CFA (khẳng định cấu trúc).
- Phản biện yêu cầu chứng minh thang đo "đáng tin và có giá trị".

## Nội dung chuyên môn

### 1. Bảng ngưỡng chuẩn

| Chỉ số | Loại đánh giá | Ngưỡng đạt | Ghi chú |
|---|---|---|---|
| Cronbach's alpha (α) | Độ tin cậy nhất quán nội tại | ≥ .70 | .60 chấp nhận với khám phá; > .95 nghi trùng lặp item |
| Composite Reliability (CR) | Độ tin cậy (trong CFA/SEM) | ≥ .70 | Tốt hơn α vì không giả định tải bằng nhau |
| Factor loading | Độ giá trị hội tụ | ≥ .50 (lý tưởng ≥ .70) | < .50 cân nhắc loại item |
| AVE | Độ giá trị hội tụ | ≥ .50 | Construct giải thích ≥ 50% phương sai item |
| HTMT | Độ giá trị phân biệt | < .85 (chặt) hoặc < .90 (lỏng) | Heterotrait-Monotrait ratio |
| Fornell-Larcker | Độ giá trị phân biệt | √AVE > tương quan với construct khác | So trên đường chéo |
| KMO | Tính phù hợp EFA | ≥ .60 (tốt ≥ .80) | Kaiser-Meyer-Olkin |
| Bartlett's test | Tính phù hợp EFA | p < .05 | Ma trận tương quan ≠ ma trận đơn vị |

### 2. Độ tin cậy

- **Cronbach's alpha**: đo nhất quán nội tại giữa các item của một thang đo.
  Báo cáo "Corrected Item-Total Correlation" (nên ≥ .30) và "Alpha if Item Deleted"
  (nếu xóa item làm α tăng đáng kể ⇒ cân nhắc loại item).
- **Composite Reliability (CR)** dùng trong CFA/PLS-SEM:
  `CR = (Σλ)² / [ (Σλ)² + Σ(1 − λ²) ]`, với λ là tải nhân tố chuẩn hóa.

### 3. Độ giá trị hội tụ (convergent validity)

Đạt khi: factor loading ≥ .50 (nên ≥ .70), CR ≥ .70, và **AVE ≥ .50**.

Công thức AVE: `AVE = Σλ² / n` (trung bình bình phương tải nhân tố chuẩn hóa của
n item trong construct). AVE ≥ .50 nghĩa là construct giải thích trên 50% phương
sai các item của nó.

### 4. Độ giá trị phân biệt (discriminant validity)

Hai cách kiểm tra:

- **Fornell-Larcker**: căn bậc hai của AVE mỗi construct (trên đường chéo) phải
  **lớn hơn** tương quan giữa construct đó với mọi construct khác (ngoài đường chéo).
- **HTMT**: tỷ số tương quan heterotrait-monotrait phải **< .85** (hoặc < .90 nếu
  các construct gần nhau về khái niệm). HTMT được xem là nhạy hơn Fornell-Larcker
  trong PLS-SEM.

### 5. EFA và CFA

| | EFA (khám phá) | CFA (khẳng định) |
|---|---|---|
| Mục đích | Tìm cấu trúc nhân tố khi chưa rõ | Kiểm chứng cấu trúc đã giả định |
| Tiền đề | KMO ≥ .60, Bartlett p < .05 | Có mô hình lý thuyết rõ ràng |
| Trích nhân tố | Eigenvalue > 1, hoặc parallel analysis | Cố định số nhân tố |
| Phép xoay | Varimax (trực giao) / Promax (xiên) | Không xoay; ước lượng tải trực tiếp |
| Tiêu chí item tốt | Tải ≥ .50, không tải chéo (cross-loading > .30 ⇒ xét loại) | Tải ≥ .50, chỉ số phù hợp mô hình đạt |
| Báo cáo | % phương sai trích (≥ 50%), ma trận xoay | CFI/TLI > .90, RMSEA < .08, SRMR < .08, χ²/df < 3 |

Quy trình thông lệ: EFA trên một nửa mẫu (hoặc nghiên cứu sơ bộ) → CFA trên mẫu
chính để khẳng định.

### Ví dụ minh họa

Thang đo "Sự hài lòng" gồm 4 item, tải chuẩn hóa: .82, .78, .71, .45.
- Item thứ 4 có tải .45 < .50 ⇒ cân nhắc loại.
- Sau khi loại, tính lại: α = .84 (≥ .70 ✔), CR = .86 (≥ .70 ✔), AVE = .61
  (≥ .50 ✔) ⇒ đạt độ tin cậy và hội tụ.
- √AVE = .78; tương quan với construct "Ý định" = .52 < .78 ⇒ đạt phân biệt
  (Fornell-Larcker); HTMT = .61 < .85 ⇒ đạt phân biệt (HTMT).

## Quy trình các bước

1. Kiểm tra điều kiện EFA: KMO ≥ .60 và Bartlett p < .05.
2. Chạy EFA, xét eigenvalue, % phương sai trích, ma trận xoay; loại item tải thấp
   hoặc tải chéo.
3. Tính Cronbach's alpha cho từng thang đo; xét item-total correlation.
4. Chạy CFA: kiểm tra factor loading, chỉ số phù hợp mô hình.
5. Tính CR và AVE cho từng construct (độ tin cậy + hội tụ).
6. Kiểm tra phân biệt bằng Fornell-Larcker và HTMT.
7. Lập bảng tổng hợp đối chiếu với ngưỡng chuẩn.

## Đầu ra

- Bảng EFA (KMO, Bartlett, % phương sai trích, ma trận xoay).
- Bảng độ tin cậy và hội tụ (α, CR, AVE, factor loading) theo từng construct.
- Bảng phân biệt (Fornell-Larcker và/hoặc HTMT).
- Chỉ số phù hợp CFA (CFI, TLI, RMSEA, SRMR, χ²/df).
- Kết luận thang đo đạt/không đạt và item đã loại.

## Lưu ý

- Ngưỡng là **hướng dẫn**, không phải luật cứng; cần biện minh theo lĩnh vực, cỡ
  mẫu và bản chất thang đo (ví dụ α hơi dưới .70 với thang đo mới khám phá).
- α cao **không** đảm bảo tính đơn hướng; cần kết hợp EFA/CFA.
- Loại item phải có cơ sở (tải thấp, tải chéo, nội dung) và phải báo cáo minh bạch.
- Đạt độ tin cậy và giá trị thang đo chỉ nói về **chất lượng đo lường**, hoàn toàn
  **không** ngụ ý quan hệ nhân quả giữa các biến.
