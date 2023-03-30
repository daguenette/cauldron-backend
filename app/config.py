from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_DRIVERNAME: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE: str
    DATABASE_PORT: str

    class Config:
        env_file = ".env"

settings = Settings()