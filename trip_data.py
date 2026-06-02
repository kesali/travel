from models import Trip, Comment


def _gallery(seed: str) -> list[str]:
    """Four picsum URLs sharing a seed prefix, so the gallery stays stable across reloads."""
    return [f"https://picsum.photos/seed/{seed}-{i}/600/400" for i in range(1, 5)]


WISHLIST_BY_USER: dict[str, list[str]] = {
    "Alex": ["rome-guide", "kyoto-guide", "bob-kyoto-blossoms", "lisbon-guide"],
}


TRIPS: list[Trip] = [

    # ---- Featured guides curated by Travel Adviser ----

    Trip(
        id="rome-guide",
        kind="featured",
        author="Travel Adviser",
        city="Rome",
        country="Italy",
        title="Rome: ancient history meets espresso",
        summary=(
            "Rome is a layered city where ancient ruins sit next to fashion boutiques "
            "and Vespa-clogged streets. Walk the Forum at sunrise, duck into a trattoria "
            "for cacio e pepe at lunch, and watch the city glow gold from a hilltop at dusk."
        ),
        image="https://picsum.photos/seed/rome/640/400",
        hero="https://picsum.photos/seed/rome/1600/700",
        gallery=_gallery("rome"),
        tags=["europe", "history", "food"],
        visibility="public",
        posted_at="Curated guide",
        likes=142,
        comments=[
            Comment("Alice", "Did this last spring - second the Trastevere walk.", "3 weeks ago"),
            Comment("Bob", "Add the Appian Way at sunset, it's quiet.", "2 weeks ago"),
        ],
        highlights=[
            "Colosseum and Roman Forum",
            "St. Peter's Basilica and the Vatican Museums",
            "Trastevere food walk",
            "Pantheon and Piazza Navona",
        ],
        best_season="April to June, September to October",
        daily_budget="100-180",
    ),

    Trip(
        id="kyoto-guide",
        kind="featured",
        author="Travel Adviser",
        city="Kyoto",
        country="Japan",
        title="Kyoto: quiet temples and cherry blossoms",
        summary=(
            "Once Japan's imperial capital, Kyoto preserves a thousand years of temples, "
            "gardens, and tea houses. Stroll the Philosopher's Path under cherry blossoms "
            "in spring, or watch the maples burn red in November."
        ),
        image="https://picsum.photos/seed/kyoto/640/400",
        hero="https://picsum.photos/seed/kyoto/1600/700",
        gallery=_gallery("kyoto"),
        tags=["asia", "temples", "spring"],
        visibility="public",
        posted_at="Curated guide",
        likes=201,
        comments=[
            Comment("Bob", "Get there before 7am if you want a photo without crowds.", "1 month ago"),
        ],
        highlights=[
            "Fushimi Inari shrine at dawn",
            "Arashiyama bamboo grove",
            "Gion district and a tea ceremony",
            "Kinkaku-ji, the Golden Pavilion",
        ],
        best_season="Late March to early April, late November",
        daily_budget="120-200",
    ),

    Trip(
        id="reykjavik-guide",
        kind="featured",
        author="Travel Adviser",
        city="Reykjavik",
        country="Iceland",
        title="Reykjavik: northern lights and lava fields",
        summary=(
            "A small capital with outsized scenery - geothermal baths, lava beaches, "
            "and the northern lights flickering above pastel rooftops."
        ),
        image="https://picsum.photos/seed/reykjavik/640/400",
        hero="https://picsum.photos/seed/reykjavik/1600/700",
        gallery=_gallery("reykjavik"),
        tags=["nature", "winter", "scandinavia"],
        visibility="public",
        posted_at="Curated guide",
        likes=96,
        comments=[],
        highlights=[
            "Blue Lagoon geothermal spa",
            "Golden Circle: Geysir, Thingvellir, Gullfoss",
            "Northern lights tour (September to March)",
            "Reynisfjara black sand beach",
        ],
        best_season="September to March for the lights, June for the midnight sun",
        daily_budget="180-280",
    ),

    Trip(
        id="lisbon-guide",
        kind="featured",
        author="Travel Adviser",
        city="Lisbon",
        country="Portugal",
        title="Lisbon: pastel streets and ocean views",
        summary=(
            "Trams clang up steep hills, custard tarts cool on bakery shelves, and fado "
            "spills out of tiny taverns. Lisbon is bright, hilly, and easy to fall for."
        ),
        image="https://picsum.photos/seed/lisbon/640/400",
        hero="https://picsum.photos/seed/lisbon/1600/700",
        gallery=_gallery("lisbon"),
        tags=["europe", "food", "weekend"],
        visibility="public",
        posted_at="Curated guide",
        likes=88,
        comments=[
            Comment("Carla", "Sintra deserves two days, not one.", "2 months ago"),
        ],
        highlights=[
            "Alfama old town wander",
            "Belem and Pasteis de Belem",
            "Tram 28 from end to end",
            "Sintra palaces day trip",
        ],
        best_season="March to May, September to October",
        daily_budget="70-130",
    ),

    Trip(
        id="marrakech-guide",
        kind="featured",
        author="Travel Adviser",
        city="Marrakech",
        country="Morocco",
        title="Marrakech: souks, spices, and the Atlas mountains",
        summary=(
            "Inside the red walls of the medina, alleys spill into spice-fragrant souks "
            "and a square that transforms from snake charmers by day to food stalls by night."
        ),
        image="https://picsum.photos/seed/marrakech/640/400",
        hero="https://picsum.photos/seed/marrakech/1600/700",
        gallery=_gallery("marrakech"),
        tags=["africa", "markets", "food"],
        visibility="public",
        posted_at="Curated guide",
        likes=73,
        comments=[],
        highlights=[
            "Jemaa el-Fnaa night market",
            "Bahia Palace",
            "Majorelle Garden",
            "Atlas Mountains day trip",
        ],
        best_season="March to May, October to November",
        daily_budget="50-110",
    ),

    Trip(
        id="queenstown-guide",
        kind="featured",
        author="Travel Adviser",
        city="Queenstown",
        country="New Zealand",
        title="Queenstown: adventure capital of the south",
        summary=(
            "Lake Wakatipu sits in a bowl of mountains, and the small town on its shore "
            "packs a year-round menu of skiing, bungee jumping, and lakeside calm."
        ),
        image="https://picsum.photos/seed/queenstown/640/400",
        hero="https://picsum.photos/seed/queenstown/1600/700",
        gallery=_gallery("queenstown"),
        tags=["adventure", "nature", "winter"],
        visibility="public",
        posted_at="Curated guide",
        likes=115,
        comments=[],
        highlights=[
            "Skyline gondola and luge",
            "Milford Sound day trip",
            "Shotover River jet boat",
            "Routeburn Track day walk",
        ],
        best_season="December to March for summer, June to September for skiing",
        daily_budget="100-180",
    ),

    # ---- User posts ----

    Trip(
        id="alice-rome-weekend",
        kind="post",
        author="Alice",
        city="Rome",
        country="Italy",
        title="Long weekend chasing pasta",
        summary=(
            "Four days, twenty-seven plates of pasta, one Vespa burn on my ankle. "
            "We started every morning at a different bakery and finished every night "
            "with a gelato at the Pantheon. Worth every euro."
        ),
        image="https://picsum.photos/seed/alice-rome/640/400",
        hero="https://picsum.photos/seed/alice-rome/1600/700",
        gallery=_gallery("alice-rome"),
        tags=["food", "weekend", "europe"],
        visibility="public",
        posted_at="2 days ago",
        likes=38,
        comments=[
            Comment("Bob", "Which trattoria? I need a name.", "1 day ago"),
            Comment("Carla", "27 plates is goals.", "1 day ago"),
            Comment("Alex", "Saving this for my October trip.", "12 hours ago"),
        ],
    ),

    Trip(
        id="bob-kyoto-blossoms",
        kind="post",
        author="Bob",
        city="Kyoto",
        country="Japan",
        title="Cherry blossoms at 5am",
        summary=(
            "Got up before sunrise to beat the crowds at Philosopher's Path. "
            "Worth it - the canal was lined with pink and there was nobody else there. "
            "Tea at a hidden cafe in Gion afterwards."
        ),
        image="https://picsum.photos/seed/bob-kyoto/640/400",
        hero="https://picsum.photos/seed/bob-kyoto/1600/700",
        gallery=_gallery("bob-kyoto"),
        tags=["spring", "photography", "asia"],
        visibility="public",
        posted_at="5 days ago",
        likes=124,
        comments=[
            Comment("Alice", "Stunning. Which cafe?", "4 days ago"),
        ],
    ),

    Trip(
        id="carla-marrakech-souks",
        kind="post",
        author="Carla",
        city="Marrakech",
        country="Morocco",
        title="Getting wonderfully lost in the medina",
        summary=(
            "Bought a rug I did not need and ate the best tagine of my life. "
            "The trick to the souks is to stop pretending you know where you are going."
        ),
        image="https://picsum.photos/seed/carla-marrakech/640/400",
        hero="https://picsum.photos/seed/carla-marrakech/1600/700",
        gallery=_gallery("carla-marrakech"),
        tags=["markets", "food", "africa"],
        visibility="public",
        posted_at="1 week ago",
        likes=56,
        comments=[],
    ),

    Trip(
        id="davide-iceland-solo",
        kind="post",
        author="Davide",
        city="Reykjavik",
        country="Iceland",
        title="Solo road trip, ring road, ten days",
        summary=(
            "Rented a tiny car and drove the whole loop. Slept in guesthouses, "
            "watched the lights from a hot spring, did not see another car for an hour at a time."
        ),
        image="https://picsum.photos/seed/davide-iceland/640/400",
        hero="https://picsum.photos/seed/davide-iceland/1600/700",
        gallery=_gallery("davide-iceland"),
        tags=["solo", "roadtrip", "nature"],
        visibility="public",
        posted_at="3 weeks ago",
        likes=211,
        comments=[
            Comment("Bob", "Did you do the eastfjords? Underrated.", "3 weeks ago"),
            Comment("Davide", "Yes, two days there. Stunning.", "3 weeks ago"),
        ],
    ),

    # ---- Alex's own posts (private notes, only Alex can see) ----

    Trip(
        id="alex-tokyo-plan",
        kind="post",
        author="Alex",
        city="Tokyo",
        country="Japan",
        title="Tokyo planning notes (do not share)",
        summary=(
            "Flights are cheapest in late October. Need to book the ryokan in Hakone early. "
            "Reminder to ask Bob for his Kyoto cafe list before I go."
        ),
        image="https://picsum.photos/seed/alex-tokyo/640/400",
        hero="https://picsum.photos/seed/alex-tokyo/1600/700",
        gallery=_gallery("alex-tokyo"),
        tags=["planning", "asia"],
        visibility="private",
        posted_at="yesterday",
        likes=0,
        comments=[],
    ),

    Trip(
        id="alex-lisbon-weekend",
        kind="post",
        author="Alex",
        city="Lisbon",
        country="Portugal",
        title="Lisbon birthday weekend (private journal)",
        summary=(
            "Mostly notes for myself. Best pastel was at Manteigaria, not Belem. "
            "Skip Tram 28 unless you start at the end of the line."
        ),
        image="https://picsum.photos/seed/alex-lisbon/640/400",
        hero="https://picsum.photos/seed/alex-lisbon/1600/700",
        gallery=_gallery("alex-lisbon"),
        tags=["weekend", "europe"],
        visibility="private",
        posted_at="1 month ago",
        likes=0,
        comments=[],
    ),
]


# tests commetn