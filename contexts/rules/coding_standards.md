# TIÊU CHUẨN CODE SẠCH & TIẾT KIỆM TOKEN (CODING STANDARDS - MÔ HÌNH CCPM)

File này quy định chuẩn viết code Streamlit phục vụ Vibe Coding mượt mà, dễ sửa và tiết kiệm token theo mô hình CCPM (Claude Code Project Manager).

## 1. Tiết Kiệm Token & Ngăn Ngừa Evaporation (Context Evaporation Prevention)
- **Kích thước File ngắn gọn**: Mỗi file `.py` chỉ chứa tối đa 150 dòng code. Nếu phát triển tính năng mới, hãy tự động tạo module mới trong `src/components/` hoặc `src/services/`.
- **Tách biệt giao diện (UI) và Logic**:
  - UI Streamlit (widgets, layout, columns) -> Đặt tại `src/components/`.
  - Logic tính toán, gọi API, xử lý data -> Đặt tại `src/services/`.
  - Quản lý Session State -> Đặt tại `src/utils/state_manager.py`.
- **Duy trì Single Source of Truth**: AI khi nhận prompt mới luôn chủ động nạp `contexts/features/feature_log.md` và `contexts/features/project_overview.md` để giữ vững ngữ cảnh dự án.

## 2. Chuẩn Code Streamlit (Pure Streamlit Widget)
- Sử dụng các widget native của Streamlit:
  - Header & Layout: `st.set_page_config`, `st.title`, `st.sidebar`, `st.columns`, `st.expander`, `st.tabs`.
  - Hiển thị dữ liệu: `st.dataframe`, `st.metric`, `st.json`, `st.line_chart`, `st.bar_chart`.
  - Nhập liệu & Form: `st.form`, `st.text_input`, `st.selectbox`, `st.button`, `st.download_button`.
- Hạn chế sử dụng `st.markdown(..., unsafe_allow_html=True)` ngoại trừ trường hợp cần chỉnh spacing nhẹ. KHÔNG dùng HTML/CSS phức tạp.

## 3. Kiểm Tra Lỗi & Quản Lý Session State An Toàn
- **Tự kiểm tra cú pháp**: AI phải kiểm tra cú pháp code bằng `py_compile` trước khi bàn giao kết quả cho người dùng.
- **Session State safe-check**: Tất cả các biến `st.session_state` PHẢI được khởi tạo giá trị mặc định tại `src/utils/state_manager.py` trước khi ứng dụng render để phòng tránh lỗi `KeyError`.
