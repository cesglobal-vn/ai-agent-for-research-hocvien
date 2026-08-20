# Kiểm tra và làm sạch dữ liệu

## Mục tiêu

Phát hiện và xử lý các vấn đề về chất lượng dữ liệu trước khi phân tích: giá trị
thiếu (missing), giá trị ngoại lai (outlier), lỗi nhập liệu, dòng trùng và phân
phối bất thường. Mục tiêu là có một bộ dữ liệu "sạch" để các bước thống kê và
kiểm định sau cho kết quả tin cậy. Đây là bước bắt buộc (data screening) trong
Chương 4 của luận án.

## Khi nào dùng

- Vừa thu được dữ liệu khảo sát/thực nghiệm, chưa chạy phân tích nào.
- Cần kiểm tra missing trước khi quyết định listwise/pairwise/imputation.
- Phát hiện đáp viên trả lời ẩu (straight-lining, ngoài thang đo).
- Giảng viên/phản biện yêu cầu báo cáo phần "data screening".

## Nội dung chuyên môn

### 1. Giá trị thiếu (missing values)

Trước hết xác định **cơ chế thiếu** vì nó quyết định cách xử lý:

| Cơ chế | Ý nghĩa | Hệ quả |
|---|---|---|
| MCAR (Missing Completely At Random) | Thiếu hoàn toàn ngẫu nhiên, không liên quan biến nào | Listwise không gây lệch |
| MAR (Missing At Random) | Thiếu phụ thuộc biến quan sát khác | Nên dùng imputation/FIML |
| MNAR (Missing Not At Random) | Thiếu phụ thuộc chính giá trị bị thiếu | Khó xử lý, cần mô hình hóa nguyên nhân |

Kiểm tra MCAR bằng **Little's MCAR test** (p > .05 ⇒ chấp nhận MCAR).

Bảng quyết định xử lý theo tỷ lệ thiếu:

| Tỷ lệ thiếu trên 1 biến/đáp viên | Cách xử lý đề xuất |
|---|---|
| < 5%, ngẫu nhiên (MCAR) | Listwise deletion hoặc mean/median imputation |
| 5% – 10% | Pairwise (cho tương quan), hoặc imputation |
| 10% – 20%, MAR | Multiple imputation (MI) hoặc FIML (cho SEM) |
| > 20% trên một biến | Cân nhắc loại biến đó |
| > 50% trên một đáp viên | Loại đáp viên đó |

- **Listwise**: xóa cả dòng nếu thiếu bất kỳ biến nào dùng trong phân tích. Đơn
  giản nhưng giảm N mạnh.
- **Pairwise**: dùng các cặp có đủ dữ liệu cho từng tương quan. N khác nhau giữa
  các ô.
- **Imputation**: thay giá trị thiếu (mean/median với biến lệch, regression, hoặc
  multiple imputation). MI và FIML được khuyến nghị cho dữ liệu MAR vì cho ước
  lượng ít chệch nhất.

### 2. Giá trị ngoại lai (outlier)

| Loại | Cách phát hiện | Ngưỡng |
|---|---|---|
| Ngoài thang đo | Lọc min/max so với thang Likert | Ví dụ thang 1–5 mà có giá trị 6, 0, 99 ⇒ lỗi |
| Outlier đơn biến | Điểm chuẩn hóa z-score | \|z\| > 3.29 (tương ứng p < .001) |
| Outlier đơn biến | Boxplot / IQR | Ngoài [Q1 − 1.5·IQR ; Q3 + 1.5·IQR]; xa: ngoài 3·IQR |
| Outlier đa biến | Khoảng cách Mahalanobis D² | So với χ² với df = số biến, p < .001 |

Công thức:
- z-score: `z = (x − mean) / SD`
- IQR: `IQR = Q3 − Q1`; cận dưới `Q1 − 1.5·IQR`, cận trên `Q3 + 1.5·IQR`.

Xử lý outlier: (a) sửa nếu là lỗi nhập; (b) giữ nếu là giá trị hợp lệ và có ý
nghĩa; (c) winsorize/transform nếu làm lệch mạnh; (d) loại nếu chắc chắn sai và
báo cáo số lượng đã loại. **Không** loại outlier chỉ vì nó "khó chịu".

### 3. Phân phối (chuẩn hóa)

| Chỉ số | Ngưỡng chấp nhận | Ghi chú |
|---|---|---|
| Skewness (độ lệch) | trong khoảng ±2 (nghiêm: ±1) | Ngoài ±2 ⇒ lệch mạnh |
| Kurtosis (độ nhọn) | trong khoảng ±2 (Kline: ±7 với SEM) | Quá nhọn/bẹt ảnh hưởng ML estimator |

Nếu vi phạm nặng: cân nhắc biến đổi dữ liệu (log, căn bậc hai), dùng bootstrap,
hoặc estimator robust (MLR, MLM trong SEM).

### 4. Lỗi nhập sai và dữ liệu trùng

- Kiểm tra **range** từng biến so với codebook (giá trị hợp lệ).
- Kiểm tra **biến đảo chiều (reverse-coded)** đã được mã hóa lại đúng chưa.
- Phát hiện **dòng trùng** (cùng ID/cùng toàn bộ câu trả lời).
- Phát hiện **trả lời ẩu**: straight-lining (chọn cùng một mức cho mọi câu), thời
  gian trả lời quá ngắn, mâu thuẫn logic giữa các câu kiểm tra.

### Ví dụ minh họa

Thang đo Likert 1–5, biến `SAT1`. Sau kiểm tra: có 3 ô trống (1,2%), một giá trị
= 7 (ngoài thang ⇒ lỗi nhập, sửa hoặc xóa), một đáp viên có z = 3.61 trên nhiều
biến. Quyết định: ô trống < 5% và MCAR ⇒ median imputation; giá trị 7 ⇒ kiểm tra
phiếu gốc, không tìm được ⇒ chuyển thành missing; đáp viên z > 3.29 trên nhiều
biến đồng thời straight-lining ⇒ loại, báo cáo "loại 1 đáp viên do trả lời bất
thường".

## Quy trình các bước

1. Xác định N ban đầu, số biến, đọc codebook.
2. Lập bảng missing theo từng biến và từng đáp viên; chạy Little's MCAR test.
3. Quyết định cách xử lý missing theo bảng quyết định ở trên.
4. Phát hiện outlier: lọc ngoài thang đo → z-score → boxplot/IQR → Mahalanobis.
5. Kiểm tra skewness/kurtosis từng biến.
6. Rà lỗi nhập, reverse-coding, dòng trùng, trả lời ẩu.
7. Ghi lại N sau khi làm sạch và mọi quyết định loại bỏ (audit trail).

## Đầu ra

- Bảng thống kê missing (số lượng, %, kết quả Little's test).
- Bảng outlier đã phát hiện và quyết định xử lý.
- Bảng skewness/kurtosis từng biến.
- Một đoạn văn "data screening" cho Chương 4: N ban đầu → N sau làm sạch và lý do.

## Lưu ý

- Mọi quyết định loại đáp viên/biến phải được **ghi lại và biện minh** được; không
  loại tùy tiện để "làm đẹp" kết quả.
- Imputation làm giảm phương sai thật; ưu tiên MI/FIML thay vì thay một giá trị đơn.
- Làm sạch dữ liệu không tạo ra quan hệ nhân quả. Dữ liệu **cắt ngang
  (cross-sectional)** dù sạch đến đâu cũng **không cho phép kết luận nhân quả**.
- Phân biệt **lỗi dữ liệu** (phải sửa) với **biến thiên thật** (phải giữ): không
  phải mọi giá trị cực trị đều là sai.
