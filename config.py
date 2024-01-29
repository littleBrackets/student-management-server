import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    ENVIRONMENT = os.environ.get("ENVIRONMENT")
    DEBUG = os.environ.get("DEBUG", False)
    # Add other configuration variables as needed