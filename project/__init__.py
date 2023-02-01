import os

import flask
import flask_sqlalchemy

# init SQLAlchemy so we can use it later in our models
db = flask_sqlalchemy.SQLAlchemy()


def create_app():
    app = flask.Flask(__name__)

    app.config["SECRET_KEY"] = os.urandom(12).hex()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app