from design_patterns.creational.builder.builder import CarBuilder


def test_build():
    # Assign
    subject = CarBuilder()

    # Act
    car = subject.engine('Petrol').body('Sedan').wheel('Steel').build()

    # Assert
    assert car.engine == 'Petrol'
    assert car.body == 'Sedan'
    assert car.wheel == 'Steel'

