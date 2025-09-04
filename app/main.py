from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware

from app.routers import router
from app.config import API_PREFIX, ORIGINS
from app.database import init_db

app = FastAPI()

origins = ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(router, prefix=API_PREFIX)


@app.get("/")
async def root():
    return {"message": "Hello and Welcome to educatu server."}