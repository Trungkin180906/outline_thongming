from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Boolean, Time
from sqlalchemy.sql import func

from app.db.session import Base


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    title = Column(String(200), nullable=False)
    subject = Column(String(100), nullable=True)
    schedule_date = Column(Date, nullable=False, index=True)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    priority = Column(String(20), nullable=False, default="medium")
    reminder_enabled = Column(Boolean, nullable=False, default=True)
    reminder_minutes_before = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
