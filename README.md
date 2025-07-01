

<li>Chạy ứng dụng:
    <pre><code>python app.py</code></pre>
  </li>
  <li>Truy cập ứng dụng tại: <code>http://127.0.0.1:5000</code></li>
</ol>

<h3>Hướng dẫn sử dụng</h3>
<ol>
  <li><strong>Chọn vai trò:</strong> Chọn User A hoặc User B từ dropdown</li>
  <li><strong>Gửi tin nhắn:</strong>
    <ul>
      <li>Chọn file âm thanh/văn bản hoặc ghi âm trực tiếp</li>
      <li>Nhấn "Gửi" để mã hóa và gửi</li>
    </ul>
  </li>
  <li><strong>Nhận tin nhắn:</strong>
    <ul>
      <li>Tin nhắn sẽ hiển thị trong chatbox</li>
      <li>Nhấn "Giải mã" để xác minh và giải mã</li>
      <li>Phát lại nội dung đã giải mã</li>
    </ul>
  </li>
</ol>

<h3>Tính năng bảo mật</h3>
<ul>
  <li><strong>Mã hóa đầu cuối:</strong> Dữ liệu được mã hóa ngay tại client</li>
  <li><strong>Tính toàn vẹn:</strong> Kiểm tra hash để phát hiện thay đổi</li>
  <li><strong>Xác thực:</strong> Chữ ký số đảm bảo nguồn gốc</li>
  <li><strong>Bảo mật khóa:</strong> Khóa AES được mã hóa bằng RSA</li>
  <li><strong>Không lưu trữ:</strong> Dữ liệu không được lưu vĩnh viễn</li>
</ul>

<h3>Giao diện ứng dụng</h3>
<p><strong>Giao diện chat 2 chiều với mã hóa bảo mật:</strong></p>
<p align="center">
  <img src="https://github.com/minhson11/NHOM_7-NGUYEN_MINH_SON/blob/main/1.jpg" alt="Giao diện chat bảo mật" width="800">
  <img src="https://github.com/minhson11/NHOM_7-NGUYEN_MINH_SON/blob/main/2.jpg" alt="Giao diện chat bảo mật" width="800">
  <img src="https://github.com/minhson11/NHOM_7-NGUYEN_MINH_SON/blob/main/3.jpg" alt="Giao diện chat bảo mật" width="800">
</p>

<h3>Thông số kỹ thuật</h3>
<ul>
  <li><strong>Thuật toán mã hóa:</strong> AES-256-CBC</li>
  <li><strong>Độ dài khóa RSA:</strong> 2048 bits</li>
  <li><strong>Hàm băm:</strong> SHA-256</li>
  <li><strong>Định dạng âm thanh:</strong> WAV, MP3, OGG</li>
  <li><strong>Định dạng file:</strong> Hỗ trợ tất cả loại file</li>
</ul>

<h3>Yêu cầu hệ thống</h3>
<ul>
  <li>Python 3.7+</li>
  <li>Trình duyệt hỗ trợ WebRTC (Chrome, Firefox, Safari)</li>
  <li>Microphone (cho tính năng ghi âm)</li>
  <li>Kết nối mạng (để giao tiếp giữa các client)</li>
</ul>

<h3>Lưu ý bảo mật</h3>
<p><strong>⚠️ Quan trọng:</strong></p>
<ul>
  <li>Đây là demo giáo dục, không sử dụng trong môi trường production</li>
  <li>Khóa RSA được hardcode trong demo, cần thay đổi trong thực tế</li>
  <li>Cần implement key exchange protocol an toàn hơn</li>
  <li>Nên sử dụng HTTPS trong môi trường thực</li>
</ul>

<p align="center">
  <strong>Phát triển bởi:</strong><br>
  <em>Nhóm 7 - CNTT 17-01 - Khoa Công nghệ Thông tin - Đại học Đại Nam</em><br>
  <em>Môn: Nhập môn An toàn Bảo mật Thông tin</em>
</p>
