# TỔNG HỢP TOÀN BỘ FILE DEMO THỰC HÀNH BUỔI 04 (TRỌN GÓI TẠI CHỖ)

> **Dành cho Giảng viên & Học viên:** Tất cả tài liệu thực hành, file PDF bài báo, dữ liệu CSV và công cụ demo của Buổi 04 ĐÃ ĐƯỢC GOM TRỌN GÓI NGAY TẠI ĐÂY. Bạn không cần phải mở hay tìm kiếm ở bất kỳ thư mục nào khác!

---

## 📂 1. Cấu Trúc Thư Mục Demo Buổi 04

```
04-buoi-04-he-thong-hoa-va-portfolio/demo/
├── 01-bai-bao-pdf/                           # 5 Bài báo khoa học toàn văn dạng PDF (cho Subagent P1A)
│   ├── bai-bao-01-chuyen-doi-so-ai-dnnvv-2026.pdf
│   ├── bai-bao-02-genai-hoc-thuat-nghiencuu-2026.pdf
│   ├── bai-bao-03-dong-luc-ket-qua-hoc-tap-chatgpt.pdf
│   ├── bai-bao-04-tu-hoc-co-dieu-chinh-chatgpt.pdf
│   └── bai-bao-05-liem-chinh-hoc-thuat-chatgpt.pdf
│   (Kèm các bản .md để đối chiếu văn bản)
│
├── 02-du-lieu-va-bao-cao-kiem-toan/         # Dữ liệu khảo sát & Báo cáo phân tích (cho Subagent P1B)
│   ├── khao-sat-doi-moi-dnnvv.csv            # File số liệu khảo sát thực tế (320 mẫu)
│   ├── bao-cao-phan-tich-du-lieu.pdf         # Báo cáo phân tích kết quả dạng PDF
│   └── bao-cao-phan-tich-du-lieu.md          # Báo cáo phân tích kết quả dạng Markdown
│
├── 03-dashboard-artifact/                    # Trực quan hóa dữ liệu nghiên cứu tương tác (Khối 3)
│   ├── dashboard-nghien-cuu-mau.html         # Mở Chrome/Edge xem ngay Dashboard mẫu
│   └── huong-dan-tao-dashboard.md            # Cẩm nang câu lệnh sinh Dashboard
│
└── 04-watermark-tool/                        # Công cụ giải mã & làm sạch Watermark ẩn (Khối 2)
    ├── clean_unicode_watermarks.py           # Script Python quét sạch ký tự vô hình
    └── sample_watermark_text.md              # File mẫu cố tình chèn Unicode ẩn để thử nghiệm
```

---

## 🎯 2. Hướng Dẫn Sử Dụng Nhanh Từng Mục Demo Trong Buổi Học

### Demo 1: Subagent P1A — Trích Xuất 5 Bài Báo Toàn Văn Dạng PDF Thành Ma Trận 1 Trang
* **Vị trí file:** `04-buoi-04-he-thong-hoa-va-portfolio/demo/01-bai-bao-pdf/*.pdf` (hoặc `*.md`)
* **Mục tiêu:** Subagent mở Context riêng, cày xới 5 bài báo toàn văn PDF (~50,000 từ), đốt cháy token trong không gian cách ly và nộp về đúng 1 Ma trận Tổng hợp Lý thuyết 6 cột + 3 khoảng trống nghiên cứu.

---

### Demo 2: Subagent P1B — Kiểm Toán Chéo Dữ Liệu Khảo Sát CSV & Báo Cáo Phân Tích PDF
* **Vị trí file:** `04-buoi-04-he-thong-hoa-va-portfolio/demo/02-du-lieu-va-bao-cao-kiem-toan/`
* **Mục tiêu:** Subagent đóng vai Kiểm toán viên độc lập, đối soát số liệu N=302, Cronbach Alpha 4 thang đo, hệ số hồi quy Beta và rà soát bóc tách các câu vi phạm kỷ luật Hedging.

---

### Demo 3: Thử Nghiệm Script Làm Sạch Unicode Zero-Width (Tẩy Rác AI Watermark)
* **Vị trí file:** `04-buoi-04-he-thong-hoa-va-portfolio/demo/04-watermark-tool/`
* **Thao tác:** Mở Terminal chạy trực tiếp:
  `python 04-buoi-04-he-thong-hoa-va-portfolio/demo/watermark-tool/clean_unicode_watermarks.py 04-buoi-04-he-thong-hoa-va-portfolio/demo/watermark-tool/sample_watermark_text.md`

---

### Demo 4: Mở Dashboard Artifact Tương Tác Nghiên Cứu Mẫu
* **Vị trí file:** `04-buoi-04-he-thong-hoa-va-portfolio/demo/03-dashboard-artifact/dashboard-nghien-cuu-mau.html`
* **Thao tác:** Mở bằng Chrome / Edge để xem bộ lọc ngành, thẻ KPI, sơ đồ Path Model và nút in báo cáo chuẩn A4.
