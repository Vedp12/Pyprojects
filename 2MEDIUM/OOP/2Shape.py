from abc import ABC, abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


#! Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


#! Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


#! Rectangle
class Rectangle(Shape):
    def __init__(self, lenght, breadth):
        self.lenght = lenght
        self.breadth = breadth

    def area(self):
        return self.lenght * self.breadth

    def perimeter(self):
        return 2 * (self.lenght + self.breadth)


S1 = Circle(20)
print(f"Area of circle {S1.area() }")
print(f"Perimeter of circle {S1.perimeter() }")
S2 = Square(20)
print(f"Area of square {S2.area() }")
print(f"Perimeter of square {S2.perimeter() }")
S3 = Rectangle(20, 30)
print(f"Area of rectangle {S3.area()}")
print(f"Perimeter of rectangle {S3.perimeter()}")
