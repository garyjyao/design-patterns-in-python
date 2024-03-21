from abc import ABC, abstractmethod
from typing import override


class SomeRequest:
    pass


class SomeResponse:
    def __init__(self, request):
        self._request = request


class Filter(ABC):
    @abstractmethod
    def filter(self, request):
        raise NotImplementedError


class DebugFilter(Filter):
    @override
    def filter(self, request):
        # print request and response
        print('Debug Filter')


class AuthenticationFilter(Filter):
    @override
    def filter(self, request):
        # authorize the request
        print('Authentication Filter')


class Target:
    def execute(self, request):
        print('Target Execute')
        return SomeResponse(request)


class FilterChain:
    def __init__(self, target, *filters):
        self._filters = list(filters)
        self.target = target

    def execute(self, request):
        for _filter in self._filters:
            _filter.filter(request)
        self.target.execute(request)


if __name__ == "__main__":
    FilterChain(Target(), DebugFilter(), AuthenticationFilter()).execute(SomeRequest())
