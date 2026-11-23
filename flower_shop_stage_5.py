# === Stage 5: Удаление и восстановление ===
# Project: FlowerShop
import datetime

BASKET_SOFT_DELETE_FLAG = "_soft_deleted"
BASKET_RESTORE_FLAG = "_restored"


def make_basket(bunch_name, composition, price, assembly_date=None):
    if assembly_date is None:
        assembly_date = datetime.date.today()
    return {
        "name": bunch_name,
        "composition": composition,
        "price": price,
        "assembled_at": assembly_date,
        BASKET_SOFT_DELETE_FLAG: False,
        BASKET_RESTORE_FLAG: False,
    }


def delete_basket(basket):
    if basket is None:
        return
    basket[BASKET_SOFT_DELETE_FLAG] = True
    basket[BASKET_RESTORE_FLAG] = False


def restore_basket(basket):
    if basket is None:
        return
    basket[BASKET_SOFT_DELETE_FLAG] = False
    basket[BASKET_RESTORE_FLAG] = True


def is_deleted(basket):
    if basket is None:
        return True
    return basket.get(BASKET_SOFT_DELETE_FLAG, False)


def is_restored(basket):
    if basket is None:
        return False
    return basket.get(BASKET_RESTORE_FLAG, False)


def remove_basket(basket):
    if basket is None:
        return
    basket.pop(BASKET_SOFT_DELETE_FLAG, None)
    basket.pop(BASKET_RESTORE_FLAG, None)


def list_active_baskets(baskets):
    return [b for b in baskets if not is_deleted(b)]


def list_available_baskets(baskets):
    return [b for b in list_active_baskets(baskets) if not is_restored(b)]


def soft_delete_and_restore_cycle(basket):
    delete_basket(basket)
    assert is_deleted(basket)
    restore_basket(basket)
    assert is_restored(basket)
    remove_basket(basket)
    assert not is_deleted(basket)
    assert not is_restored(basket)
