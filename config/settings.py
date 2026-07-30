import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

# Đường dẫn tới thư mục gốc dự án
BASE_DIR = Path(__file__).resolve().parent.parent

# Ưu tiên tìm file .env trong folder config/ hoặc root
env_path_config = BASE_DIR / "config" / ".env"
env_path_root = BASE_DIR / ".env"

if env_path_config.exists():
    load_dotenv(dotenv_path=env_path_config)
elif env_path_root.exists():
    load_dotenv(dotenv_path=env_path_root)
else:
    load_dotenv()


def get_config(key: str, default: str = "") -> str:
    """
    Hàm đọc giá trị cấu hình an toàn:
    1. Ưu tiên đọc từ Streamlit Secrets (dùng trên Streamlit Cloud).
    2. Đọc từ biến môi trường OS / file .env.
    3. Trả về giá trị mặc định nếu không tìm thấy.
    """
    try:
        if hasattr(st, "secrets") and key in st.secrets:
            return str(st.secrets[key])
    except Exception:
        pass
    
    return os.getenv(key, default)


# Các hằng số cấu hình mặc định của ứng dụng
APP_TITLE = get_config("APP_TITLE", "Streamlit Starter Kit")
APP_ICON = get_config("APP_ICON", "🚀")
ENVIRONMENT = get_config("ENVIRONMENT", "development")
DEBUG_MODE = get_config("DEBUG_MODE", "True").lower() in ("true", "1", "yes")

# Thu mục lưu trữ Data
DATA_DIR = BASE_DIR / "data"
