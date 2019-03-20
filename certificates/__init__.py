from flask import Flask
from .views import views
from .connection import db
from .config import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(views)

    return app
