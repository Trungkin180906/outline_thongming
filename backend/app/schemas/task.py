from datetime import date, time
from typing import Literal
from pydantic import BaseModel, Field
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    subject: str | None = None
    description: str | None = None
    due_date: date
    start_time: time | None = None
    end_time: time | None = None
    priority: Literal["low", "medium", "high"] = "medium"
class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=200)
    subject: str | None = None
    description: str | None = None
    due_date: date | None = None
    start_time: time | None = None
    end_time: time | None = None
    priority: Literal["low", "medium", "high"] | None = None
    status: Literal["todo", "in_progress", "completed"] | None = None
class TaskResponse(BaseModel):
    id: int
    user_id: int
    title: str
    subject: str | None
    description: str | None
    due_date: date
    start_time: time | None
    end_time: time | None
    priority: str
    status: str
    class Config:
        from_attributes = True
