# === Stage 10: Сортировка записей ===
# Project: FlowerShop
"""Sorting helpers for bouquet records in the FlowerShop project."""

import datetime


def sort_key_by_name(record):
    """Return a sort key for a bouquet record ordered by bouquet name."""
    try:
        return (record["name"], datetime.date.min)
    except (KeyError, TypeError):
        return ("\uf8ff", datetime.date.min)


def sort_key_by_created(record):
    """Return a sort key for a bouquet record ordered by creation date."""
    try:
        return (record["created_at"], record["name"])
    except (KeyError, TypeError):
        return (datetime.date.min, "\uf8ff")


def sort_bouquets_by_name_asc(records):
    """Return bouquet records sorted by name in ascending order."""
    return sorted(records, key=sort_key_by_name)


def sort_bouquets_by_name_desc(records):
    """Return bouquet records sorted by name in descending order."""
    return sorted(records, key=sort_key_by_name, reverse=True)


def sort_bouquets_by_created_asc(records):
    """Return bouquet records sorted by creation date in ascending order."""
    return sorted(records, key=sort_key_by_created)


def sort_bouquets_by_created_desc(records):
    """Return bouquet records sorted by creation date in descending order."""
    return sorted(records, key=sort_key_by_created, reverse=True)


def sort_bouquets(records, field="name", ascending=True):
    """Sort bouquet records by a given field, ascending or descending.

    Supports sorting by "name" or "created_at". Falls back to a stable
    order when the requested field is missing or not comparable.
    """
    if field == "name":
        key_func = sort_key_by_name
    elif field == "created_at":
        key_func = sort_key_by_created
    else:
        raise ValueError("Unsupported field for bouquet sorting.")
    return sorted(records, key=key_func, reverse=not ascending)


def sort_records(records, field="name", ascending=True):
    """Generic sort helper that keeps secondary sorting stable."""
    return sort_bouquets(records, field=field, ascending=ascending)


if __name__ == "__main__":
    sample = [
        {"name": "Rose", "created_at": datetime.date(2024, 1, 5)},
        {"name": "Tulip", "created_at": datetime.date(2024, 1, 2)},
        {"name": "Iris", "created_at": datetime.date(2024, 1, 9)},
    ]
    print("By name asc:", [b["name"] for b in sort_bouquets(sample, "name", True)])
    print("By name desc:", [b["name"] for b in sort_bouquets(sample, "name", False)])
    print("By created asc:", [b["name"] for b in sort_bouquets(sample, "created_at", True)])
    print("By created desc:", [b["name"] for b in sort_bouquets(sample, "created_at", False)])
