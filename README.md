# Outline Thông Minh — Full-stack MVP

Website responsive hỗ trợ học sinh lớp 12 quản lý nhiệm vụ, thời gian biểu, tiến độ và nhắc nhở. Frontend React + TypeScript + Vite; backend FastAPI; SQLite.

## 1. Yêu cầu
- Python 3.11+ (khuyến nghị 3.12)
- Node.js 20+

## 2. Chạy backend trên Windows
Mở terminal tại thư mục dự án:
```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```
Mở `backend/.env`, thay `SECRET_KEY` bằng chuỗi bí mật dài và đặt `ADMIN_PASSWORD` riêng dài ít nhất 12 ký tự. Sau đó tạo Admin:
```powershell
python -m app.core.admin_setup
```
Chạy API:
```powershell
uvicorn app.main:app --reload
```
API docs: http://127.0.0.1:8000/docs

Nếu PowerShell chặn activate, dùng CMD và chạy `.venv\Scripts\activate.bat`.

## 3. Chạy frontend
Mở terminal thứ hai tại thư mục gốc:
```powershell
cd frontend
npm install
npm run dev
```
Mở URL hiện ra, thường là http://localhost:5173.

## 4. Tài khoản
- Học sinh: đăng ký từ giao diện, sau đó đăng nhập.
- Admin: dùng `ADMIN_USERNAME` và `ADMIN_PASSWORD` đã đặt trong `backend/.env`. Không đăng ký Admin qua giao diện.
- Không commit file `.env` hoặc database chứa dữ liệu thật.

## 5. Chức năng hiện có
- Đăng ký, đăng nhập bằng JWT, endpoint thông tin tài khoản.
- Hash mật khẩu PBKDF2-HMAC-SHA256.
- Phân quyền admin ở backend; admin xem/khóa/mở khóa tài khoản học sinh.
- CRUD nhiệm vụ cơ bản, đánh dấu hoàn thành, tiến độ tính từ dữ liệu database.
- Tạo lịch học, phát hiện trùng giờ.
- Nhắc nhở phía trình duyệt khi website đang mở; có thể hiện Web Notification nếu đã cấp quyền.

## 6. Giới hạn cần biết
- Chuông dựa trên việc website đang mở; trình duyệt/OS có thể chặn autoplay âm thanh. Nếu cần nhắc khi trình duyệt đóng, cần triển khai Web Push/service worker và backend push.
- Dashboard MVP hiển thị nhiệm vụ theo ngày hiện tại; thống kê thời gian học thực tế và biểu đồ tuần chưa được triển khai.
- Cấu trúc database tự tạo bảng khi khởi động phù hợp MVP; production nên dùng migration Alembic, HTTPS, refresh-token/cookie an toàn, rate limiting và kiểm thử bảo mật.
