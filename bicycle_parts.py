# parent class to Wheel and Frame classes
class BikePart:

    # weight is weight of BikePart, expects float
    # cost is production cost of BikePart, expects float
    def __init__(self, weight, cost):
        self.weight = weight
        self.cost = cost


class Wheel(BikePart):

    # all valid types of of wheel
    types = ["mountain", "road", "cross"]

    # model is production name of wheel, expects string
    # type_number represents type of wheel is in reference to types list
    def __init__(self, weight, cost, model, type_number):
        super().__init__(weight, cost)
        self.type = self.types[type_number]
        self.type_number = type_number
        self.model = model


class Frame(BikePart):

    # all valid materials for frame
    materials = ["aluminum", "carbon", "steel"]

    # material_number represents type of material frame is created with in reference to types list
    def __init__(self, weight, cost, material_number):
        super().__init__(weight, cost)
        self.material = self.materials[material_number]
