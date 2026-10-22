from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_current_user, get_db
from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse, UserResponse
router = APIRouter(prefix="/auth", tags=["Authentication"])
@router.post("/register", response_model=UserResponse, status_code=201)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter((User.username == data.username) | (User.email == data.email)).first():
        raise HTTPException(status_code=409, detail="Tên đăng nhập hoặc email đã được sử dụng")
    user = User(username=data.username, email=data.email.lower(), full_name=data.full_name.strip(), password_hash=hash_password(data.password), role="student", is_active=True)
    db.add(user); db.commit(); db.refresh(user)
    return user
@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Tên đăng nhập hoặc mật khẩu không đúng")
    if not user.is_active: raise HTTPException(status_code=403, detail="Tài khoản đã bị khóa")
    return {"access_token": create_access_token(user.username, user.role), "token_type":"bearer", "user":user}
@router.get("/me", response_model=UserResponse)
def me(user: User = Depends(get_current_user)):
    return user
