class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f'{self.make} {self.model}'

class Car(Vehicle):
    def __init__(self,make, model, fuel_type):
        self.fuel_type = fuel_type
        super().__init__(make, model)
    def get_info(self):
        print(super().get_info(), self.fuel_type)

machina = Car("Toyota", "Camry", "95")
machina.get_info()