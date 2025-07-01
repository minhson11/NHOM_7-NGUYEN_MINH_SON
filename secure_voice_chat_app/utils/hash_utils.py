# hash_utils.py - Tạo và kiểm tra giá trị băm bằng SHA-512.

from Crypto.Hash import SHA256

def compute_hash(data: bytes) -> bytes:
    """
    Tính giá trị băm của dữ liệu đầu vào bằng SHA-512
    """
    h = SHA256.new()
    h.update(data)
    return h.digest()

def verify_hash(data: bytes, expected_hash: bytes) -> bool:
    """
    So sánh giá trị băm tính được và băm mong đợi
    """
    h = SHA256.new()
    h.update(data)
    return h.digest() == expected_hash
