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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

### MY SOLUTION ###

def print_report(money):
    """ Printing report """
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"

def things_from_dictionary(user_choice, ingredient):
    """ Formatting ingredients from MENU dictionary for easier usage """
    if ingredient in MENU[user_choice]["ingredients"]:
        ingredients = MENU[user_choice]["ingredients"][ingredient]
        return ingredients
    else:
        ingredients = 0
        return ingredients

def calc_of_users_money():
    """ Calculating how much money we got from the user """
    print("Insert money, please.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

def calc_of_change(user_money, coffee_cost):
    """ Calculating change for user """
    return user_money - coffee_cost

def calc_of_money(money,coffee_cost):
    """ Calculating money in coffee machine """
    return money + coffee_cost

def update_of_resources(user_choice):
    """ Updating amount of resources in coffee machine """
    for resource in resources:
        resources[resource] -= things_from_dictionary(user_choice,resource)
    print(f"Here is your {user_choice}. Enjoy your drink!")

def drink_process(user_choice, coffee_cost):
    """ Making drink process """
    global money
    water = "water"
    milk = "milk"
    coffee = "coffee"

    if resources[water] >= things_from_dictionary(user_choice,water):   # checking if there is enough water to make a drink
        if resources[milk] >= things_from_dictionary(user_choice,milk): # checking if there is enough milk to make a drink
            if resources[coffee] >= things_from_dictionary(user_choice,coffee): # checking if there is enough coffee to make a drink
                user_money = calc_of_users_money()  # calculating how much money user gave us
                if user_money > coffee_cost:    # user gave us more than enough money
                    change = calc_of_change(user_money, coffee_cost)    # calculating change for a user
                    print(f"Here is your change: ${change}")
                    money = calc_of_money(money, coffee_cost)   # counting how much money we earned
                    update_of_resources(user_choice)    # updating amount of resources left after a drink
                elif user_money == coffee_cost: # user gave us exact amount of money for a drink
                    money = calc_of_money(money, coffee_cost)   # counting how much money we earned
                    update_of_resources(user_choice)    # updating amount of resources left after a drink
                else:   # user gave us not enough money for a drink
                    print("Sorry, not enough money.\nReturned money.")
            else:   # there is not enough coffee in resources for that drink
                print("Sorry, not enough coffee.")
        else:   # there is not enough milk in resources for that drink
            print("Sorry, not enough milk.")
    else:   # there is not enough water in resources for that drink
        print("Sorry, not enough water.")

def coffee_machine():
    """ Coffee Machine program """
    is_turned_on = True

    while is_turned_on: # loop for program until user gives us 'off' command
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_choice != "report" and user_choice != "off":    # checking if user chose a drink not a report or shut down
            # making variables for ingredients from MENU dictionary for easier usage
            coffee_cost = MENU[user_choice]["cost"]

        if user_choice == "off":    # shutting down the coffee machine
            is_turned_on = False
        elif user_choice == "report":   # printing the report of how much of ingredients is there
            report = print_report(money)
            print(report)
        elif user_choice == "espresso": # process for espresso
            drink_process(user_choice,coffee_cost)
        elif user_choice == "latte":    # process for latte
            drink_process(user_choice, coffee_cost)
        elif user_choice == "cappuccino":   # process for cappuccino
            drink_process(user_choice, coffee_cost)
        else:
            print("Not such a drink. ")

money = 0   # global money variable for counting how much we earned

coffee_machine()


### HER SOLUTION ###

# def is_resource_sufficient(order_ingredients):
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True
#
# def process_coins():
#     print("Please insert coins.")
#     total =int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
# def is_transaction_successful(money_received, drink_cost):
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
# def make_coffee(drink_name, order_ingredients):
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
# is_on = True
#
# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment,drink["cost"]):
#                 make_coffee(choice,drink["ingredients"])