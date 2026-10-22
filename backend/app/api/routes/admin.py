from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, require_admin
from app.models.user import User
from app.schemas.auth import UserResponse
router = APIRouter(prefix="/admin", tags=["Admin"])
@router.get("/summary")
def summary(db: Session = Depends(get_db), admin: User = Depends(require_admin)):
    return {"total_users": db.query(User).filter(User.role == "student").count(), "active_users": db.query(User).filter(User.role == "student", User.is_active.is_(True)).count()}
@router.get("/users", response_model=list[UserResponse])
def users(db: Session = Depends(get_db), admin: User = Depends(require_admin)):
    return db.query(User).filter(User.role == "student").order_by(User.created_at.desc()).all()
@router.patch("/users/{user_id}/active")
def set_active(user_id: int, active: bool, db: Session = Depends(get_db), admin: User = Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id, User.role == "student").first()
    if not user: raise HTTPException(404, "Không tìm thấy tài khoản học sinh")
    user.is_active = active; db.commit(); return {"id": user.id, "is_active": user.is_active}
