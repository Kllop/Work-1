import uvicorn

from fastapi import FastAPI

from api.write_data import write_data_router
from api.check_data import check_data_router

app = FastAPI()

app.include_router(write_data_router)
app.include_router(check_data_router)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=9000)