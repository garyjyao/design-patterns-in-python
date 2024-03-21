from unittest.mock import Mock, patch

from design_patterns.behavioral.state.state import StateContext, LowerCaseState, UpperCaseState, State


class TestLowerCaseState:
    def test_write_name(self):
        # Assign
        state_context = StateContext()
        lower_case_state = LowerCaseState(state_context)

        # Act
        name = lower_case_state.write_name("Hello")

        # Assert
        assert name == "hello"
        assert isinstance(state_context.state, UpperCaseState)


class TestUpperCaseState:
    def test_write_name(self):
        # Assign
        state_context = StateContext()
        upper_case_state = UpperCaseState(state_context)

        # Act
        name = upper_case_state.write_name("Hello")

        # Assert
        assert name == "HELLO"
        assert isinstance(state_context.state, LowerCaseState)


class TestStateContext:
    def test_init(self):
        # Assign

        # Act
        state_context = StateContext()

        # Assert
        assert isinstance(state_context.state, LowerCaseState)

    def test_set_state(self):
        # Assign
        state_context = StateContext()
        mocked_state = Mock()

        # Act
        state_context.set_state(mocked_state)

        # Assert
        assert state_context.state == mocked_state

    @patch.object(LowerCaseState, "write_name")
    def test_write_name(self, mocked_lower_case_state_write_name):
        # Assign
        state_context = StateContext()

        # Act
        state_context.write_name("Hello")

        # Assert
        mocked_lower_case_state_write_name.assert_called_once_with("Hello")

    @patch.object(UpperCaseState, "write_name")
    def test_write_name(self, mocked_upper_case_state_write_name):
        # Assign
        state_context = StateContext()
        state_context.set_state(UpperCaseState(state_context))

        # Act
        state_context.write_name("Hello")

        # Assert
        mocked_upper_case_state_write_name.assert_called_once_with("Hello")
