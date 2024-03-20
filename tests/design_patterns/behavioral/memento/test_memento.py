from design_patterns.behavioral.memento.memento import *


def test_memento():
    # Assign
    originator = Originator()
    care_taker = CareTaker()

    # Act
    originator.set_state("s1")
    originator.set_state("s2")
    care_taker.add(originator.save_to_memento())
    originator.set_state("s3")
    originator.set_state("s4")
    originator.restore_from_memento(care_taker.get(0))

    # Assert
    assert originator._state == "s2"


class TestMemento:
    def test_init_and_get_state(self):
        # Assign

        # Act
        memento = Memento("state")

        # Assert
        assert memento.get_state() == "state"


class TestOriginator:
    def test_init(self):
        # Assign

        # Act
        originator = Originator()

        # Assert
        assert originator._state == None

    def test_save_to_memento(self):
        # Assign
        originator = Originator()
        originator.set_state("s1")

        # Act
        memento = originator.save_to_memento()

        # Assert
        assert memento.get_state() == "s1"

    def test_restore_from_memento(self):
        # Assign
        originator = Originator()
        memento = Memento("s1")

        # Act
        originator.restore_from_memento(memento)

        # Assert
        assert originator._state == "s1"

    def test_set_state(self):
        # Assign
        originator = Originator()

        # Act
        originator.set_state("s1")

        # Assert
        assert originator._state == "s1"


class TestCareTaker:
    def test_init(self):
        # Assign

        # Act
        care_taker = CareTaker()

        # Assert
        assert care_taker._memento_list == []

    def test_add(self):
        # Assign
        care_taker = CareTaker()
        memento = Memento("s1")

        # Act
        care_taker.add(memento)

        # Assert
        assert care_taker._memento_list == [memento]

    def test_get(self):
        # Assign
        care_taker = CareTaker()
        memento = Memento("s1")
        care_taker.add(memento)

        # Act
        result = care_taker.get(0)

        # Assert
        assert result == memento