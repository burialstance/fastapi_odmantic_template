from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.containers import RootContainer
from src.db.mongo import MongoDatabase

router = APIRouter()


@router.get('')
@inject
async def healthcheck(
        db: MongoDatabase = Depends(Provide[RootContainer.database.mongo]),
):
    return {
        'database': await db.get_connection_status()
    }
