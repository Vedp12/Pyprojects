class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        # return f"battery size {battery_size}"


Ele = Electric_car("Tesla", "X", "80kvw")
print(Ele.brand, Ele.model, Ele.battery_size)
