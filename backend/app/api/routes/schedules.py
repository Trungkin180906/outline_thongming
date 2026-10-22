from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.api.deps import get_current_user, get_db
from app.models.schedule import Schedule
from app.models.user import User
from app.schemas.schedule import ScheduleCreate, ScheduleResponse
router = APIRouter(prefix="/schedules", tags=["Schedules"])
@router.get("/", response_model=list[ScheduleResponse])
def list_schedules(schedule_date: date | None = None, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    q = db.query(Schedule).filter(Schedule.user_id == user.id)
    if schedule_date: q = q.filter(Schedule.schedule_date == schedule_date)
    return q.order_by(Schedule.schedule_date, Schedule.start_time).all()
@router.post("/", response_model=ScheduleResponse, status_code=201)
def create_schedule(data: ScheduleCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if data.end_time <= data.start_time: raise HTTPException(422, "Giờ kết thúc phải sau giờ bắt đầu")
    conflict = db.query(Schedule).filter(Schedule.user_id == user.id, Schedule.schedule_date == data.schedule_date, Schedule.start_time < data.end_time, Schedule.end_time > data.start_time).first()
    if conflict: raise HTTPException(409, f"Lịch bị trùng với: {conflict.title}")
    item = Schedule(user_id=user.id, **data.model_dump()); db.add(item); db.commit(); db.refresh(item); return item
@router.delete("/{schedule_id}", status_code=204)
def delete_schedule(schedule_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    item = db.query(Schedule).filter(Schedule.id == schedule_id, Schedule.user_id == user.id).first()
    if not item: raise HTTPException(404, "Không tìm thấy lịch học")
    db.delete(item); db.commit(); return Response(status_code=204)
