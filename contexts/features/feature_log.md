# NHẬT KÝ TÍNH NĂNG DỰ ÁN (DYNAMIC FEATURE LOG)

File này lưu trữ thông tin tóm tắt của tất cả các tính năng đã được xây dựng trong ứng dụng.
**Mỗi lần AI hỗ trợ viết xong 1 tính năng hoặc chỉnh sửa code, AI SẼ TỰ ĐỘNG THÊM MỘT MỤC MỚI VÀO ĐÂY.**

---

## [2026-07-30] Khởi Tạo Khung Dự Án Trống (Blank Starter Kit Framework)

- **Mục tiêu**: Khởi tạo khung dự án Streamlit siêu tinh gọn, sẵn sàng đón nhận yêu cầu phát triển công cụ từ phía người dùng.
- **Các file cơ bản**:
  - [app.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/app.py): Entry point điều hướng chính (<20 dòng code).
  - [config/settings.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/config/settings.py): Cấu hình môi trường & load `.env`.
  - [src/utils/state_manager.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/utils/state_manager.py): Khởi tạo và quản lý `st.session_state` an toàn.
  - [src/services/data_service.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/services/data_service.py): Helper đọc/ghi file JSON/CSV dùng chung trong `data/`.
  - [src/components/header.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/components/header.py): Header & Banner giao diện đơn giản.
  - [src/components/widgets.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/components/widgets.py): Màn hình chào mừng ban đầu.
- **Session State Schema**:
  - `st.session_state.initialized`: Boolean (Trạng thái khởi tạo).
