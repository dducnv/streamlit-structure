import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import streamlit as st
from utils.state_manager import init_session_state
from services.data_service import get_data_as_dataframe
from components.header import render_header, render_sidebar
from components.widgets import render_metrics_cards, render_data_table, render_add_campaign_form


def main() -> None:
    init_session_state()
    render_header()
    selected_mode = render_sidebar()
    df_campaigns = get_data_as_dataframe()
    if selected_mode == "Demo Dashboard":
        render_metrics_cards(df_campaigns)
        render_data_table(df_campaigns)
    elif selected_mode == "Thêm Chiến Dịch Mới":
        render_add_campaign_form()


if __name__ == "__main__":
    main()
