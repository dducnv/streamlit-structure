#!/usr/bin/env bash

# =======================================================
# SCRIPT TỰ ĐỘNG CHẠY APP STREAMLIT (DÀNH CHO MACOS / LINUX)
# Người dùng chỉ cần nhấp đúp hoặc gõ: ./run.sh
# =======================================================

echo "🚀 Đang kiểm tra môi trường chạy ứng dụng Streamlit..."

# 1. Kiểm tra Python và tự động cài đặt nếu chưa có
if ! command -v python3 &> /dev/null; then
    echo "Chưa tìm thấy Python 3 trên máy tính!"
    echo "Đang cố gắng tự động cài đặt Python 3..."
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if ! command -v brew &> /dev/null; then
            echo "🍺 Chưa cài đặt Homebrew. Đang tiến hành cài đặt Homebrew (có thể yêu cầu mật khẩu)..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            
            # Đưa brew vào PATH ngay lập tức (dành cho Apple Silicon và Intel)
            if [ -x /opt/homebrew/bin/brew ]; then
                eval "$(/opt/homebrew/bin/brew shellenv)"
            elif [ -x /usr/local/bin/brew ]; then
                eval "$(/usr/local/bin/brew shellenv)"
            fi
        fi

        if command -v brew &> /dev/null; then
            echo "Đang cài đặt Python 3 bằng Homebrew..."
            brew install python3
        else
            echo "Cài đặt Homebrew thất bại. Vui lòng tải Python từ: https://www.python.org/downloads/"
            exit 1
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        if command -v apt-get &> /dev/null; then
            echo "🐧 Đang cài đặt bằng apt-get (có thể sẽ yêu cầu mật khẩu sudo)..."
            sudo apt-get update && sudo apt-get install -y python3 python3-venv python3-pip
        elif command -v yum &> /dev/null; then
            echo "🐧 Đang cài đặt bằng yum (có thể sẽ yêu cầu mật khẩu sudo)..."
            sudo yum install -y python3
        elif command -v dnf &> /dev/null; then
            echo "🐧 Đang cài đặt bằng dnf (có thể sẽ yêu cầu mật khẩu sudo)..."
            sudo dnf install -y python3
        elif command -v pacman &> /dev/null; then
            echo "🐧 Đang cài đặt bằng pacman (có thể sẽ yêu cầu mật khẩu sudo)..."
            sudo pacman -S --noconfirm python
        else
            echo "❌ Không tìm thấy trình quản lý gói phổ biến. Vui lòng tự cài Python."
            exit 1
        fi
    else
        echo "❌ Hệ điều hành không hỗ trợ tự động cài đặt. Vui lòng tải Python từ: https://www.python.org/downloads/"
        exit 1
    fi
    
    # Kiểm tra lại sau khi cài đặt
    if ! command -v python3 &> /dev/null; then
        echo "❌ Cài đặt tự động thất bại. Vui lòng tự cài đặt bằng tay."
        exit 1
    else
        echo "✅ Đã cài đặt Python 3 thành công!"
    fi
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
