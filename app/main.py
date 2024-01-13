from fastapi import FastAPI

from .routers import routers

app = FastAPI()

app.include_router(routers.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}