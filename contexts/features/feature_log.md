# NHẬT KÝ TÍNH NĂNG DỰ ÁN (DYNAMIC FEATURE LOG)

File này lưu trữ thông tin tóm tắt của tất cả các tính năng đã được xây dựng trong ứng dụng.
**Mỗi lần AI hỗ trợ viết xong 1 tính năng hoặc chỉnh sửa code, AI SẼ TỰ ĐỘNG THÊM MỘT MỤC MỚI VÀO ĐÂY.**

---

## [2026-07-30] Dashboard Thống Kê Chuyển Đổi UTM Marketing

- **Mục tiêu**: Xây dựng dashboard trực quan hóa dữ liệu thống kê chuyển đổi từ lượt click qua lượt cài đặt ứng dụng từ 2 API Supabase Edge Functions.
- **Các file triển khai**:
  - [config/settings.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/config/settings.py): Đăng ký API URL `KPI_STATS_API_URL` và `CHART_DATA_API_URL`.
  - [src/services/utm_analytics_service.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/services/utm_analytics_service.py): Service xử lý gọi POST request đến Supabase API theo tham số khoảng thời gian.
  - [src/utils/state_manager.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/utils/state_manager.py): Khởi tạo và quản lý state dữ liệu `kpi_data`, `chart_data`, `last_start`, `last_end`.
  - [src/components/sidebar_filters.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/components/sidebar_filters.py): Bộ lọc chọn ngày/khoảng thời gian nhanh ở Sidebar.
  - [src/components/kpi_cards.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/components/kpi_cards.py): Các thẻ Metric chỉ số KPI (Lượt click, Lượt cài đặt, Tỷ lệ CR%).
  - [src/components/charts_view.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/components/charts_view.py): Biểu đồ đường xu hướng theo ngày, biểu đồ cột theo Nguồn & App Bucket, tỷ lệ HĐH (OS).
  - [src/components/campaign_table.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/components/campaign_table.py): Bảng dữ liệu chi tiết danh sách chiến dịch UTM với ô tìm kiếm.
  - [app.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/app.py): Tích hợp toàn bộ component (< 25 dòng code).
- **Session State Schema**:
  - `st.session_state.initialized`: Boolean
  - `st.session_state.start_date`: String / None
  - `st.session_state.end_date`: String / None
  - `st.session_state.kpi_data`: Dict (Dữ liệu trả về từ `get-utm-mkt-kpi-stats`)
  - `st.session_state.chart_data`: Dict (Dữ liệu trả về từ `get-utm-mkt-chart-data`)
  - `st.session_state.last_start`: String / None
  - `st.session_state.last_end`: String / None

---

## [2026-07-30] Khởi Tạo Khung Dự Án Trống Tối Giản (Minimal Blank Starter Kit)

- **Mục tiêu**: Khởi tạo khung dự án Streamlit tối giản tuyệt đối (Blank Starter Kit), sẵn sàng tự động tạo các UI Component và Service khi nhận prompt từ người dùng.
- **Các file cơ bản**:
  - [app.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/app.py): Entry point điều hướng chính (8 dòng code siêu sạch).
  - [config/settings.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/config/settings.py): Cấu hình môi trường & nạp biến `.env`.
  - [src/utils/state_manager.py](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/utils/state_manager.py): Khởi tạo và quản lý `st.session_state` an toàn.
  - [src/components/](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/components): Thư mục UI Component.
  - [src/services/](file:///Users/ducnv/Documents/Projects/streamlit-structure/src/services): Thư mục Business Logic & API.
- **Session State Schema**:
  - `st.session_state.initialized`: Boolean (Trạng thái khởi tạo mặc định).
