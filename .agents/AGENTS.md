# QUY TẮC VIBE CODING & QUẢN LÝ CONTEXT DÀNH CHO AI AGENT

Bạn là AI Assistant hỗ trợ lập trình **TOÀN TỰ ĐỘNG (Auto-Pilot)** cho người dùng (Marketer, Content Creator, người KHÔNG BIẾT CODE) xây dựng ứng dụng Web bằng **Streamlit**.

Người dùng CHỈ CẦN đưa ra ý tưởng/yêu cầu bằng ngôn ngữ tự nhiên. **AI CHỊU TRÁCH NHIỆM LÀM TOÀN BỘ CÁC BƯỚC KỸ THUẬT**.

---

## 1. NGUYÊN TẮC "AI LÀM TẤT CẢ" (ZERO-CODE FOR USER)

- **Người dùng KHÔNG CẦN đụng vào code**, không tự tạo file hay chỉnh sửa cấu trúc.
- Khi người dùng nói ý tưởng (ví dụ: *"Tạo giúp tôi công cụ viết caption Facebook"* hoặc *"Thêm bảng tính ROI"*), AI tự động:
  1. Tự phân tích yêu cầu thành các UI Widget & Logic tương ứng.
  2. Tự tạo/sửa file UI trong `src/components/`.
  3. Tự viết logic xử lý dữ liệu/API trong `src/services/`.
  4. Tự đăng ký biến state trong `src/utils/state_manager.py`.
  5. Tự kiểm tra cú pháp code (chạy py_compile nếu có lệnh).
  6. Tự động ghi lại tóm tắt tính năng vào `contexts/features/feature_log.md`.
  7. Hướng dẫn người dùng cách trải nghiệm hoặc nhấn nút chạy đơn giản nhất.

---

## 2. QUY TẮC KỸ THUẬT CỐ ĐỊNH (BẮT BUỘC TUÂN THỦ)

1. **Thuần Streamlit (Pure Streamlit Widget)**:
   - CHỈ sử dụng các widget native của Streamlit (`st.metric`, `st.dataframe`, `st.columns`, `st.form`, `st.sidebar`, ...).
   - KHÔNG bắt người dùng viết HTML, CSS, JavaScript.
2. **Tiết kiệm Token (Token Efficiency)**:
   - Chia nhỏ code thành các file trong `src/components/`, `src/services/`, `src/utils/`.
   - Mỗi file CHỈ dài dưới 150 dòng code.
   - Giữ file `app.py` cực kỳ tinh gọn (< 40 dòng).
3. **Bảo mật & Cấu hình**:
   - KHÔNG bao giờ hardcode API Keys, password hay secrets trong code.
   - Luôn sử dụng `config/settings.py` hoặc `st.secrets` / `.env` để đọc biến môi trường.
4. **Không ngắt gãy ứng dụng**:
   - Khởi tạo tất cả `st.session_state` qua `src/utils/state_manager.py` để tránh lỗi `KeyError`.
   - Xử lý try-except khi đọc/ghi dữ liệu trong `src/services/data_service.py`.

---

## 3. QUY TRÌNH QUẢN LÝ CONTEXT TỰ ĐỘNG

Trước khi viết code, AI CẦN:
1. Tự đọc quy chuẩn tại `contexts/rules/security_rules.md` và `contexts/rules/coding_standards.md`.
2. Kiểm tra sơ đồ vị trí file tại `contexts/rules/architecture_map.md`.
3. Kiểm tra tính năng hiện tại trong `contexts/features/feature_log.md`.

**SAU KHI THÊM/SỬA BẤT KỲ TÍNH NĂNG NÀO**:
👉 AI **BẮT BUỘC** tự động cập nhật nhật ký tính năng vào file `contexts/features/feature_log.md` theo định dạng:
- **Tên tính năng mới / chỉnh sửa**.
- **File đã thay đổi** (ví dụ: `src/components/widgets.py`).
- **Mô tả ngắn gọn & State Schema** (ví dụ: `st.session_state.user_data`).

Mục đích: Đảm bảo các lượt prompt tiếp theo của người dùng (dù rất ngắn như "sửa lại cái nút") AI vẫn nắm 100% ngữ cảnh dự án mà tốn cực kỳ ít token!
