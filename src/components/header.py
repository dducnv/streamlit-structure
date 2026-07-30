import streamlit as st
from config.settings import APP_TITLE, APP_ICON


def render_header() -> None:
    """Hiển thị Header và Banner của ứng dụng"""
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title(f"{APP_ICON} {APP_TITLE}")
    st.caption("🚀 Framework Streamlit dành cho Marketer & Content Creators - Tối ưu cho AI Vibe Coding")
    st.divider()


def render_sidebar() -> str:
    """Hiển thị Thanh điều hướng Sidebar"""
    with st.sidebar:
        st.header("📌 Điều Hướng")
        mode = st.radio(
            "Chọn chế độ:",
            options=["Demo Dashboard", "Thêm Chiến Dịch Mới"],
            index=0,
        )
        
        st.divider()
        st.info(
            "💡 **Mẹo Vibe Coding**:\n\n"
            "Khi muốn thêm tính năng mới, hãy gắn kèm đường dẫn file `contexts/features/feature_log.md` "
            "trong câu prompt để AI nắm bắt ngữ cảnh dự án!"
        )
        return mode
