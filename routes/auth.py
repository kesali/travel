from flask import Blueprint, flash, request, redirect, url_for, render_template
from flask_login import LoginManager, login_user, logout_user, current_user
from sqlalchemy import select

from models import db, User

bp = Blueprint("auth", __name__)

# Flask-Login's central object. app.py binds it with login_manager.init_app().
login_manager = LoginManager()
# Where @login_required sends anonymous visitors.
login_manager.login_view = "auth.login_form"

@login_manager.user_loader
def load_user(user_id: str) -> User | None:
    """Flask-Login stores the user id in the session; this turns it back into a User."""
    return db.session.get(User, int(user_id))


def viewer_name() -> str | None:
    """The signed-in user's name, or None. Used to filter what trips are visible."""
    return current_user.name if current_user.is_authenticated else None

@bp.get("/login")
def login_form():
    return render_template("login.html")

@bp.post("/login")
def login():
    name = request.form.get("name", "").strip()
    if name:
        user = db.session.scalar(select(User).where(User.name == name))
        if user is None:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()
        login_user(user)
    return redirect(url_for("logbook.logbook"))

@bp.get("/reset-password")
def reset_password_form():
    return render_template("reset_password.html")

@bp.post("/reset-password")
def reset_password():
    email = request.form.get("email","").strip()
    password1 = request.form.get("password1","").strip()
    password2 = request.form.get("password2","").strip()
    if password1 == password2:
        return redirect(url_for("auth.password_submitted"))
    else:
        flash("Error: different passwords!")
        return redirect(url_for("auth.reset_password_form"))

@bp.get("/password-submitted")
def password_submitted():
    return render_template("password_submitted.html")

@bp.get("/registration")
def registration_form():
    return render_template("register.html")

@bp.post("/registration")
def registration():
    return redirect(url_for("auth.login_form"))

@bp.post("/logout")
def logout():
    logout_user()
    return redirect(url_for("feed.index"))
