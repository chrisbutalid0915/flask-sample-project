import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# CONSTANT
BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    # setup database
    # DATABASE_NAME = os.getenv('DATABASE_NAME', 'db') 
    # SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/{DATABASE_NAME}.sqlite3" # SQLite
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:password@postgres:5432/app_db" # postgreSQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "a3f9b74e8c6d0e2a92e90118d7c19e85"  # Configure SECRET KEY
    ALGORITHM="HS256"
    # Load in enviornemnt variables
    TESTING = True
    FLASK_DEBUG = True
    SERVER = "0.0.0.0"
    ERROR_404_HELP = False # disable 404 error occurs
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30