# Configuration settings for Flask App

import os

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    DEBUG = os.environ.get('DEBUG') in ['True', 'true', '1']

    # API keys
    API_KEY = os.environ.get('API_KEY')
    ANOTHER_API_KEY = os.environ.get('ANOTHER_API_KEY')

    # Other environment variables
    DATABASE_URI = os.environ.get('DATABASE_URI')
    SOME_OTHER_SETTING = os.environ.get('SOME_OTHER_SETTING')
