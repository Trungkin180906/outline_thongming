# Kiến trúc tổng quan

```text
Học sinh / Admin
       |
       v
Frontend React + TypeScript
       |
       | HTTP API
       v
Backend FastAPI
  |-- auth: đăng ký, đăng nhập, phân quyền
  |-- schedules: thời gian biểu
  |-- tasks: nhiệm vụ và tiến độ
  |-- reminders: dữ liệu nhắc nhở
  |-- admin: quản trị tài khoản
       |
       v
SQLite (MVP) -> có thể nâng cấp PostgreSQL
```

## Vai trò
- `student`: chỉ xem và sửa dữ liệu thuộc tài khoản của mình.
- `admin`: tài khoản được tạo/cấu hình riêng, không đăng ký công khai.

## Dashboard
- Tỷ lệ hoàn thành = số nhiệm vụ hoàn thành / tổng số nhiệm vụ * 100.
- Khi chưa có nhiệm vụ, tỷ lệ hiển thị là 0% hoặc trạng thái trống.
- Số liệu phải được tính từ dữ liệu thật, không hard-code trong bản chạy thật.

## Nhắc nhở
Frontend có thể phát âm thanh và hiển thị thông báo khi ứng dụng đang hoạt động và đã được cấp quyền. Muốn nhắc khi trình duyệt đóng cần triển khai push notification/service phù hợp; không thể bảo đảm chỉ bằng timer JavaScript.
