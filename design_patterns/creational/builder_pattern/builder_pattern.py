class Engine:
    pass


class Body:
    pass


class Wheel:
    pass


class Car:
    def __init__(self, engine, body, wheel):
        self.engine = engine
        self.body = body
        self.wheel = wheel


class CarBuilder:
    def __init__(self):
        self._engine = None
        self._body = None
        self._wheel = None

    def engine(self, engine):
        self._engine = engine
        return self

    def body(self, body):
        self._body = body
        return self

    def wheel(self, wheel):
        self._wheel = wheel
        return self

    def build(self):
        return Car(self._engine, self._body, self._wheel)


if __name__ == "__main__":
    # """
    # The CarBuilder class is used to construct a Car object.
    # The CarBuilder class has methods to set the engine, body, and wheel of the car.
    # This can be further simplified by using a Director class to manage the construction of the Car object.
    # such as, car = CarBuilderDirector.construct()
    # """
    car = CarBuilder().engine('Petrol').body('Sedan').wheel('Steel').build()
    print(f'Car: {car.engine}, {car.body}, {car.wheel}')
