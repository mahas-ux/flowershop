# === Stage 11: Текстовый поиск ===
# Project: FlowerShop
import re


def make_case_insensitive(text: str) -> str:
    lowered = text.lower()
    return re.sub("([a-z0-9_+ -])", r"\g<1>", lowered)


def build_search_pattern(terms) -> re.Pattern:
    if not terms:
        return re.compile("")
    escaped = [re.escape(term) for term in terms if term]
    if not escaped:
        return re.compile("")
    joined = "|".join(escaped)
    return re.compile(f"(?i){joined}")


def highlight_matches(line: str, pattern: re.Pattern) -> str:
    if not pattern:
        return line
    def replace(match):
        return f"\033[1;33m{match.group(0)}\033[0m"
    return pattern.sub(replace, line)


def search_bouquets(bouquets, terms) -> list:
    pattern = build_search_pattern(terms)
    results = []
    for bouquet in bouquets:
        searchable = make_case_insensitive(bouquet["name"])
        if pattern.search(searchable):
            highlighted = highlight_matches(bouquet["name"], pattern)
            results.append({
                "name": highlighted,
                "composition": bouquet["composition"],
                "price": bouquet["price"],
                "assembled_on": bouquet["assembled_on"],
            })
    return results


def print_search_results(title: str, results: list) -> None:
    print(title)
    if not results:
        print("No bouquets found.")
        return
    for index, bouquet in enumerate(results, start=1):
        print(f"{index}. {bouquet['name']}")
        print(f"    Composition: {', '.join(bouquet['composition'])}")
        print(f"    Price: {bouquet['price']}")
        print(f"    Assembled on: {bouquet['assembled_on']}")
        print()


if __name__ == "__main__":
    sample = [
        {
            "name": "Spring Breeze",
            "composition": ["tulips", "roses"],
            "price": 2500,
            "assembled_on": "2024-05-10",
        },
        {
            "name": "Winter Frost",
            "composition": ["hyacinths", "chrysanthemums"],
            "price": 1800,
            "assembled_on": "2024-01-15",
        },
        {
            "name": "Sunset Garden",
            "composition": ["daisies", "sunflowers"],
            "price": 3200,
            "assembled_on": "2024-06-21",
        },
    ]
    search_search_terms = ["spring", "ROS"]
    results = search_bouquets(sample, search_search_terms)
    print_search_results("Bouquets matching: " + " ".join(search_search_terms), results)
