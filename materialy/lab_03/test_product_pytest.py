# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow."""
    return Product("Laptop", 1000.0, 10)


# --- Testy z fixture ---

def test_is_available(product):
    assert product.is_available() is True


def test_total_value(product):
    assert product.total_value() == 1000.0 * 10


# --- Testy z parametryzacja ---

@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 15),
    (0, 10),
    (100, 110),
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    product.add_stock(amount)
    assert product.quantity == expected_quantity


# --- Testy bledow ---

def test_remove_stock_too_much_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(999)


def test_add_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.add_stock(-5)

#zadanie dodatkowe
@pytest.mark.parametrize("percent, expected_price", [
    (0, 1000.0),
    (50, 500.0),
    (100, 0.0),
])
def test_apply_discount_valid(product, percent, expected_price):
    product.apply_discount(percent)
    assert product.price == expected_price


@pytest.mark.parametrize("percent", [
    -10,
    -1,
    101,
    150,
])
def test_apply_discount_invalid(product, percent):
    with pytest.raises(ValueError):
        product.apply_discount(percent)