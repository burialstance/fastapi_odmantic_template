from fastapi import APIRouter, FastAPI

from . import v1
from . import healthcheck

api_router = APIRouter()
api_router.include_router(v1.router, prefix='/v1')


def register(app: FastAPI, include_healthcheck: bool = False):
    if include_healthcheck:
        app.include_router(healthcheck.router, prefix='/healthcheck')

    app.include_router(api_router, prefix='/api')
