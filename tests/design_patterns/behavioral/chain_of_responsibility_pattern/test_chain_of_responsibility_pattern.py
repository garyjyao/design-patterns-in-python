from design_patterns.behavioral.chain_of_responsibility_pattern.chain_of_responsibility_pattern import SomeOtherProcessor, \
    DefaultProcessor, Request


def test_chain_of_responsibility(mocker):
    # Assign
    some_other_processor = SomeOtherProcessor()
    some_other_processor_spy = mocker.spy(some_other_processor, 'process')
    default_processor = DefaultProcessor(some_other_processor)
    request = Request()

    # Act
    default_processor.process(request)

    # Assert
    some_other_processor_spy.assert_called_once_with(request)
