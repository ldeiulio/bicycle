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

    def __init__(self, name, bikes_made, margin):
        self.name = name
        self.bikes_made = bikes_made
        self.margin = margin

    def make_bike(self, bike_listing_num):
        bike = self.bikes_made[bike_listing_num]
        return Bicycle(bike.model, bike.wheels[0], bike.wheels[1], bike.frame, self)


class BikeShop:

    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = inventory
        self.profit = 0
        self.margin = 1 + margin

    def sell_bike(self, bike, customer):
        bike_index = self.inventory[0].index(bike)
        self.inventory[1][bike_index] -= 1
        if self.inventory[1][bike_index] == 0:
            del self.inventory[0][bike_index]
            del self.inventory[1][bike_index]
        self.profit += self.margin * bike.cost - (1 + bike.manufacturer.margin) * bike.cost
        customer.budget -= self.margin * bike.cost
        customer.bikes_owned.append(bike)
        return bike

    def bikes_in_budget(self, budget):
        bike_list = []
        for bike in self.inventory[0]:
            if self.margin * bike.cost < budget:
                bike_list.append(bike)
        return bike_list


class Customer:

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.bikes_owned = []


class MismatchedWheelsError(Exception):
    pass
