class BikePart:

    def __init__(self, weight, cost):
        self.weight = weight
        self.cost = cost


class Wheel(BikePart):

    types = ["mountain", "road", "cross"]

    def __init__(self, weight, cost, model, type_number):
        super().__init__(weight, cost)
        self.type = self.types[type_number]
        self.type_number = type_number
        self.model = model


class Frame(BikePart):

    materials = ["aluminum", "carbon", "steel"]

    def __init__(self, weight, cost, material_number):
        super().__init__(weight, cost)
        self.material = self.materials[material_number]
