# === Stage 7: Связи между сущностями ===
# Project: FlowerShop
"""FlowerShop - Stage 7: fetch all flowers for a given bouquet and verify link integrity."""

from datetime import datetime


def build_bouquet_index(bouquets):
    """Build a lookup of bouquet identifiers to their metadata."""
    index = {}
    for bouquet in bouquets:
        bouquet_id = bouquet["id"]
        index[bouquet_id] = {
            "name": bouquet["name"],
            "assembled_on": bouquet["assembled_on"],
        }
    return index


def get_flowers_for_bouquet(bouquets, flowers):
    """Return the flowers that make up a given bouquet.

    Args:
        bouquets: iterable of bouquet records with id, name, assembled_on.
        flowers: iterable of flower records with id, bouquet_id, name, price.

    Returns:
        A dict mapping bouquet_id to a list of flower records.
    """
    bouquet_ids = {b["id"] for b in bouquets}
    flowers_by_bouquet = {}
    for flower in flowers:
        bouquet_id = flower["bouquet_id"]
        flowers_by_bouquet.setdefault(bouquet_id, []).append(flower)
    return flowers_by_bouquet


def verify_integrity(bouquets, flowers):
    """Verify referential integrity between bouquets and flowers.

    Checks that every bouquet has at least one flower and that every
    flower references a known bouquet.

    Returns:
        A tuple (is_valid, messages) where messages is a list of strings.
    """
    messages = []
    bouquet_ids = {b["id"] for b in bouquets}
    flower_ids = {f["id"] for f in flowers}

    for bouquet in bouquets:
        if not bouquet_ids or bouquet["id"] not in bouquet_ids:
            messages.append(f"Bouquet {bouquet['id']} has no flowers.")

    for flower in flowers:
        if flower["bouquet_id"] not in bouquet_ids:
            messages.append(
                f"Flower {flower['id']} references unknown bouquet "
                f"{flower['bouquet_id']}."
            )

    is_valid = not messages
    return is_valid, messages


def get_bouquet_assembled_on(bouquets, bouquet_id):
    """Return the assembly date for a given bouquet, or None if not found."""
    for bouquet in bouquets:
        if bouquet["id"] == bouquet_id:
            return bouquet["assembled_on"]
    return None


if __name__ == "__main__":
    sample_bouquets = [
        {"id": "b1", "name": "Morning Glory", "assembled_on": datetime(2024, 5, 1)},
        {"id": "b2", "name": "Evening Rose", "assembled_on": datetime(2024, 5, 2)},
    ]
    sample_flowers = [
        {"id": "f1", "bouquet_id": "b1", "name": "Tulip", "price": 1.5},
        {"id": "f2", "bouquet_id": "b1", "name": "Sunflower", "price": 2.0},
        {"id": "f3", "bouquet_id": "b2", "name": "Rose", "price": 3.0},
    ]
    valid, messages = verify_integrity(sample_bouquets, sample_flowers)
    print("Valid:", valid)
    for message in messages:
        print(message)
