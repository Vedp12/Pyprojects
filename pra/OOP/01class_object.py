
class Car:
    def __init__(self, brand ,model):
        self.brand = brand
        self.model = model
    
    def functionallity(self,car_color,car_engine):
        self.car_color = car_color
        self.car_engine = car_engine
        return f"Car is {self.brand} with {self.model} and the color {self.car_color} and engine {self.car_engine}"
        
My_car = Car("Toyota","Supra")
print(My_car.brand , My_car.model)
print(My_car.functionallity("black","V8"))
