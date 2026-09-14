# Buổi 2: Dựng tổng quan tài liệu và báo cáo có trích dẫn từ tài liệu thật

> Cách dùng file này: mỗi phần có hai khúc. Khúc **Lý thuyết** đọc để hiểu mình sắp làm gì và vì sao, có ví von cho dễ nhớ. Khúc **Thao tác** là các bước có sẵn prompt, cứ copy dán vào Claude.
>
> Làm lần lượt, không nhảy cóc. Bước sau dùng kết quả bước trước.
>
> Trước khi bắt đầu: mở VS Code, mở đúng thư mục dự án luận án đã dựng ở buổi 1 (ví dụ `k3-research`), rồi mở panel Claude Code (biểu tượng tia sáng). Có sẵn một tab trình duyệt đăng nhập tài khoản Google.
>
> Sáu phần, đi từ dễ tới khó:
> - Phần A: đặt đề tài thật làm trục cho cả buổi
> - Phần B: cho AI đọc cả kho tài liệu của bạn
> - Phần C: tìm khoảng trống nghiên cứu có bằng chứng
> - Phần D: tổng hợp tài liệu theo chủ đề
> - Phần E: viết báo cáo tổng quan có trích dẫn APA 7
> - Phần F: đóng gói cách xuất báo cáo docx thành một skill riêng
>
> Cuối bài có một Phần mở rộng tùy chọn (Studio NotebookLM) để giảng viên demo hoặc bạn tự làm ở nhà.

## Nhịp buổi

| Phần | Nội dung | Phút | Dạng | Bước |
|---|---|---|---|---|
| A | Đặt đề tài làm trục | 8' | LT 3' + HV 5' | 1-2 |
| B | Cho AI đọc kho tài liệu | 28' | LT 6' + HV 22' | 3-7 |
| C | Tìm khoảng trống có bằng chứng | 20' | LT 6' + HV 14' | 8-10 |
| D | Tổng hợp theo chủ đề | 14' | LT 4' + HV 10' | 11-12 |
| E | Viết báo cáo có trích dẫn | 24' | LT 6' + HV 18' | 13-15 |
| F | Đóng gói thành skill riêng | 12' | LT 4' + HV 8' | 16-17 |
| Chốt | Rà lại sản phẩm | 4' | HV 4' | 18 |
| Mở rộng | Studio NotebookLM (tùy chọn) | - | DEMO / về nhà | 19-23 |

LT = giảng viên nói. HV = học viên tự làm. DEMO = giảng viên làm, học viên xem. Tổng 110 phút phần lõi, còn khoảng 10 phút dự phòng cho buổi 2 tiếng. Phần mở rộng nằm ngoài 120 phút.

---

## PHẦN A. Đặt đề tài thật làm trục cho cả buổi

### Lý thuyết

Buổi trước bạn đã xây xong một văn phòng nghiên cứu: có tờ dặn dò `CLAUDE.md`, có các phòng (thư mục) theo giai đoạn, có sẵn bộ tám skill. Nhưng văn phòng đó đang trống. Hôm nay là ngày dọn vào làm việc thật.

Việc đầu tiên khi dọn vào là treo một tấm biển tên ở cửa: **căn phòng này nghiên cứu về cái gì.** Tấm biển đó chính là **đề tài**, và bạn ghi nó vào `CLAUDE.md`. Ghi rồi thì mọi việc sau đó, mọi câu bạn nhờ Claude, đều xoay quanh đúng đề tài này, không lạc sang chuyện khác.

Vì sao đáng làm ngay: khi `CLAUDE.md` đã có đề tài, bạn không phải nhắc lại chủ đề ở từng câu lệnh nữa. Claude đọc tờ dặn dò trước mỗi phiên, nên nó luôn bám đúng hướng của bạn.

Một hiểu lầm hay gặp: nhiều người nghĩ phải có đề tài thật chuẩn, thật chính xác rồi mới bắt đầu được. Không phải. Chỉ cần một **hướng đủ hẹp** là làm được, và nó sẽ sắc lại dần khi bạn đọc tài liệu. Chưa có hướng thì Bước 2 có sẵn cách nhờ Claude gợi ý để bạn chọn.

### Thao tác

**Bước 1. Kiểm tra văn phòng buổi 1 còn nguyên**

Để làm gì: chắc chắn workspace và bộ skill vẫn sẵn sàng trước khi làm việc thật.

Gõ vào Claude:
```
Hãy liệt kê các skill bạn đang có và xác nhận dự án này đã có CLAUDE.md, cây thư mục và 8 skill.
```

Bạn sẽ thấy: Claude liệt kê tám skill (trong đó có `literature-review`) và xác nhận cây thư mục còn đủ.

Nếu thiếu skill: đóng và mở lại VS Code rồi hỏi lại. Vẫn thiếu thì làm lại bước cài skill ở buổi 1.

---

**Bước 2. Ghi đề tài vào CLAUDE.md**

Để làm gì: treo tấm biển tên cho căn phòng, để cả buổi bám đúng một đề tài.

Đã có đề tài rồi thì gõ vào Claude:
```
Đề tài của tôi: [nghiên cứu ảnh hưởng của chuyển đổi số đến kết quả hoạt động của doanh nghiệp nhỏ và vừa (DNNVV) tại Việt Nam]. Cập nhật mục Đề tài trong CLAUDE.md.
```

Chưa có đề tài thì nhờ Claude gợi ý để chọn:
```
Tôi quan tâm lĩnh vực [quản trị doanh nghiệp và chuyển đổi số trong DNNVV]. Gợi ý 3 đề tài khả thi, mỗi đề tài kèm 1 câu hỏi nghiên cứu, để tôi chọn 1 dùng cho hôm nay. Đừng bịa số liệu, chỉ gợi ý hướng.
```

Bạn sẽ thấy: Claude ghi đề tài vào mục Đề tài trong `CLAUDE.md` (hoặc đưa ra 3 hướng để bạn chọn một).

---

## PHẦN B. Cho AI đọc cả kho tài liệu của bạn

### Lý thuyết

Hình dung bạn có một xấp ba chục bài báo cần đọc. Cách cũ là tự đọc từng bài, tự nhớ bài nào nói gì. Vừa lâu, vừa dễ sót.

Có một trợ lý làm việc này hộ, tên là **NotebookLM, tức một thủ thư chỉ trả lời dựa trên đúng những tài liệu bạn đưa cho nó.** Bạn đưa bài nào, nó đọc bài đó, và khi bạn hỏi thì nó trả lời kèm chỉ rõ câu đó lấy từ nguồn nào. Vì nó chỉ bám tài liệu bạn đưa, nó **ít bịa hơn nhiều** so với hỏi AI chay.

Bình thường bạn phải mở trang web NotebookLM rồi bê từng tài liệu vào bằng tay. Hôm nay ta gắn thêm một cầu nối tên **notebooklm-py, tức một công cụ để Claude Code tự điều khiển NotebookLM bằng lời** thay vì bạn bấm tay. Nhờ nó, bạn chỉ nói một câu là Claude bê cả chồng tài liệu vào và hỏi hộ.

Hai điều cần nhớ:

- **Bạn không cần biết code để cài.** Cứ nhờ Claude cài hộ, y như buổi 1 bạn nhờ nó cài git và python. Nó tự chạy các lệnh cần thiết.
- **Cài xong phải đăng nhập Google một lần** trên trình duyệt. Chỗ này Claude không bấm hộ được, bạn tự đăng nhập.

Nói thẳng một giới hạn: notebooklm-py là công cụ **không chính thức**, chạy nhờ lách vào NotebookLM, nên đôi khi có thể kẹt hoặc bị giới hạn. Kẹt thì đừng mất thời gian, quay lại dùng **NotebookLM bản web** ở `notebooklm.google.com`, mọi bước sau vẫn làm được.

### Thao tác

**Bước 3. Nhờ Claude cài notebooklm-py**

Để làm gì: gắn cầu nối để Claude điều khiển được NotebookLM.

Gõ vào Claude:
```
https://github.com/teng-lin/notebooklm-py

Đọc repo này và cài đặt notebooklm-py cho project này cho tôi, đọc kỹ các hướng dẫn rồi cài đặt MCP server cho tôi luôn. Cần cài đặt hoặc chạy các lệnh gì thì bạn làm luôn cho tôi. Khi xong thì báo tôi kết quả và giải thích ngắn gọn.
```

Bạn sẽ thấy: Claude chạy vài lệnh cài đặt, rồi báo đã cài xong và gắn MCP server (cầu nối) cho Claude Code.

Nếu báo lỗi thiếu Python: gõ `Máy tôi chưa có Python 3.10 trở lên, cài giúp tôi trước rồi cài lại notebooklm-py.` Vẫn kẹt thì bỏ qua phần tự động, dùng NotebookLM web cho các bước sau.

---

**Bước 4. Đăng nhập Google cho NotebookLM**

Để làm gì: cho công cụ quyền dùng tài khoản NotebookLM của bạn.

Gõ vào Claude:
```
Chạy giúp tôi lệnh đăng nhập NotebookLM để tôi đăng nhập Google trên trình duyệt. Xong thì kiểm tra kết nối và báo kết quả cho tôi.
```

Bạn sẽ thấy: một cửa sổ trình duyệt mở ra cho bạn đăng nhập Google. Đăng nhập xong, Claude báo kết nối thành công.

Nếu trình duyệt không mở hoặc báo lỗi đăng nhập: đăng nhập Google trên trình duyệt trước, rồi gõ `Thử kiểm tra lại kết nối NotebookLM.` Vẫn kẹt thì chuyển sang NotebookLM web.

---

**Bước 5. Tìm nguồn thật cho đề tài**

Để làm gì: gom một danh sách bài báo thật để nạp vào, thay vì tài liệu bịa.

Gõ vào Perplexity:
```
Tìm 10 nghiên cứu thực nghiệm (2020-2025) về [chuyển đổi số trong DNNVV Việt Nam], ưu tiên bài bình duyệt, kèm link và năm. Trả về dạng danh sách link.
```

Bạn sẽ thấy: một danh sách khoảng 10 bài kèm link và năm. Bấm thử vài link xem có mở ra bài thật không, bỏ link nào chết.

Mẹo: nếu bạn đã có sẵn vài file PDF của mình, để chúng vào thư mục `du-lieu/tho` để bước sau nạp thêm.

---

**Bước 6. Tạo notebook và nạp cả loạt nguồn**

Để làm gì: đưa toàn bộ tài liệu vào cho thủ thư đọc, chỉ bằng một câu.

Gõ vào Claude:
```
Tạo giúp tôi một notebook tên [Chuyển đổi số DNNVV] và nạp các nguồn sau vào đó: [dán danh sách link từ Perplexity]. Nếu thư mục du-lieu/tho có PDF của tôi thì nạp thêm. Xong báo kết quả cho tôi.
```

Bạn sẽ thấy: Claude tạo notebook và báo đã nạp các nguồn vào.

Nếu một nguồn không nạp được (link chặn tải): bỏ nguồn đó, hoặc tải PDF về `du-lieu/tho` rồi gõ `Nạp thêm các PDF trong thư mục du-lieu/tho vào notebook.`

---

**Bước 7. Xử lý link bị chặn và kiểm tra**

Để làm gì: lấy nốt các bài mà link bị chặn không tải được, rồi rà đủ nguồn.

Gõ vào Claude:
```
Trong các nguồn vừa nạp, link nào bị chặn không tải được thì bạn tự mở bằng browser tích hợp sẵn, lấy nội dung bài, lưu thành file .md trong du-lieu/tho, rồi thêm file đó vào notebook cho tôi. Xong liệt kê lại toàn bộ nguồn trong notebook để tôi kiểm tra.
```

Bạn sẽ thấy: Claude mở các link bị chặn bằng trình duyệt, lưu nội dung thành file trong `du-lieu/tho`, thêm vào notebook, rồi liệt kê lại toàn bộ nguồn. Đối chiếu thiếu thì nạp bù.

---

## PHẦN C. Tìm khoảng trống nghiên cứu có bằng chứng

### Lý thuyết

Hình dung một kệ sách trong thư viện. Đọc lướt qua cả kệ, bạn mới nhận ra có một mảng đề tài chưa ai viết, hoặc mọi người viết rồi nhưng còn bỏ ngỏ một góc. Cái chỗ trống đó chính là **khoảng trống nghiên cứu, tức một câu hỏi mà tài liệu hiện có chưa trả lời trọn.** Tiếng chuyên ngành gọi là research gap.

Điểm mấu chốt: khoảng trống phải **tựa trên bằng chứng thật**, không phải cảm giác của bạn. Bạn tìm ra nó bằng cách hỏi thủ thư NotebookLM: trên đống tài liệu này, cái gì đã có bằng chứng, cái gì còn để ngỏ. Vì thủ thư chỉ trả lời trên nguồn thật và chỉ rõ trích dẫn, khoảng trống bạn rút ra sẽ có chỗ dựa.

Một hiểu lầm hay gặp: tưởng khoảng trống là "cái tôi thấy còn thiếu". Sai. Nó là "cái tài liệu cho thấy còn thiếu". Và một cảnh báo không được bỏ: AI, kể cả khi trả lời, vẫn có thể **bịa tên bài, tác giả, DOI** nghe rất thật. Chưa tự kiểm được nguồn thì chưa đưa vào bài.

### Thao tác

**Bước 8. Hỏi thủ thư: cái gì đã có, cái gì còn bỏ ngỏ**

Để làm gì: lấy bức tranh có bằng chứng, tách rõ phần đã biết và phần còn trống.

Gõ vào Claude:
```
Trên các nguồn trong notebook, cho biết cái gì đã có bằng chứng và cái gì còn bỏ ngỏ về [chuyển đổi số trong DNNVV Việt Nam]. Mỗi ý kèm trích dẫn nguồn. Chỉ dựa trên tài liệu trong notebook, không tự bịa.
```

Bạn sẽ thấy: câu trả lời tách hai phần rõ ràng, phần "đã có bằng chứng" và phần "còn bỏ ngỏ", mỗi ý chỉ về đúng nguồn. Ghi lại các điểm còn bỏ ngỏ.

---

**Bước 9. Tổng hợp theme và phát biểu khoảng trống**

Để làm gì: biến các điểm còn bỏ ngỏ thành một khoảng trống nghiên cứu viết được thành câu hỏi.

Gõ vào Claude:
```
Dùng skill literature-review. Từ kết quả trên, tổng hợp 3-4 theme và phát biểu 3 research gap kèm câu hỏi nghiên cứu cho mỗi gap. Chỉ dùng bằng chứng từ tài liệu đã đọc, không bịa nguồn. Lưu vào tong-quan-tai-lieu/research-gap.md.
```

Bạn sẽ thấy: Claude lưu file `tong-quan-tai-lieu/research-gap.md` gồm 3-4 theme và 3 khoảng trống, mỗi khoảng trống kèm một câu hỏi nghiên cứu.

---

**Bước 10. Kiểm chứng nguồn (bước không được bỏ)**

Để làm gì: chặn nguồn bịa trước khi nó lọt vào bài của bạn.

Gõ vào Claude:
```
Rà lại các nguồn tôi đã dùng ở phần research gap. Chỉ ra nguồn nào đáng nghi bịa (DOI sai định dạng, tạp chí không có thật, tác giả không khớp) và nhắc tôi phải tự kiểm chứng cái nào bằng Google Scholar hoặc DOI.
```

Bạn sẽ thấy: Claude chỉ ra các nguồn cần bạn tự kiểm. Mở Google Scholar, chép tên bài vào tra, đối chiếu tác giả, năm, DOI có khớp không.

Nhớ: đây là kỹ năng sống còn của người nghiên cứu. Cùng lắm để trống một nguồn còn hơn đưa vào một nguồn giả.

---

## PHẦN D. Tổng hợp tài liệu theo chủ đề

### Lý thuyết

Dọn tủ quần áo, không ai kể lể "cái áo này mua ở đâu, cái quần kia ai tặng". Người ta xếp theo loại: áo một ngăn, quần một ngăn. Nhìn vào là thấy mình có gì, thiếu gì.

Tổng quan tài liệu cũng vậy. **Tổng hợp theo chủ đề, tức gom các nghiên cứu cùng hướng lại một nhóm** rồi nói nhóm đó phát hiện chung gì, chỗ nào đồng thuận, chỗ nào mâu thuẫn. Trước khi gom, ta lập một bảng gọi là **ma trận tài liệu, tức bảng mỗi dòng một nghiên cứu**, để nhìn cả kho trong một trang.

Vì sao đáng làm: khi xếp theo chủ đề, khoảng trống tự lộ ra, vì bạn thấy ngay chủ đề nào ai cũng làm rồi và chủ đề nào còn mỏng.

Một hiểu lầm hay gặp: tổng quan không phải là tóm tắt lần lượt từng bài, kiểu "bài 1 nói..., bài 2 nói...". Đó chỉ là danh sách. Tổng quan thật là gom theo chủ đề và so sánh giữa các bài.

### Thao tác

**Bước 11. Lập ma trận tài liệu**

Để làm gì: nhìn cả kho tài liệu trong một bảng, mỗi dòng một nghiên cứu.

Gõ vào Claude:
```
Dùng skill literature-review. Lập ma trận các nguồn đã chọn, mỗi dòng một nghiên cứu, các cột: tác giả/năm, bối cảnh, thiết kế, cỡ mẫu, phương pháp, phát hiện chính, hạn chế. Chỉ điền từ tài liệu thật, chỗ nào không rõ thì để trống, không bịa. Lưu vào tong-quan-tai-lieu/ma-tran-tai-lieu.md.
```

Bạn sẽ thấy: file `ma-tran-tai-lieu.md` là một bảng, mỗi nghiên cứu một dòng, các ô đã điền theo tài liệu.

---

**Bước 12. Dựng dàn ý tổng quan theo chủ đề**

Để làm gì: biến ma trận thành một dàn ý xếp theo chủ đề, sẵn để viết.

Gõ vào Claude:
```
Từ ma trận, lập dàn ý tổng quan tài liệu theo chủ đề, mỗi mục ghi ý chính và các nguồn sẽ trích cho mục đó. Lưu vào tong-quan-tai-lieu/dan-y-tong-quan.md.
```

Bạn sẽ thấy: file `dan-y-tong-quan.md` chia theo vài chủ đề lớn, mỗi chủ đề ghi ý chính và các nguồn thuộc chủ đề đó.

---

## PHẦN E. Viết báo cáo tổng quan có trích dẫn APA 7

### Lý thuyết

Viết báo cáo học thuật giống khai thuế: mỗi con số, mỗi khẳng định đều phải có hóa đơn kèm. Hóa đơn ở đây là **trích dẫn, tức chỉ rõ khẳng định này lấy từ tác giả nào, năm nào.** Chuẩn phổ biến ở Việt Nam là **APA phiên bản 7**, viết trong bài dạng `(Tác giả, năm)` và liệt kê đầy đủ ở mục Tài liệu tham khảo cuối bài.

Vì sao đáng làm đúng ngay từ đầu: một báo cáo có trích dẫn khớp và kiểm chứng được thì gửi giảng viên hướng dẫn hay nộp hội đồng đều đứng vững. Trích dẫn lộn xộn thì mất điểm tin cậy ngay.

Một hiểu lầm hay gặp, và là chỗ nguy hiểm nhất: AI viết trích dẫn nghe **rất thật** nhưng có thể hoàn toàn bịa. Vì vậy quy tắc trong dự án này là nguồn nào chưa tự kiểm chứng được thì đánh dấu `[CẦN NGUỒN]`, để trống chờ bạn kiểm, tuyệt đối không để AI tự điền một nguồn nghe hợp lý.

### Thao tác

**Bước 13. Viết phần tổng quan tài liệu**

Để làm gì: có một bản báo cáo tổng quan viết theo văn phong học thuật, đúng đề tài.

Gõ vào Claude:
```
Dùng skill academic-writing. Viết phần "Tổng quan tài liệu" khoảng 1200 từ theo dàn ý trong tong-quan-tai-lieu/dan-y-tong-quan.md, văn phong học thuật tiếng Việt, tổng hợp theo chủ đề (không liệt kê từng bài). Trích dẫn trong bài theo APA 7 dạng (Tác giả, năm). Nguồn nào chưa kiểm chứng thì đánh dấu [CẦN NGUỒN], không tự bịa nguồn. Cuối bài có mục Tài liệu tham khảo theo APA 7. Lưu thành file tong-quan-tai-lieu/bao-cao-tong-quan-tai-lieu.md.
```

Bạn sẽ thấy: file `tong-quan-tai-lieu/bao-cao-tong-quan-tai-lieu.md` gồm phần tổng quan viết liền mạch theo chủ đề, có trích dẫn trong bài và danh mục tài liệu tham khảo ở cuối, các chỗ chưa chắc để `[CẦN NGUỒN]`.

---

**Bước 14. Rà lại trích dẫn cho khớp**

Để làm gì: chắc chắn mọi trích dẫn trong bài đều có trong danh mục và ngược lại.

Gõ vào Claude:
```
Dùng skill citation-manager. Rà phần vừa viết: mọi trích dẫn trong bài phải có trong danh mục tài liệu tham khảo và ngược lại, đúng định dạng APA 7. Liệt kê các chỗ chưa khớp và các chỗ còn [CẦN NGUỒN].
```

Bạn sẽ thấy: một danh sách các chỗ chưa khớp hoặc còn thiếu nguồn để bạn sửa. Tự kiểm các nguồn còn `[CẦN NGUỒN]` bằng Google Scholar trước khi coi là xong.

---

**Bước 15. Xuất ra Word đúng format chuẩn**

Để làm gì: có một file Word đúng format báo cáo nghiên cứu để gửi giảng viên hướng dẫn. Chọn 1 trong 2 hướng.

Hướng 1 - chưa có file mẫu, tự áp format chuẩn Việt Nam. Gõ vào Claude:
```
Xuất bản báo cáo bao-cao-tong-quan-tai-lieu.md thành file Word (.docx) để tôi gửi giảng viên hướng dẫn, trình bày đúng format báo cáo nghiên cứu chuẩn Việt Nam. Bạn tự research format chuẩn; tối thiểu phải đạt: A4, Times New Roman cỡ 13, giãn dòng 1.5, lề trên 2cm dưới 2cm trái 3cm phải 2cm, căn đều hai bên, đánh số trang, Tài liệu tham khảo APA 7. Cần cài công cụ gì thì cài giúp tôi, xong báo tôi đường dẫn file.
```

Hướng 2 - đã có file mẫu chuẩn của trường (.docx hoặc .pdf). Gõ vào Claude:
```
Tôi có một file báo cáo mẫu đúng chuẩn định dạng của trường tôi ở [phu-luc/mau-bao-cao-truong.docx]. Hãy xuất file bao-cao-tong-quan-tai-lieu.md ra Word (.docx) sao cho định dạng (font, cỡ chữ, giãn dòng, lề, kiểu tiêu đề, cách đánh số) giống file mẫu đó. Nếu file mẫu là PDF thì đọc và mô phỏng lại định dạng của nó. Cần cài công cụ gì thì cài giúp tôi, xong báo tôi đường dẫn file kết quả.
```

Bạn sẽ thấy: Claude tạo file `.docx` đúng format và báo đường dẫn. Mở file kiểm lại font, lề, bảng biểu.

Mẹo: format thân bài (cỡ 13 hay 14, lề) khác nhau tùy trường. Có file mẫu của trường thì dùng Hướng 2 cho chính xác.

---

## PHẦN F. Đóng gói việc lặp thành một skill riêng

### Lý thuyết

Xuất báo cáo ra Word đúng format chuẩn không phải làm một lần. Suốt luận án, chương nào viết xong bạn cũng phải xuất lại đúng font, đúng lề, đúng cách trích dẫn. Mỗi lần dặn Claude lại từ đầu thì mất công, mà kết quả không đều tay.

**Skill là một công thức nấu ăn viết sẵn:** đóng gói cách làm một việc một lần, lần sau gọi tên là nó làm đúng chuẩn của bạn, không phải nghĩ lại. Ta sẽ đóng gói chính cách xuất docx vừa làm ở Phần E thành một skill. Bạn để skill ở `.claude/skills/<tên>/SKILL.md` ngay trong thư mục dự án, nằm cạnh tám skill có sẵn.

Vì sao đáng làm: lần sau chỉ cần nói "tạo file docx chuẩn báo cáo nghiên cứu" là Claude làm đúng format bạn đã chốt, không phải dặn lại cả bộ font, lề, trích dẫn.

Hai điều cần nhớ để khỏi kẹt:

- **Tên skill chỉ dùng chữ thường và gạch nối,** không chứa từ "claude" hay "anthropic".
- **Tạo xong phải đóng và mở lại VS Code** thì Claude mới nạp skill mới.

### Thao tác

**Bước 16. Nhờ Claude đóng gói cách xuất docx thành skill**

Để làm gì: lần sau chỉ nói một câu là Claude xuất docx đúng format, không phải dặn lại.

Gõ vào Claude:
```
Tôi vừa xuất một file docx chuẩn báo cáo nghiên cứu. Hãy đóng gói cách làm đó thành một skill, để sau này tôi chỉ cần nói "tạo giúp tôi file docx chuẩn báo cáo nghiên cứu" là bạn làm đúng và có file word đúng format như vầy.
```

Bạn sẽ thấy: Claude báo đã tạo file `SKILL.md` trong `.claude/skills/` và giải thích skill làm gì, khi nào gọi.

---

**Bước 17. Chạy thử skill**

Để làm gì: chắc chắn skill hoạt động khi bạn gọi tên.

Đóng và mở lại VS Code trước, rồi gõ vào Claude (gọi đúng tên skill Claude vừa đặt):
```
Dùng skill /... để xuất file ... ra Word đúng format chuẩn cho tôi.
```

Bạn sẽ thấy: Claude gọi đúng skill và tạo lại file `.docx` đúng format.

Nếu báo không tìm thấy skill: kiểm tra thư mục nằm trong `.claude/skills/`, file có đủ hai dòng ba dấu gạch bao quanh phần khai báo, rồi đóng mở lại VS Code và thử lại.

---

## Chốt buổi

**Bước 18. Rà lại các sản phẩm hôm nay**

Để làm gì: gom danh sách sản phẩm hôm nay để bạn kiểm cho đủ.

Gõ vào Claude:
```
Liệt kê các file sản phẩm tôi đã tạo hôm nay trong dự án và vị trí của chúng.
```

Bạn sẽ thấy: danh sách các file trong `tong-quan-tai-lieu/`, bản `.docx`, và skill mới trong `.claude/skills/`.

---

## PHẦN MỞ RỘNG (tùy chọn) - Khai thác Studio của NotebookLM

> Phần này ngoài 120 phút lõi. Giảng viên demo, hoặc bạn tự làm ở nhà. Còn giờ thì làm ngay ở lớp.

### Lý thuyết

Cùng một kho tài liệu trong notebook, NotebookLM có một "xưởng chế biến" tên **Studio** biến nó thành nhiều sản phẩm khác nhau: mind map, slide, bảng dữ liệu, báo cáo, bản tóm tắt dạng podcast. Qua notebooklm-py, bạn nhờ Claude gọi các món này rồi làm tiếp ngay trong workspace.

Nói thẳng giới hạn: các món này chạy qua công cụ không chính thức nên có thể chậm hoặc kẹt; audio mất vài phút. Kẹt thì bấm tay ngay trong Studio của NotebookLM web.

### Thao tác

**Bước 19. Mind map rồi bung thành dàn ý**

Để làm gì: có một bản đồ chủ đề trực quan, rồi biến nó thành dàn ý.

Gõ vào Claude:
```
Trên notebook hiện tại, tạo giúp tôi một mind map tổng hợp các chủ đề chính, rồi từ mind map đó bung thành một dàn ý chi tiết cho phần tổng quan.
```

Bạn sẽ thấy: Claude tạo mind map trong Studio và trả về một dàn ý chi tiết theo các nhánh của mind map.

---

**Bước 20. Slide deck để trình bày**

Để làm gì: có sẵn bộ slide để báo cáo với giảng viên.

Gõ vào Claude:
```
Tạo một slide deck tóm tắt tổng quan tài liệu và các research gap từ notebook này. Tải file slide (.pptx) về lưu vào tong-quan-tai-lieu/slide-tong-quan.pptx để tôi trình bày với giảng viên.
```

Bạn sẽ thấy: Claude tạo slide trong Studio và tải file `.pptx` về `tong-quan-tai-lieu/`.

---

**Bước 21. Data Table rồi đối chiếu với ma trận**

Để làm gì: lấy bảng trích xuất của NotebookLM để kiểm chéo ma trận của bạn.

Gõ vào Claude:
```
Dùng tính năng Data Table của notebook để trích xuất từ các nguồn thành bảng: tác giả, năm, phương pháp, cỡ mẫu, phát hiện chính. Rồi đối chiếu với file ma-tran-tai-lieu.md của tôi và chỉ ra chỗ nào khác nhau.
```

Bạn sẽ thấy: một bảng trích xuất và danh sách các chỗ khác nhau so với ma trận bạn tự lập.

---

**Bước 22. Report của NotebookLM làm bản đối chiếu**

Để làm gì: có một báo cáo grounded để soi lại báo cáo bạn tự viết.

Gõ vào Claude:
```
Tạo một Tailored Report từ notebook này về [chuyển đổi số trong DNNVV Việt Nam], rồi đối chiếu với báo cáo tôi tự viết và chỉ ra điểm khác biệt.
```

Bạn sẽ thấy: một báo cáo do NotebookLM dựng và danh sách các điểm khác so với bản của bạn.

---

**Bước 23. Audio Overview để nghe lại**

Để làm gì: có bản tóm tắt dạng podcast để nghe khi di chuyển.

Gõ vào Claude:
```
Tạo một Audio Overview (bản tóm tắt dạng podcast) cho notebook này.
```

Bạn sẽ thấy: Claude tạo một bản audio tóm tắt trong Studio (mất vài phút).

---

## Xong buổi 2, kiểm lại bạn đã có

Tự tay làm được:
- [ ] Đề tài thật ghi trong `CLAUDE.md`
- [ ] Một notebook đã nạp nhiều nguồn thật (qua notebooklm-py hoặc NotebookLM web)
- [ ] File `tong-quan-tai-lieu/research-gap.md` đã kiểm chứng nguồn
- [ ] File `ma-tran-tai-lieu.md` và `dan-y-tong-quan.md`, tổng hợp theo chủ đề
- [ ] File `bao-cao-tong-quan-tai-lieu.md` và bản `.docx`, trích dẫn APA 7
- [ ] Một skill riêng xuất docx chuẩn trong `.claude/skills/`, đã chạy thử được

Hiểu để dùng sau:
- [ ] Vì sao hỏi trên tài liệu thật (có nguồn) thì ít bịa hơn hỏi AI chay
- [ ] notebooklm-py là công cụ không chính thức, kẹt thì quay lại NotebookLM web; và kiểm chứng nguồn vẫn luôn là việc của bạn

Thiếu mục nào thì làm lại đúng bước đó. Buổi sau ta đổ dữ liệu khảo sát thật vào thư mục `du-lieu` và học cách phân tích rồi viết báo cáo kết quả có khai báo dùng AI.
