from unittest.mock import patch
from design_patterns.structural.proxy_pattern.proxy_pattern import RealImage, ProxyImage


def test_real_image():
    """
    Test RealImage class
    when display_image is called
    then it should print "Displaying test.jpg" (Displaying the image)
    """
    # Assign
    real_image = RealImage("test.jpg")

    # Act
    with patch('builtins.print') as mocked_print:
        real_image.display_image()

        # Assert
        mocked_print.assert_called_once_with("Displaying test.jpg")

    assert real_image.filename == "test.jpg"


@patch.object(RealImage, 'display_image')
@patch.object(RealImage, 'load_image_from_disk')
def test_proxy_image(mocked_load_image_from_disk, mock_display_image):
    """
    Test ProxyImage class
    lazy initialization of RealImage
    when display_image is called
    then it should call the proxied RealImage display_image method
    """
    # Assign
    proxy_image = ProxyImage("test.jpg")

    # Check - RealImage is not loaded yet
    mocked_load_image_from_disk.assert_not_called()

    # Act
    proxy_image.display_image()

    # Assert
    mock_display_image.assert_called_once()
