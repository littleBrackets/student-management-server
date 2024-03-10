from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import router
from app.config import API_PREFIX, ORIGINS

app = FastAPI()

origins = ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix=API_PREFIX)

@app.get("/educatu-server")
async def root():
    return {"message": "Hello and Welcome to educatu server."}
