from src.fast_pow import fastPow


def test_unit_tests(): # unit тесты
    assert fastPow(2, 2) == 4
    assert fastPow(1, 10) == 1
    assert fastPow(3, 4) == 81
    assert fastPow(5, 3) == 125


def test_extreme_cases(): # Крайние случаи
    assert fastPow(-1, 4) == 1
    assert fastPow(0, 10) == 0
    assert fastPow(67, 0) == 1
    assert fastPow(-2, 3) == -8

def test_property_based_tests(): # Property based тесты
    assert fastPow(7, 4) == 7 ** 4
    assert fastPow(23, 0) == 23 ** 0
