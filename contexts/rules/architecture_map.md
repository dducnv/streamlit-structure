# BẢN ĐỒ KIẾN TRÚC DỰ ÁN (ARCHITECTURE MAP)

Bản đồ này giúp AI Agent và Developer lập tức định vị đúng vị trí file cần chỉnh sửa mà không cần tìm kiếm lan man.

```
streamlit-structure/
├── .agents/
│   └── AGENTS.md               --> [QUY TẮC AGENT] Chứa chỉ thị Vibe Coding & Cập nhật context
├── contexts/                   --> [HỆ THỐNG CONTEXT] Lưu bộ nhớ dự án cho AI
│   ├── rules/                  --> [QUY CHUẨN CỐ ĐỊNH] Bảo mật, Coding Standards, Architecture
│   │   ├── security_rules.md
│   │   ├── coding_standards.md
│   │   └── architecture_map.md
│   └── features/               --> [NHẬT KÝ TÍNH NĂNG] Cập nhật sau mỗi lần code
│       ├── project_overview.md --> Mục đích dự án & Khách hàng mục tiêu
│       └── feature_log.md      --> Danh sách tính năng & State schema đã tạo
├── data/                       --> [DỮ LIỆU LOCAL] Lưu CSV, JSON, SQLite mẫu
│   ├── README.md
│   └── sample_data.json
├── config/                     --> [CẤU HÌNH & MÔI TRƯỜNG] Chứa .env và settings.py
│   ├── README.md
│   ├── .env.example
│   └── settings.py
├── src/                        --> [MÃ NGUỒN CHÍNH]
│   ├── components/             --> [UI COMPONENTS] Tách biệt các phần giao diện
│   │   ├── header.py           --> Title, Banner, Sidebar
│   │   └── widgets.py          --> Metrics, Cards, Form inputs
│   ├── services/               --> [BUSINESS LOGIC] Xử lý dữ liệu & gọi API
│   │   └── data_service.py     --> Đọc/Ghi dữ liệu từ folder data/
│   └── utils/                  --> [HELPERS]
│       └── state_manager.py    --> Quản lý st.session_state tập trung
├── app.py                      --> [ENTRY POINT] File chạy ứng dụng tinh gọn (<40 dòng)
├── .gitignore                  --> File bỏ qua Git (.env, __pycache__, venv)
├── requirements.txt            --> Thư viện phụ thuộc
└── README.md                   --> Hướng dẫn sử dụng cho Marketer / Người không code
```

## Vị trí file khi muốn thêm tính năng mới:
- Muốn thêm **Nút bấm / Giao diện mới** -> Sửa/Thêm tại `src/components/widgets.py`
- Muốn thêm **Logic tính toán / API / Đọc file mới** -> Sửa/Thêm tại `src/services/data_service.py`
- Muốn thêm **Lưu biến trạng thái mới** -> Thêm khởi tạo tại `src/utils/state_manager.py`
- Sau khi xong -> Thêm 1 dòng tóm tắt vào `contexts/features/feature_log.md`
