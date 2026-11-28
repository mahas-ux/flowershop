# === Stage 12: Поиск по нескольким словам ===
# Project: FlowerShop
from datetime import date


def parse_query(query):
    """Parse the search query into a list of words and negations."""
    words = []
    for token in query.split():
        if token.startswith("-"):
            words.append(("exclude", token[1:]))
        else:
            words.append(("include", token))
    return words


def build_match(query):
    """Build a predicate that matches bouquets against the query."""
    parsed = parse_query(query)
    if not parsed:
        return lambda bouquet: True
    words = [word for _, word in parsed]
    excludes = [word for _, word in parsed if "_" in ("exclude", word)]
    excludes = [word for _, word in parsed if word.startswith("-")]
    includes = [word for _, word in parsed if not word.startswith("-")]

    def match(bouquet):
        name = bouquet["name"].lower()
        composition = " ".join(bouquet["composition"]).lower()
        haystack = name + " " + composition
        for word in includes:
            if word.lower() not in haystack:
                return False
        for word in excludes:
            if word.lower() in haystack:
                return False
        return True

    return match


def search_bouquets(query, bouquets):
    """Search bouquets by multiple words with negation support."""
    predicate = build_match(query)
    return [bouquet for bouquet in bouquets if predicate(bouquet)]


if __name__ == "__main__":
    demo = [
        {"name": "Spring", "composition": ["rose", "tulip"], "price": 100, "assembled": date(2024, 1, 1)},
        {"name": "Summer", "composition": ["sunflower"], "price": 80, "assembled": date(2024, 6, 1)},
        {"name": "Autumn", "composition": ["rose", "chrysanthemum"], "price": 120, "assembled": date(2024, 9, 1)},
    ]

    print(search_bouquets("rose", demo))
    print(search_bouquets("rose -summer", demo))
    print(search_bouquets("spring summer", demo))
