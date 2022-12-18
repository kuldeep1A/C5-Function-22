from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
import time
def clear(): return os.system('cls')


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
game_on = True
while game_on:
    option = menu.get_item()
    print(f"Show available coffee:\n{option}")
    choice = input("which coffee would you like to drink: ").lower()
    if choice == "off":
        game_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        time.sleep(20)
        print("\n\n\n")
        clear()
    else:
        people = int(input("how many people are drink the coffee: "))
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_available(drink) and money_machine.make_payment(drink.cost, people):
            coffee_maker.make_coffee(drink, people)
