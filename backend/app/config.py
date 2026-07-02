from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://tecido:tecido123@localhost:5432/tecido"
    redis_url: str = "redis://localhost:6379"
    camera_source: str = "0"
    laser_port: str = "/dev/ttyUSB0"
    log_level: str = "INFO"
    defect_confidence_threshold: float = 0.7

    class Config:
        env_file = ".env"


settings = Settings()
