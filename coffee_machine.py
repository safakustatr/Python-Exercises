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

def report_sources(resource_list):
    print(f"Water: {resource_list['water']}ml")
    print(f"Milk: {resource_list['milk']}ml")
    print(f"Coffee: {resource_list['coffee']}gr")

def check_resources(ingredients, resource_list):
    for ingredient in ingredients:
        if ingredients[ingredient] > resource_list[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def insert_coins(price):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    quarters = quarters * 0.25
    dimes = dimes * 0.1
    nickels = nickels * 0.05
    pennies = pennies * 0.01
    total = quarters + dimes + nickels + pennies
    change = total - price
    if total < price:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${change:.2f} in change.")
        return True

def make_coffee(coffee, ingredients):
    global resources
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {coffee} ☕. Enjoy!")



espresso_ingredients = MENU["espresso"]["ingredients"]
latte_ingredients = MENU["latte"]["ingredients"]
cappuccino_ingredients = MENU["cappuccino"]["ingredients"]
espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]
is_machine_on = True

while is_machine_on:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "off":
        is_machine_on = False
    elif prompt == "report":
        report_sources(resources)
    elif prompt == "espresso":
        if check_resources(espresso_ingredients, resources):
            is_money_enough = insert_coins(espresso_cost)
            if is_money_enough:
                make_coffee("espresso", espresso_ingredients)
    elif prompt == "latte":
        if check_resources(latte_ingredients, resources):
            is_money_enough = insert_coins(latte_cost)
            if is_money_enough:
                make_coffee("latte", latte_ingredients)
    elif prompt == "cappuccino":
        if check_resources(cappuccino_ingredients, resources):
            is_money_enough = insert_coins(cappuccino_cost)
            if is_money_enough:
                make_coffee("cappuccino", cappuccino_ingredients)
    else:
        print("Please enter a valid input.")