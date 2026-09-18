#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Công cụ quét và làm sạch ký tự Unicode vô hình (Zero-width Watermarks)
Dành cho Nghiên cứu sinh & Giảng viên làm sạch bản thảo luận án, bài báo khoa học.

Không phụ thuộc thư viện ngoài (chỉ dùng Python Standard Library).
"""

import sys
import re
from pathlib import Path

# Danh mục các ký tự vô hình / Watermark Unicode phổ biến
INVISIBLE_CHARS = {
    '\u200B': 'Zero-Width Space',
    '\u200C': 'Zero-Width Non-Joiner',
    '\u200D': 'Zero-Width Joiner',
    '\u2060': 'Word Joiner',
    '\uFEFF': 'Zero-Width No-Break Space (BOM)',
    '\u202A': 'Left-to-Right Embedding',
    '\u202B': 'Right-to-Left Embedding',
    '\u202C': 'Pop Directional Formatting',
    '\u202D': 'Left-to-Right Override',
    '\u202E': 'Right-to-Left Override',
    '\u00A0': 'Non-Breaking Space',
}

# Regex gom tất cả ký tự vô hình
PATTERN_INVISIBLE = re.compile('[' + ''.join(re.escape(c) for c in INVISIBLE_CHARS.keys() if c != '\u00A0') + ']')

def scan_and_clean_text(text: str, replace_nbsp: bool = True) -> tuple[str, dict]:
    """
    Quét và làm sạch chuỗi văn bản.
    Trả về (văn bản sạch, thống kê số lượng ký tự tìm thấy).
    """
    stats = {}
    total_found = 0
    
    for char, name in INVISIBLE_CHARS.items():
        count = text.count(char)
        if count > 0:
            stats[name] = count
            total_found += count

    # Làm sạch ký tự zero-width
    cleaned_text = PATTERN_INVISIBLE.sub('', text)
    
    # Thay thế non-breaking space thành khoảng trắng thường nếu được yêu cầu
    if replace_nbsp:
        cleaned_text = cleaned_text.replace('\u00A0', ' ')
        
    return cleaned_text, stats

def process_file(file_path: Path, backup: bool = True) -> bool:
    """Xử lý làm sạch một file văn bản UTF-8."""
    if not file_path.is_file():
        print(f"[!] Không tìm thấy file: {file_path}")
        return False
        
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"[!] Lỗi khi đọc file {file_path}: {e}")
        return False
        
    cleaned, stats = scan_and_clean_text(content)
    
    if not stats:
        print(f"[✓] File {file_path.name} HOÀN TOÀN TINH SẠCH, không có ký tự ẩn nào.")
        return True
        
    print(f"[*] Phát hiện ký tự ẩn trong file {file_path.name}:")
    for name, count in stats.items():
        print(f"    - {name}: {count} lần")
        
    if backup:
        backup_path = file_path.with_name(f"{file_path.stem}_backup{file_path.suffix}")
        backup_path.write_text(content, encoding='utf-8')
        print(f"[+] Đã tạo bản sao lưu tại: {backup_path.name}")
        
    file_path.write_text(cleaned, encoding='utf-8')
    print(f"[✓] Đã làm sạch thành công {file_path.name}!")
    return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Cách dùng: python clean_unicode_watermarks.py <duong_dan_file>")
        print("Ví dụ: python clean_unicode_watermarks.py luan-an-chuong-3.md")
    else:
        target = Path(sys.argv[1])
        process_file(target)
