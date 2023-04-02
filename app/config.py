"""
Description: The file containing configurations and settings for the application.
"""

## -- 3rd Party Imports -- ##

from pydantic import BaseSettings

## -- Extend BaseSettings -- ##

class Settings(BaseSettings):

    # Database settings
    DATABASE_URL: str
    DATABASE_DRIVERNAME: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_PORT: str

    # API settings
    API_PORT: str

    # Middleware settings
    ORIGIN_URL1: str
    ORIGIN_URL2: str

    class Config:
        env_file = ".env"

settings = Settings()