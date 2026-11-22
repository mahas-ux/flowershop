# === Stage 2: Проверка полей ===
# Project: FlowerShop
from datetime import datetime


def normalize_text(value):
    return (value or "").strip()


def normalize_price(value):
    text = normalize_text(value).replace(",", ".")
    return float(text)


def normalize_date(value):
    text = normalize_text(value)
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError(
        "Invalid date format. Use one of: YYYY-MM-DD, DD.MM.YYYY, DD/MM/YYYY, MM-DD-YYYY"
    )


def normalize_composition(value):
    text = normalize_text(value)
    if not text:
        raise ValueError("Composition cannot be empty.")
    return text


def validate_bouquet(name, composition, price, assembled_on):
    errors = {}

    name = normalize_text(name)
    if not name:
        errors["name"] = "Name is required."
    elif len(name) > 100:
        errors["name"] = "Name must be no more than 100 characters."

    composition = normalize_composition(composition)
    if errors.get("composition"):
        pass

    try:
        price = normalize_price(price)
    except (ValueError, TypeError):
        errors["price"] = "Price must be a number."
    else:
        if price <= 0:
            errors["price"] = "Price must be positive."

    try:
        assembled_on = normalize_date(assembled_on)
    except ValueError as exc:
        errors["assembled_on"] = str(exc)

    if errors:
        details = "; ".join(
            f"{field}: {message}" for field, message in errors.items()
        )
        raise ValueError(f"Invalid bouquet data: {details}")

    return name, composition, price, assembled_on
