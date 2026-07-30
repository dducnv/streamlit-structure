import streamlit as st
from typing import Any


def init_session_state(defaults: dict = None) -> None:
    """Khởi tạo các biến Session State an toàn để tránh lỗi KeyError"""
    initial_defaults = {
        "initialized": True,
    }
    if defaults:
        initial_defaults.update(defaults)

    for key, value in initial_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def get_state(key: str, default_val: Any = None) -> Any:
    """Truy cập biến state an toàn"""
    return st.session_state.get(key, default_val)


def set_state(key: str, value: Any) -> None:
    """Cập nhật biến state an toàn"""
    st.session_state[key] = value
