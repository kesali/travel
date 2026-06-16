from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from services import get_wishlist_trips, get_journal_trips


bp = Blueprint("logbook", __name__)


@bp.get("/logbook")
@login_required
def logbook():
    user = current_user.name

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
