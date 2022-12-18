class MoneyMachine:

    CURRENCY_SYMBOL = "₹"

    CURRENCY_COIN = {
        '₹5': 5,
        '₹10': 10,
        '₹20': 20,
        '₹50': 50,
        '₹100': 100,
        '₹200': 200,
        '₹500': 500,
        '₹2000': 2000,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY_SYMBOL}{self.profit}")

    def process_coin(self):
        """Returns all total calculated from coins inserted"""
        for coin in self.CURRENCY_COIN:
            self.money_received += int(input(f"How many {coin}: ")) * self.CURRENCY_COIN[coin]
        return self.money_received

    def make_payment(self, cost, people):
        print(f"Total money: {cost * people}")
        self.process_coin()
        if self.money_received > cost*people:
            change = round(self.money_received - cost * people, 2)
            print(f"Here your change {self.CURRENCY_SYMBOL}{change}.")
            self.profit += cost * people
            self.money_received = 0
            return True
        elif self.money_received == cost*people:
            self.profit += cost * people
            self.money_received = 0
            return True
        else:
            more_money = round(cost * people - self.money_received, 3)
            print("Sorry that's not enough money. Money refunded.")
            print(f"Please give {more_money} more money.")
            return False
