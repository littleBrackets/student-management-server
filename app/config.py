import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    ENVIRONMENT = os.environ.get("ENVIRONMENT")
    DEBUG = os.environ.get("DEBUG", False)
    ORIGINS = [
        "http://localhost:3000",
        "http://ec2-15-207-16-20.ap-south-1.compute.amazonaws.com"
    ]
    API_PREFIX = "/educatu-server/api"
    # Add other configuration variables as needed

