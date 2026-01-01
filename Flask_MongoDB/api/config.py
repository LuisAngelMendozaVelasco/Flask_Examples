import os
from dotenv import load_dotenv

# Load environment variables from .env file
if not os.getenv('DB_USER'):
    load_dotenv("../.env")

# Access environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_database = os.getenv('DB_DATABASE')

class Config:
    MONGO_URI = f'mongodb://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}?authSource=admin'
