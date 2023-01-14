import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"X: {self.x} Y: {self.y}"


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"X: {self.x} Y: {self.y}"


class Line:
    def __init__(self, origin_point: Point, direction_vector: Vector):
        self.origin_point = origin_point
        self.direction_vector = direction_vector

    def get_point_along_line(self, t):
        return Point(t * self.direction_vector.x + self.origin_point.x,
                     t * self.direction_vector.y + self.origin_point.y)

    def get_derivative(self):
        return self.direction_vector.y / self.direction_vector.x


class Ellipse:
    def __init__(self, x_radius, y_radius):
        self.x_radius = x_radius
        self.y_radius = y_radius

    def get_point_along_line(self, t):
        a = math.atan2(
            self.x_radius * math.sin(t),
            self.y_radius * math.cos(t),
        )
        return Point(self.x_radius * math.cos(a),
                     self.y_radius * math.sin(a))

    def get_derivative(self, t):
        a = math.atan2(
            self.x_radius * math.sin(t),
            self.y_radius * math.cos(t),
        )
        return Point(self.x_radius * -math.sin(a),
                     self.y_radius * math.cos(a))
