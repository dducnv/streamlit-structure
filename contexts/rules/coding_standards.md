# TIÊU CHUẨN CODE SẠCH & UI DESIGN CHUYÊN NGHIỆP (CODING & UI STANDARDS)

File này quy định chuẩn viết code và chuẩn thiết kế giao diện Streamlit chuyên nghiệp, mượt mà và tối ưu UX/UI.

## 1. Chuẩn Thiết Kế Giao Diện (Executive Professional UI & Material Icons)
- **NGHIÊM CẤM DÙNG EMOJI MÀU SẮC RƯỜM RÀ**: Tuyệt đối không dùng emoji màu sắc (như 🚀, 📈, 📊, ⚡, 🔑...). Emoji khiến giao diện bị lộn xộn và kém sang.
- **SỬ DỤNG STREAMLIT NATIVE MATERIAL ICONS (`:material/icon_name:`)**:
  - Streamlit hỗ trợ sẵn bộ icon vector Google Material Symbols cao cấp qua cú pháp `:material/icon_name:`.
  - Tiêu đề & Header: `st.title(":material/analytics: Dashboard Thống Kê")`
  - Nút bấm: `st.button("Xuất Báo Cáo", icon=":material/download:")`
  - Các tab & Sidebar: `st.tabs([":material/bar_chart: Biểu Đồ", ":material/table_view: Chi Tiết"])`
  - Danh sách icon chuẩn: `:material/dashboard:`, `:material/analytics:`, `:material/trending_up:`, `:material/calendar_today:`, `:material/filter_alt:`, `:material/key:`, `:material/table_view:`, `:material/download:`, `:material/refresh:`.
- **Dùng Các Widget Hiện Đại (Modern Streamlit Components)**:
  - Dùng `st.segmented_control` thay cho `st.radio(..., horizontal=True)` để tạo bộ chọn pill hiện đại.
  - Dùng `st.pills` cho các lựa chọn lọc nhanh.
  - Dùng `st.container(border=True)` để nhóm các thẻ thông tin dạng Card sạch sẽ.
- **Phân bổ Typography & Size rõ ràng**:
  - `st.title()`: Chỉ dùng duy nhất 1 lần ở đầu trang chính.
  - `st.subheader()`: Dùng cho tiêu đề các khối/chức năng chính.
  - `st.caption()`: Dùng cho mô tả phụ, nguồn dữ liệu hoặc chú thích nhỏ.
  - Sử dụng khoảng cách (spacing) đồng nhất với `st.divider()` và `st.columns()` để giao diện có bố cục mạch lạc, chuyên nghiệp.
- **Dùng Widget Native Chuẩn UI**:
  - Thẻ số liệu KPI: Dùng `st.metric(label=..., value=..., delta=...)`.
  - Bảng dữ liệu: Dùng `st.dataframe()` với cấu hình cột rõ ràng.
  - Biểu đồ: Dùng `st.line_chart` hoặc `st.bar_chart` với tham số `x` và `y` được chỉ định rõ ràng.

## 2. Tiết Kiệm Token & Cấu Trúc File
- **Kích thước File ngắn gọn**: Mỗi file `.py` chỉ chứa tối đa 150 dòng code. Nếu quá dài, hãy tự động tách nhỏ thành module trong `src/components/` hoặc `src/services/`.
- **Tách biệt UI và Logic**:
  - Giao diện Streamlit -> Đặt tại `src/components/`.
  - Logic tính toán, gọi API, xử lý dữ liệu -> Đặt tại `src/services/`.
  - Quản lý State -> Đặt tại `src/utils/state_manager.py`.

## 3. Kiểm Tra Lỗi & Quản Lý Session State An Toàn
- **Tự kiểm tra cú pháp**: AI phải kiểm tra cú pháp code bằng `py_compile` trước khi bàn giao cho người dùng.
- **Session State safe-check**: Tất cả các biến `st.session_state` PHẢI được khởi tạo giá trị mặc định tại `src/utils/state_manager.py` trước khi ứng dụng render để phòng tránh lỗi `KeyError`.
