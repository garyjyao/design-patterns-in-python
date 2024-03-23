class CoffeeFlavour:
    _cache = {}

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @classmethod
    def intern(cls, name):
        if name not in cls._cache:
            cls._cache[name] = CoffeeFlavour(name)
        return cls._cache[name]

    @classmethod
    def flavours_in_cache(cls):
        return len(cls._cache)

    @classmethod
    def clear_cache(cls):
        cls._cache.clear()


class Order:
    def __init__(self, flavour, table_number):
        self.flavour = flavour
        self.table_number = table_number

    def __call__(self):
        print(f"Serving {self.flavour} to table {self.table_number}")

    @staticmethod
    def of(flavour_name, table_number):
        flavour = CoffeeFlavour.intern(flavour_name)
        return Order(flavour, table_number)


class CoffeeShop:
    def __init__(self):
        self.orders = []

    def take_order(self, flavour_name, table_number):
        self.orders.append(Order.of(flavour_name, table_number))

    def service(self):
        for order in self.orders:
            order()


if __name__ == "__main__":
    shop = CoffeeShop()
    shop.take_order("Cappuccino", 2)
    shop.take_order("Frappe", 1)
    shop.take_order("Espresso", 1)
    shop.take_order("Frappe", 3)
    shop.take_order("Espresso", 3)
    shop.take_order("Cappuccino", 3)

    shop.service()
    print(f"CoffeeFlavour objects in cache: {CoffeeFlavour.flavours_in_cache()}")
    # FlyWeight is to reduce memory usage by sharing objects with similar state
