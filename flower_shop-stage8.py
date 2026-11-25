# === Stage 8: Генерация идентификаторов ===
# Project: FlowerShop
PREFIX = "fsh"


def generate_id(entity_type):
    """Generate a unique identifier with a project prefix and collision check."""
    suffix = 0
    while True:
        candidate = f"{PREFIX}_{entity_type}_{suffix:05d}"
        if candidate not in _registry:
            _registry[candidate] = entity_type
            return candidate
        suffix += 1


_registry = {}


def is_reserved(entity_type, candidate):
    """Check whether a candidate identifier already exists for an entity type."""
    return candidate in _registry and _registry[candidate] == entity_type


def reserve_id(entity_type):
    """Reserve a new unique identifier and return it."""
    return generate_id(entity_type)


def release_id(candidate):
    """Release a previously reserved identifier so it can be reused."""
    _registry.pop(candidate, None)


def get_type(candidate):
    """Return the entity type associated with a reserved identifier."""
    return _registry.get(candidate)
