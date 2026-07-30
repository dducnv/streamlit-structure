# NHẬT KÝ TÍNH NĂNG DỰ ÁN (DYNAMIC FEATURE LOG)

File này lưu trữ thông tin tóm tắt của tất cả các tính năng đã được xây dựng trong ứng dụng.
**Mỗi lần AI hỗ trợ viết xong 1 tính năng hoặc chỉnh sửa code, AI SẼ TỰ ĐỘNG THÊM MỘT MỤC MỚI VÀO ĐÂY.**

---

## [2026-07-30] Khởi Tạo Cấu Trúc Khung Ứng Dụng (Base Starter Kit Framework)

- **Mục tiêu**: Thiết lập cấu trúc dự án Streamlit modular chuẩn Pythonic cho Marketer & Non-coders.
- **Các file liên quan**:
  - [app.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/app.py): Entry point điều hướng giao diện chính.
  - [config/settings.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/config/settings.py): Cấu hình môi trường & load `.env`.
  - [src/utils/state_manager.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/utils/state_manager.py): Quản lý `st.session_state` tập trung.
  - [src/services/data_service.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/services/data_service.py): Đọc & lưu trữ dữ liệu JSON từ folder `data/`.
  - [src/components/header.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/components/header.py): Banner, Header & Sidebar Navigation.
  - [src/components/widgets.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/components/widgets.py): Reusable UI Widgets (Metrics cards, Form demo, Data table).
- **Session State Schema**:
  - `st.session_state.initialized`: Boolean (Trạng thái khởi tạo app).
  - `st.session_state.app_mode`: String (`"Demo Dashboard"` hoặc `"Thêm Dữ Liệu"`).
  - `st.session_state.data_records`: List[Dict] (Danh sách bản ghi dữ liệu mẫu).
