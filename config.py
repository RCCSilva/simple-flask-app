
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    RESPONSE_TEXT = os.environ.get('RESPONSE_TEXT') or 'You did not configure the RESPONSE_TEXT variable!'
