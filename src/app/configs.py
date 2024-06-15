import logging
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from pydantic import MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


logging.basicConfig(level=logging.INFO)

BASE_DIR = Path(__file__).parent.parent
ENV_FILE = BASE_DIR.parent.joinpath('.env')


class BaseEnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore'
    )


class AppSettings(BaseEnvSettings):
    debug: bool = False
    title: str = 'telegram cryptobox provider'
    version: str = '0.0.1'
    description: str = 'provider backend'


class MongoSettings(BaseEnvSettings):
    url: str | None = None
    database: str


class RedisSettings(BaseSettings):
    url: str | None = None


@dataclass
class Settings:
    app: AppSettings
    mongo: MongoSettings
    redis: RedisSettings

    @classmethod
    def build(cls) -> 'Settings':
        return cls(
            app=AppSettings(_env_prefix='APP_'),
            mongo=MongoSettings(_env_prefix='MONGO_'),
            redis=RedisSettings(_env_prefix='REDIS_')
        )


@lru_cache
def get_settings() -> Settings:
    return Settings.build()
