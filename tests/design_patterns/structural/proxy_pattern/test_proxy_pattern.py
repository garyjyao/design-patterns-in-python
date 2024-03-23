from unittest.mock import patch
from design_patterns.structural.proxy_pattern.proxy_pattern import RealImage, ProxyImage


def test_real_image():
    # Assign
    real_image = RealImage("test.jpg")

    # Act
    with patch('builtins.print') as mocked_print:
        real_image.display_image()

        # Assert
        mocked_print.assert_called_once_with("Displaying test.jpg")

    assert real_image.filename == "test.jpg"


@patch.object(RealImage, 'display_image')
def test_proxy_image(mock_display_image):
    # Assign
    proxy_image = ProxyImage("test.jpg")

    # Act
    proxy_image.display_image()

    # Assert
    mock_display_image.assert_called_once()
