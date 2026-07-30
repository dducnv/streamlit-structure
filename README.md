# 🚀 STREAMLIT STARTER KIT DÀNH CHO MARKETER & VIBE CODING

Khung dự án **Streamlit Modular Standard** tối ưu hóa đặc biệt cho **Marketers, Content Creators, Founders và người không chuyên về lập trình (Low-code / No-code)** xây dựng Web App nhanh chóng bằng AI Vibe Coding (Antigravity, Cursor, Claude Code, ChatGPT) mà **KHÔNG CẦN VIẾT HTML, CSS HOẶC JAVASCRIPT**.

---

## ✨ CÁC ĐIỂM NỔI BẬT CỦA STARTER KIT (TÍCH HỢP MÔ HÌNH CCPM)

1. **Thuần Streamlit (100% Pure Streamlit)**: Toàn bộ giao diện, nút bấm, bảng dữ liệu, biểu đồ được tạo lập hoàn toàn bằng Python/Streamlit widget native.
2. **Mô Hình CCPM Dual-Persona (Project Manager + Technical Developer)**: AI đóng vai trò PM hỗ trợ phỏng vấn khởi tạo dự án và ghi nhận spec, sau đó đóng vai Dev tự động tạo mã nguồn gọn gàng.
3. **Tiết Kiệm Token & Phòng Bỏ Quên Context (Context Evaporation Prevention)**: Cấu trúc chia nhỏ module (< 150 dòng/file) và hệ thống lưu trữ context động trong `contexts/features/` giúp AI nắm 100% ngữ cảnh dù trò chuyện bao lâu.
4. **Chạy 1-Click & Tự Động Reload Tức Thì**: Hỗ trợ `run.sh` / `run.bat` và module `watchdog` tự làm mới trang web ngay khi lưu code.
5. **Chuẩn Bảo Mật Cấu Hình (`config/`)**: Tự động load biến môi trường an toàn từ `.env` bằng `python-dotenv` hoặc `st.secrets` mà không lo lộ API Keys.

---

## 📂 CẤU TRÚC DỰ ÁN CHUẨN PYTHONIC

```
streamlit-structure/
├── .agents/
│   └── AGENTS.md                  # Quy tắc Vibe Coding cho AI Agent
├── contexts/                      # Bộ nhớ ngữ cảnh (Context Memory) cho AI
│   ├── rules/                     # Quy chuẩn cố định (Bảo mật, Coding standards, Architecture)
│   │   ├── security_rules.md
│   │   ├── coding_standards.md
│   │   └── architecture_map.md
│   └── features/                  # Nhật ký tính năng động (Cập nhật sau mỗi đợt code)
│       ├── project_overview.md    # Mục đích dự án & Đối tượng mục tiêu
│       └── feature_log.md         # Nhật ký tính năng & State Schema đã xây dựng
├── data/                          # Lưu trữ dữ liệu Local (CSV, JSON, SQLite)
│   ├── README.md
│   └── sample_data.json
├── config/                        # Cấu hình môi trường & `.env`
│   ├── README.md
│   ├── .env.example
│   └── settings.py
├── src/                           # Mã nguồn chính (Tách biệt UI và Logic)
│   ├── components/                # Reusable Streamlit UI Widgets
│   │   ├── header.py              # Header, Banner & Sidebar Navigation
│   │   └── widgets.py             # Metrics Cards, Form nhập liệu, Data Table
│   ├── services/                  # Business Logic & Đọc/Ghi dữ liệu
│   │   └── data_service.py        # Logic đọc/ghi file từ folder data/
│   └── utils/                     # Helpers & State Management
│       └── state_manager.py       # Quản lý st.session_state tập trung
├── app.py                         # Entry point tinh gọn (<40 dòng code)
├── .gitignore                     # Bảo vệ thông tin nhạy cảm (.env, venv)
├── requirements.txt               # Các thư viện Python cần thiết
└── README.md                      # File hướng dẫn này
```

---

## ⚡ CHẠY ỨNG DỤNG BẰNG 1-CLICK (KHÔNG CẦN GÕ LỆNH TERMINAL)

Dành cho người không chuyên kỹ thuật: **Bạn không cần gõ bất kỳ câu lệnh phức tạp nào!**

### 🍏 Đối với MacOS / Linux:
Mở Terminal tại thư mục dự án và gõ duy nhất 1 dòng:
```bash
./run.sh
```
*(Script sẽ tự động cài venv, cài thư viện và bật ứng dụng trên trình duyệt giúp bạn).*

### 🪟 Đối với Windows:
Nhấp đúp chuột vào file **`run.bat`** (hoặc gõ `run.bat` trong CMD/PowerShell).

---

## 🛠️ HƯỚNG DẪN CHI TIẾT (DÀNH CHO ĐỒNG BỘ NẾU CẦN KIỂM TRA)

### Bước 0: Kiểm tra & Cài đặt Python (Dành cho người mới)

1. **Kiểm tra xem máy tính đã cài Python chưa**:
   - Nếu chưa có Python: Tải tại [python.org/downloads](https://www.python.org/downloads/).
   - ⚠️ **LƯU Ý VỚI WINDOWS**: Nhớ tích chọn **`Add python.exe to PATH`** khi cài đặt.

---

## 🤖 QUY TRÌNH ZERO-CODE DÀNH CHO MARKETER & CONTENT CREATOR (AI LÀM TẤT CẢ)

Với Starter Kit này, **bạn KHÔNG CẦN biết viết code hay chỉnh sửa file thủ công**. AI Assistant sẽ tự động đóng vai trò là một Senior Developer chịu trách nhiệm toàn bộ mặt kỹ thuật.

### 💡 Bạn chỉ cần nói với AI ý tưởng theo ngôn ngữ tự nhiên:

> 🌟 **Cơ chế Ghi Đè Context Ban Đầu (Auto-Replace Template)**:
> - File `contexts/features/project_overview.md` ban đầu chỉ là **Khung Mẫu Trống (Template)**.
> - Ở lần đầu tiên bạn prompt ý tưởng, AI sẽ **tự động GHI ĐÈ THAY THẾ (OVERWRITE)** toàn bộ nội dung file này bằng thông tin dự án thực tế của bạn (từ câu trả lời phỏng vấn hoặc từ mô tả của bạn).
> - **Riêng về API**: AI hỏi *"Có cần kết nối API bên thứ 3 nào không?"*. Nếu **Không** $\rightarrow$ Dừng câu hỏi API và làm ngay. Nếu **Có** $\rightarrow$ AI hỏi thêm cần Key xác thực nào để hướng dẫn lưu an toàn vào `config/.env`.

#### 1. Mẫu Prompt Thêm Tính Năng Mới:
> *"Tôi muốn vẽ một biểu đồ doanh thu kết nối với API OpenAI để tự động đọc xu hướng. Hãy tự làm tất cả giúp tôi nhé!"*

#### 2. Mẫu Prompt Chỉnh Sửa / Nâng Cấp:
> *"Hãy thêm nút xuất file PDF cho báo cáo chiến dịch và cho phép chọn màu giao diện."*

#### 3. Mẫu Prompt Sửa Lỗi (Nếu có):
> *"Ứng dụng báo lỗi khi tôi bấm nút Lưu dữ liệu, hãy kiểm tra và sửa lại giúp tôi."*

---

### ⚙️ Cách AI Tự Động Xử Lý Ngầm (Bạn không cần can thiệp):
1. **Đọc Context**: AI tự động nạp thông tin quy tắc từ `contexts/rules/` và lịch sử từ `contexts/features/feature_log.md`.
2. **Tự Tạo/Sửa File**: AI tự phân tách UI vào `src/components/`, logic vào `src/services/`, quản lý state tại `src/utils/state_manager.py`.
3. **Tự Kiểm Tra Lỗi**: AI tự động compile code để đảm bảo ứng dụng chạy mượt không bị gãy.
4. **Tự Cập Nhật Nhật Ký**: AI tự động lưu lại tóm tắt tính năng mới vào `contexts/features/feature_log.md` để các lượt chat sau ngày càng thông minh hơn mà tốn rất ít token.

---

## 🔒 BẢO MẬT & DEPLOY LÊN STREAMLIT COMMUNITY CLOUD

- File `.env` chứa bí mật (API Key) đã được tự động bỏ qua không commit lên Git.
- Khi đưa ứng dụng lên **Streamlit Community Cloud**, bạn vào mục **Settings -> Secrets** của App và dán nội dung từ file `.env` vào. Hệ thống `config/settings.py` sẽ tự động đọc từ `st.secrets` trên Cloud.
