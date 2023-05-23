from flask import Flask
from config import Config
from flask_migrate import Migrate

migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        from . import routes, models
        from . database import db

        db.init_app(app)
        migrate.init_app(app, db)

        app.register_blueprint(routes.main)

        from .data import generate_data

        @app.cli.command("generate-data")
        def _generate_data():
            with app.app_context():
                generate_data()

    return app
