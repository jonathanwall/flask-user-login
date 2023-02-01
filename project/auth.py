import flask
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
import flask_login

auth = flask.Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return flask.render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    remember = True if flask.request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flask.flash("Please check your login details and try again.")
        return flask.redirect(flask.url_for("auth.login"))

    flask_login.login_user(user, remember=remember)
    return flask.redirect(flask.url_for("main.profile"))


@auth.route("/signup")
def signup():
    return flask.render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
    email = flask.request.form.get("email")
    name = flask.request.form.get("name")
    password = flask.request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user:
        flask.flash("Email address already exists")
        return flask.redirect(flask.url_for("auth.signup"))

    new_user = User(
        email=email, name=name, password=generate_password_hash(password, method="sha256")
    )

    db.session.add(new_user)
    db.session.commit()

    return flask.redirect(flask.url_for("auth.login"))


@auth.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for("main.index"))
