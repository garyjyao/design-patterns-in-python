import pytest
from design_patterns.behavioral.strategy_pattern.strategy_pattern import NormalBillingStrategy, HappyHourBillingStrategy, Customer


class TestCustomer:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.normal_strategy = NormalBillingStrategy()
        self.happy_hour_strategy = HappyHourBillingStrategy()
        self.customer = Customer()

    def test_add_drink_normal_strategy(self):
        self.customer.set_billing_strategy(self.normal_strategy)
        self.customer.add_drink(20.0, 1)
        assert self.customer.drinks[-1] == 20.0

    def test_add_drink_happy_hour_strategy(self):
        self.customer.set_billing_strategy(self.happy_hour_strategy)
        self.customer.add_drink(20.0, 1)
        assert self.customer.drinks[-1] == 10.0

    def test_set_billing_strategy(self):
        self.customer.set_billing_strategy(self.happy_hour_strategy)
        assert self.customer.billing_strategy == self.happy_hour_strategy

    def test_print_bill(self):
        self.customer.set_billing_strategy(self.normal_strategy)
        self.customer.add_drink(20.0, 1)
        self.customer.set_billing_strategy(self.happy_hour_strategy)
        self.customer.add_drink(20.0, 1)
        assert self.customer.print_bill() == 30.0
