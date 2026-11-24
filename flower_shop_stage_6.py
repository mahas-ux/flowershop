# === Stage 6: Связанная сущность ===
# Project: FlowerShop
"""flower.py — Flower entity for FlowerShop.

A Flower is a single stem with a name, species, quantity, purchase date,
and a link to a bouquet (by bouquet id). This module is self-contained
and depends only on the standard library.
"""

from datetime import date


class Flower:
    """A single flower stem available for sale or bouquet building."""

    def __init__(self, name, species, quantity, purchase_date, bouquet_id):
        self.name = name
        self.species = species
        self.quantity = quantity
        self.purchase_date = purchase_date
        self.bouquet_id = bouquet_id

    def __repr__(self):
        return (
            f"Flower(name={self.name!r}, species={self.species!r}, "
            f"quantity={self.quantity}, purchase_date={self.purchase_date}, "
            f"bouquet_id={self.bouquet_id!r})"
        )


def add_flower(flowers, flower):
    """Append a new flower to the collection and return its index.

    Parameters
    ----------
    flowers : list[Flower]
        The current collection of flowers.
    flower : Flower
        The flower to add.

    Returns
    -------
    int
        The index of the newly added flower in ``flowers``.
    """
    flowers.append(flower)
    return len(flowers) - 1


def flowers_by_species(flowers, species):
    """Return all flowers whose species matches ``species``."""
    return [f for f in flowers if f.species == species]


def total_quantity_by_species(flowers, species):
    """Return the total quantity of ``species`` across all flowers."""
    return sum(f.quantity for f in flowers if f.species == species)
