import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    RESPONSE_TEXT = os.environ.get('RESPONSE_TEXT') or 'You did not configure the RESPONSE_TEXT variable!'

    DATABASE_USER = os.environ['DATABASE_USER']
    DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
    DATABASE_HOST = os.environ['DATABASE_HOST']
    DATABASE_PORT = os.environ['DATABASE_PORT']
    DATABASE_NAME = os.environ['DATABASE_NAME']

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}' \
                              f'/{DATABASE_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
