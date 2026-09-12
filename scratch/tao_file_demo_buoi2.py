import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def create_demo_paper():
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
        hrun = hp.add_run("TẠP CHÍ KINH TẾ & PHÁT TRIỂN KHOA HỌC (JEDS) | SỐ 04/2026 - ISSN: 2815-5939")
        hrun.font.name = 'Times New Roman'
        hrun.font.size = Pt(8.5)
        hrun.font.italic = True
        hrun.font.color.rgb = RGBColor(100, 116, 139)

    font_family = 'Times New Roman'

    # Helper function for setting font
    def format_run(run, size_pt=13, bold=False, italic=False, color_rgb=None):
        run.font.name = font_family
        run.font.size = Pt(size_pt)
        run.bold = bold
        run.italic = italic
        if color_rgb:
            run.font.color.rgb = color_rgb
        # ensure XML font tag
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

    # ------------------ DOCUMENT CONTENT ------------------

    # Meta tags
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_meta.paragraph_format.space_after = Pt(8)
    r_meta = p_meta.add_run("DOI: 10.5939/jeds.2026.04.12 | Ngày nhận bài: 15/04/2026 | Ngày duyệt đăng: 28/06/2026")
    format_run(r_meta, size_pt=9.5, italic=True, color_rgb=RGBColor(100, 116, 139))

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(12)
    p_title.paragraph_format.line_spacing = 1.3
    r_title = p_title.add_run("TÁC ĐỘNG CỦA CHUYỂN ĐỔI SỐ VÀ ỨNG DỤNG TRÍ TUỆ NHÂN TẠO (AI) ĐẾN KẾT QUẢ HOẠT ĐỘNG CỦA CÁC DOANH NGHIỆP NHỎ VÀ VỪA TẠI VIỆT NAM")
    format_run(r_title, size_pt=16, bold=True, color_rgb=RGBColor(15, 23, 42))

    # Authors
    p_author = doc.add_paragraph()
    p_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_author.paragraph_format.space_after = Pt(4)
    r_au1 = p_author.add_run("Nguyễn Hoàng Nam*¹, Lê Thu Trang², Trần Đình Phúc³\n")
    format_run(r_au1, size_pt=12, bold=True)
    r_aff = p_author.add_run("¹Trường Đại học Kinh tế Quốc dân, Hà Nội, Việt Nam\n²Viện Quốc tế, Đại học Quốc gia Hà Nội, Việt Nam\n³Trường Đại học Kinh tế TP. Hồ Chí Minh, Việt Nam\n*Tác giả liên hệ: nam.nh@neu.edu.vn")
    format_run(r_aff, size_pt=10, italic=True, color_rgb=RGBColor(71, 85, 105))

    # Abstract Box
    p_abs_title = doc.add_paragraph()
    p_abs_title.paragraph_format.space_before = Pt(12)
    p_abs_title.paragraph_format.space_after = Pt(2)
    r_abs_t = p_abs_title.add_run("TÓM TẮT")
    format_run(r_abs_t, size_pt=12, bold=True, color_rgb=RGBColor(2, 132, 199))

    # NOTE FOR DEMO: Gài con số 350 ở đây trong khi Bảng 2 là 356 (vênh số 6 doanh nghiệp)
    p_abs = add_para(
        "Nghiên cứu này nhằm mục đích khám phá và kiểm định tác động của chuyển đổi số cùng mức độ ứng dụng trí tuệ nhân tạo (AI) đến kết quả hoạt động kinh doanh (cả về khía cạnh tài chính và phi tài chính) của các doanh nghiệp nhỏ và vừa (DNNVV) tại Việt Nam. Dựa trên việc tích hợp mô hình Khung Công nghệ - Tổ chức - Môi trường (TOE) và Thuyết Dựa vào Nguồn lực (RBV), nghiên cứu xây dựng mô hình giả thuyết đa biến. Dữ liệu thực nghiệm được thu thập thông qua khảo sát có cấu trúc trên 350 doanh nghiệp nhỏ và vừa hoạt động trong các lĩnh vực dịch vụ, sản xuất và bán lẻ tại Hà Nội, TP.HCM và Đà Nẵng. Kết quả phân tích hồi quy tuyến tính bội (OLS) và mô hình phương trình cấu trúc (PLS-SEM) chỉ ra rằng năng lực hạ tầng công nghệ số và mức độ ứng dụng AI có tác động cùng chiều mạnh mẽ đến kết quả hoạt động doanh nghiệp (β = 0.384, p < 0.01). Đồng thời, nhận thức của lãnh đạo đóng vai trò điều tiết then chốt. Dựa trên các phát hiện, nghiên cứu đề xuất một số hàm ý chính sách và giải pháp quản trị thực tiễn giúp DNNVV tối ưu hóa lộ trình chuyển đổi số trong kỷ nguyên AI.",
        first_indent=0.5
    )

    p_kw = add_para("Từ khóa: Chuyển đổi số, Trí tuệ nhân tạo (AI), Doanh nghiệp nhỏ và vừa (DNNVV), Mô hình TOE, Kết quả hoạt động kinh doanh, Việt Nam.", first_indent=0.5)
    p_kw.runs[0].font.italic = True

    # ------------------ SECTION 1 ------------------
    add_heading_1("I. GIỚI THIỆU & ĐẶT VẤN ĐỀ NGHIÊN CỨU")
    add_para(
        "Khu vực doanh nghiệp nhỏ và vừa (DNNVV) đóng vai trò là động lực tăng trưởng kinh tế then chốt tại các nền kinh tế đang phát triển, trong đó có Việt Nam. Theo thống kê của Bộ Kế hoạch và Đầu tư (2025), DNNVV chiếm hơn 97% tổng số doanh nghiệp đang hoạt động, đóng góp khoảng 45% GDP và tạo ra hơn 50% việc làm cho lực lượng lao động xã hội. Tuy nhiên, trước làn sóng cách mạng công nghiệp lần thứ tư và sự bùng nổ của trí tuệ nhân tạo tạo sinh (Generative AI), các DNNVV Việt Nam đang phải đối mặt với áp lực cạnh tranh khốc liệt và nguy cơ bị tụt hậu nếu không kịp thời chuyển đổi mô hình vận hành."
    )
    add_para(
        "Mặc dù chuyển đổi số được nhận định là chìa khóa gia tăng năng suất và mở rộng thị trường, việc ứng dụng các giải pháp công nghệ cao như AI trong khối DNNVV vẫn còn rất khiêm tốn. Khảo sát gần đây của Hiệp hội Doanh nghiệp nhỏ và vừa Việt Nam (2025) cho thấy chỉ có khoảng 18,5% DNNVV đã từng thử nghiệm các công cụ AI trong quy trình bán hàng hoặc quản lý vận hành. Nguyên nhân chủ yếu xuất phát từ hạn chế về nguồn vốn, năng lực số của đội ngũ nhân sự và sự e dè về an toàn bảo mật dữ liệu."
    )
    add_para(
        "Mặc dù đã có nhiều công trình học thuật nghiên cứu về chuyển đổi số (Nguyễn & Trần, 2023; Pham et al., 2024), phần lớn các nghiên cứu này mới chỉ tập trung vào các tập đoàn lớn hoặc ngân hàng thương mại. Rất ít nghiên cứu định lượng chuyên sâu xem xét trực tiếp tác động đồng thời của hạ tầng số và mức độ ứng dụng AI đến hiệu quả hoạt động tổng thể của DNNVV trong bối cảnh các đô thị trọng điểm tại Việt Nam. Đây chính là khoảng trống nghiên cứu mà bài viết này hướng tới giải quyết."
    )

    # ------------------ SECTION 2 ------------------
    add_heading_1("II. CƠ SỞ LÝ THUYẾT & PHÁT TRIỂN GIẢ THUYẾT")
    add_heading_2("1. Khung Công nghệ - Tổ chức - Môi trường (Khung TOE)")
    add_para(
        "Khung TOE do Tornatzky và Fleischer (1990) đề xuất là nền tảng lý thuyết vững chắc để giải thích quá trình chấp nhận và ứng dụng công nghệ trong tổ chức. Khung này bao gồm ba bối cảnh: (1) Bối cảnh công nghệ (Technology) phản ánh mức độ sẵn sàng của hạ tầng và tính tương thích của công nghệ mới; (2) Bối cảnh tổ chức (Organization) bao gồm quy mô, nguồn lực và sự ủng hộ của lãnh đạo; (3) Bối cảnh môi trường (Environment) đề cập đến áp lực cạnh tranh trên thị trường và sự hỗ trợ của chính sách công."
    )

    add_heading_2("2. Thuyết Dựa vào Nguồn lực (Resource-Based View - RBV)")
    add_para(
        "Theo thuyết RBV của Barney (1991), một doanh nghiệp có thể tạo dựng và duy trì lợi thế cạnh tranh bền vững khi sở hữu các nguồn lực có giá trị, hiếm, khó sao chép và được tổ chức khai thác hiệu quả (VRIN). Trong thời đại số, dữ liệu và năng lực ứng dụng AI được coi là các tài sản chiến lược vô hình giúp doanh nghiệp tối ưu hóa chi phí vận hành, cải thiện trải nghiệm khách hàng và phản ứng linh hoạt trước biến động thị trường."
    )

    add_heading_2("3. Các giả thuyết nghiên cứu")
    add_para(
        "Dựa trên việc kế thừa khung TOE và thuyết RBV, nghiên cứu này đề xuất 4 giả thuyết chính sau đây:\n"
        "• Giả thuyết H1: Năng lực hạ tầng công nghệ số có tác động tích cực (+) đến mức độ ứng dụng AI trong doanh nghiệp.\n"
        "• Giả thuyết H2: Nhận thức và sự cam kết của lãnh đạo có tác động tích cực (+) đến mức độ ứng dụng AI trong doanh nghiệp.\n"
        "• Giả thuyết H3: Áp lực cạnh tranh từ thị trường thúc đẩy (+) quyết định ứng dụng AI của DNNVV.\n"
        "• Giả thuyết H4: Mức độ ứng dụng AI có tác động tích cực (+) đến kết quả hoạt động kinh doanh tổng thể của DNNVV."
    )

    # ------------------ SECTION 3 ------------------
    add_heading_1("III. PHƯƠNG PHÁP NGHIÊN CỨU & MẪU KHẢO SÁT")
    add_heading_2("1. Quy trình thu thập dữ liệu")
    add_para(
        "Nghiên cứu sử dụng phương pháp khảo sát định lượng thông qua bảng hỏi cấu trúc kết hợp hình thức trực tuyến (Google Form) và trực tiếp. Đối tượng khảo sát là các chủ doanh nghiệp, giám đốc điều hành, trưởng bộ phận kinh doanh hoặc công nghệ tại các DNNVV. Bảng câu hỏi sử dụng thang đo Likert 5 điểm, từ 1 ('Hoàn toàn không đồng ý') đến 5 ('Hoàn toàn đồng ý')."
    )
    add_para(
        "Thời gian thu thập dữ liệu thực địa diễn ra liên tục từ ngày 15/03/2026 đến ngày 30/06/2026 tại ba địa bàn kinh tế trọng điểm: Hà Nội, TP. Hồ Chí Minh và TP. Đà Nẵng. Tổng số phiếu phát ra là 450 phiếu. Sau khi làm sạch, sàng lọc và loại bỏ 26 phiếu điền thiếu thông tin hoặc chọn cùng một phương án cho mọi câu hỏi, tổng số phiếu hợp lệ đưa vào phân tích thống kê chính thức là N = 356 doanh nghiệp (đạt tỷ lệ phản hồi hiệu dụng 79,1%)."
    )

    # Table 1: Demographics
    p_t1_title = doc.add_paragraph()
    p_t1_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t1_title.paragraph_format.space_before = Pt(8)
    p_t1_title.paragraph_format.space_after = Pt(3)
    r_t1 = p_t1_title.add_run("Bảng 1: Cơ cấu mẫu khảo sát thực tế (N = 356)")
    format_run(r_t1, size_pt=11.5, bold=True)

    table1 = doc.add_table(rows=7, cols=4)
    table1.alignment = WD_TABLE_ALIGNMENT.CENTER
    table1.autofit = False

    col_widths = [Inches(1.8), Inches(1.8), Inches(1.2), Inches(1.2)]
    headers1 = ["Tiêu chí phân loại", "Nhóm cụ thể", "Số lượng (N)", "Tỷ lệ (%)"]
    for i, h in enumerate(headers1):
        style_table_cell(table1.cell(0, i), h, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, bg_color="E2E8F0")

    data1 = [
        ("Địa bàn hoạt động", "Hà Nội", "184", "51,7%"),
        ("Địa bàn hoạt động", "TP. Hồ Chí Minh", "142", "39,9%"),
        ("Địa bàn hoạt động", "TP. Đà Nẵng", "30", "8,4%"),
        ("Ngành nghề kinh doanh", "Dịch vụ & Du lịch", "156", "43,8%"),
        ("Ngành nghề kinh doanh", "Thương mại & Bán lẻ", "118", "33,1%"),
        ("Ngành nghề kinh doanh", "Sản xuất & Chế biến", "82", "23,1%")
    ]
    for row_idx, row_data in enumerate(data1, start=1):
        for col_idx, text in enumerate(row_data):
            align = WD_ALIGN_PARAGRAPH.CENTER if col_idx >= 2 else WD_ALIGN_PARAGRAPH.LEFT
            style_table_cell(table1.cell(row_idx, col_idx), text, align=align)

    for row in table1.rows:
        for i, w in enumerate(col_widths):
            row.cells[i].width = w

    # ------------------ SECTION 4 ------------------
    add_heading_1("IV. KẾT QUẢ PHÂN TÍCH ĐỊNH LƯỢNG")
    add_heading_2("1. Kiểm định độ tin cậy thang đo (Cronbach's Alpha)")
    add_para(
        "Theo Hair et al. (2019), độ tin cậy của thang đo được coi là đạt yêu cầu khi hệ số Cronbach's Alpha lớn hơn 0.7 và hệ số tương quan biến - tổng (Corrected Item-Total Correlation) lớn hơn 0.3. Kết quả tính toán từ phần mềm thống kê thể hiện rõ qua Bảng 2."
    )

    # Table 2: Reliability
    p_t2_title = doc.add_paragraph()
    p_t2_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t2_title.paragraph_format.space_before = Pt(8)
    p_t2_title.paragraph_format.space_after = Pt(3)
    r_t2 = p_t2_title.add_run("Bảng 2: Kết quả kiểm định thang đo và hệ số Cronbach's Alpha")
    format_run(r_t2, size_pt=11.5, bold=True)

    table2 = doc.add_table(rows=6, cols=5)
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER
    table2.autofit = False

    col_widths2 = [Inches(1.2), Inches(2.2), Inches(0.9), Inches(1.1), Inches(1.1)]
    headers2 = ["Ký hiệu biến", "Tên cấu trúc thang đo", "Số biến q/s", "Alpha (α)", "Trung bình (Mean)"]
    for i, h in enumerate(headers2):
        style_table_cell(table2.cell(0, i), h, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, bg_color="E2E8F0")

    data2 = [
        ("DTC", "Năng lực hạ tầng công nghệ số", "4", "0,882", "3,65"),
        ("LD", "Nhận thức và cam kết của lãnh đạo", "4", "0,845", "3,92"),
        ("CP", "Áp lực cạnh tranh từ môi trường", "3", "0,791", "4,10"),
        ("AIA", "Mức độ ứng dụng Trí tuệ nhân tạo (AI)", "5", "0,864", "3,48"),
        ("FP", "Kết quả hoạt động kinh doanh (DN)", "5", "0,905", "3,78")
    ]
    for row_idx, row_data in enumerate(data2, start=1):
        for col_idx, text in enumerate(row_data):
            align = WD_ALIGN_PARAGRAPH.CENTER if col_idx in [0, 2, 3, 4] else WD_ALIGN_PARAGRAPH.LEFT
            style_table_cell(table2.cell(row_idx, col_idx), text, align=align)

    for row in table2.rows:
        for i, w in enumerate(col_widths2):
            row.cells[i].width = w

    add_heading_2("2. Kết quả phân tích hồi quy đa biến (Regression Analysis)")
    add_para(
        "Mô hình hồi quy tuyến tính được thiết lập nhằm kiểm định tác động của mức độ ứng dụng AI đến Kết quả hoạt động kinh doanh (FP) cùng các biến độc lập thuộc khung TOE. Kết quả phân tích hồi quy OLS đạt hệ số R² hiệu chỉnh = 0,425, F = 48,62 (p < 0,001), chứng tỏ mô hình có độ tương thích cao và giải thích được 42,5% sự biến thiên của kết quả hoạt động doanh nghiệp."
    )
    add_para(
        "Cụ thể, mức độ ứng dụng AI (AIA) có hệ số chuẩn hóa β = 0,384 với giá trị p-value = 0,002 (p < 0,01), ủng hộ mạnh mẽ giả thuyết H4. Năng lực hạ tầng số (DTC) đạt β = 0,265 (p = 0,008). Cam kết lãnh đạo (LD) đạt β = 0,210 (p = 0,015). Như vậy, tất cả 4 giả thuyết H1, H2, H3 và H4 đều được chấp nhận ở mức ý nghĩa thống kê 5%."
    )

    # ------------------ SECTION 5 ------------------
    add_heading_1("V. THẢO LUẬN KẾT QUẢ & HÀM Ý QUẢN TRỊ")
    add_para(
        "Kết quả nghiên cứu mang lại bằng chứng thực nghiệm vững chắc chứng minh rằng việc triển khai AI không còn là đặc quyền của các tập đoàn lớn mà hoàn toàn có thể đem lại giá trị đo lường được cho các DNNVV. Cụ thể, các doanh nghiệp ứng dụng AI vào tự động hóa chăm sóc khách hàng và dự báo tồn kho ghi nhận mức tăng trưởng doanh thu trung bình cao hơn 14,8% so với nhóm chưa áp dụng."
    )
    add_para(
        "Về mặt hàm ý quản trị, các chủ doanh nghiệp nhỏ và vừa cần nhận thức rằng công nghệ chỉ là công cụ hỗ trợ. Yếu tố cốt lõi quyết định thành công của quá trình ứng dụng AI nằm ở sự cởi mở và tư duy đổi mới sáng tạo của người lãnh đạo (LD), cùng với việc xây dựng dữ liệu nội bộ sạch và chuẩn hóa trước khi tích hợp các thuật toán học máy."
    )

    # ------------------ SECTION 6 (GÀI RESEARCH GAP) ------------------
    add_heading_1("VI. HẠN CHẾ CỦA ĐỀ TÀI & HƯỚNG NGHIÊN CỨU TƯƠNG LAI")
    add_para(
        "Mặc dù đã đạt được những kết quả đáng ghi nhận, bài báo vẫn tồn tại một số hạn chế nhất định cần được các nghiên cứu tiếp theo khắc phục và mở rộng:\n"
        "1. Hạn chế về phạm vi không gian địa lý: Mẫu nghiên cứu mới chỉ tập trung 91,6% tại hai thành phố lớn là Hà Nội và TP. Hồ Chí Minh, trong khi tỷ lệ DNNVV tại khu vực miền Trung (Đà Nẵng chỉ chiếm 8,4%) và vùng nông thôn còn rất hạn chế. Do đó, tính đại diện cho toàn bộ các tỉnh thành trên cả nước chưa cao.\n"
        "2. Hạn chế về phương pháp tiếp cận thời gian: Nghiên cứu áp dụng thiết kế nghiên cứu cắt ngang (cross-sectional) tại một thời điểm, chưa theo dõi được tác động dài hạn của AI sau 2–3 năm triển khai.\n"
        "3. Hạn chế về biến số nghiên cứu: Đề tài chưa xem xét vai trò điều tiết của biến Văn hóa chấp nhận rủi ro của doanh nghiệp và chưa phân tách rõ ràng giữa AI truyền thống (Machine Learning) và AI tạo sinh (Generative AI)."
    )

    # ------------------ SECTION 7 (GÀI BẪY CHỐNG BỊA) ------------------
    add_heading_1("VII. TUYÊN BỐ VỀ NGUỒN DỮ LIỆU & TÀI CHÍNH")
    add_para(
        "Nghiên cứu này được tài trợ một phần bởi Quỹ Phát triển Khoa học & Công nghệ của Trường Đại học Kinh tế Quốc dân. Nhóm tác giả cam kết tính trung thực của các số liệu khảo sát được trình bày. Nghiên cứu chỉ tập trung đánh giá mức độ nhận thức và tần suất sử dụng các giải pháp AI, hoàn toàn không thu thập cũng như không đề cập đến thông tin về số tiền ngân sách chi tiêu cụ thể bằng tiền mặt của các doanh nghiệp được khảo sát."
    )

    # ------------------ REFERENCES (APA 7) ------------------
    add_heading_1("TÀI LIỆU THAM KHẢO")
    
    refs = [
        "Barney, J. (1991). Firm resources and sustained competitive advantage. Journal of Management, 17(1), 99-120. https://doi.org/10.1177/014920639101700108",
        "Bộ Kế hoạch và Đầu tư. (2025). Sách trắng Doanh nghiệp nhỏ và vừa Việt Nam năm 2025. NXB Thống Kê, Hà Nội.",
        "Hair, J. F., Black, W. C., Babin, B. J., & Anderson, R. E. (2019). Multivariate data analysis (8th ed.). Cengage Learning.",
        "Hiệp hội Doanh nghiệp nhỏ và vừa Việt Nam. (2025). Báo cáo khảo sát mức độ sẵn sàng chuyển đổi số của DNNVV Việt Nam. Hà Nội: NXB Công Thương.",
        "Nguyễn, H. N., & Trần, Đ. P. (2023). Tác động của năng lực số đến khả năng phục hồi của doanh nghiệp bán lẻ sau đại dịch. Tạp chí Kinh tế & Phát triển, 312, 45-56.",
        "Pham, T. H., Nguyen, M. T., & Le, T. T. (2024). Artificial intelligence adoption in emerging markets: A moderated mediation model. International Journal of Information Management, 74, Article 102710. https://doi.org/10.1016/j.ijinfomgt.2023.102710",
        "Tornatzky, L. G., & Fleischer, M. (1990). The processes of technological innovation. Lexington Books."
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

    out_path = "f:/GitHub/ai-agent-for-research-hocvien/du-lieu-mau/demo/bai-bao-nghien-cuu-demo-chuyen-doi-so-ai-2026.docx"
    doc.save(out_path)
    print("SUCCESS: Saved demo docx to", out_path)

if __name__ == "__main__":
    create_demo_paper()
