from design_patterns.behavioral.intercepting_filter.filter import *


def test_intercepting_filter(mocker):
    # Assign
    filter1 = DebugFilter()
    filter2 = AuthenticationFilter()
    target = Target()
    filter1_filter_spy = mocker.spy(filter1, 'filter')
    filter2_filter_spy = mocker.spy(filter2, 'filter')
    target_execute_spy = mocker.spy(target, 'execute')
    filter_chain = FilterChain(target, filter1, filter2)
    request = SomeRequest()

    # Act
    filter_chain.execute(request)

    # Assert
    filter1_filter_spy.assert_called_once_with(request)
    filter2_filter_spy.assert_called_once_with(request)
    target_execute_spy.assert_called_once_with(request)