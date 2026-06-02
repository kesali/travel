import os

from dotenv import load_dotenv
from flask import Flask

from routes.feed import bp as feed_bp
from routes.auth import bp as auth_bp, current_user
from routes.logbook import bp as logbook_bp


load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.environ["FLASK_SECRET_KEY"]

    app.register_blueprint(feed_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(logbook_bp)

    @app.context_processor
    def inject_current_user():
        return {"current_user": current_user()}

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
