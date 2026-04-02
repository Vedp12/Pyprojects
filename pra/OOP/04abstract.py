from abc import ABC, abstractmethod


class vechile(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(vechile):
    def go(self):
        print("You can go!")

    def stop(self):
        print("You can stop!")


class Bike(vechile):
    def go(self):
        print("You can go!")

    def stop(self):
        print("You can stop!")


B1 = Bike()
B1.go()
B2 = Bike()
B2.stop()
