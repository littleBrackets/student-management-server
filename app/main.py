from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.routers import router
from app.config import Config
from app.users import model as userModel

from app.database import engine

app = FastAPI()
userModel.Base.metadata.create_all(bind=engine)

origins = Config.ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix=Config.API_PREFIX)

@app.get("/educatu-server")
async def root():
    return {"message": "Hello and Welcome to educatu server."}