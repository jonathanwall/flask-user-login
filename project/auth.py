import flask
from . import db

auth = flask.Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "Login"


@auth.route("/signup")
def signup():
    return "Signup"


@auth.route("/logout")
def logout():
    return "Logout"
