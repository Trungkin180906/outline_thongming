"""Chạy `python -m app.core.admin_setup` từ thư mục backend để tạo/cập nhật Admin."""
from app.core.config import settings
from app.core.security import hash_password
from app.db.session import Base, SessionLocal, engine
from app.models.user import User
from app.models import task, schedule, user_settings  # noqa: F401
Base.metadata.create_all(bind=engine)
db = SessionLocal()
try:
    username = settings.admin_username
    password = settings.admin_password
    if password == "change-this-password" or len(password) < 12:
        raise SystemExit("Hãy đặt ADMIN_PASSWORD dài ít nhất 12 ký tự trong file .env trước khi tạo Admin.")
    user = db.query(User).filter(User.username == username).first()
    if user:
        user.role = "admin"; user.password_hash = hash_password(password); user.is_active = True
        user.email = user.email or f"{username}@localhost.invalid"
        user.full_name = "System Administrator"
    else:
        user = User(username=username, email=f"{username}@localhost.invalid", full_name="System Administrator", password_hash=hash_password(password), role="admin", is_active=True)
        db.add(user)
    db.commit()
    print(f"Admin '{username}' đã được tạo/cập nhật. Hãy giữ bí mật thông tin đăng nhập.")
finally:
    db.close()
