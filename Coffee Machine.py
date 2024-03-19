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

# stop = False
# while not stop:

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")

# TODO process coins
def payment():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    quarter_value = quarters * 0.25
    dime_value = dimes * 0.1
    nickle_value = nickles * 0.05
    pennies_value = pennies * 0.01
    total_payment = quarter_value + dime_value + nickle_value + pennies_value
    q = round(total_payment, 2)
    print(q)


# TODO print report and ask for order

def make_coffee(order):
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]
        print(f"{item.capitalize()}: {resources[item]}")
    print(f"Here is your {order} ☕")


# TODO check resources sufficient to make drink order
def is_resource_sufficient():
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO print report and ask for order
order = input("What would you like? (espresso/latte/cappuccino): ")

if order == "report":
  report()
elif order in MENU:  # Check if order is a valid coffee type
  if is_resource_sufficient():
      payment()
      make_coffee(order)
  else:
      print("insufficient resources")
else:
  print("Invalid coffee choice.")





# how many quarters
# how many dimes
# how many nickles
# how many pennies
# enough money = > here is you drink, here is your change
# not enough money = > "Sorry that's not enough money. Money refunded."
# TODO check transaction successful
# if transaction successful, make coffee => minus resources
# TODO make coffee

