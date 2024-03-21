class SearchRequest:
    pass


class SearchResponse:
    def __init__(self, request):
        self._request = request

    def get_request(self):
        return self._request


class HttpClient:
    def post(self, request):
        return SearchResponse(request)


class SearchCommand:
    def __init__(self, search_request, http_client):
        self._http_client = http_client
        self._search_request = search_request

    def execute(self):
        return self._http_client.post(self._search_request)


# If you want to complete Object-Oriented like Java
# class CommandPattern:
#     @staticmethod
#     def main():
#         SearchCommand(SearchRequest(), HttpClient()).execute()


if __name__ == "__main__":
    SearchCommand(SearchRequest(), HttpClient()).execute()
