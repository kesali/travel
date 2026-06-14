from flask import Blueprint, session, request, redirect, url_for, render_template


bp = Blueprint("auth", __name__)


def current_user() -> str | None:
    return session.get("user")


@bp.get("/login")
def login_form():
    return render_template("login.html")

@bp.get("/register")
def register_form():
    return render_template("register.html")


@bp.post("/login")
def login():
    name = request.form.get("name", "").strip()
    if name:
        session["user"] = name
    return redirect(url_for("logbook.logbook"))


@bp.post("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("feed.index"))
