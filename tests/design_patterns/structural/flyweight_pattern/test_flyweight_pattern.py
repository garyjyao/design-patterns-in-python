from unittest.mock import MagicMock

from design_patterns.structural.flyweight_pattern.flyweight_pattern import CoffeeShop, CoffeeFlavour


def setup_function():
    """
    Setup function
    Because the CoffeeFlavour class has a class variable _cache, we need to clear the cache before each test
    """
    CoffeeFlavour.clear_cache()


def test_coffee_shop():
    # Assign
    shop = CoffeeShop()

    # Act
    shop.take_order("Cappuccino", 2)
    shop.take_order("Frappe", 1)

    # Assert
    assert len(shop.orders) == 2
    assert shop.orders[0].flavour.name == "Cappuccino"
    assert shop.orders[0].table_number == 2
    assert shop.orders[1].flavour.name == "Frappe"
    assert shop.orders[1].table_number == 1


def test_coffee_flavour_cache():
    # Assign

    # Act
    CoffeeFlavour.intern("Cappuccino")
    CoffeeFlavour.intern("Cappuccino")

    # Assert
    """
    flyweight pattern ensures that there is only one instance of the object in the cache
    """
    assert CoffeeFlavour.flavours_in_cache() == 1


def test_service():
    # Assign
    shop = CoffeeShop()

    # Act
    shop.take_order("Cappuccino", 2)
    shop.take_order("Frappe", 1)

    # Assign Mock
    shop.orders[0] = MagicMock()
    shop.orders[1] = MagicMock()

    # Act
    shop.service()

    # Assert
    """
    The order object is called as a function
    """
    shop.orders[0].assert_called_once()
    shop.orders[1].assert_called_once()