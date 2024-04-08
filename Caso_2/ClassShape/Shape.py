import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_coordinates(self):
        return self._x, self._y

class Line:
    def __init__(self, initial_point, final_point):
        self._initial_point = initial_point
        self._final_point = final_point

    def length(self):
        x1, y1 = self._initial_point.get_coordinates() 
        x2, y2 = self._final_point.get_coordinates()
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class Shape:
    def __init__(self):
        pass

    def initialize_shape(self, vertices):
        self.vertices = vertices

    def get_vertices(self):
        return self.vertices

    def compute_perimeter(self):
        raise NotImplementedError("Subclases deben implementar compute_perimeter()")

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar compute_area()")

    def compute_angles(self):
        raise NotImplementedError("Subclases deben implementar compute_angles()")