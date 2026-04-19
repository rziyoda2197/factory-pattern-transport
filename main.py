class Vehicle:
    def __init__(self, name):
        self.name = name

    def description(self):
        pass


class Car(Vehicle):
    def __init__(self):
        super().__init__("Car")

    def description(self):
        return f"{self.name} is a car."


class Bike(Vehicle):
    def __init__(self):
        super().__init__("Bike")

    def description(self):
        return f"{self.name} is a bike."


class Truck(Vehicle):
    def __init__(self):
        super().__init__("Truck")

    def description(self):
        return f"{self.name} is a truck."


class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Invalid vehicle type")


# Test
factory = VehicleFactory()
car = factory.create_vehicle("car")
bike = factory.create_vehicle("bike")
truck = factory.create_vehicle("truck")

print(car.description())
print(bike.description())
print(truck.description())
```

Kodda quyidagilar mavjud:

- `Vehicle` - umumiy `Vehicle` klassi, unda `name` atributi va `description` metodi mavjud.
- `Car`, `Bike`, `Truck` - transport vositalari uchun klasslar, ular `Vehicle` klassidan meros oladi.
- `VehicleFactory` - transport vositalari yaratish uchun klass, unda `create_vehicle` metodi mavjud, u transport vositalarini yaratish uchun foydalaniladi.
