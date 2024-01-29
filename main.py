from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import routers
from config import Config

app = FastAPI()

environment = Config.ENVIRONMENT
print(f"The current environment is: {environment}")

origins = [
    "http://localhost:3000",
    "http://ec2-15-207-16-20.ap-south-1.compute.amazonaws.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.router, prefix="/educatu-server/api")

@app.get("/educatu-server")
async def root():
    return {"message": "Hello and Welcome to educatu server. docker test 1"}