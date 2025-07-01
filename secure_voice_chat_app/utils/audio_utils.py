# audio_utils.py - Ghi dữ liệu âm thanh chuẩn WAV bất kể định dạng gốc là gì

import os
from io import BytesIO
from pydub import AudioSegment

TEMP_AUDIO_PATH = "static/decrypted.wav"

def save_audio_bytes(audio_bytes: bytes, path: str = TEMP_AUDIO_PATH):
    """
    Ghi âm thanh từ nhiều định dạng thành WAV chuẩn (16-bit PCM, mono, 44.1kHz)
    """
    os.makedirs("static", exist_ok=True)

    # Nhận diện định dạng từ nội dung (pydub dùng ffmpeg phía sau)
    audio = AudioSegment.from_file(BytesIO(audio_bytes))

    # Chuẩn hóa định dạng WAV có thể phát trên mọi trình duyệt
    audio = audio.set_frame_rate(44100).set_channels(1).set_sample_width(2)

    audio.export(path, format="wav")
    print(f"[DEBUG] Đã ghi file WAV tại: {path}")

def read_audio_bytes(file_path: str) -> bytes:
    """
    Đọc file âm thanh gốc bất kỳ để mã hóa
    """
    audio = AudioSegment.from_file(file_path)  # tự động đoán định dạng
    buffer = BytesIO()
    audio.export(buffer, format="wav")
    return buffer.getvalue()

def save_text_bytes(text_bytes: bytes, path: str = "static/decrypted.txt"):
    """
    Ghi dữ liệu text vào file
    """
    os.makedirs("static", exist_ok=True)
    with open(path, "wb") as f:
        f.write(text_bytes)
    print(f"[DEBUG] Đã ghi file text tại: {path}")

def save_file_bytes(file_bytes: bytes, original_extension: str, path: str = None):
    """
    Ghi file với định dạng gốc
    """
    os.makedirs("static", exist_ok=True)
    
    if not path:
        path = f"static/decrypted{original_extension}"
    
    with open(path, "wb") as f:
        f.write(file_bytes)
    
    print(f"[DEBUG] Đã ghi file tại: {path}")
    return path
