import uuid
from abc import ABC, abstractmethod


class BillingStrategy(ABC):
    @abstractmethod
    def actual_amount(self, amount, quantity):
        raise NotImplementedError


class NormalBillingStrategy(BillingStrategy):
    def actual_amount(self, amount, quantity):
        return amount * quantity


class HappyHourBillingStrategy(BillingStrategy):
    def actual_amount(self, amount, quantity):
        return amount * quantity * 0.50


class Customer:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.drinks = []
        self.billing_strategy = NormalBillingStrategy()

    def set_billing_strategy(self, billing_strategy):
        self.billing_strategy = billing_strategy

    def add_drink(self, amount, quantity):
        self.drinks.append(self.billing_strategy.actual_amount(amount, quantity))

    def print_bill(self):
        print(f"Customer {self.id} bill is {sum(self.drinks)}")
        return sum(self.drinks)


if __name__ == "__main__":
    normal = NormalBillingStrategy()
    happy_hour = HappyHourBillingStrategy()
    customer1 = Customer()
    customer1.add_drink(20.0, 1)
    customer1.print_bill()
    customer1.set_billing_strategy(happy_hour)
    customer1.add_drink(20, 1)
    customer1.print_bill()
