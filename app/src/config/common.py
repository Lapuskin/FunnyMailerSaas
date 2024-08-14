import os

from dotenv import dotenv_values, load_dotenv

load_dotenv()

PROJECT_SETTINGS = {
    'PROJECT_NAME': os.environ.get('PROJECT_NAME'),
    'DEBUG': os.environ.get('DEBUG'),
    'VERSION': os.environ.get('VERSION')
}

CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS')
CORS_ALLOWED_HEADERS = os.environ.get('CORS_ALLOWED_HEADERS')
CORS_ALLOWED_METHODS = os.environ.get('CORS_ALLOWED_METHODS')