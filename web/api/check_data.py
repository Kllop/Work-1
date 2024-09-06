from fastapi import APIRouter

from starlette import status
from starlette.responses import Response

import aioredis

check_data_router = APIRouter(tags=['check_data'])
redis = aioredis.from_url("redis://redis")

@check_data_router.get('/check_data', status_code=200)
async def write_data(phone:str):
    resualt = await redis.get(phone)
    return Response(content=resualt, status_code=status.HTTP_200_OK)