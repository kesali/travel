from flask import Blueprint, render_template, request, abort

from services import get_trip, can_view_trip, get_feed_trips
from routes.auth import viewer_name


bp = Blueprint("feed", __name__)


@bp.get("/")
def index():
    query = request.args.get("q", "").strip()
    trips = get_feed_trips(viewer=viewer_name(), query=query)
    return render_template("index.html", trips=trips, query=query)


@bp.get("/trip/<trip_id>")
def trip_detail(trip_id: str):
    trip = get_trip(trip_id)
    if trip is None or not can_view_trip(trip, viewer_name()):
        abort(404)
    return render_template("trip.html", trip=trip)
