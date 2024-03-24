class Taxi:
    def __init__(self, plate, taxi_company):
        self.plate = plate
        self.taxi_company = taxi_company

    def call(self, location, passenger):
        print(f"Taxi {self.plate}: called by {passenger} from {location}")
        # logic to acknowledge th call if it agrees
        self.taxi_company.notify_event("call acknowledged", self)


class TaxiCompany:
    def __init__(self):
        self.taxi_list = []

    def register(self, taxi):
        self.taxi_list.append(taxi)

    def __str__(self):
        return ','.join(taxi.plate for taxi in self.taxi_list)

    def find_nearest(self, location, passenger):
        print(f'finding nearest taxi for {passenger} from {location}')
        # not really finding the nearest but just find first one
        if self.taxi_list:
            taxi = self.taxi_list[0]
            return taxi
        return None

    def call(self, location, passenger):
        taxi: Taxi = self.find_nearest(location, passenger)
        if taxi:
            taxi.call(location, passenger)

    def notify_event(self, event, taxi):
        print(f"Taxi {taxi.plate}: {event}")
        for t in self.taxi_list:
            if t == taxi:
                self.taxi_list.remove(taxi)
                break


class Location:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


if __name__ == "__main__":
    company = TaxiCompany()
    company.register(Taxi('111-111', company))
    company.register(Taxi('222-222', company))
    # print(company)  # show list of taxis in the company, 111-111, 222-222
    company.call(Location("Newtown"), 'some-passenger')
    # print(company)  # 222-222
