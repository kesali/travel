from flask import Blueprint,flash, session, request, redirect, url_for, render_template


bp = Blueprint("auth", __name__)


def current_user() -> str | None:
    return session.get("user")


@bp.get("/login")
def login_form():
    return render_template("login.html")

@bp.post("/login")
def login():
    name = request.form.get("name", "").strip()
    if name:
        session["user"] = name
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


@bp.post("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("feed.index"))
