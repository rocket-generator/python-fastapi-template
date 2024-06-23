import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    DB_DRIVER: str = os.getenv("DB_DRIVER", "postgresql")
    DB_USERNAME: str = os.getenv("DB_USERNAME", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_HOST: str = os.getenv("DB_HOST", "127.0.0.1")
    DB_NAME: str = os.getenv("DB_NAME", "")

    SQLALCHEMY_DATABASE_URI: str = f"{DB_DRIVER}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

    AWS_ACCESS_ID: str = os.getenv("AWS_ACCESS_ID", "")
    AWS_ACCESS_SECRET: str = os.getenv("AWS_ACCESS_SECRET", "")
    S3_REGION: str = os.getenv("S3_REGION", "")
    S3_BUCKET: str = os.getenv("S3_BUCKET", "")

    JWT_SECRET: str = os.getenv("JWT_SECRET", "")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRE_MINUTES: int = int(os.getenv("JWT_EXPIRE_MINUTES", "120"))

    def __init__(self, **kwargs):
        _env = os.getenv("ENVIRONMENT", "unknown")
        super().__init__(**kwargs)
        database_uri = f"{self.DB_DRIVER}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}"
        if self.DB_DRIVER == "sqlite":
            database_uri = f"{self.DB_DRIVER}:///{self.DB_NAME}"

        self.SQLALCHEMY_DATABASE_URI = database_uri


config = Config()
