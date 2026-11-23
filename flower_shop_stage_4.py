# === Stage 4: Редактирование записей ===
# Project: FlowerShop
import datetime

ALLOWED_BOUQUET_FIELDS = ("name", "composition", "price", "assembled_at")


def edit_bouquet(bouquets: list[dict], bouquet_id: str,
                 updates: dict[str, object]) -> tuple[dict | None, str | None]:
    """Edit an existing bouquet by identifier.

    Only fields allowed for bouquets are changed. Returns the updated bouquet
    dict on success or None when the bouquet is missing, and an error message
    when an unknown or disallowed field is supplied.
    """
    if bouquet_id not in bouquets:
        return None, f"bouquet {bouquet_id!r} not found"

    unknown = set(updates) - ALLOWED_BOUQUET_FIELDS
    if unknown:
        return None, f"unknown field(s): {', '.join(sorted(unknown))}"

    for key, value in updates.items():
        bouquets[bouquet_id][key] = value

    bouquet = bouquets[bouquet_id]
    if bouquet["assembled_at"] is None and isinstance(value, datetime.datetime):
        bouquet["assembled_at"] = value.isoformat(sep=" ", timespec="seconds")

    return bouquets[bouquet_id], None
