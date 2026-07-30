# TIÊU CHUẨN CODE SẠCH & UI DESIGN CHUYÊN NGHIỆP (CODING & UI STANDARDS)

File này quy định chuẩn viết code và chuẩn thiết kế giao diện Streamlit chuyên nghiệp, mượt mà và tối ưu UX/UI.

## 1. Chuẩn Thiết Kế Giao Diện (Executive Professional UI Design)
- **Hạn chế dùng Emoji lạm dụng**: KHÔNG gắn emoji tràn lan ở mọi tiêu đề/thẻ. Chỉ sử dụng icon hoặc emoji cực kỳ tiết chế ở vị trí hợp lý (như trang chính hoặc nút hành động quan trọng).
- **Phân bổ Typography & Size rõ ràng**:
  - `st.title()`: Chỉ dùng duy nhất 1 lần ở đầu trang chính.
  - `st.subheader()`: Dùng cho tiêu đề các khối/chức năng chính.
  - `st.caption()`: Dùng cho mô tả phụ, nguồn dữ liệu hoặc chú thích nhỏ.
  - Sử dụng khoảng cách (spacing) đồng nhất với `st.divider()` và `st.columns()` để giao diện có bố cục mạch lạc, chuyên nghiệp.
- **Dùng Widget Native Chuẩn UI**:
  - Thẻ số liệu KPI: Dùng `st.metric(label=..., value=..., delta=...)`.
  - Bảng dữ liệu: Dùng `st.dataframe()` với cấu hình cột rõ ràng.
  - Phân luồng giao diện: Dùng `st.tabs()` hoặc `st.container()`.

## 2. Tiết Kiệm Token & Cấu Trúc File
- **Kích thước File ngắn gọn**: Mỗi file `.py` chỉ chứa tối đa 150 dòng code. Nếu quá dài, hãy tự động tách nhỏ thành module trong `src/components/` hoặc `src/services/`.
- **Tách biệt UI và Logic**:
  - Giao diện Streamlit -> Đặt tại `src/components/`.
  - Logic tính toán, gọi API, xử lý dữ liệu -> Đặt tại `src/services/`.
  - Quản lý State -> Đặt tại `src/utils/state_manager.py`.

## 3. Kiểm Tra Lỗi & Quản Lý Session State An Toàn
- **Tự kiểm tra cú pháp**: AI phải kiểm tra cú pháp code bằng `py_compile` trước khi bàn giao cho người dùng.
- **Session State safe-check**: Tất cả các biến `st.session_state` PHẢI được khởi tạo giá trị mặc định tại `src/utils/state_manager.py` trước khi ứng dụng render để phòng tránh lỗi `KeyError`.
