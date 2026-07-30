import streamlit as st
from typing import Any


def init_session_state() -> None:
    """
    Khởi tạo tất cả các biến Session State mặc định.
    Giúp ứng dụng không bị lỗi KeyError khi người dùng reload hoặc thao tác UI.
    """
    defaults = {
        "initialized": True,
        "app_mode": "Demo Dashboard",
        "data_records": [],
        "last_added_item": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def get_state(key: str, default_val: Any = None) -> Any:
    """Truy cập biến state an toàn"""
    return st.session_state.get(key, default_val)


def set_state(key: str, value: Any) -> None:
    """Cập nhật biến state an toàn"""
    st.session_state[key] = value
