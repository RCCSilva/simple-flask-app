from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

from config import Config

db = SQLAlchemy()
migrate = Migrate()


class Posts(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return {'status': 'ok', 'message': Config.RESPONSE_TEXT}

    @app.route('/health')
    def index():
        return {'status': 'ok'}

    @app.route('/post', methods=['POST'])
    def create_post():
        name = request.json['name']
        post = Posts(name=name)
        db.session.add(post)
        db.session.commit()

        return post.to_dict()

    @app.route('/posts', methods=['GET'])
    def get_posts():
        posts = Posts.query.all()
        return {'data': [p.to_dict() for p in posts]}

    return app
