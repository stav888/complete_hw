from abc import ABC, abstractmethod


class Chargeable(ABC):
    @abstractmethod
    def charge(self):
        pass


class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass


class Vehicle(ABC):
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Vehicle(model={self.model})"

    @abstractmethod
    def move(self):
        pass


class ElectricCar(Vehicle, Chargeable, Drivable):
    def __init__(self, model, battery_level):
        super().__init__(model)
        self.battery_level = battery_level

    def __str__(self):
        return f"ElectricCar(model={self.model}, battery_level={self.battery_level})"

    def move(self):
        return f"{self.model} moves silently"

    def charge(self):
        return f"{self.model} is charging"

    def drive(self):
        return f"{self.model} is driving"


class ElectricScooter(Vehicle, Chargeable):
    def __init__(self, model, max_speed):
        super().__init__(model)
        self.max_speed = max_speed

    def __str__(self):
        return f"ElectricScooter(model={self.model}, max_speed={self.max_speed})"

    def move(self):
        return f"{self.model} moves"

    def charge(self):
        return f"{self.model} is charging"
