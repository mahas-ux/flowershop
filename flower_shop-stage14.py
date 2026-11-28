# === Stage 14: Группировка ===
# Project: FlowerShop
from collections import Counter


def group_bouquets_by_composition(bouquets):
    """Group bouquets by their composition and count each group.

    Args:
        bouquets: iterable of dict-like bouquet objects, each exposing
                  a ``composition`` attribute (list of flower names).

    Returns:
        dict mapping a normalized composition tuple to the number of
        bouquets sharing that composition.
    """
    groups = Counter()
    for bouquet in bouquets:
        composition = tuple(sorted(bouquet.composition))
        groups[composition] += 1
    return dict(groups)


def summarize_composition_counts(bouquets):
    """Return a human-readable summary of composition grouping.

    Args:
        bouquets: iterable of bouquet objects as described above.

    Returns:
        str with each composition and its count, one per line.
    """
    groups = group_bouquets_by_composition(bouquets)
    lines = []
    for composition, count in groups.most_common():
        flowers = ", ".join(composition)
        lines.append(f"{count} bouquet(s) with composition: {flowers}")
    return "\n".join(lines)


def find_most_common_composition(bouquets):
    """Find the composition shared by the most bouquets.

    Args:
        bouquets: iterable of bouquet objects as described above.

    Returns:
        tuple of the composition (sorted list of flower names) that appears
        most often, or None when there are no bouquets.
    """
    groups = group_bouquets_by_composition(bouquets)
    if not groups:
        return None
    composition, _ = groups.most_common(1)[0]
    return list(composition)
