from flask import Blueprint, render_template, request, redirect, url_for

from services import get_wishlist_trips, get_journal_trips
from routes.auth import current_user


bp = Blueprint("logbook", __name__)


@bp.get("/logbook")
def logbook():
    user = current_user()
    if user is None:
        return redirect(url_for("auth.login_form"))

    tab = request.args.get("tab", "wishlist")
    if tab not in {"wishlist", "journal"}:
        tab = "wishlist"

    return render_template(
        "logbook.html",
        tab=tab,
        wishlist=get_wishlist_trips(user),
        journal=get_journal_trips(user),
        user_name=user,
    )
