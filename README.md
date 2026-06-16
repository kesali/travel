# Travel Adviser

A social-feed-style travel app built with Flask, with a SQLAlchemy database underneath. Trip data is stored in SQLite and seeded from starter data on first run. There are no real user accounts yet — "login" is name-only.

## How to run

```
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Tailwind CSS

This project already uses Tailwind CSS for styling, but it uses the **Tailwind Play CDN** instead of an npm build step.

The Tailwind script is loaded in [templates/base.html](c:/Users/DursunaliK/Desktop/lesson/project/travel_adviser/templates/base.html), so every template that extends `base.html` can use Tailwind utility classes immediately.

```html
<script src="https://cdn.tailwindcss.com"></script>
```

### What this means for developers

- No `npm install` step is required.
- No `tailwind.config.js` file is needed for the current setup.
- You add styling by writing Tailwind classes directly in the Jinja templates.
- Shared layout styles should usually go in `templates/base.html`.

### When to use this setup

This CDN approach is fine for a small lesson project because it is simple and keeps the project focused on Flask basics.

If the app grows later, consider switching to the Tailwind CLI or a Node-based build so you can:

- generate a smaller production CSS bundle,
- customize the Tailwind theme,
- scan templates automatically for used classes,
- and keep styling easier to manage as the project gets larger.

## Configuration

The app reads two settings from environment variables, loaded automatically from a `.env` file by `python-dotenv` at startup:

```
FLASK_SECRET_KEY=any-non-empty-string
DATABASE_URL=sqlite:///travel.db
```

- `FLASK_SECRET_KEY` signs the session cookie. If it is missing the app fails to start with a clear `KeyError` — better than silently falling back to an insecure default.
- `DATABASE_URL` is the SQLAlchemy connection string. It is optional; if unset the app defaults to `sqlite:///travel.db`. With Flask-SQLAlchemy a relative SQLite path lands in the `instance/` folder, so the database file is created at `instance/travel.db` (gitignored — delete it to reset the data).

A working `.env` is committed alongside this README so the project runs out of the box. In a real project you would:
- Add `.env` to `.gitignore` so secrets never reach the repo
- Commit `.env.example` (also included here) as a template for collaborators
- Set the real values in your hosting platform (Heroku, Render, etc.)

## Folder structure

```
travel_adviser/
  app.py            # create_app() factory; also creates tables and seeds on first run
  models.py         # SQLAlchemy ORM models (Trip, Comment) + the db handle
  trip_data.py      # build_seed_trips() starter rows + WISHLIST_BY_USER
  services.py       # business logic: DB queries, search, visibility, seeding
  routes/           # Flask blueprints, one per feature area
    __init__.py     # (empty - just marks routes as a package)
    feed.py         # / and /trip/<id>
    auth.py         # /login, /logout, current_user()
    logbook.py      # /logbook
  templates/        # Jinja templates
    base.html
    index.html      # the feed
    trip.html       # a single post
    login.html
    logbook.html
  instance/
    travel.db       # SQLite database (created at runtime, gitignored)
```

## What each layer does

- **models.py** — the shape of the data, as SQLAlchemy ORM models. `Trip` and `Comment` are `db.Model` classes; each `Mapped[...]` attribute becomes a database column. A `Trip` has many `Comment`s via a relationship, so `trip.comments` is a list you can loop over in a template.
- **trip_data.py** — `build_seed_trips()` returns the starter rows as ORM objects, plus `WISHLIST_BY_USER`. This is only used to fill an empty database; once seeded, the database is the source of truth.
- **services.py** — the operations: `get_trip`, `can_view_trip`, `get_feed_trips`, `get_wishlist_trips`, `get_journal_trips`, and `seed_database`. These run SQLAlchemy queries (`db.session.get`, `select(...)`). Routes never touch the database directly; they always go through services.
- **routes/** — Flask blueprints. Each file groups related routes. The blueprint's name prefixes endpoints, so `url_for("feed.index")` and `url_for("auth.login_form")` in templates.
- **app.py** — the wiring. `create_app()` (the application factory pattern) loads `.env`, builds the app, reads config from the environment, binds the database with `db.init_app(app)`, registers blueprints, injects `current_user` into every template, and on first run creates the tables (`db.create_all()`) and seeds them.

## Authentication in lesson 1

There is no real login yet. The `/login` route just stores whatever name you type into Flask's signed session cookie. In a later lesson we will add a real `users` table with passwords.

The "current user" gates two things:
- Whose **private** trips show up in the feed (private posts are visible only to their author).
- Access to `/logbook` — redirects to `/login` if nobody is signed in.

Try signing in as **`Alex`** — that account has mock wishlist and journal entries.

## Visibility model

Each trip has a visibility:
- `public` — everyone sees it.
- `private` — only the author sees it.

The `can_view_trip` function in `services.py` is the single source of truth for this rule. It is used both by the feed filter and by the trip-detail 404 guard.

## Database (SQLAlchemy)

The app uses [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) on top of SQLite.

- **Models** — `Trip` and `Comment` in `models.py` are ORM classes. Each `Mapped[...]` attribute is a column. List fields (`gallery`, `tags`, `highlights`) are stored as JSON in a single column, which is fine at this scale; comments are a proper related table.
- **Relationship** — `Trip.comments` is a one-to-many relationship to `Comment`. SQLAlchemy loads the related rows for you, and `cascade="all, delete-orphan"` means deleting a trip deletes its comments.
- **Session** — queries go through `db.session`: `db.session.get(Trip, trip_id)` for a single row by primary key, `db.session.scalars(select(Trip)...)` for many.
- **Seeding** — on first run `app.py` calls `db.create_all()` then `seed_database()`, which loads the starter trips only if the table is empty. Re-running the app does not duplicate data.
- **Resetting** — delete `instance/travel.db` and restart; the tables are recreated and reseeded.

The trips keep a `position` column purely to control feed order, because rows in a database have no inherent order — you only get a predictable order when you ask for one with `ORDER BY` (here, `.order_by(Trip.position)`).

## Why these patterns

- **Application factory** (`create_app()`) — the canonical Flask setup. Keeps initialisation in one obvious place and makes testing easier later on.
- **Blueprints** — the canonical way to split routes by feature. Each blueprint groups related views, and the blueprint's name prefixes its endpoint names. That is why every `url_for(...)` in the templates uses the dotted form.
- **ORM (SQLAlchemy)** — instead of writing raw SQL like lesson 10's `UserManager`, we describe tables as Python classes and let SQLAlchemy generate the SQL. We still get named attributes (`trip.title`, `comment.author`) and type hints (`Mapped[str]`), now backed by a real database. Compare this with the raw `sqlite3` approach from lesson 10 — same idea, less boilerplate, and relationships handled for you.
- **Layered architecture** — `routes/ → services → data + models`. Each layer only knows the one below it. Swapping the in-memory list for a database only touched `models.py`, `trip_data.py`, `services.py`, and a few lines of `app.py`; the routes and templates did not change at all.

## Mocked images and avatars

- Trip photos use [picsum.photos](https://picsum.photos) with a stable seed per trip — these are placeholder images, **not** real photos of the destinations.
- Author "avatars" are pure HTML/CSS: a coloured circle showing the first letter of the author's name. No external dependency.

## What is not wired up yet

The following exist visually in the templates but are not functional in lesson 1:

- **Like / Save / Share buttons** on the trip detail page — they look like buttons but do nothing yet.
- **Comment form** at the bottom of a trip — the input is there but submitting it shows an alert.

These will be wired to real routes and a database in a later lesson.

## Future lessons (planned)

- Forms for posting new trips and comments that write to the database (replacing the placeholder buttons above)
- A real `users` table with passwords, replacing name-only login
- Move the wishlist into the database as a many-to-many relationship between users and trips
- AI helper to suggest trips based on preferences
- Image uploads, real likes/saves, follow relationships
