# 📋 TỔNG QUAN DỰ ÁN: DASHBOARD THỐNG KÊ CHUYỂN ĐỔI UTM MARKETING

---

- **Tên dự án / Công cụ**: Dashboard Thống Kê Chuyển Đổi UTM Marketing
- **Mô tả ngắn**: Dashboard phân tích và theo dõi tỷ lệ chuyển đổi từ lượt click liên kết UTM (Pending Clicks) sang lượt tải ứng dụng thành công (Successful Installs) theo thời gian, kênh tiếp thị (Source), bộ ứng dụng (App Bucket), hệ điều hành (OS) và các chiến dịch (Campaigns).
- **Đối tượng sử dụng**: Marketing Team, User Acquisition Managers, Data Analysts, Product Owners.
- **Các tính năng chính**:
  1. **Bộ lọc khoảng thời gian (Date Filter)**: Chọn tùy chỉnh khoảng thời gian bắt đầu và kết thúc để truy vấn dữ liệu từ API.
  2. **Thẻ Chỉ Số KPI (KPI Metric Cards)**: Hiển thị Tổng lượt click, Tổng lượt cài đặt thành công, và Tỷ lệ chuyển đổi (Conversion Rate %).
  3. **Biểu đồ Phân Tích (Charts & Visualization)**:
     - Biểu đồ đường xu hướng cài đặt và click theo từng ngày (Trend Chart).
     - Biểu đồ cột hiệu suất chuyển đổi theo Nguồn tiếp thị (Facebook, TikTok, Google...).
     - Biểu đồ cột phân bổ lượt tải theo từng nhóm ứng dụng (App Bucket).
     - Thống kê phân bổ thiết bị HĐH (iOS / Android).
  4. **Bảng Danh Sách Chiến Dịch (Campaign Table)**: Bảng dữ liệu chi tiết từng chiến dịch UTM hỗ trợ tìm kiếm và sắp xếp.
- **API & Cấu hình**:
  - `KPI_STATS_API_URL`: `https://etrziohfkpykyokxoglm.supabase.co/functions/v1/get-utm-mkt-kpi-stats`
  - `CHART_DATA_API_URL`: `https://etrziohfkpykyokxoglm.supabase.co/functions/v1/get-utm-mkt-chart-data`
