class Bicycle:

    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost


class Wheels:

    types = ["mountain", "road", "cross"]

    def __init__(self, model, weight, cost, type_number):
        self.type = self.types[type_number]
        self.model = model
        self.weight = weight
        self.cost = cost


class Frame:

    materials = ["aluminum", "carbon", "steel"]

    def __init__(self, material_number, weight, cost):
        self.material = self.materials[material_number]
        self.weight = weight
        self.cost = cost


class BikeShop:

    margin = 1.2

    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.profit = 0


class Customer:

    def __init__(self, name, budget):
        self.name = name;
        self.budget = budget
        self.bikes_owned = []


class MismatchedWheelsError(Exception):
    pass
