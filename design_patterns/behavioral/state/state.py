from abc import ABC, abstractmethod
from typing import override


class State(ABC):
    @abstractmethod
    def write_name(self, name):
        pass


class LowerCaseState(State):
    def __init__(self, state_context):
        self.context = state_context

    @override
    def write_name(self, name):
        print(f'State 1 {name.lower()}')
        self.context.set_state(UpperCaseState(self.context))
        return name.lower()


class UpperCaseState(State):
    def __init__(self, state_context):
        self.context = state_context

    @override
    def write_name(self, name):
        print(f'State 2 {name.upper()}')
        self.context.set_state(LowerCaseState(self.context))
        return name.upper()


class StateContext:
    def __init__(self):
        self.state = LowerCaseState(self)

    def set_state(self, state):
        self.state = state

    def write_name(self, name):
        self.state.write_name(name)


if __name__ == "__main__":
    context = StateContext()  # initial state is LowerCaseState
    context.write_name('Gary')  # Output: State 1 gary
    context.write_name('Gary')  # Output: State 2 GARY
    context.write_name('Gary')  # Output: State 1 gary
    context.write_name('Gary')  # Output: State 2 GARY
