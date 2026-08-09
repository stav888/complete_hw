class Vehicle:
    def __init__(self, base_fee):
        self.name = "Vehicle"
        self.base_fee = float(base_fee)

    def trip_cost(self, distance_km):
        return self.base_fee

    def __str__(self):
        return f"{self.name}: base_fee: {self.base_fee}"


class GasCar(Vehicle):
    def __init__(self, liters_per_100km, price_per_liter, base_fee):
        super().__init__(base_fee)
        self.name = "GasCar"
        self.liters_per_100km = float(liters_per_100km)
        self.price_per_liter = float(price_per_liter)

    def trip_cost(self, distance_km):
        return self.base_fee + distance_km / 100 * self.liters_per_100km * self.price_per_liter

    def __str__(self):
        return f"{self.name}: liters_per_100km={self.liters_per_100km}, price_per_liter={self.price_per_liter}, trip_50km={self.trip_cost(50):.2f}"


class ElectricCar(Vehicle):
    def __init__(self, kwh_per_100km, price_per_kwh, base_fee):
        super().__init__(base_fee)
        self.name = "ElectricCar"
        self.kwh_per_100km = float(kwh_per_100km)
        self.price_per_kwh = float(price_per_kwh)

    def trip_cost(self, distance_km):
        return self.base_fee + distance_km / 100 * self.kwh_per_100km * self.price_per_kwh

    def __str__(self):
        return f"{self.name}: kwh_per_100km={self.kwh_per_100km}, price_per_kwh={self.price_per_kwh}, trip_50km={self.trip_cost(50):.2f}"


class Taxi(Vehicle):
    def __init__(self, price_per_km, is_night, base_fee):
        super().__init__(base_fee)
        self.name = "Taxi"
        self.price_per_km = float(price_per_km)
        self.is_night = bool(is_night)

    def trip_cost(self, distance_km):
        cost = self.base_fee + distance_km * self.price_per_km
        return cost * 1.2 if self.is_night else cost

    def __str__(self):
        return f"{self.name}: price_per_km={self.price_per_km}, is_night={self.is_night}, trip_50km={self.trip_cost(50):.2f}"
