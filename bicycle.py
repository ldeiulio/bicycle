class Bicycle:

    # initializes Bicycle object
    # model is name of bicycle model in string format
    # wheel0 and wheel1 are wheels of matching type, else error is thrown
    # weight calculated by summing together weight of wheels and frame
    # production cost calculated by summing costs of wheels and frame
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

    # name expects string
    # bikes_made is list of bicycles produced by manufacturer. expects list of Bicycles
    # margin is price premium over production cost charged to stores for expects float above 0
    def __init__(self, name, bikes_made, margin):
        self.name = name
        self.bikes_made = bikes_made
        self.margin = 1 + margin

    # creates bike object for use in BikeShop object
    def make_bike(self, bike_listing_num):
        bike = self.bikes_made[bike_listing_num]
        return Bicycle(bike.model, bike.wheels[0], bike.wheels[1], bike.frame, self)


class BikeShop:

    # name is name of BikeShop, expects string
    # inventory represents what model bikes are in stock as well as number of bikes in stock
    # the inventory expects a list containing two lists such that the top list contains the bicycle objects and the
    # bottom list contains the number of bikes contained within the corresponding index of the top list
    # margin is price premium over production cost to determine retail price. expects float above 0
    # initializes profit to 0
    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = inventory
        self.profit = 0
        self.margin = 1 + margin

    # sells bike to customer. Charges customer for corresponding bike, subtracts retail price from customer, adds net
    # profit to profit variable (retail price - manufacturer charge)
    def sell_bike(self, bike, customer):
        bike_index = self.inventory[0].index(bike)
        self.inventory[1][bike_index] -= 1
        if self.inventory[1][bike_index] == 0:
            del self.inventory[0][bike_index]
            del self.inventory[1][bike_index]
        self.profit += self.margin * bike.cost - bike.manufacturer.margin * bike.cost
        customer.budget -= self.margin * bike.cost
        customer.bikes_owned.append(bike)
        return bike

    # returns list of bikes from shop that could be afforded by supplied budget
    def bikes_in_budget(self, budget):
        bike_list = []
        for bike in self.inventory[0]:
            if self.margin * bike.cost < budget:
                bike_list.append(bike)
        return bike_list


class Customer:

    # name is name of customer, expects string
    # budget is budget of customer for bike, expects float
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.bikes_owned = []


# error to be thrown if wheels being added to bike are not the same type
class MismatchedWheelsError(Exception):
    pass
