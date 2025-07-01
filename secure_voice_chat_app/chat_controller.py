# chat_controller.py - Quản lý luồng chat 2 chiều. 

import os
import uuid
import time
from datetime import datetime
from flask import Blueprint, request, jsonify
from utils import rsa_utils, aes_utils, hash_utils, audio_utils
from binascii import unhexlify, hexlify

chat_bp = Blueprint('chat', __name__)

CHAT_LOG = []  # Lưu danh sách gói tin
UPLOAD_FOLDER = "static/messages"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@chat_bp.route("/chat/send", methods=["POST"])
def send_message():
    file = request.files.get("audio")
    user_id = request.form.get("user_id", "")

    if not file or not user_id:
        return jsonify({"error": "Thiếu file hoặc user_id"}), 400

    audio_data = file.read()
    filename = file.filename or f"upload_{uuid.uuid4()}"
    filesize_kb = round(len(audio_data) / 1024, 2)

    start_time = time.time()
    aes_key, iv, ciphertext = aes_utils.encrypt_audio(audio_data)
    data_to_hash = iv + ciphertext
    hash_val = hash_utils.compute_hash(data_to_hash)
    signature = rsa_utils.sign_data(hash_val)
    encrypted_aes_key = rsa_utils.encrypt_key_for_receiver(aes_key)
    encode_time = round(time.time() - start_time, 3)

    packet_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    CHAT_LOG.append({
        "id": packet_id,
        "iv": hexlify(iv).decode(),
        "cipher": hexlify(ciphertext).decode(),
        "hash": hexlify(hash_val).decode(),
        "sig": hexlify(signature).decode(),
        "encrypted_key": hexlify(encrypted_aes_key).decode(),
        "from_user": user_id,
        "filename": filename,
        "filesize": filesize_kb,
        "encode_time": encode_time,
        "timestamp": timestamp,
        "direction": "sent"
    })

    log_line = f"[{timestamp}] {user_id} gửi file {filename} ({filesize_kb} KB) | mã hoá: {encode_time}s"

    return jsonify({"status": "sent", "id": packet_id, "log": log_line})

@chat_bp.route("/chat/messages", methods=["GET"])
def get_messages():
    return jsonify(CHAT_LOG)

@chat_bp.route("/chat/verify/<packet_id>", methods=["POST"])
def verify_message(packet_id):
    try:
        msg = next((p for p in CHAT_LOG if p["id"] == packet_id), None)
        if not msg:
            return jsonify({"status": "error", "reason": "Not found"}), 404

        iv = unhexlify(msg['iv'])
        cipher = unhexlify(msg['cipher'])
        hash_received = unhexlify(msg['hash'])
        sig = unhexlify(msg['sig'])
        encrypted_key = unhexlify(msg['encrypted_key'])

        start = time.time()
        aes_key = rsa_utils.decrypt_key_from_sender(encrypted_key)
        valid_hash = hash_utils.verify_hash(iv + cipher, hash_received)
        valid_sig = rsa_utils.verify_signature(hash_received, sig)
        decode_time = round(time.time() - start, 3)

        if not valid_hash:
            return jsonify({"status": "fail", "reason": "Hash mismatch"}), 400
        if not valid_sig:
            return jsonify({"status": "fail", "reason": "Signature invalid"}), 400

        decrypted_data = aes_utils.decrypt_audio(cipher, aes_key, iv)
        
        # Xử lý file với định dạng gốc
        original_extension = os.path.splitext(msg.get("filename", ""))[1].lower()
        filename = f"{packet_id}{original_extension}"
        path = os.path.join(UPLOAD_FOLDER, filename)
        
        # Đảm bảo định dạng âm thanh phù hợp với trình duyệt
        if original_extension in ['.mp3', '.wav', '.ogg']:
            audio_utils.save_file_bytes(decrypted_data, original_extension, path)
            file_type = "audio"
        elif original_extension == '.txt':
            audio_utils.save_file_bytes(decrypted_data, original_extension, path)
            file_type = "text"
        else:
            # Nếu không phải định dạng hỗ trợ, vẫn lưu nhưng coi là binary
            audio_utils.save_file_bytes(decrypted_data, original_extension, path)
            file_type = "binary"

        msg["decrypted"] = filename
        msg["direction"] = "received"

        return jsonify({
            "status": "success",
            "file": f"/static/messages/{filename}",
            "decode_time": decode_time,
            "original_name": msg.get("filename", ""),
            "file_type": file_type
        })

    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500
