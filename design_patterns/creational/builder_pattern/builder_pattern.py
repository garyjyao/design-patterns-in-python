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
    car = CarBuilder().engine('Petrol').body('Sedan').wheel('Steel').build()
    print(f'Car: {car.engine}, {car.body}, {car.wheel}')
