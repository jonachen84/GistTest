import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    GITHUB_API_URL = os.getenv('GITHUB_API_URL', 'https://api.github.com')
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
