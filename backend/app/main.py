from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import Base, engine
from app.models import user, task, schedule, user_settings  # noqa: F401
from app.api.routes import auth, tasks, schedules, admin
from app.core.config import settings

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Outline Thông Minh API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://outline-thongming-frontend.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")
app.include_router(schedules.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
@app.get("/")
def root(): return {"message":"Outline Thông Minh API đang chạy", "docs":"/docs"}
@app.get("/api/health")
def health(): return {"status":"ok"}
