class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    def __init__(self):
        self._state = None

    def save_to_memento(self):
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()
        print(f"State = {self._state}")

    def set_state(self, state):
        self._state = state
        print(f"State = {self._state}")


class CareTaker:
    def __init__(self):
        self._memento_list = []

    def add(self, memento):
        self._memento_list.append(memento)

    def get(self, index):
        return self._memento_list[index]


if __name__ == "__main__":
    originator = Originator()
    care_taker = CareTaker()
    originator.set_state("s1")
    originator.set_state("s2")
    care_taker.add(originator.save_to_memento())
    originator.set_state("s3")
    originator.set_state("s4")
    originator.restore_from_memento(care_taker.get(0))
