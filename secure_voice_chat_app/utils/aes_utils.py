# aes_utils.py - Mã hóa và giải mã bằng AES-256 (CBC) cho dữ liệu âm thanh
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = 16  # AES block size
KEY_SIZE = 32    # AES-256

def generate_aes_key() -> bytes:
    return get_random_bytes(KEY_SIZE)

def encrypt_audio(audio_data: bytes) -> tuple[bytes, bytes, bytes]:
    """
    Mã hóa dữ liệu bằng AES-256-CBC
    Trả về: key, iv, ciphertext
    """
    key = generate_aes_key()
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(audio_data, BLOCK_SIZE))
    return key, iv, ciphertext

def decrypt_audio(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    """
    Giải mã dữ liệu AES-CBC. Ném lỗi rõ ràng nếu giải mã sai.
    """
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plain_audio = unpad(cipher.decrypt(ciphertext), BLOCK_SIZE)
        return plain_audio
    except (ValueError, KeyError) as e:
        raise ValueError(f"Giải mã thất bại: {str(e)}")
