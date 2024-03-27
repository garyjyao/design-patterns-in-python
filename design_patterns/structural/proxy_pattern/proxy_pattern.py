class Image:
    """
    An interface that represents an image

    Methods:
        display_image():
            Displays the image
    """

    def display_image(self):
        pass


class RealImage(Image):
    """
    A class that represents a real image

    Attributes:
        filename (string): The filename of the image

    Methods:
        load_image_from_disk():
            Loads the image from disk
        display_image():
            Displays the image
    """

    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading {self.filename}")

    def display_image(self):
        print(f"Displaying {self.filename}")


class ProxyImage(Image):
    """
    A class that represents a proxy image that will load the real image when needed (Lazy initialization).

    Proxy Pattern is a structural design pattern that provides a proxy or placeholder for another object
    and control access to it.

    ProxyImage is a proxy class, the proxy class will control access to the real object (RealImage)
    and will create it only when required.

    ProxyImage can be used for
    - Lazy initialization
    - Access control
    - Logging
    - Caching

    Attributes:
        filename (string): The filename of the image
        image (RealImage): The real image

    Methods:
        display_image():
            Displays the image
    """

    def __init__(self, filename):
        self.filename = filename
        self.image = None

    def display_image(self):
        if self.image is None:
            self.image = RealImage(self.filename)
        self.image.display_image()


if __name__ == "__main__":
    image = ProxyImage("some-image.jpg")
    image.display_image()
