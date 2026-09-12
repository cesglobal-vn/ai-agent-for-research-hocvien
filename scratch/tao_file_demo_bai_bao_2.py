import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def create_demo_paper_2():
    doc = Document()

    # 1. Page Setup: A4, Top 2cm, Bottom 2cm, Left 3cm, Right 2cm
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(2.0 / 2.54)
        section.bottom_margin = Inches(2.0 / 2.54)
        section.left_margin = Inches(3.0 / 2.54)
        section.right_margin = Inches(2.0 / 2.54)

        # Header
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("TẠP CHÍ NGHIÊN CỨU KHOA HỌC GIÁO DỤC ĐẠI HỌC (JHER) | TẬP 18, SỐ 02/2026")
        hrun.font.name = 'Times New Roman'
        hrun.font.size = Pt(8.5)
        hrun.font.italic = True
        hrun.font.color.rgb = RGBColor(100, 116, 139)

    font_family = 'Times New Roman'

    def format_run(run, size_pt=13, bold=False, italic=False, color_rgb=None):
        run.font.name = font_family
        run.font.size = Pt(size_pt)
        run.bold = bold
        run.italic = italic
        if color_rgb:
            run.font.color.rgb = color_rgb
        rPr = run._r.get_or_add_rPr()
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="{font_family}" w:hAnsi="{font_family}" w:cs="{font_family}"/>')
        rPr.append(rFonts)

    def add_para(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=3, space_after=3, line_spacing=1.5, first_indent=0.5):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = line_spacing
        if first_indent > 0:
            p.paragraph_format.first_line_indent = Inches(first_indent)
        if text:
            r = p.add_run(text)
            format_run(r, size_pt=13)
        return p

    def add_heading_1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.3
        p.paragraph_format.first_line_indent = 0
        r = p.add_run(text)
        format_run(r, size_pt=14, bold=True, color_rgb=RGBColor(15, 23, 42))
        return p

    def add_heading_2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.3
        p.paragraph_format.first_line_indent = 0
        r = p.add_run(text)
        format_run(r, size_pt=13, bold=True, italic=True, color_rgb=RGBColor(30, 41, 59))
        return p

    def style_table_cell(cell, text="", bold=False, align=WD_ALIGN_PARAGRAPH.LEFT, bg_color=None):
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = align
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.first_line_indent = 0
        if text:
            r = p.add_run(text)
            format_run(r, size_pt=10.5, bold=bold)
        if bg_color:
            tcPr = cell._tc.get_or_add_tcPr()
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color}"/>')
            tcPr.append(shd)

    # ------------------ DOCUMENT METADATA ------------------
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_meta.paragraph_format.space_after = Pt(8)
    r_meta = p_meta.add_run("DOI: 10.1016/j.jher.2026.05.021 | Nhận bài: 02/03/2026 | Phản biện duyệt: 19/05/2026 | Xuất bản online: 24/06/2026")
    format_run(r_meta, size_pt=9.5, italic=True, color_rgb=RGBColor(100, 116, 139))

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(12)
    p_title.paragraph_format.line_spacing = 1.3
    r_title = p_title.add_run("CÁC YẾU TỐ ẢNH HƯỞNG ĐẾN Ý ĐỊNH ỨNG DỤNG TRÍ TUỆ NHÂN TẠO TẠO SINH (GENAI) TRONG NGHIÊN CỨU HỌC THUẬT CỦA HỌC VIÊN CAO HỌC TẠI VIỆT NAM")
    format_run(r_title, size_pt=16, bold=True, color_rgb=RGBColor(15, 23, 42))

    # Authors
    p_author = doc.add_paragraph()
    p_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_author.paragraph_format.space_after = Pt(4)
    r_au = p_author.add_run("Trần Minh Hoàng*¹, Vũ Phương Thảo², Đặng Quốc Bảo³\n")
    format_run(r_au, size_pt=12, bold=True)
    r_aff = p_author.add_run("¹Trường Đại học Bách Khoa Hà Nội, Việt Nam\n²Trường Đại học Kinh tế Quốc dân, Hà Nội, Việt Nam\n³Trường Đại học Sư phạm Kỹ thuật TP. Hồ Chí Minh, Việt Nam\n*Tác giả liên hệ: hoang.tm@hust.edu.vn")
    format_run(r_aff, size_pt=10, italic=True, color_rgb=RGBColor(71, 85, 105))

    # Abstract Box
    p_abs_title = doc.add_paragraph()
    p_abs_title.paragraph_format.space_before = Pt(12)
    p_abs_title.paragraph_format.space_after = Pt(2)
    r_abs_t = p_abs_title.add_run("TÓM TẮT")
    format_run(r_abs_t, size_pt=12, bold=True, color_rgb=RGBColor(2, 132, 199))

    add_para(
        "Sự trỗi dậy của các công cụ Trí tuệ nhân tạo tạo sinh (Generative AI - GenAI) như ChatGPT, Claude và Gemini đang định hình lại sâu sắc phương thức làm việc và nghiên cứu trong giáo dục đại học. Nghiên cứu này được thực hiện nhằm kiểm định các nhân tố thúc đẩy và rào cản tác động đến ý định ứng dụng GenAI trong quá trình thực hiện luận văn của học viên cao học tại Việt Nam. Dựa trên mô hình Hợp nhất Chấp nhận và Sử dụng Công nghệ mở rộng (UTAUT2) kết hợp với Thuyết Rủi ro cảm nhận (Perceived Risk Theory), nghiên cứu khảo sát định lượng trên 412 học viên cao học thuộc các khối ngành Kinh tế, Kỹ thuật và Công nghệ thông tin tại Hà Nội và TP.HCM. Phân tích mô hình phương trình cấu trúc bình phương nhỏ nhất từng phần (PLS-SEM) chỉ ra rằng: Hiệu quả kỳ vọng (β = 0.342, p < 0.001) và Động lực hưởng thụ (β = 0.228, p = 0.002) là động lực thúc đẩy mạnh mẽ nhất. Ngược lại, Rủi ro vi phạm liêm chính học thuật (Academic Integrity Risk) tác động tiêu cực đáng kể đến ý định tiếp tục sử dụng (β = -0.215, p = 0.004). Mô hình giải thích được 51,8% sự biến thiên của ý định ứng dụng GenAI. Kết quả này cung cấp cơ sở khoa học quan trọng để các cơ sở giáo dục đại học ban hành khung quy định liêm chính học thuật trong kỷ nguyên AI.",
        first_indent=0.5
    )

    p_kw = add_para("Từ khóa: Trí tuệ nhân tạo tạo sinh (GenAI), UTAUT2, Liêm chính học thuật, Học viên cao học, Nghiên cứu khoa học, Việt Nam.", first_indent=0.5)
    p_kw.runs[0].font.italic = True

    # ------------------ SECTION 1 ------------------
    add_heading_1("I. GIỚI THIỆU & TÍNH CẤP THIẾT CỦA ĐỀ TÀI")
    add_para(
        "Trí tuệ nhân tạo tạo sinh (GenAI) đã tạo ra một bước ngoặt chưa từng có trong lịch sử công nghệ thông tin. Trong môi trường học thuật và nghiên cứu sau đại học, các công cụ GenAI có khả năng hỗ trợ học viên tìm kiếm tài liệu, gợi ý cấu trúc đề cương, tóm tắt bài báo khoa học và hỗ trợ viết mã phân tích dữ liệu chỉ trong vài giây (Dwivedi et al., 2023). Đối với học viên cao học — đối tượng thường xuyên chịu áp lực lớn về thời gian hoàn thành luận văn và công bố bài báo — GenAI được xem như một 'trợ lý ảo' nâng cao năng suất đột phá."
    )
    add_para(
        "Tuy nhiên, việc sử dụng GenAI cũng làm dấy lên những quan ngại sâu sắc về mặt đạo đức nghiên cứu, nguy cơ đạo văn vô thức (unintentional plagiarism), sự phụ thuộc nhận thức và hiện tượng ảo giác thông tin (hallucination) khi AI tự bịa đặt trích dẫn học thuật (Cotton et al., 2024). Tại Việt Nam, nhiều trường đại học hàng đầu vẫn đang trong giai đoạn lúng túng giữa việc cấm đoán hay hướng dẫn sử dụng có kiểm soát. Mặc dù các nghiên cứu trên thế giới đã bước đầu tìm hiểu hành vi dùng AI của sinh viên đại học (Strzelecki, 2023), có rất ít nghiên cứu thực nghiệm khảo sát chuyên sâu đối tượng học viên cao học trong bối cảnh văn hóa học thuật tại Việt Nam."
    )

    # ------------------ SECTION 2 ------------------
    add_heading_1("II. MÔ HÌNH NGHIÊN CỨU & GIẢ THUYẾT")
    add_heading_2("1. Mô hình UTAUT2 mở rộng")
    add_para(
        "Mô hình UTAUT2 của Venkatesh et al. (2012) là một trong những khung lý thuyết có năng lực giải thích hành vi ứng dụng công nghệ mạnh mẽ nhất hiện nay. Nghiên cứu này kế thừa 4 cấu trúc gốc gồm: (1) Hiệu quả kỳ vọng (Performance Expectancy - PE); (2) Nỗ lực kỳ vọng (Effort Expectancy - EE); (3) Ảnh hưởng xã hội (Social Influence - SI); (4) Động lực hưởng thụ (Hedonic Motivation - HM)."
    )

    add_heading_2("2. Cấu trúc mở rộng: Rủi ro vi phạm liêm chính học thuật (AIR)")
    add_para(
        "Để phù hợp với đặc thù nghiên cứu khoa học, nghiên cứu tích hợp thêm biến Rủi ro vi phạm liêm chính học thuật (Academic Integrity Risk - AIR). AIR phản ánh nỗi sợ hãi của học viên về việc bị hội đồng đánh giá đạo văn, bị thu hồi bằng thạc sĩ hoặc chịu chế tài kỷ luật nếu lạm dụng AI không đúng chuẩn mực."
    )

    add_heading_2("3. Hệ thống giả thuyết nghiên cứu")
    add_para(
        "Dựa trên cơ sở lý thuyết, nghiên cứu đề xuất 5 giả thuyết then chốt:\n"
        "• H1: Hiệu quả kỳ vọng (PE) tác động tích cực (+) đến Ý định ứng dụng GenAI (BI).\n"
        "• H2: Nỗ lực kỳ vọng (tính dễ sử dụng) (EE) tác động tích cực (+) đến Ý định ứng dụng GenAI (BI).\n"
        "• H3: Ảnh hưởng xã hội từ giảng viên hướng dẫn và đồng nghiệp (SI) tác động tích cực (+) đến Ý định (BI).\n"
        "• H4: Động lực hưởng thụ và sự tò mò công nghệ (HM) tác động tích cực (+) đến Ý định (BI).\n"
        "• H5: Rủi ro vi phạm liêm chính học thuật (AIR) tác động tiêu cực (-) đến Ý định ứng dụng GenAI (BI)."
    )

    # ------------------ SECTION 3 ------------------
    add_heading_1("III. PHƯƠNG PHÁP NGHIÊN CỨU & MẪU KHẢO SÁT")
    add_para(
        "Khảo sát được thiết kế với thang đo Likert 5 mức độ (1 = Hoàn toàn không đồng ý đến 5 = Hoàn toàn đồng ý), kế thừa từ Venkatesh et al. (2012) và Cotton et al. (2024). Dữ liệu được thu thập từ ngày 01/02/2026 đến 30/04/2026 tại 5 trường đại học lớn: ĐH Bách Khoa Hà Nội, ĐH Kinh tế Quốc dân, ĐH Quốc gia Hà Nội, ĐH Bách Khoa TP.HCM và ĐH Kinh tế TP.HCM."
    )
    add_para(
        "Tổng cộng có 500 phiếu khảo sát được phát ra, thu về 428 phản hồi. Sau khi làm sạch, loại bỏ các phiếu không hợp lệ, mẫu nghiên cứu chính thức gồm N = 412 học viên cao học đang trong giai đoạn làm đề cương hoặc viết luận văn thạc sĩ (đạt tỷ lệ 82,4%)."
    )

    # Table 1: Demographics
    p_t1 = doc.add_paragraph()
    p_t1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t1.paragraph_format.space_before = Pt(8)
    p_t1.paragraph_format.space_after = Pt(3)
    r_t1 = p_t1.add_run("Bảng 1: Cơ cấu mẫu khảo sát học viên cao học (N = 412)")
    format_run(r_t1, size_pt=11.5, bold=True)

    t1 = doc.add_table(rows=6, cols=4)
    t1.alignment = WD_TABLE_ALIGNMENT.CENTER
    t1.autofit = False
    c_widths1 = [Inches(1.8), Inches(1.8), Inches(1.2), Inches(1.2)]
    h1 = ["Đặc điểm nhân khẩu", "Phân nhóm cụ thể", "Số lượng (N)", "Tỷ lệ (%)"]
    for i, h in enumerate(h1):
        style_table_cell(t1.cell(0, i), h, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, bg_color="E2E8F0")

    d1 = [
        ("Khối ngành đào tạo", "Kinh tế & Quản trị kinh doanh", "198", "48,1%"),
        ("Khối ngành đào tạo", "Công nghệ thông tin & Khoa học dữ liệu", "126", "30,6%"),
        ("Khối ngành đào tạo", "Kỹ thuật & Công nghệ khác", "88", "21,3%"),
        ("Địa bàn theo học", "Hà Nội", "245", "59,5%"),
        ("Địa bàn theo học", "TP. Hồ Chí Minh", "167", "40,5%")
    ]
    for r_idx, r_data in enumerate(d1, start=1):
        for c_idx, val in enumerate(r_data):
            align = WD_ALIGN_PARAGRAPH.CENTER if c_idx >= 2 else WD_ALIGN_PARAGRAPH.LEFT
            style_table_cell(t1.cell(r_idx, c_idx), val, align=align)

    for row in t1.rows:
        for i, w in enumerate(c_widths1):
            row.cells[i].width = w

    # ------------------ SECTION 4 ------------------
    add_heading_1("IV. KẾT QUẢ PHÂN TÍCH ĐỊNH LƯỢNG")
    add_heading_2("1. Đánh giá độ tin cậy thang đo (Cronbach's Alpha) & Độ hội tụ")
    add_para(
        "Kết quả phân tích độ tin cậy được thể hiện tại Bảng 2. Tất cả các thang đo đều có hệ số Cronbach's Alpha vượt ngưỡng 0.75, độ tin cậy tổng hợp (Composite Reliability - CR) lớn hơn 0.82 và phương sai trích trung bình (Average Variance Extracted - AVE) lớn hơn 0.50, chứng minh thang đo đạt độ tin cậy và giá trị hội tụ cao."
    )

    # Table 2: Reliability
    p_t2 = doc.add_paragraph()
    p_t2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t2.paragraph_format.space_before = Pt(8)
    p_t2.paragraph_format.space_after = Pt(3)
    r_t2 = p_t2.add_run("Bảng 2: Kết quả kiểm định độ tin cậy và giá trị hội tụ thang đo")
    format_run(r_t2, size_pt=11.5, bold=True)

    t2 = doc.add_table(rows=7, cols=5)
    t2.alignment = WD_TABLE_ALIGNMENT.CENTER
    t2.autofit = False
    c_widths2 = [Inches(1.2), Inches(2.3), Inches(0.9), Inches(0.9), Inches(0.9)]
    h2 = ["Ký hiệu", "Cấu trúc thang đo", "Alpha (α)", "CR", "Mean"]
    for i, h in enumerate(h2):
        style_table_cell(t2.cell(0, i), h, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, bg_color="E2E8F0")

    d2 = [
        ("PE", "Hiệu quả kỳ vọng trong nghiên cứu", "0,895", "0,921", "4,12"),
        ("EE", "Nỗ lực kỳ vọng (tính dễ dùng)", "0,852", "0,894", "3,85"),
        ("SI", "Ảnh hưởng xã hội (GVHD, bạn học)", "0,788", "0,845", "3,60"),
        ("HM", "Động lực hưởng thụ & khám phá", "0,834", "0,881", "3,94"),
        ("AIR", "Rủi ro vi phạm liêm chính học thuật", "0,865", "0,902", "4,25"),
        ("BI", "Ý định ứng dụng GenAI trong luận văn", "0,912", "0,935", "3,98")
    ]
    for r_idx, r_data in enumerate(d2, start=1):
        for c_idx, val in enumerate(r_data):
            align = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [0, 2, 3, 4] else WD_ALIGN_PARAGRAPH.LEFT
            style_table_cell(t2.cell(r_idx, c_idx), val, align=align)

    for row in t2.rows:
        for i, w in enumerate(c_widths2):
            row.cells[i].width = w

    add_heading_2("2. Kết quả kiểm định mô hình cấu trúc (Structural Model)")
    add_para(
        "Mô hình cấu trúc giải thích được R² = 0,518 (51,8%) phương sai của Ý định ứng dụng GenAI (BI), với F = 56,8 (p < 0,001). Kết quả chi tiết kiểm định các giả thuyết:\n"
        "• H1 (PE ➔ BI): β = 0,342; t-value = 6,84; p < 0,001 (Chấp nhận).\n"
        "• H2 (EE ➔ BI): β = 0,165; t-value = 3,12; p = 0,002 (Chấp nhận).\n"
        "• H3 (SI ➔ BI): β = 0,118; t-value = 2,24; p = 0,025 (Chấp nhận).\n"
        "• H4 (HM ➔ BI): β = 0,228; t-value = 4,45; p < 0,001 (Chấp nhận).\n"
        "• H5 (AIR ➔ BI): β = -0,215; t-value = -4,18; p < 0,001 (Chấp nhận)."
    )
    add_para(
        "Điểm phát hiện đặc biệt: Hệ số tác động của Rủi ro vi phạm liêm chính học thuật (AIR) mang dấu âm có ý nghĩa rất mạnh (β = -0.215), chứng minh rằng nỗi sợ bị phát hiện đạo văn hoặc vi phạm quy chế là rào cản tâm lý hàng đầu kìm hãm học viên khai thác AI một cách chính danh."
    )

    # ------------------ SECTION 5 ------------------
    add_heading_1("V. THẢO LUẬN & HÀM Ý GIẢNG DẠY SAU ĐẠI HỌC")
    add_para(
        "Kết quả khẳng định học viên cao học đánh giá rất cao hiệu quả của GenAI trong việc giảm thiểu thời gian đọc tài liệu và viết mã. Tuy nhiên, việc thiếu vắng các văn bản hướng dẫn rõ ràng từ nhà trường khiến học viên phải sử dụng AI trong trạng thái 'lén lút', tiềm ẩn rủi ro nộp các sản phẩm nghiên cứu chứa lỗi ảo giác mà không tự kiểm chứng."
    )
    add_para(
        "Nghiên cứu kiến nghị các trường đại học cần: (1) Ban hành Hướng dẫn chính thức về sử dụng AI có trách nhiệm; (2) Đưa môn học 'Ứng dụng AI Agent & Liêm chính nghiên cứu' vào chương trình đào tạo thạc sĩ/tiến sĩ; (3) Cho phép học viên khai báo minh bạch phần nội dung có sự hỗ trợ của AI."
    )

    # ------------------ SECTION 6 (GÀI RESEARCH GAP) ------------------
    add_heading_1("VI. HẠN CHẾ & KHOẢNG TRỐNG CHO CÁC NGHIÊN CỨU TIẾP THEO")
    add_para(
        "Nghiên cứu có một số hạn chế mở ra khoảng trống nghiên cứu (Research Gap) rất giá trị:\n"
        "1. Hạn chế về phân tầng ngành học: Mẫu khảo sát mới chỉ tập trung vào khối ngành Kinh tế và Kỹ thuật/CNTT (chiếm 100% mẫu), hoàn toàn chưa khảo sát khối ngành Y Dược, Luật học và Khoa học Xã hội & Nhân văn — những nơi có yêu cầu về dữ liệu lâm sàng và quy chuẩn trích dẫn khác biệt rõ rệt.\n"
        "2. Hạn chế về biến đo lường: Đề tài mới chỉ dừng lại ở việc đo lường Ý định (Behavioral Intention), chưa đo lường Hành vi sử dụng thực tế (Actual Usage Behavior) và chưa theo dõi điểm số luận văn thực tế của nhóm dùng AI so với nhóm không dùng.\n"
        "3. Hạn chế về biến can thiệp: Chưa xem xét vai trò của các phần mềm phát hiện AI (AI Detectors) như Turnitin hay GPTZero đối với hành vi né tránh của học viên."
    )

    # ------------------ SECTION 7 (GÀI BẪY CHỐNG BỊA) ------------------
    add_heading_1("VII. TUYÊN BỐ VỀ TÍNH LIÊM CHÍNH VÀ DỮ LIỆU")
    add_para(
        "Nghiên cứu này được phê duyệt bởi Hội đồng Đạo đức Nghiên cứu Khoa học. Nhóm tác giả tuyên bố bài báo CHỈ khảo sát nhận thức và ý định của học viên, hoàn toàn KHÔNG thu thập, KHÔNG lưu trữ và KHÔNG đề cập đến bất kỳ số liệu nào về tỷ lệ học viên bị kỷ luật, đình chỉ luận văn hoặc điểm số học tập cá nhân của người tham gia khảo sát."
    )

    # ------------------ REFERENCES ------------------
    add_heading_1("TÀI LIỆU THAM KHẢO")
    refs = [
        "Cotton, D. R., Cotton, P. A., & Shipway, J. R. (2024). Chatting and cheating: Ensuring academic integrity in the era of ChatGPT. Innovations in Education and Teaching International, 61(2), 228-239. https://doi.org/10.1080/14703297.2023.2190148",
        "Dwivedi, Y. K., Kshetri, N., Hughes, L., Slade, E. L., Jeyaraj, A., Kar, A. K., ... & Wright, R. (2023). Opinion Paper: 'So what if ChatGPT wrote it?' Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research and practice. International Journal of Information Management, 71, Article 102642. https://doi.org/10.1016/j.ijinfomgt.2023.102642",
        "Strzelecki, A. (2023). To use or not to use ChatGPT in higher education? A study on students' acceptance of technology. Interactive Learning Environments, 1-14. https://doi.org/10.1080/10494820.2023.2209881",
        "Venkatesh, V., Thong, J. Y., & Xu, X. (2012). Consumer acceptance and use of information technology: extending the unified theory of acceptance and use of technology. MIS Quarterly, 36(1), 157-178. https://doi.org/10.2307/41410412"
    ]

    for ref in refs:
        p_ref = doc.add_paragraph()
        p_ref.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_ref.paragraph_format.space_before = Pt(3)
        p_ref.paragraph_format.space_after = Pt(3)
        p_ref.paragraph_format.line_spacing = 1.3
        p_ref.paragraph_format.first_line_indent = -Inches(0.5)
        p_ref.paragraph_format.left_indent = Inches(0.5)
        r_ref = p_ref.add_run(ref)
        format_run(r_ref, size_pt=11)

    out_docx = "f:/GitHub/ai-agent-for-research-hocvien/du-lieu-mau/demo/bai-bao-so-02-demo-genai-hoc-thuat-2026.docx"
    doc.save(out_docx)
    print("SUCCESS: Saved demo paper 2 to", out_docx)

    # Export markdown counterpart
    md_lines = []
    for p in doc.paragraphs:
        if p.text.strip():
            md_lines.append(p.text)
    out_md = "f:/GitHub/ai-agent-for-research-hocvien/du-lieu-mau/demo/bai-bao-so-02-demo-genai-hoc-thuat-2026.md"
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(md_lines))
    print("SUCCESS: Saved markdown counterpart to", out_md)

if __name__ == "__main__":
    create_demo_paper_2()
