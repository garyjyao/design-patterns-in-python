from unittest.mock import MagicMock

from design_patterns.structural.flyweight_pattern.flyweight_pattern import CoffeeShop, CoffeeFlavour


def setup_function():
    CoffeeFlavour.clear_cache()


def test_coffee_shop():
    shop = CoffeeShop()
    shop.take_order("Cappuccino", 2)
    shop.take_order("Frappe", 1)
    assert len(shop.orders) == 2
    assert shop.orders[0].flavour.name == "Cappuccino"
    assert shop.orders[0].table_number == 2
    assert shop.orders[1].flavour.name == "Frappe"
    assert shop.orders[1].table_number == 1


def test_coffee_flavour_cache():
    CoffeeFlavour.intern("Cappuccino")
    CoffeeFlavour.intern("Cappuccino")
    assert CoffeeFlavour.flavours_in_cache() == 1


def test_service():
    shop = CoffeeShop()
    shop.take_order("Cappuccino", 2)
    shop.take_order("Frappe", 1)
    shop.orders[0] = MagicMock()
    shop.orders[1] = MagicMock()
    shop.service()
    shop.orders[0].assert_called_once()
    shop.orders[1].assert_called_once()