<h2 align="center">Ứng dụng Chat Âm thanh Bảo mật</h2>
<p>
Dự án được xây dựng bằng Python và Flask, nhằm thực hiện việc giao tiếp âm thanh bảo mật sử dụng kết hợp nhiều thuật toán mã hóa tiên tiến: AES-256 CBC, RSA và SHA-256.
</p>

<h3>Chức năng của ứng dụng</h3>
<ul>
  <li><strong>Gửi tin nhắn âm thanh bảo mật:</strong>
    <ul>
      <li>Ghi âm trực tiếp từ microphone</li>
      <li>Tải lên file âm thanh hoặc văn bản</li>
      <li>Mã hóa AES-256 CBC cho dữ liệu</li>
      <li>Mã hóa RSA cho khóa AES</li>
      <li>Ký số SHA-256 + RSA để xác thực</li>
    </ul>
  </li>
  <li><strong>Nhận và xác minh tin nhắn:</strong>
    <ul>
      <li>Xác minh tính toàn vẹn dữ liệu</li>
      <li>Xác minh chữ ký số</li>
      <li>Giải mã khóa AES bằng RSA</li>
      <li>Giải mã nội dung và phát lại</li>
    </ul>
  </li>
  <li><strong>Giao diện chat 2 chiều:</strong>
    <ul>
      <li>Chuyển đổi vai trò User A/B</li>
      <li>Hiển thị thông tin mã hóa/giải mã</li>
      <li>Phát lại file âm thanh</li>
      <li>Xem nội dung file văn bản</li>
    </ul>
  </li>
</ul>

<h3>Công nghệ bảo mật sử dụng</h3>
<ul>
  <li><strong>Mã hóa đối xứng:</strong> AES-256 CBC</li>
  <li><strong>Mã hóa bất đối xứng:</strong> RSA-2048</li>
  <li><strong>Hàm băm:</strong> SHA-256</li>
  <li><strong>Chữ ký số:</strong> RSA + SHA-256</li>
  <li><strong>Xác thực tính toàn vẹn:</strong> HMAC</li>
</ul>

<h3>Công nghệ phát triển</h3>
<ul>
  <li>Python 3.x</li>
  <li>Flask Framework</li>
  <li>HTML5 + CSS3 + JavaScript</li>
  <li>Web Audio API (MediaRecorder)</li>
  <li>Font Awesome Icons</li>
  <li>Responsive Design</li>
</ul>

<h3>Cấu trúc dự án</h3>
<ul>
  <li><code>app.py</code> - Ứng dụng Flask chính</li>
  <li><code>chat_controller.py</code> - Controller quản lý chat 2 chiều</li>
  <li><code>utils/</code> - Thư viện tiện ích:
    <ul>
      <li><code>rsa_utils.py</code> - Xử lý mã hóa RSA</li>
      <li><code>aes_utils.py</code> - Xử lý mã hóa AES</li>
      <li><code>hash_utils.py</code> - Xử lý hàm băm</li>
      <li><code>audio_utils.py</code> - Xử lý file âm thanh</li>
    </ul>
  </li>
  <li><code>templates/</code> - Giao diện HTML</li>
  <li><code>static/</code> - Tài nguyên tĩnh</li>
</ul>

<h3>Hướng dẫn cài đặt</h3>
<ol>
  <li>Cài đặt thư viện:
    <pre><code>pip install flask pycryptodome</code></pre>
    <pre><code>pip install pydub</code></pre>
  </li>
  <li>Tạo khóa RSA (nếu chưa có):
    <pre><code>python -c "from utils import rsa_utils; rsa_utils.generate_keys()"</code></pre>
  </li>
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


