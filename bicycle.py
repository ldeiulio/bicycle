class Bicycle:

    def __init__(self, model, wheel0, wheel1, frame, manufacturer=None):
        self.model = model
        if wheel0.type != wheel1.type:
            raise MismatchedWheelsError
        self.wheels = [wheel0, wheel1]
        self.frame = frame
        self.weight = wheel0.weight + wheel1.weight + frame.weight
        self.cost = wheel0.cost + wheel1.cost + frame.cost
        self.manufacturer = manufacturer


class Manufacturer:

    def __init__(self, name, bike_model_0, bike_model_1, bike_model_2, percent_over_cost):
        self.name = name
        self.bikes_made = [bike_model_0, bike_model_1, bike_model_2]
        self.percent_over_cost = percent_over_cost

    def make_bike(self, bike_listing_num):
        bike = self.bikes_made[bike_listing_num]
        return Bicycle(bike.model, bike.wheels[0], bike.wheels[1], bike.frame, self)


class BikeShop:

    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = inventory
        self.profit = 0
        self.margin = margin


class Customer:

    def __init__(self, name, budget):
        self.name = name;
        self.budget = budget
        self.bikes_owned = []


class MismatchedWheelsError(Exception):
    pass
