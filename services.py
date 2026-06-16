from sqlalchemy import select

from models import db, Trip
from trip_data import build_seed_trips, WISHLIST_BY_USER


def seed_database() -> None:
    """Populate an empty database with the starter trips. No-op if rows exist."""
    already_seeded = db.session.scalar(select(Trip).limit(1)) is not None
    if already_seeded:
        return
    for position, trip in enumerate(build_seed_trips()):
        trip.position = position
        db.session.add(trip)
    db.session.commit()


def get_trip(trip_id: str) -> Trip | None:
    return db.session.get(Trip, trip_id)


def can_view_trip(trip: Trip, viewer: str | None) -> bool:
    if trip.visibility == "private":
        return viewer is not None and trip.author == viewer
    return True


def get_feed_trips(viewer: str | None, query: str = "") -> list[Trip]:
    """Trips visible to the viewer, optionally filtered by a search query.
    Matches case-insensitively against title, summary, city, country, author, and tags.
    """
    trips = db.session.scalars(select(Trip).order_by(Trip.position)).all()
    visible = [t for t in trips if can_view_trip(t, viewer)]

    q = query.lower().strip()
    if not q:
        return visible

    results = []
    for trip in visible:
        haystack = " ".join([
            trip.title, trip.summary, trip.city, trip.country, trip.author,
            " ".join(trip.tags),
        ]).lower()
        if q in haystack:
            results.append(trip)
    return results


def get_wishlist_trips(user: str) -> list[Trip]:
    ids = WISHLIST_BY_USER.get(user, [])
    trips = [db.session.get(Trip, tid) for tid in ids]
    return [t for t in trips if t is not None]


def get_journal_trips(user: str) -> list[Trip]:
    stmt = select(Trip).where(Trip.author == user).order_by(Trip.position)
    return list(db.session.scalars(stmt).all())
