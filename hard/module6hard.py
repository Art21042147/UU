import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = False
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return (all(isinstance(side, int) and side > 0 for side in sides) and
                len(sides) == self.sides_count)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def segment_area(self, h):
        if h > 2 * self.__radius or h < 0:
            raise ValueError("Height must be between 0 and the diameter of the circle")
        r = self.__radius
        segment_area = r ** 2 * (math.acos((r - h) / r)) - (r - h) * math.sqrt(2 * r * h - h ** 2)
        return segment_area


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = None
        self.__calculate_height()

    def __calculate_height(self):
        s = sum(self.get_sides()) / 2
        a, b, c = self.get_sides()
        self.__height = (2 / a) * (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def get_square(self):
        a, _, _ = self.get_sides()
        return 0.5 * a * self.__height

    def get_height(self):
        return self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


circle1 = Circle((255, 0, 0), 10)
triangle1 = Triangle((0, 255, 0), 3, 4, 5)
cube1 = Cube((0, 0, 255), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка высоты треугольника:
print(triangle1.get_height())

# Проверка площади сигмента круга:
print(round(circle1.segment_area(2), 2))
