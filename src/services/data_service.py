import json
import pandas as pd
from typing import List, Dict, Any
from config.settings import DATA_DIR

SAMPLE_DATA_FILE = DATA_DIR / "sample_data.json"


def load_campaign_data() -> List[Dict[str, Any]]:
    """
    Đọc dữ liệu chiến dịch từ file JSON trong thư mục data/.
    Trả về danh sách các dictionary.
    """
    if not SAMPLE_DATA_FILE.exists():
        return []
    
    try:
        with open(SAMPLE_DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Lỗi khi đọc file dữ liệu: {e}")
        return []


def save_new_campaign(campaign_name: str, channel: str, budget: float, status: str = "Active") -> bool:
    """
    Thêm một chiến dịch mới vào file sample_data.json.
    """
    current_data = load_campaign_data()
    new_id = max([item.get("id", 0) for item in current_data], default=0) + 1

    new_item = {
        "id": new_id,
        "campaign_name": campaign_name,
        "channel": channel,
        "budget": budget,
        "status": status,
    }
    
    current_data.append(new_item)

    try:
        with open(SAMPLE_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(current_data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Lỗi khi lưu dữ liệu: {e}")
        return False


def get_data_as_dataframe() -> pd.DataFrame:
    """Chuyển đổi dữ liệu thành Pandas DataFrame để hiển thị trên bảng Streamlit"""
    data = load_campaign_data()
    if not data:
        return pd.DataFrame(columns=["id", "campaign_name", "channel", "budget", "status"])
    return pd.DataFrame(data)
