from helpers.discount import apply_discount


def test_apply_discount():
    assert apply_discount(80, 10) == 70
