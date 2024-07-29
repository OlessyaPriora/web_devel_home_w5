from flask import Flask
from flask_migrate import Migrate

from app.models import db
from app.routes.categories import categories_bp
from app.routes.questions import questions_bp
from app.routes.responses import responses_bp
from config import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    app.register_blueprint(questions_bp)
    app.register_blueprint(responses_bp)
    app.register_blueprint(categories_bp)
    return app
