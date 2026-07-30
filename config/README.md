# HƯỚNG DẪN CẤU HÌNH & MÔI TRƯỜNG (CONFIG & ENVIRONMENT)

Folder này chứa tất cả các cấu hình môi trường và quản lý biến bí mật (Secrets / API Keys).

## 1. Các file trong folder `config/`
- `.env.example`: File mẫu chứa danh sách các tên biến môi trường.
- `settings.py`: Module Python sử dụng `python-dotenv` để tự động nạp cấu hình từ `.env` hoặc `st.secrets`.

## 2. Cách thiết lập file `.env` cá nhân
1. Tạo một file tên là `.env` ngay bên cạnh `.env.example` (trong folder `config/` hoặc ở root dự án).
2. Sao chép nội dung từ `.env.example` sang `.env` và điền các giá trị thực tế của bạn:
   ```env
   APP_NAME="My Streamlit App"
   ENV="development"
   DEBUG_MODE=True
   # Điền API Key của bạn (nếu có)
   OPENAI_API_KEY="sk-proj-xxxxxx"
   ```
3. File `.env` **TUYỆT ĐỐI KHÔNG COMMIT LÊN GIT** (Đã được `.gitignore` bảo vệ).

## 3. Cấu hình khi Deploy lên Streamlit Community Cloud
Khi đưa app lên cloud của Streamlit:
- Mở Settings của App trên Streamlit Cloud -> chọn **Secrets**.
- Dán nội dung tương tự file `.env` theo cú pháp TOML:
  ```toml
  APP_NAME = "My Streamlit App"
  OPENAI_API_KEY = "sk-proj-xxxxxx"
  ```
- File `config/settings.py` sẽ tự động ưu tiên đọc từ `st.secrets` nếu chạy trên Streamlit Cloud!
