from dependency_injector import containers, providers

from src.app import get_settings, Settings
from src.db.containers import DatabaseContainer


class RootContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        'src.api.healthcheck'
    ])

    settings = providers.Dependency(Settings)

    database = providers.Container(
        DatabaseContainer,
        settings=settings.provided.mongo
    )
