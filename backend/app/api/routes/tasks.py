from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.api.deps import get_current_user, get_db
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
router = APIRouter(prefix="/tasks", tags=["Tasks"])
@router.get("/", response_model=list[TaskResponse])
def list_tasks(due_date: date | None = None, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    q = db.query(Task).filter(Task.user_id == user.id)
    if due_date: q = q.filter(Task.due_date == due_date)
    return q.order_by(Task.due_date, Task.start_time).all()
@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(data: TaskCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if data.start_time and data.end_time and data.end_time <= data.start_time: raise HTTPException(422, "Giờ kết thúc phải sau giờ bắt đầu")
    task = Task(user_id=user.id, **data.model_dump())
    db.add(task); db.commit(); db.refresh(task); return task
@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
    if not task: raise HTTPException(404, "Không tìm thấy nhiệm vụ")
    for key, value in data.model_dump(exclude_unset=True).items(): setattr(task, key, value)
    if task.start_time and task.end_time and task.end_time <= task.start_time: raise HTTPException(422, "Giờ kết thúc phải sau giờ bắt đầu")
    db.commit(); db.refresh(task); return task
@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
    if not task: raise HTTPException(404, "Không tìm thấy nhiệm vụ")
    db.delete(task); db.commit(); return Response(status_code=204)
