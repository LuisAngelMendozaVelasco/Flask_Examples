import os

os.makedirs('instance', exist_ok=True)

class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.getcwd()}/instance/tasks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
