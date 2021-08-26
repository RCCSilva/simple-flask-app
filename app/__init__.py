from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return {'status': 'ok', 'message': Config.RESPONSE_TEXT}

    return app