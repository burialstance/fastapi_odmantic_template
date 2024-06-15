from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient


class MongoDatabase:
    def __init__(self, url: str, database: str):
        self.client = AsyncIOMotorClient(url)
        self.engine = AIOEngine(client=self.client, database=database)

    async def get_connection_status(self) -> dict:
        try:
            return await self.client.admin.command('ping')
        except Exception as e:
            return dict(error=str(e))
