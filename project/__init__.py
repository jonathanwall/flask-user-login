import os

import flask
import flask_sqlalchemy
import flask_login

# init SQLAlchemy so we can use it later in our models
db = flask_sqlalchemy.SQLAlchemy()


def create_app():
    app = flask.Flask(__name__)

    app.config["SECRET_KEY"] = os.urandom(12).hex()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

    db.init_app(app)

    login_manager = flask_login.LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    @app.before_first_request
    def create_table():
        db.create_all()

    return app
