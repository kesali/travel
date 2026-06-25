import os

from dotenv import load_dotenv
from flask import Flask

from models import db
from routes.feed import bp as feed_bp
from routes.auth import bp as auth_bp, login_manager
from routes.logbook import bp as logbook_bp
from services import seed_database


load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.environ["FLASK_SECRET_KEY"]
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///travel.db")

    db.init_app(app)
    # Flask-Login also makes `current_user` available in every template.
    login_manager.init_app(app)

    app.register_blueprint(feed_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(logbook_bp)

    # Create tables and load starter data on first run.
    with app.app_context():
        db.create_all()
        seed_database()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
