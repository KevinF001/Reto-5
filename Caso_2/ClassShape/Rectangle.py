import math
from ClassShape.Shape import Shape

class Rectangle(Shape):
    def __init__(self):
        super().__init__()

    def compute_perimeter(self):
        sides = self.calculate_sides()
        return 2 * (sides[0] + sides[1])

    def compute_area(self):
        sides = self.calculate_sides()
        return sides[0] * sides[1]

    def calculate_sides(self):
        vertices = self.get_vertices()
        x1, y1 = vertices[0]
        x2, y2 = vertices[1]
        x3, y3 = vertices[2]
        x4, y4 = vertices[3]
        side1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        side2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        return side1, side2

class Square(Rectangle):
    def __init__(self):
        super().__init__()

    def compute_perimeter(self):
        sides = self.calculate_sides()
        return 4 * sides[0]

    def compute_area(self):
        sides = self.calculate_sides()
        return sides[0] ** 2