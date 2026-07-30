#!/usr/bin/env bash

# =======================================================
# SCRIPT TỰ ĐỘNG CHẠY APP STREAMLIT (DÀNH CHO MACOS / LINUX)
# Người dùng chỉ cần nhấp đúp hoặc gõ: ./run.sh
# =======================================================

echo "🚀 Đang kiểm tra môi trường chạy ứng dụng Streamlit..."

# 1. Kiểm tra Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Chưa tìm thấy Python 3 trên máy tính!"
    echo "👉 Vui lòng tải và cài đặt Python từ: https://www.python.org/downloads/"
    exit 1
fi

# 2. Tự động tạo venv nếu chưa có
if [ ! -d ".venv" ]; then
    echo "📦 Đang khởi tạo môi trường ảo (.venv)..."
    python3 -m venv .venv
fi

# 3. Kích hoạt venv
source .venv/bin/activate

# 4. Tự động cài đặt thư viện nếu chưa cài
if [ -f "requirements.txt" ]; then
    echo "📥 Đang kiểm tra & cài đặt thư viện..."
    pip install -q -r requirements.txt
fi

# 5. Chạy ứng dụng Streamlit
echo "✨ Đang mở ứng dụng Streamlit trên trình duyệt..."
streamlit run app.py
