# QUY TẮC BẢO MẬT & CẤU HÌNH MÔI TRƯỜNG (SECURITY RULES)

File này quy định các tiêu chuẩn bảo mật cho dự án Streamlit. Mọi AI Agent và Developer đều phải tuân thủ nghiêm ngặt.

## 1. Quản lý API Key & Bí mật (Secrets Management)
- **TỔNG KHÔNG**: Không bao giờ viết trực tiếp API key, Password, Token, Database Credentials trong file mã nguồn (`.py`).
- **File `.env`**: Tất cả biến môi trường phải đặt trong file `config/.env` (hoặc `.env` ở root). File này ĐÃ ĐƯỢC THÊM VÀO `.gitignore` và không bao giờ commit lên Git.
- **File mẫu `.env.example`**: Luôn duy trì file `config/.env.example` chứa tên các biến môi trường mà không chứa giá trị thực (chỉ chứa placeholder như `YOUR_API_KEY_HERE`).
- **Streamlit Secrets (`.streamlit/secrets.toml`)**: Khi deploy lên Streamlit Community Cloud, sử dụng `st.secrets` để đọc các cấu hình này.

## 2. Kiểm tra dữ liệu đầu vào (Input Validation)
- Mọi dữ liệu do người dùng nhập qua `st.text_input`, `st.file_uploader` hoặc `st.text_area` đều phải được kiểm tra (sanitized/validated) trước khi xử lý hoặc gửi tới external API.
- Khi upload file trong `st.file_uploader`, chỉ cho phép các extension hợp lệ (ví dụ: `['csv', 'json', 'xlsx']`).

## 3. Nhật ký & Lỗi (Error Handling & Privacy)
- Không hiển thị nguyên văn lỗi traceback chi tiết (`traceback.format_exc()`) cho end-user trên giao diện Streamlit trừ khi đang ở chế độ Debug (`DEBUG_MODE=True`).
- Dùng `st.error("Có lỗi xảy ra, vui lòng thử lại sau.")` cho giao diện người dùng và print lỗi chi tiết ra console server.
