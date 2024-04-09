class Device:

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def print_parameters(self):
        return f"Brand: {self.__brand}, Model: {self.model}"

class CoffeeMachine(Device):
    def __init__(self, brand, model, coffee_type):
        super().__init__(brand,model)
        self.coffe_type = coffee_type

    def print_coffee_type(self):
        return f"Brewing {self.coffe_type}"
class Blender(Device):
    def __init__(self, brand, model, speed_levels):
        super().__init__(brand,model)
        self.speed_levels = speed_levels

    def print_speed_levels(self):
        return f"Blender has {self.speed_levels} speed levels"

class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def print_meatgrinder(self):
       return f"Grinding meat with {self.power} watts power"

coffee_machine = CoffeeMachine("Delonghi", "M-10", "Special")
blender = Blender("Kenwood", "5200", 4)
meat_grinder = MeatGrinder("Kenwood", "FGA", 350)

print(coffee_machine.print_parameters())
print(coffee_machine.print_coffee_type())

print(blender.print_parameters())
print(blender.print_speed_levels())

print(meat_grinder.print_parameters())
print(meat_grinder.print_meatgrinder())