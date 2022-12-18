class CoffeeMaker:
    """Modules the machine that makes the coffee"""
    def __init__(self):
        self.resource = {
            "water": 3000,
            "milk": 2000,
            "coffee": 1000
        }

    def report(self):
        """Show the all resources"""
        print(f"Water: {self.resource['water']}ml")
        print(f"Milk: {self.resource['milk']}ml")
        print(f"Coffee: {self.resource['coffee']}gm")

    def is_resource_available(self, drink):
        """if the resource are available then returns true otherwise returns false"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resource[item]:
                can_make = False
        return can_make

    def make_coffee(self, order, people):
        """Deducts the ingredients from the resources"""
        for item in order.ingredients:
            self.resource[item] -= order.ingredients[item]*people
        print(f"Here is your {people} {order.name} ☕️. Enjoy!")
