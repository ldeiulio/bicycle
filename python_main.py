from bicycle import Bicycle, Manufacturer, BikeShop, Customer
from bicycle_parts import Wheel, Frame


def main():
    manufacturers = [setup_manufacturer1(), setup_manufacturer2()]
    customers = setup_customers()
    shop = setup_shop(manufacturers)
    print_customer_names_and_bikes(customers, shop)
    print_init_shop_inventory(shop)
    buy_bikes(customers, shop)
    print_final_shop_inventory(shop)

# sets up first manufacturer that makes cheapest 3 bikes
def setup_manufacturer1():
    bikes = []
    wheel = Wheel(5, 15, "basic mountain", 0)
    frame = Frame(10, 20, 2)
    bikes.append(Bicycle("El Rusty", wheel, wheel, frame))

    wheel = Wheel(3, 25, "basic road", 1)
    frame = Frame(9, 100, 2)
    bikes.append(Bicycle("The Economical", wheel, wheel, frame))

    wheel = Wheel(4, 50, "basic cross", 2)
    frame = Frame(7, 250, 0)
    bikes.append(Bicycle("Ol' Reliable", wheel, wheel, frame))

    return Manufacturer("OK Bikes", bikes, .1)


# sets up second manufacturer that makes most expensive 3 bikes
def setup_manufacturer2():
    bikes = []
    wheel = Wheel(5, 75, "pro cross", 2)
    frame = Frame(7, 265, 0)
    bikes.append(Bicycle("The Bike", wheel, wheel, frame))

    wheel = Wheel(2, 100, "pro road", 1)
    frame = Frame(3, 400, 1)
    bikes.append(Bicycle("Speedster", wheel, wheel, frame))

    wheel = Wheel(1, 150, "True Road", 1)
    frame = Frame(1, 500, 1)
    bikes.append(Bicycle("SuperSpeed", wheel, wheel, frame))

    return Manufacturer("Fast Bikes", bikes, .05)


# creates three customers with budgets of $200, $500 and $1000
def setup_customers():
    return [Customer("Adam", 200), Customer("Bill", 500), Customer("Charlie", 1000)]


# creates bike shop using the 6 bikes made from the 2 manufacturers made previously
def setup_shop(manufacturers):
    shop = BikeShop("The Bike Shop", [[], []], .2)
    for manufacturer in manufacturers:
        for bike_index in range(len(manufacturer.bikes_made)):
            shop.inventory[0].append(manufacturer.make_bike(bike_index))
            shop.inventory[1].append(8)
    return shop


# iterates through customers and prints out list of affordable bikes for each one
def print_customer_names_and_bikes(customers, shop):
    for customer in customers:
        print("%s (budget: $%.2f) can afford: " % (customer.name, customer.budget))
        bikes = shop.bikes_in_budget(customer.budget)
        for bike in bikes:
            print(bike.model, end="")
            if bike is not bikes[-1]:
                print(", ", end="")
        print("\n")


# prints shop inventory before any buying takes place
def print_init_shop_inventory(shop):
    print("initial shop inventory:")
    print_shop_inventory(shop)


# prints current shop inventory
def print_shop_inventory(shop):
    inv = shop.inventory
    for bike_index in range(len(inv[0])):
        print("%s, retail price: $%.2f, production cost: $%.2f, manufacturer price: $%.2f number in inventory: %d" %
              (inv[0][bike_index].model, shop.margin * inv[0][bike_index].cost, inv[0][bike_index].cost,
               inv[0][bike_index].manufacturer.margin * inv[0][bike_index].cost, inv[1][bike_index]))
    print()


# all customers buy the most expensive bike they can afford
def buy_bikes(customers, shop):
    for customer in customers:
        bikes = shop.bikes_in_budget(customer.budget)
        shop.sell_bike(bikes[-1], customer)
        print("%s bought %s for %.2f. Remaining budget: %.2f" % (customer.name, customer.bikes_owned[0].model,
                                                                 shop.margin * customer.bikes_owned[0].cost,
                                                                 customer.budget))
    print()


# prints shop inventory after buying takes place, also prints total shop profit
def print_final_shop_inventory(shop):
    print("final shop inventory:")
    print_shop_inventory(shop)
    print("profit: $%.2f" % shop.profit)


# if current file is used as main file, start program by calling main()
if __name__ == "__main__":
    main()
