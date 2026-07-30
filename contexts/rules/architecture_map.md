# BẢN ĐỒ KIẾN TRÚC DỰ ÁN (ARCHITECTURE MAP)

Bản đồ này giúp AI Agent định vị chính xác quy tắc tự động khởi tạo file khi nhận prompt từ người dùng.

```
streamlit-structure/
├── .agents/
│   └── AGENTS.md               --> [QUY TẮC AGENT] Quy định AI Auto-Pilot (Zero-Code)
├── contexts/                   --> [HỆ THỐNG CONTEXT] Bộ nhớ dự án cho AI
│   ├── rules/                  --> [QUY CHUẨN CỐ ĐỊNH] Bảo mật, Coding Standards, Architecture
│   │   ├── security_rules.md
│   │   ├── coding_standards.md
│   │   └── architecture_map.md
│   └── features/               --> [NHẬT KÝ TÍNH NĂNG] AI tự cập nhật sau mỗi lần code
│       ├── project_overview.md --> Khung dàn ý dự án (Template)
│       └── feature_log.md      --> Nhật ký danh sách tính năng & State schema đã tạo
├── data/                       --> [DỮ LIỆU LOCAL] Thư mục chứa CSV, JSON, SQLite (Ban đầu trống)
│   └── README.md
├── config/                     --> [CẤU HÌNH & MÔI TRƯỜNG] Chứa .env và settings.py
│   ├── README.md
│   ├── .env.example
│   └── settings.py
├── src/                        --> [MÃ NGUỒN CHÍNH] (Tự động khởi tạo file khi prompt)
│   ├── components/             --> [UI COMPONENTS] AI tự tạo file UI tại đây khi có yêu cầu
│   │   └── __init__.py
│   ├── services/               --> [BUSINESS LOGIC & API] AI tự tạo file logic/API tại đây
│   │   └── __init__.py
│   └── utils/                  --> [HELPERS]
│       └── state_manager.py    --> Quản lý st.session_state tập trung
├── app.py                      --> [ENTRY POINT] File chạy ứng dụng tinh gọn siêu sạch (<15 dòng)
├── .streamlit/                 --> [CONFIG RELOAD] Cấu hình runOnSave = true
│   └── config.toml
├── run.sh                      --> [1-CLICK MACOS/LINUX] Lệnh khởi chạy tự động
├── run.bat                     --> [1-CLICK WINDOWS] Lệnh khởi chạy tự động
├── .gitignore                  --> Bảo vệ thông tin nhạy cảm (.env, venv)
├── requirements.txt            --> Thư viện phụ thuộc
└── README.md                   --> Hướng dẫn sử dụng cho Marketer / Người không code
```

## Quy tắc AI Tự Động Khởi Tạo File Khi Người Dùng Prompt:
1. **Khi cần thêm Giao diện (UI Widget, Form, Card, Chart)**:
   - AI tự tạo file mới trong `src/components/` (ví dụ: `src/components/form_widget.py`).
2. **Khi cần thêm Logic (Gọi API, Tính toán, Đọc/Ghi dữ liệu)**:
   - AI tự tạo file mới trong `src/services/` (ví dụ: `src/services/ai_service.py`).
3. **Khi cần Lưu Trạng Thái**:
   - AI tự khai báo biến mặc định trong `src/utils/state_manager.py`.
4. **Nhập mã nguồn vào `app.py`**:
   - AI import component vào `app.py` và hiển thị trên giao diện.
5. **Ghi nhật ký**:
   - AI thêm 1 mục tóm tắt tính năng vừa tạo vào `contexts/features/feature_log.md`.
