# 🚀 STREAMLIT STARTER KIT DÀNH CHO MARKETER & VIBE CODING

Khung dự án **Streamlit Modular Standard** tối ưu hóa đặc biệt cho **Marketers, Content Creators, Founders và người không chuyên về lập trình (Low-code / No-code)** xây dựng Web App nhanh chóng bằng AI Vibe Coding (Antigravity, Cursor, Claude Code, ChatGPT) mà **KHÔNG CẦN VIẾT HTML, CSS HOẶC JAVASCRIPT**.

---

## ✨ CÁC ĐIỂM NỔI BẬT CỦA STARTER KIT

1. **Thuần Streamlit (100% Pure Streamlit)**: Toàn bộ giao diện, nút bấm, bảng dữ liệu, biểu đồ được tạo lập hoàn toàn bằng Python/Streamlit widget native.
2. **Tiết Kiệm Token Tối Đa (Token Efficiency)**: Cấu trúc chia nhỏ module (< 150 dòng/file) giúp AI chỉ cần đọc đúng file cần sửa thay vì tải toàn bộ mã nguồn.
3. **Hệ Thống Context Tự Động (`contexts/`)**:
   - `contexts/rules/`: Chứa các quy định bảo mật, coding standards và sơ đồ thư mục cố định.
   - `contexts/features/`: Chứa tổng quan dự án và **nhật ký tính năng động (`feature_log.md`)**. Mỗi lần AI code xong 1 tính năng, AI tự động thêm tóm tắt vào đây.
4. **Chuẩn Bảo Mật Cấu Hình (`config/`)**: Tự động load biến môi trường an toàn từ `.env` bằng `python-dotenv` hoặc `st.secrets` mà không lo lộ API Keys.

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

### 💡 Bạn chỉ cần nói với AI ý tưởng theo ngôn ngữ tự nhiên (KHÔNG CẦN đính kèm hay kéo thả file):

> 🌟 **Lưu ý**: Bạn không cần gắn link hay kéo thả bất kỳ file nào! AI được lập trình để **tự động tìm và đọc toàn bộ quy tắc, key bảo mật và bộ nhớ dự án** trước khi làm việc.

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
