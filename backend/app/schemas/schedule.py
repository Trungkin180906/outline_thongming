from datetime import date, time
from pydantic import BaseModel, Field
class ScheduleCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    subject: str | None = None
    schedule_date: date
    start_time: time
    end_time: time
    priority: str = "medium"
    reminder_enabled: bool = True
    reminder_minutes_before: int = 0
class ScheduleResponse(BaseModel):
    id: int
    user_id: int
    title: str
    subject: str | None
    schedule_date: date
    start_time: time
    end_time: time
    priority: str
    reminder_enabled: bool
    reminder_minutes_before: int
    class Config:
        from_attributes = True
