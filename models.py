from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# Shared SQLAlchemy handle. app.py binds it to the Flask app with db.init_app().
db = SQLAlchemy(model_class=Base)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    # No password column yet - login is name-only. That comes in a later lesson.

    # UserMixin supplies is_authenticated / is_active / is_anonymous / get_id()
    # that Flask-Login needs, so we don't have to write them ourselves.


class Trip(db.Model):
    __tablename__ = "trips"

    id: Mapped[str] = mapped_column(primary_key=True)   # slug, e.g. "rome-guide"
    position: Mapped[int]                               # display order in the feed
    kind: Mapped[str]                                   # "featured" or "post"
    author: Mapped[str]
    city: Mapped[str]
    country: Mapped[str]
    title: Mapped[str]
    summary: Mapped[str]
    image: Mapped[str]
    hero: Mapped[str]
    visibility: Mapped[str]                             # "public" or "private"
    posted_at: Mapped[str]
    likes: Mapped[int]

    # Lists are stored as JSON in a single column - fine at this scale.
    gallery: Mapped[list[str]] = mapped_column(JSON)
    tags: Mapped[list[str]] = mapped_column(JSON)

    # Featured-only extras; NULL for regular user posts.
    highlights: Mapped[list[str] | None] = mapped_column(JSON)
    best_season: Mapped[str | None]
    daily_budget: Mapped[str | None]

    # One trip has many comments. cascade deletes a trip's comments with it.
    comments: Mapped[list["Comment"]] = relationship(
        back_populates="trip",
        cascade="all, delete-orphan",
        order_by="Comment.id",
    )


class Comment(db.Model):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    trip_id: Mapped[str] = mapped_column(ForeignKey("trips.id"))
    author: Mapped[str]
    body: Mapped[str]
    posted_at: Mapped[str]

    trip: Mapped["Trip"] = relationship(back_populates="comments")
