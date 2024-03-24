from unittest.mock import patch

import pytest

from design_patterns.behavioral.mediator_pattern.mediator_pattern import TaxiCompany, Taxi, Location


class TestTaxi:
    def test_init(self, mocker):
        # Assign
        mocked_taxi_company = mocker.Mock()

        # Act
        taxi = Taxi("123-ABC", mocked_taxi_company)

        # Assert
        assert taxi.plate == "123-ABC"
        assert taxi.taxi_company == mocked_taxi_company

    def test_call(self, mocker):
        # Assign
        mocked_taxi_company = mocker.Mock()

        taxi = Taxi("123-ABC", mocked_taxi_company)
        location = Location("Downtown")
        passenger = "John Doe"

        # Call the call method and check if notify_event is called
        taxi.call(location, passenger)
        mocked_taxi_company.notify_event.assert_called_once_with("call acknowledged", taxi)


class TestTaxiCompany:
    def test_init_register_and_str(self):
        # Assign
        company = TaxiCompany()
        taxi1 = Taxi("111-111", company)
        taxi2 = Taxi("222-222", company)

        # Act
        company.register(taxi1)
        company.register(taxi2)

        # Assert
        assert str(company) == "111-111,222-222"

    def test_find_nearest_exists(self):
        # Assign
        company = TaxiCompany()
        taxi1 = Taxi("111-111", company)
        taxi2 = Taxi("222-222", company)
        company.register(taxi1)
        company.register(taxi2)

        location = Location("Downtown")
        passenger = "John Doe"

        # Act
        nearest_taxi = company.find_nearest(location, passenger)

        # Assert
        assert nearest_taxi == taxi1

    def test_find_nearest_none(self):
        # Assign
        company = TaxiCompany()

        location = Location("Downtown")
        passenger = "John Doe"

        # Act
        nearest_taxi = company.find_nearest(location, passenger)

        # Assert
        assert nearest_taxi is None

    @patch.object(TaxiCompany, 'find_nearest')
    def test_call(self, mocked_taxi_company_find_nearest, mocker):
        # Assign
        company = TaxiCompany()
        taxi1 = Taxi("111-111", company)
        company.register(taxi1)
        taxi1_call_spy = mocker.spy(taxi1, 'call')

        mocked_taxi_company_find_nearest.return_value = taxi1

        location = Location("Downtown")
        passenger = "John Doe"

        # Act
        company.call(location, passenger)

        # Assert
        taxi1_call_spy.assert_called_once_with(location, passenger)


@pytest.mark.integration_test
def test_taxi_company():
    # Assign
    company = TaxiCompany()
    taxi1 = Taxi('111-111', company)
    taxi2 = Taxi('222-222', company)

    # Act
    company.register(taxi1)
    company.register(taxi2)

    # Assert
    assert company.taxi_list == [taxi1, taxi2]
    # print(company)  # show list of taxis in the company, 111-111, 222-222

    # Act
    company.call(Location("Oldtown"), 'some-passenger')
    # print(company)  # 222-222

    # Assert
    assert company.taxi_list == [taxi2]

    # Act
    company.call(Location("Newtown"), 'another-passenger')
    print(company)  # []

    # Assert
    assert company.taxi_list == []

    # Act
    company.call(Location("Newtown"), 'badluck-passenger')

    # Assert
    # Nothing happens when we run out of taxi in taxi_list


