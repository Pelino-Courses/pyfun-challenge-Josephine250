import math

class Shape:
    """
    Base class for geometric shapes.

    Attributes:
    - name (str): The name of the shape.

    Methods:
    - area(): Returns the area of the shape (to be overridden by subclasses).
    - __str__(): Human-readable description of the shape.
    """

    def __init__(self, name: str):
        self.name = name

    def area(self) -> float:
        """
        Returns the area of the shape. This method should be overridden by subclasses.

        Raises:
        - NotImplementedError: If called on base class.
        """
        raise NotImplementedError("Subclasses must implement the area method.")

    def __str__(self):
        return f"This is a {self.name}."


class Circle(Shape):
    """
    Circle shape class inheriting from Shape.

    Attributes:
    - radius (float): Radius of the circle (must be > 0).

    Methods:
    - area(): Returns the area of the circle.
    """

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"{super().__str__()} Radius: {self.radius}, Area: {self.area():.2f}"


class Rectangle(Shape):
    """
    Rectangle shape class inheriting from Shape.

    Attributes:
    - width (float): Width of the rectangle (must be > 0).
    - height (float): Height of the rectangle (must be > 0).

    Methods:
    - area(): Returns the area of the rectangle.
    """

    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def __str__(self):
        return f"{super().__str__()} Width: {self.width}, Height: {self.height}, Area: {self.area():.2f}"


class Triangle(Shape):
    """
    Triangle shape class inheriting from Shape.

    Attributes:
    - base (float): Base length of the triangle (must be > 0).
    - height (float): Height of the triangle (must be > 0).

    Methods:
    - area(): Returns the area of the triangle.
    """

    def __init__(self, base: float, height: float):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"{super().__str__()} Base: {self.base}, Height: {self.height}, Area: {self.area():.2f}"


# Example usage
if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 7)
    ]

    for shape in shapes:
        print(shape)