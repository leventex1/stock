import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY: str = os.getenv("API_KEY")
    DB_MAIN_URI: str = os.getenv("DB_MAIN_URI")
    DB_CACHE_URI: str = os.getenv("DB_CACHE_URI")
    BASE_API: str = os.getenv("BASE_API")