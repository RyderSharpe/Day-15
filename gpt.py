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

has_paid = False  # Flag to track successful payment


def report():
    """Prints a report on coffee machine resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g\n")
    print(f"Espresso costs ${MENU['espresso']['cost']:.2f}")
    print(f"Latte costs ${MENU['latte']['cost']:.2f}")
    print(f"Cappuccino costs ${MENU['cappuccino']['cost']:.2f}")


def payment():
    """Collects user input for coins and checks if payment is sufficient."""
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    quarter_value = quarters * 0.25
    dime_value = dimes * 0.1
    nickle_value = nickles * 0.05
    pennies_value = pennies * 0.01

    total_payment = quarter_value + dime_value + nickle_value + pennies_value
    total_payment_rounded = round(total_payment, 2)

    print(f"You paid ${total_payment_rounded:.2f}")

    # Check if payment is enough based on order cost
    if total_payment_rounded >= MENU[order]["cost"]:
        return True  # Payment sufficient
    else:
        print("Sorry, that is not enough money. Money refunded.")
        return False  # Payment insufficient


def is_resource_sufficient():
    """Checks if there are enough resources to make a coffee."""
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False  # Not enough resources
    return True  # Enough resources


def make_coffee(order):
    """Makes coffee if resources are sufficient and payment successful."""
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]
        print(f"{item.capitalize()}: {resources[item]}")
    print(f"Here is your {order} ☕")


# Get user input for coffee choice
order = input("What would you like? (espresso/latte/cappuccino): \n")

if order == "report":
    report()
elif order in MENU:  # Check if order is a valid coffee type
    if is_resource_sufficient():
        if not has_paid:  # Check if payment already successful
            if payment():
                has_paid = True  # Update flag only if payment successful here
                make_coffee(order)
        else:
            print("Payment already attempted. Please insert coins again or choose another option.")
    else:
        print("insufficient resources")
else:
    print("Invalid coffee choice.")


