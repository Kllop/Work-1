from fastapi import APIRouter
from pydantic import BaseModel

from starlette import status
from starlette.responses import Response

import aioredis

write_data_router = APIRouter(tags=['write_data'])
redis = aioredis.from_url("redis://redis")

class Item(BaseModel):
    phone: str
    address: str

@write_data_router.post('/write_data', status_code=200)
async def write_data_post(item: Item):
    await redis.set(name = item.phone, value = item.address)
    return Response(status_code=status.HTTP_200_OK)

@write_data_router.put('/write_data', status_code=200)
async def write_data_put(item: Item):
    await redis.set(name = item.phone, value = item.address)
    return Response(status_code=status.HTTP_200_OK)