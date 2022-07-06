from typing import Dict

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
income = 0

flag = True

while flag:
    order = input("What would you like?(espresso/latte/cappuccino):")
    if order == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {income}")
    elif order == "exit":
        flag = False
    else:
        print("Please insert coins.")
        quarters = float(input("how many quarters?"))
        dimes = float(input("how many dimes?"))
        nickels = float(input("how many nickles?"))
        pennies = float(input("how many pennies?"))
        total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    try:
        if MENU[order]['cost'] > total:
            print("Sorry that's not enough money. Money refunded.")
        else:
            if MENU[order]['ingredients']['water'] <= resources['water'] and MENU[order]['ingredients']['milk'] <= resources['milk'] and MENU[order]['ingredients']['coffee'] <= resources['coffee']:
                income += MENU[order]['cost']
                resources['water'] -= MENU[order]['ingredients']['water']
                resources['milk'] -= MENU[order]['ingredients']['milk']
                resources['coffee'] -= MENU[order]['ingredients']['coffee']
                print(f"Here is your {order} 🧼. Enjoy!!")
            elif MENU[order]['ingredients']['water'] > resources['water']:
                print("Sorry there is not enough water.")
            elif MENU[order]['ingredients']['milk'] > resources['milk']:
                print("Sorry there is not enough milk.")
            elif MENU[order]['ingredients']['coffee'] > resources['coffee']:
                print("Sorry there is not enough coffee.")
    except KeyError as e:
        print("Please select the specific type of coffee.")
        continue