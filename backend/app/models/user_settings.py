from sqlalchemy import Boolean, Column, ForeignKey, Integer
from app.db.session import Base


class UserSettings(Base):
    __tablename__ = "user_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    daily_study_goal_minutes = Column(Integer, nullable=False, default=300)
    reminder_sound_enabled = Column(Boolean, nullable=False, default=True)
