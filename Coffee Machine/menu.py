class MenuItem:
    def __init__(self, name, water, coffee, milk, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water': water,
            'coffee': coffee,
            'milk': milk
        }


class Menu:

    def __init__(self):
        self.menu = [
            MenuItem(name="nescafe", water=100, coffee=30, milk=200, cost=100),
            MenuItem(name="bru", water=200, coffee=24, milk=150, cost=80),
            MenuItem(name="starbucks", water=250, coffee=24, milk=100, cost=150)
        ]

    def get_item(self):
        """Return the all names and cost of the available item"""
        option = ""
        for item in self.menu:
            option += f"{item.name}:{item.cost}\n"
        return option

    def find_drink(self, order_name):
        """Searches the menu item of the drink by name, Returns that item if it exits, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
