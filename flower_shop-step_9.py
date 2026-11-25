# === Stage 9: Фильтрация записей ===
# Project: FlowerShop
from datetime import date


def filter_bouquets_by_flowers(bouquets, flowers):
    """Return bouquets whose composition contains every flower in flowers."""
    flowers = set(flowers)
    return [bouquet for bouquet in bouquets if flowers.issubset(bouquet["composition"])]


def filter_bouquets_by_date_range(bouquets, start_date, end_date):
    """Return bouquets assembled within the inclusive [start_date, end_date] range."""
    return [bouquet for bouquet in bouquets if start_date <= bouquet["assembled_on"] <= end_date]


def filter_bouquets(bouquets, flowers=None, start_date=None, end_date=None):
    """Filter bouquets by composition and/or assembly-date range."""
    result = bouquets
    if flowers is not None:
        result = filter_bouquets_by_flowers(result, flowers)
    if start_date is not None or end_date is not None:
        result = filter_bouquets_by_date_range(
            result,
            start_date if start_date is not None else date.min,
            end_date if end_date is not None else date.max,
        )
    return result


if __name__ == "__main__":
    sample = [
        {"name": "Spring", "composition": ["rose", "tulip"], "price": 1200, "assembled_on": date(2025, 1, 10)},
        {"name": "Garden", "composition": ["tulip", "daisy"], "price": 900, "assembled_on": date(2025, 1, 12)},
        {"name": "Summer", "composition": ["sunflower"], "price": 1500, "assembled_on": date(2025, 1, 20)},
    ]
    print([b["name"] for b in filter_bouquets(sample, flowers={"tulip"})])
    print([b["name"] for b in filter_bouquets(sample, start_date=date(2025, 1, 11), end_date=date(2025, 1, 15))])
    print([b["name"] for b in filter_bouquets(sample, flowers={"rose"}, start_date=date(2025, 1, 1), end_date=date(2025, 1, 31))])
