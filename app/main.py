from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import routers

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}