import flask
from . import db

main = flask.Blueprint("main", __name__)


@main.route("/")
def index():
    return flask.render_template("index.html")


@main.route("/profile")
def profile():
    return flask.render_template("profile.html")
