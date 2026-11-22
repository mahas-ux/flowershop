# === Stage 3: Хранилище в памяти ===
# Project: FlowerShop
"""FlowerShop: in-memory store for bouquets.

This module provides a small, self-contained in-memory repository for
bouquet entities. It supports adding a bouquet, retrieving one by its
identifier, and listing all stored bouquets.
"""


class Bouquet:
    """A bouquet entity with a name, composition, price, and assembly date."""

    def __init__(self, bouquet_id, name, composition, price, assembled_on):
        self.id = bouquet_id
        self.name = name
        self.composition = composition
        self.price = price
        self.assembled_on = assembled_on

    def __repr__(self):
        return (
            f"Bouquet(id={self.id!r}, name={self.name!r}, "
            f"composition={self.composition!r}, price={self.price}, "
            f"assembled_on={self.assembled_on!r})"
        )


class BouquetStore:
    """A simple in-memory store for bouquet entities."""

    def __init__(self):
        self._bouquets = {}

    def add(self, bouquet):
        """Add a bouquet to the store, replacing any existing entry."""
        if bouquet.id is None:
            raise ValueError("A bouquet must have an identifier.")
        self._bouquets[bouquet.id] = bouquet
        return bouquet

    def get(self, bouquet_id):
        """Return the bouquet with the given identifier or None."""
        return self._bouquets.get(bouquet_id)

    def list_bouquets(self):
        """Return all stored bouquets as a list."""
        return list(self._bouquets.values())


def main():
    store = BouquetStore()
    store.add(Bouquet("b1", "Spring", ["rose", "tulip"], 500, "2024-05-01"))
    store.add(Bouquet("b2", "Summer", ["sunflower", "lily"], 750, "2024-06-15"))
    print(store.get("b1"))
    print(store.list_bouquets())


if __name__ == "__main__":
    main()
