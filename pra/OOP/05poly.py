from abc import ABC, abstractmethod


class shape:
    @abstractmethod
    def area(self):
        pass


class circle(shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius**2


class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class pizza(circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


# Object in list
shapes = [circle(6), square(10)]
for shapes in shapes:
    print(shapes.area())

pizza1 = pizza("tomato", 4)
print("Pizza radius: ", pizza1.area())
