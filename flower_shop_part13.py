# === Stage 13: Теги ===
# Project: FlowerShop
import random


class BunchTagError(Exception):
    """Raised when a tag operation fails."""


class Bunch:
    def __init__(self, name, composition, price, assembled_on):
        self.name = name
        self.composition = composition
        self.price = price
        self.assembled_on = assembled_on
        self.tags = []

    def add_tag(self, tag):
        if not isinstance(tag, str) or not tag.strip():
            raise BunchTagError("Tag must be a non-empty string")
        if tag in self.tags:
            raise BunchTagError(f"Tag '{tag}' already exists on bunch '{self.name}'")
        self.tags.append(tag)

    def remove_tag(self, tag):
        if tag not in self.tags:
            raise BunchTagError(f"Tag '{tag}' not found on bunch '{self.name}'")
        self.tags.remove(tag)

    def find_tag(self, tag):
        return tag in self.tags


def find_bunch_by_tag(bunches, tag):
    for bunch in bunches:
        if bunch.find_tag(tag):
            return bunch
    return None


def random_tags(count=1):
    pool = ["fresh", "romantic", "summer", "winter", "gift", "eco", "premium"]
    return [random.choice(pool) for _ in range(count)]


def tag_report(bunch):
    return {"name": bunch.name, "tags": list(bunch.tags)}
