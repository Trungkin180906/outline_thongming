from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name: str = "Outline Thong Minh"
    database_url: str = "sqlite:///./outline.db"
    secret_key: str = "development-only-change-me"
    admin_username: str = "admin"
    admin_password: str = "change-this-password"
    access_token_expire_minutes: int = 60
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
settings = Settings()
