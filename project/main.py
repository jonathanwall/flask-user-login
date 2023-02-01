import flask
import flask_login
from . import db

main = flask.Blueprint("main", __name__)


@main.route("/")
def index():
    return flask.render_template("index.html")


@main.route("/profile")
@flask_login.login_required
def profile():
    return flask.render_template("profile.html", name=flask_login.current_user.name)
