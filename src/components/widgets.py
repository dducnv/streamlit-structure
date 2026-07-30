import streamlit as st
import pandas as pd
from services.data_service import save_new_campaign, load_campaign_data


def render_metrics_cards(df: pd.DataFrame) -> None:
    """Hiển thị các thẻ chỉ số chính (Metrics Cards)"""
    col1, col2, col3 = st.columns(3)

    total_campaigns = len(df)
    total_budget = df["budget"].sum() if not df.empty and "budget" in df.columns else 0.0
    active_count = len(df[df["status"] == "Active"]) if not df.empty and "status" in df.columns else 0

    with col1:
        st.metric(label="Tổng Số Chiến Dịch", value=f"{total_campaigns}")
    with col2:
        st.metric(label="Tổng Ngân Sách ($)", value=f"${total_budget:,.2f}")
    with col3:
        st.metric(label="Đang Hoạt Động", value=f"{active_count}")

    st.divider()


def render_data_table(df: pd.DataFrame) -> None:
    """Hiển thị bảng dữ liệu chiến dịch"""
    st.subheader("📊 Danh Sách Chiến Dịch Marketing")
    if df.empty:
        st.warning("Chưa có dữ liệu chiến dịch nào.")
    else:
        st.dataframe(
            df,
            column_config={
                "id": "ID",
                "campaign_name": "Tên Chiến Dịch",
                "channel": "Kênh Marketing",
                "budget": st.column_config.NumberColumn("Ngân Sách ($)", format="$%.2f"),
                "status": "Trạng Thái",
            },
            use_container_width=True,
            hide_index=True,
        )


def render_add_campaign_form() -> None:
    """Hiển thị Form thêm chiến dịch mới"""
    st.subheader("➕ Thêm Chiến Dịch Marketing Mới")
    
    with st.form("add_campaign_form", clear_on_submit=True):
        campaign_name = st.text_input("Tên chiến dịch:", placeholder="Ví dụ: TikTok Ads Q4 Launch")
        channel = st.selectbox("Kênh Marketing:", ["Facebook", "Google Ads", "TikTok", "Email Marketing", "SEO / Content"])
        budget = st.number_input("Ngân sách ($):", min_value=10.0, max_value=100000.0, value=500.0, step=50.0)
        status = st.selectbox("Trạng thái:", ["Active", "Paused", "Completed"])

        submitted = st.form_submit_button("Lưu Chiến Dịch", type="primary")

        if submitted:
            if not campaign_name.strip():
                st.error("Vui lòng nhập tên chiến dịch!")
            else:
                success = save_new_campaign(campaign_name, channel, budget, status)
                if success:
                    st.success(f"Đã thêm chiến dịch '{campaign_name}' thành công!")
                    st.balloons()
                else:
                    st.error("Không thể lưu chiến dịch. Vui lòng kiểm tra lại.")
