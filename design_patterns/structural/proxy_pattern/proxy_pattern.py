class Image:
    def display_image(self):
        pass


class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading {self.filename}")

    def display_image(self):
        print(f"Displaying {self.filename}")


class ProxyImage(Image):
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
