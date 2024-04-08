import math
from ClassShape.Shape import Shape

class Triangle(Shape):
    def __init__(self):
        super().__init__()

    def compute_perimeter(self):
        sides = self.calculate_sides()
        return sum(sides)

    def compute_area(self):
        sides = self.calculate_sides()
        s = sum(sides) / 2
        return math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))

    def calculate_sides(self):
        vertices = self.get_vertices()
        x1, y1 = vertices[0]
        x2, y2 = vertices[1]
        x3, y3 = vertices[2]
        side1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        side2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        side3 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
        return side1, side2, side3

class Equilateral(Triangle):
    def __init__(self):
        super().__init__()

    def compute_perimeter(self):
        sides = self.calculate_sides()
        return 3 * sides[0]

    def compute_area(self):
        sides = self.calculate_sides()
        return (math.sqrt(3) / 4) * sides[0] ** 2

class Isosceles(Triangle):
    def __init__(self):
        super().__init__()

    def compute_perimeter(self):
        sides = self.calculate_sides()
        return sum(sides)

    def compute_area(self):
        sides = self.calculate_sides()
        if sides[0] == sides[1]:
            return (sides[2] / 4) * math.sqrt(4 * sides[0] ** 2 - sides[2] ** 2)
        else:
            return (sides[0] / 4) * math.sqrt(4 * sides[1] ** 2 - sides[0] ** 2)

class Scalene(Triangle):
    def __init__(self):
        super().__init__()

class RectangleTriangle(Triangle):
    def __init__(self):
        super().__init__()