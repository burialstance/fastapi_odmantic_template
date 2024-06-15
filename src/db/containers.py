from dependency_injector import containers, providers

from src.app.configs import MongoSettings
from .mongo import MongoDatabase


class DatabaseContainer(containers.DeclarativeContainer):
    settings = providers.Dependency(MongoSettings)

    mongo = providers.Singleton(
        MongoDatabase,
        url=settings.provided.url,
        database=settings.provided.database
    )
