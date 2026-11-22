# === Stage 1: Каркас модуля ===
# Project: FlowerShop
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List


@dataclass
class Bouquet:
    name: str
    composition: List[str]
    price: float
    assembled_on: date


def make_demo_bouquets() -> List[Bouquet]:
    today = date.today()
    rose = Bouquet("Rose Bouquet", ["red rose", "green leaf"], 1200.0, today)
    tulip = Bouquet("Tulip Mix", ["yellow tulip", "pink tulip"], 850.0, today - timedelta(days=2))
    mixed = Bouquet("Spring Mix", ["daisy", "tulip", "rose"], 1500.0, today - timedelta(days=5))
    return [rose, tulip, mixed]


def main() -> None:
    bouquets = make_demo_bouquets()
    print("FlowerShop demo bouquets:")
    for bouquet in bouquets:
        print(f"  {bouquet.name} -> {', '.join(bouquet.composition)} -> {bouquet.price} rub -> {bouquet.assembled_on}")


if __name__ == "__main__":
    main()
