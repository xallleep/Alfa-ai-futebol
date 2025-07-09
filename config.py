import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-render')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///predictions.db').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False