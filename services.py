from models import Trip
from trip_data import TRIPS, WISHLIST_BY_USER


# Built once at import time so get_trip is O(1).
_BY_ID: dict[str, Trip] = {t.id: t for t in TRIPS}


def get_trip(trip_id: str) -> Trip | None:
    return _BY_ID.get(trip_id)


def can_view_trip(trip: Trip, viewer: str | None) -> bool:
    if trip.visibility == "private":
        return viewer is not None and trip.author == viewer
    return True


def get_feed_trips(viewer: str | None, query: str = "") -> list[Trip]:
    """Trips visible to the viewer, optionally filtered by a search query.
    Matches case-insensitively against title, summary, city, country, author, and tags.
    """
    q = query.lower().strip()
    results: list[Trip] = []
    for trip in TRIPS:
        if not can_view_trip(trip, viewer):
            continue
        if q:
            haystack = " ".join([
                trip.title, trip.summary, trip.city, trip.country, trip.author,
                " ".join(trip.tags),
            ]).lower()
            if q not in haystack:
                continue
        results.append(trip)
    return results


def get_wishlist_trips(user: str) -> list[Trip]:
    ids = WISHLIST_BY_USER.get(user, [])
    return [_BY_ID[tid] for tid in ids if tid in _BY_ID]


def get_journal_trips(user: str) -> list[Trip]:
    return [t for t in TRIPS if t.author == user]
