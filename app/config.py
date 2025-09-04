import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ENVIRONMENT = os.environ.get("ENVIRONMENT")
DEBUG = os.environ.get("DEBUG", False)
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
CLIENT_URL = os.getenv("CLIENT_URL")
ORIGINS = [
    CLIENT_URL
]
API_PREFIX = "/api"
TOKEN_SECRET_KEY = "knm5e5xxyxe6g8ufmnwk"
TOKEN_ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 120   # in min
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"