# NHẬT KÝ TÍNH NĂNG DỰ ÁN (DYNAMIC FEATURE LOG)

File này lưu trữ thông tin tóm tắt của tất cả các tính năng đã được xây dựng trong ứng dụng.
**Mỗi lần AI hỗ trợ viết xong 1 tính năng hoặc chỉnh sửa code, AI SẼ TỰ ĐỘNG THÊM MỘT MỤC MỚI VÀO ĐÂY.**

---

## [2026-07-30] Khởi Tạo Khung Dự Án Trống Tối Giản (Minimal Blank Starter Kit)

- **Mục tiêu**: Khởi tạo khung dự án Streamlit tối giản tuyệt đối (Blank Starter Kit), sẵn sàng tự động tạo các UI Component và Service khi nhận prompt từ người dùng.
- **Các file cơ bản**:
  - [app.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/app.py): Entry point điều hướng chính (8 dòng code siêu sạch).
  - [config/settings.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/config/settings.py): Cấu hình môi trường & nạp biến `.env`.
  - [src/utils/state_manager.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/utils/state_manager.py): Khởi tạo và quản lý `st.session_state` an toàn.
  - [src/components/](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/components): Thư mục UI Component (Ban đầu trống, AI tự tạo file UI khi prompt).
  - [src/services/](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/services): Thư mục Business Logic & API (Ban đầu trống, AI tự tạo file logic khi prompt).
- **Session State Schema**:
  - `st.session_state.initialized`: Boolean (Trạng thái khởi tạo mặc định).
