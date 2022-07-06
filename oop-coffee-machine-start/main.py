from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
cofe_make = CoffeeMaker()
money_machine = MoneyMachine()
print(menu.menu)
while True:
    product = menu.get_items()
    order = input(f"What would you like? ({product}) ")
    if order != "off" and order != "report" and order != "cappucino" and order != "latte" and order != "espresso":
        continue
    elif order == "off":
        break
    elif order == "report":
        cofe_make.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if cofe_make.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            cofe_make.make_coffee(drink)

