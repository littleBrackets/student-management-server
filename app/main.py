from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import routers
from app.config import Config

app = FastAPI()

origins = Config.ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.router, prefix=Config.API_PREFIX)

@app.get("/educatu-server")
async def root():
    return {"message": "Hello and Welcome to educatu server."}
