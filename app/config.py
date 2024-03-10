import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ENVIRONMENT = os.environ.get("ENVIRONMENT")
DEBUG = os.environ.get("DEBUG", False)
ORIGINS = [
    "http://localhost:3000",
    "http://ec2-15-207-16-20.ap-south-1.compute.amazonaws.com"
]
API_PREFIX = "/educatu-server/api"
TOKEN_SECRET_KEY = "knm5e5xxyxe6g8ufmnwk"
TOKEN_ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30