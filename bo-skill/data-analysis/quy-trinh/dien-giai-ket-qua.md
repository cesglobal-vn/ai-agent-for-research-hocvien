# Diễn giải kết quả nghiên cứu

## Mục tiêu

Đọc và diễn giải đúng output thống kê (bảng hồi quy, trung gian, điều tiết) thành
câu văn học thuật chính xác, phân biệt rõ ý nghĩa thống kê / thực tiễn / lý thuyết,
và tránh khẳng định vượt quá dữ liệu — đặc biệt không suy ra nhân quả từ dữ liệu
cắt ngang. Đây là phần kết quả và thảo luận của Chương 4 và Chương 5.

## Khi nào dùng

- Đã có output (SPSS/AMOS/R/SmartPLS), cần viết thành đoạn văn.
- Cần đọc một bảng hồi quy (β, p, R², VIF).
- Cần diễn giải trung gian một phần/toàn phần.
- Cần viết câu kết quả "chuẩn" mà không suy nhân quả sai.

## Nội dung chuyên môn

### 1. Đọc bảng hồi quy

| Thành phần | Đọc thế nào |
|---|---|
| β (chuẩn hóa) | Hướng (dấu) và độ mạnh tác động; so sánh được giữa các biến |
| B (chưa chuẩn hóa) | Thay đổi của Y khi X tăng 1 đơn vị (theo đơn vị gốc) |
| p (Sig.) | < .05 ⇒ có ý nghĩa thống kê |
| R² | % phương sai của Y được mô hình giải thích |
| Adjusted R² | R² hiệu chỉnh theo số biến — báo cáo cùng R² |
| VIF | Đa cộng tuyến; **< 5** (lý tưởng < 3) là chấp nhận được |
| F (ANOVA của mô hình) | Mô hình tổng thể có ý nghĩa hay không |

Mẫu câu chuẩn: "Lãnh đạo chuyển đổi có tác động dương và có ý nghĩa thống kê đến
gắn kết nhân viên (β = .34, p < .001). Mô hình giải thích được 41% phương sai biến
phụ thuộc (R² = .41, adjusted R² = .39). Các chỉ số VIF dao động 1,2–2,8 (< 5),
cho thấy không có vấn đề đa cộng tuyến nghiêm trọng."

### 2. Ba lớp ý nghĩa cần phân biệt

| Lớp | Câu hỏi | Cách đánh giá |
|---|---|---|
| Ý nghĩa thống kê | Kết quả có do ngẫu nhiên không? | p < .05 |
| Ý nghĩa thực tiễn | Hiệu ứng có đủ lớn để quan tâm? | Effect size (d, η², r, f², β, R²) |
| Ý nghĩa lý thuyết | Đóng góp gì cho lý thuyết/thực tiễn? | Đối chiếu literature, khung lý thuyết |

Cảnh báo: với N lớn, p có thể rất nhỏ trong khi β = .08 (gần như không đáng kể về
thực tiễn). Phải nêu cả ba lớp, không dừng ở p.

### 3. Diễn giải trung gian

- **Trung gian toàn phần (full mediation)**: hiệu ứng gián tiếp (a×b) có ý nghĩa
  (bootstrap 95% CI không chứa 0) **và** đường trực tiếp c' không còn ý nghĩa
  ⇒ M giải thích trọn vẹn quan hệ X–Y.
- **Trung gian một phần (partial mediation)**: cả a×b và c' đều có ý nghĩa ⇒ M chỉ
  giải thích một phần; X vẫn còn tác động trực tiếp.

Mẫu câu: "Hiệu ứng gián tiếp của X lên Y qua M có ý nghĩa (a×b = .21, 95% CI
[.12, .31], không chứa 0). Do đường trực tiếp vẫn có ý nghĩa (c' = .15, p = .03),
hài lòng đóng vai trò **trung gian một phần** trong quan hệ giữa X và Y."

### 4. Câu kết quả "chuẩn" và cách tránh suy nhân quả sai

| Nên viết (mô tả liên hệ) | Tránh viết (ngụ ý nhân quả) |
|---|---|
| "có liên hệ với", "dự báo", "tương quan với" | "gây ra", "dẫn đến", "làm cho" |
| "kết quả ủng hộ giả thuyết H1" | "chứng minh rằng X tạo ra Y" |
| "trong mẫu nghiên cứu này" | khái quát vô điều kiện cho mọi bối cảnh |

Với dữ liệu **cắt ngang**, dùng ngôn ngữ liên hệ/dự báo (predict, associate), nêu
rõ giới hạn không suy nhân quả trong phần Limitations.

### Ví dụ minh họa

Output: β = .27, p = .002, R² = .18, f² = .04 (nhỏ).
Diễn giải đầy đủ: "Quan hệ có ý nghĩa thống kê (p = .002) và ủng hộ H2. Tuy nhiên
độ lớn hiệu ứng nhỏ (f² = .04) và mô hình chỉ giải thích 18% phương sai, nên về
mặt thực tiễn tác động còn khiêm tốn. Vì dữ liệu cắt ngang, kết quả phản ánh liên
hệ chứ không khẳng định X gây ra Y."

## Quy trình các bước

1. Đọc bảng output, xác định β, p, R², adjusted R², VIF, effect size.
2. Đối chiếu từng giả thuyết: ủng hộ hay bị bác bỏ.
3. Viết câu mô tả kết quả thống kê (con số trong ngoặc, đúng định dạng).
4. Bổ sung diễn giải thực tiễn (độ lớn hiệu ứng) và lý thuyết (so literature).
5. Với trung gian: xác định một phần/toàn phần từ a×b và c'.
6. Soát ngôn ngữ: thay mọi câu nhân quả bằng câu liên hệ nếu dữ liệu cắt ngang.
7. Nêu giới hạn diễn giải trong phần Limitations.

## Đầu ra

- Đoạn văn kết quả cho từng giả thuyết (Chương 4).
- Đoạn thảo luận đối chiếu literature và khung lý thuyết (Chương 5).
- Bảng tóm tắt giả thuyết (ủng hộ/bác bỏ) kèm β, p, effect size.
- Ghi chú giới hạn diễn giải (cross-sectional, mẫu, bối cảnh).

## Lưu ý

- **Không suy nhân quả từ dữ liệu cắt ngang**: dùng "liên hệ", "dự báo", "tương
  quan"; tránh "gây ra", "dẫn đến".
- Luôn tách bạch **ý nghĩa thống kê** (p), **ý nghĩa thực tiễn** (effect size) và
  **ý nghĩa lý thuyết** (đóng góp); một kết quả p < .05 chưa chắc quan trọng.
- Không khái quát kết quả vượt khỏi mẫu, bối cảnh và thời điểm nghiên cứu.
- Báo cáo trung thực cả giả thuyết bị bác bỏ; không "uốn" diễn giải để khớp kỳ vọng.
- Trích đúng con số từ output, đúng định dạng (ví dụ p < .001, không viết p = .000).
