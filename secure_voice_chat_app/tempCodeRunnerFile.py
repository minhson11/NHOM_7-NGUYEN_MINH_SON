# app.py - Ứng dụng Flask chính để gửi, nhận và xác minh tin nhắn âm thanh bảo mật. 

import os
from flask import Flask, request, render_template, jsonify, redirect, url_for
from utils import rsa_utils, aes_utils, hash_utils, audio_utils
from binascii import unhexlify, hexlify
from chat_controller import chat_bp

app = Flask(__name__)
app.register_blueprint(chat_bp)

# Trang khởi đầu mô phỏng handshake đơn giản
@app.route('/')
def index():
    return render_template('chatroom.html')

# Bắt đầu phiên chat - người gửi bắt đầu
@app.route('/start', methods=['GET'])
def start_chat():
    # Mô phỏng handshake đơn giản
    handshake_info = {
        "status": "Connection Accepted",
        "sender_public_key": rsa_utils.get_sender_public_key_base64(),
        "receiver_public_key": rsa_utils.get_receiver_public_key_base64()
    }
    return jsonify(handshake_info)

# Trang tải lên có hỗ trợ tiến trình
@app.route('/upload', methods=['GET'])
def upload_audio_form():
    return render_template('index.html')

# Trang khung chat 2 chiều
@app.route('/chatroom', methods=['GET'])
def chatroom():
    return render_template('chatroom.html')

# Người gửi gửi file âm thanh, thực hiện mã hóa và ký
@app.route('/send', methods=['POST'])
def send_audio():
    file = request.files.get('audio')
    if not file:
        return "Không có file âm thanh!", 400

    audio_data = file.read()

    # Mã hóa AES-256 CBC
    aes_key, iv, ciphertext = aes_utils.encrypt_audio(audio_data)

    # Hash IV || ciphertext và ký bằng RSA
    data_to_hash = iv + ciphertext
    hash_val = hash_utils.compute_hash(data_to_hash)
    signature = rsa_utils.sign_data(hash_val)

    # Mã hóa khóa AES bằng RSA
    encrypted_aes_key = rsa_utils.encrypt_key_for_receiver(aes_key)

    # Gói xác thực (mô phỏng signed_info)
    auth_packet = {
        "signed_info": hexlify(signature).decode(),
        "encrypted_aes_key": hexlify(encrypted_aes_key).decode()
    }

    # Gói dữ liệu chính
    data_packet = {
        "iv": hexlify(iv).decode(),
        "cipher": hexlify(ciphertext).decode(),
        "hash": hexlify(hash_val).decode(),
        "sig": hexlify(signature).decode(),
        "encrypted_key": hexlify(encrypted_aes_key).decode()
    }

    return render_template('receive.html', packet=data_packet, auth=auth_packet)

# Người nhận xác minh và giải mã
@app.route('/verify', methods=['POST'])
def verify_audio():
    data = request.get_json()
    try:
        iv = unhexlify(data['iv'])
        cipher = unhexlify(data['cipher'])
        hash_received = unhexlify(data['hash'])
        sig = unhexlify(data['sig'])
        encrypted_key = unhexlify(data['encrypted_key'])

        # Giải mã khóa AES
        aes_key = rsa_utils.decrypt_key_from_sender(encrypted_key)

        # Kiểm tra tính toàn vẹn
        valid_hash = hash_utils.verify_hash(iv + cipher, hash_received)

        # Kiểm tra chữ ký
        valid_sig = rsa_utils.verify_signature(hash_received, sig)

        if not valid_hash:
            return jsonify({"status": "NACK", "reason": "Integrity check failed"}), 400
        if not valid_sig:
            return jsonify({"status": "NACK", "reason": "Signature invalid"}), 400

        # Giải mã dữ liệu
        audio = aes_utils.decrypt_audio(cipher, aes_key, iv)
        audio_utils.save_audio_bytes(audio)

        return jsonify({"status": "ACK"}), 200

    except Exception as e:
        return jsonify({"status": "NACK", "reason": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)