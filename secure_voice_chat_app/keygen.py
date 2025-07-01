# keygen.py - Tạo cặp khóa RSA cho sender và receiver. 

import os
import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils.rsa_utils import save_keys

KEY_DIR = "keys"

def ensure_key_folder():
    if not os.path.exists(KEY_DIR):
        os.makedirs(KEY_DIR)

def main():
    ensure_key_folder()

    print("🔐 Đang tạo khóa cho người gửi (sender)...")
    save_keys(f"{KEY_DIR}/sender_priv.pem", f"{KEY_DIR}/sender_pub.pem")
    print("✅ Đã lưu sender_priv.pem và sender_pub.pem")

    print("🔐 Đang tạo khóa cho người nhận (receiver)...")
    save_keys(f"{KEY_DIR}/receiver_priv.pem", f"{KEY_DIR}/receiver_pub.pem")
    print("✅ Đã lưu receiver_priv.pem và receiver_pub.pem")

    print("🎉 Hoàn tất sinh khóa!")

if __name__ == "__main__":
    main()
