from contextlib import asynccontextmanager

from fastapi import FastAPI

from src import api
from src.app import get_settings, Settings
from src.containers import RootContainer


@asynccontextmanager
async def fastapi_lifespan(app: FastAPI):
    api.register(app, include_healthcheck=True)

    container: RootContainer = getattr(app.state, 'container')
    if init_resources := container.init_resources():
        await init_resources

    yield

    if shutdown_resources := container.shutdown_resources():
        await shutdown_resources


def create_app(**kwargs) -> FastAPI:
    settings: Settings = get_settings()

    _app = FastAPI(
        debug=settings.app.debug,
        title=settings.app.title,
        description=settings.app.description,
        version=settings.app.version,
        lifespan=fastapi_lifespan,
        **kwargs
    )
    _app.state.container = RootContainer(settings=settings)
    return _app


app = create_app()



