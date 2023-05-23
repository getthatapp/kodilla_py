from flask import Flask
from .data import generate_data
from .database import db
from config import Config
from flask_migrate import Migrate

migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.cli.command("generate-data")
    def _generate_data():
        with app.app_context():
            generate_data()

    return app
