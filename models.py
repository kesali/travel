from dataclasses import dataclass


@dataclass
class Comment:
    author: str
    body: str
    posted_at: str


@dataclass
class Trip:
    id: str
    kind: str            # "featured" or "post"
    author: str
    city: str
    country: str
    title: str
    summary: str
    image: str
    hero: str
    gallery: list[str]
    tags: list[str]
    visibility: str      # "public" or "private"
    posted_at: str
    likes: int
    comments: list[Comment]
    # Featured-only extras; None for regular user posts.
    highlights: list[str] | None = None
    best_season: str | None = None
    daily_budget: str | None = None

# I'm Monica and this is a test
