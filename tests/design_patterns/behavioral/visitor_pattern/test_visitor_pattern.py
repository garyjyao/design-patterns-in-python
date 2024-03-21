import pytest
from design_patterns.behavioral.visitor_pattern.visitor_pattern import Car, Wheel, Engine, Body, CarElementDoVisitor


class TestVisitorPattern:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.car = Car()
        self.wheel = Wheel()
        self.engine = Engine()
        self.body = Body()
        self.visitor = CarElementDoVisitor()

    def test_car_accept(self):
        # Assign

        # Act
        result = self.car.accept(self.visitor)

        # Assert
        assert result == ["Body", "Engine", "Wheel", "Car"]
