from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP
import os
import base64

# Đường dẫn thư mục chứa khóa
KEY_DIR = "keys"
os.makedirs(KEY_DIR, exist_ok=True)

# Đường dẫn các file khóa
SENDER_PRIVATE_KEY = os.path.join(KEY_DIR, "sender_priv.pem")
SENDER_PUBLIC_KEY = os.path.join(KEY_DIR, "sender_pub.pem")
RECEIVER_PRIVATE_KEY = os.path.join(KEY_DIR, "receiver_priv.pem")
RECEIVER_PUBLIC_KEY = os.path.join(KEY_DIR, "receiver_pub.pem")

def generate_key_pair(key_size=2048):
    """Tạo cặp khóa RSA mới"""
    key = RSA.generate(key_size)
    return key

def save_keys(private_key_path: str, public_key_path: str, key_size=2048):
    """
    Tạo và lưu cặp khóa RSA
    :param private_key_path: Đường dẫn lưu private key
    :param public_key_path: Đường dẫn lưu public key
    :param key_size: Độ dài khóa (2048 hoặc 4096 bit)
    """
    key = generate_key_pair(key_size)
    
    # Lưu private key
    with open(private_key_path, 'wb') as f:
        f.write(key.export_key())
    
    # Lưu public key
    with open(public_key_path, 'wb') as f:
        f.write(key.publickey().export_key())

def get_sender_public_key_base64() -> str:
    """Lấy public key của người gửi dạng base64"""
    with open(SENDER_PUBLIC_KEY, 'rb') as f:
        key = RSA.import_key(f.read())
        return base64.b64encode(key.export_key()).decode('utf-8')

def get_receiver_public_key_base64() -> str:
    """Lấy public key của người nhận dạng base64"""
    with open(RECEIVER_PUBLIC_KEY, 'rb') as f:
        key = RSA.import_key(f.read())
        return base64.b64encode(key.export_key()).decode('utf-8')

def sign_data(data: bytes) -> bytes:
    """
    Ký dữ liệu bằng private key của người gửi
    :param data: Dữ liệu cần ký (dạng bytes)
    :return: Chữ ký số (dạng bytes)
    """
    if not os.path.exists(SENDER_PRIVATE_KEY):
        raise FileNotFoundError(f"Private key not found at {SENDER_PRIVATE_KEY}")
    
    with open(SENDER_PRIVATE_KEY, "rb") as key_file:
        private_key = RSA.import_key(key_file.read())
    
    h = SHA256.new(data)
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

def verify_signature(data_hash: bytes, signature: bytes) -> bool:
    """
    Xác minh chữ ký bằng public key của người gửi
    :param data_hash: Giá trị hash của dữ liệu
    :param signature: Chữ ký cần xác minh
    :return: True nếu chữ ký hợp lệ, False nếu không
    """
    if not os.path.exists(SENDER_PUBLIC_KEY):
        raise FileNotFoundError(f"Public key not found at {SENDER_PUBLIC_KEY}")
    
    with open(SENDER_PUBLIC_KEY, "rb") as key_file:
        public_key = RSA.import_key(key_file.read())
    
    try:
        pkcs1_15.new(public_key).verify(SHA256.new(data_hash), signature)
        return True
    except (ValueError, TypeError):
        return False

def encrypt_key_for_receiver(aes_key: bytes) -> bytes:
    with open(RECEIVER_PUBLIC_KEY, "rb") as key_file:
        public_key = RSA.import_key(key_file.read())
    
    cipher = PKCS1_OAEP.new(public_key, hashAlgo=SHA256)  # Thêm hashAlgo
    return cipher.encrypt(aes_key)

def decrypt_key_from_sender(encrypted_key: bytes) -> bytes:
    with open(RECEIVER_PRIVATE_KEY, "rb") as key_file:
        private_key = RSA.import_key(key_file.read())
    
    cipher = PKCS1_OAEP.new(private_key, hashAlgo=SHA256)  # Thêm hashAlgo
    return cipher.decrypt(encrypted_key)

