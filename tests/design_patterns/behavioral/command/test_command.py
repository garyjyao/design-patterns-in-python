from unittest.mock import patch

from design_patterns.behavioral.command.command import *


@patch.object(HttpClient, 'post', return_value="mocked_response")
def test_execute_mocked_method(mocked_post):
    # Assign
    request = SearchRequest()
    client = HttpClient()
    # mocked_post.return_value = "mocked_response"

    # Act
    command = SearchCommand(request, client)
    response = command.execute()

    # Assert
    mocked_post.assert_called_once_with(request)
    assert response == "mocked_response"


def test_execute_real():
    # Assign
    request = SearchRequest()
    client = HttpClient()

    # Act
    command = SearchCommand(request, client)
    response = command.execute()

    # Assert
    assert response.get_request() == request
