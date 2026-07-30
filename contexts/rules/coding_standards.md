# TIÊU CHUẨN CODE SẠCH & TIẾT KIỆM TOKEN (CODING STANDARDS)

File này quy định chuẩn viết code Streamlit phục vụ Vibe Coding mượt mà, dễ sửa và tiết kiệm token.

## 1. Tiết Kiệm Token Cho Lần Prompt Sau
- **Kích thước File ngắn gọn**: Mỗi file `.py` chỉ chứa tối đa 150-200 dòng code. Nếu quá dài, hãy tách nhỏ thành module mới trong `src/components/` hoặc `src/services/`.
- **Tách biệt giao diện (UI) và Logic**:
  - UI Streamlit (widgets, layout, columns) -> Đặt tại `src/components/`.
  - Logic tính toán, gọi API, xử lý data -> Đặt tại `src/services/`.
  - Quản lý Session State -> Đặt tại `src/utils/state_manager.py`.
- **Tự động đọc nhật ký**: AI khi nhận prompt mới chỉ cần đọc `contexts/features/feature_log.md` thay vì đọc toàn bộ codebase.

## 2. Chuẩn Code Streamlit (Pure Streamlit)
- Sử dụng các widget native của Streamlit:
  - Header & Layout: `st.set_page_config`, `st.title`, `st.sidebar`, `st.columns`, `st.expander`, `st.tabs`.
  - Hiển thị dữ liệu: `st.dataframe`, `st.metric`, `st.json`, `st.area_chart`, `st.bar_chart`.
  - Nhập liệu & Form: `st.form`, `st.text_input`, `st.selectbox`, `st.button`, `st.download_button`.
- Hạn chế sử dụng `st.markdown(..., unsafe_allow_html=True)` ngoại trừ trường hợp cần chỉnh spacing nhẹ. KHÔNG dùng HTML/CSS phức tạp.

## 3. Quản lý Session State Cực Kỳ An Toàn
- Không gán trực tiếp `st.session_state.my_var` ở giữa UI mà không kiểm tra tồn tại.
- Tất cả các biến `st.session_state` PHẢI được khởi tạo giá trị mặc định tại `src/utils/state_manager.py` trước khi ứng dụng render.
