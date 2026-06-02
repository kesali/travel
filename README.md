# Travel Adviser

A static, social-feed-style travel app built with Flask. This is the **lesson 1** version — no database, no real user accounts, just mock data and HTML templates.

## How to run

```
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Configuration

The app reads its secret key from the `FLASK_SECRET_KEY` environment variable. A `.env` file in this directory is loaded automatically by `python-dotenv` at startup, so for local development you just need:

```
FLASK_SECRET_KEY=any-non-empty-string
```

A working `.env` is committed alongside this README so the project runs out of the box. In a real project you would:
- Add `.env` to `.gitignore` so secrets never reach the repo
- Commit `.env.example` (also included here) as a template for collaborators
- Set the real value in your hosting platform (Heroku, Render, etc.)

If the env var is missing the app fails to start with a clear `KeyError` — better to know up front than to silently fall back to an insecure default.

## Folder structure

```
travel_adviser/
  app.py            # create_app() factory and entry point
  models.py         # Trip and Comment dataclasses
  trip_data.py      # mock data (TRIPS, WISHLIST_BY_USER)
  services.py       # business logic (queries, search, visibility rules)
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
```

## What each layer does

- **models.py** — the shape of the data. Two dataclasses (`Trip`, `Comment`). Same `@dataclass` pattern as lesson 10.
- **trip_data.py** — the actual mock data lives here as plain Python lists. In a future lesson this gets replaced by a database. Nothing else has to change.
- **services.py** — the operations: `get_trip`, `can_view_trip`, `get_feed_trips`, `get_wishlist_trips`, `get_journal_trips`. Routes never touch `trip_data` directly; they always go through services.
- **routes/** — Flask blueprints. Each file groups related routes. The blueprint's name prefixes endpoints, so `url_for("feed.index")` and `url_for("auth.login_form")` in templates.
- **app.py** — the wiring. `create_app()` (the application factory pattern) loads `.env`, builds the app, reads the secret key from the environment, registers blueprints, and injects `current_user` into every template via a context processor.

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

## Why these patterns

- **Application factory** (`create_app()`) — the canonical Flask setup. Keeps initialisation in one obvious place and makes testing easier later on.
- **Blueprints** — the canonical way to split routes by feature. Each blueprint groups related views, and the blueprint's name prefixes its endpoint names. That is why every `url_for(...)` in the templates uses the dotted form.
- **Dataclasses** — `Trip` and `Comment` are dataclasses (callback to lesson 10), so we get named attributes (`trip.title`, `comment.author`) and type hints across the whole app.
- **Layered architecture** — `routes/ → services → data + models`. Each layer only knows the one below it. When we add a database later, only `trip_data.py` (and maybe `services.py`) change; the routes and templates do not notice.

## Mocked images and avatars

- Trip photos use [picsum.photos](https://picsum.photos) with a stable seed per trip — these are placeholder images, **not** real photos of the destinations.
- Author "avatars" are pure HTML/CSS: a coloured circle showing the first letter of the author's name. No external dependency.

## What is not wired up yet

The following exist visually in the templates but are not functional in lesson 1:

- **Like / Save / Share buttons** on the trip detail page — they look like buttons but do nothing yet.
- **Comment form** at the bottom of a trip — the input is there but submitting it shows an alert.

These will be wired to real routes and a database in a later lesson.

## Future lessons (planned)

- Replace `trip_data.py` with a SQLite database (callback to lesson 10's `UserManager`)
- Forms for posting new trips and comments (replacing the placeholder buttons above)
- Real users table with passwords
- AI helper to suggest trips based on preferences
- Image uploads, real likes/saves, follow relationships
