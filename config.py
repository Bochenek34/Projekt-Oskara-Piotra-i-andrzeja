from pydantic_settings import BaseSettings

class SystemConfig(BaseSettings):
    app_mode: str = "developer"

    class Config:
        env_file = ".env"
