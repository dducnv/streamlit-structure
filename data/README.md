# THƯ MỤC LƯU TRỮ DỮ LIỆU LOCAL (DATA STORAGE)

Thư mục này dùng để lưu trữ dữ liệu tĩnh hoặc dữ liệu ứng dụng nhỏ mà không cần cài đặt Cơ sở dữ liệu phức tạp.

## 1. Loại file hỗ trợ
- **File JSON (`.json`)**: Thích hợp cho cấu hình, danh sách bản ghi mẫu, dữ liệu dạng dictionary.
- **File CSV (`.csv`)**: Thích hợp cho bảng dữ liệu Marketing, báo cáo, danh sách khách hàng (đọc nhanh bằng `pandas`).
- **File SQLite (`.db`)**: Nếu ứng dụng cần lưu trữ dữ liệu có cấu trúc câu hỏi/câu trả lời phức tạp hơn.

## 2. Lưu ý quan trọng khi dùng Data trong Streamlit
- Nếu dữ liệu chứa thông tin cá nhân khách hàng (PII) hoặc dữ liệu nhạy cảm, vui lòng thêm tên file vào `.gitignore` để không đẩy lên GitHub.
- Mọi thao tác đọc/ghi file trong folder `data/` NÊN được xử lý thông qua module `src/services/data_service.py` để giữ cho giao diện UI luôn sạch sẽ và tách biệt.
