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


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g\n")
    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]
    print(f"Espresso costs ${espresso_cost:.2f}")
    print(f"Latte costs ${latte_cost:.2f}")
    print(f"Cappuccino costs ${cappuccino_cost:.2f}")

# TODO process coins

has_paid = False
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
  change = total_payment_rounded - MENU[order]["cost"]
  print(f"Here is your change ${change}")

  # Check if payment is enough based on order cost (assuming 'order' is defined)
  if total_payment_rounded >= MENU[order]["cost"]:
      has_paid = True
      return True  # Payment sufficient
  else:
      print("Sorry, that is not enough money.")
      return False  # Payment insufficient


# TODO make coffee
def make_coffee(order):
    """Makes coffee if resources are sufficient and payment successful."""
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]
        #print(f"{item.capitalize()}: {resources[item]}")
    print(f"Here is your {order} ☕")


# TODO check resources sufficient to make drink order
def is_resource_sufficient():
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# TODO print report and ask for order
stop = False
while not stop:
    order = input("What would you like? (espresso/latte/cappuccino): \n")

    if order == "report":
        report()
    elif order in MENU:  # Check if order is a valid coffee type
        # TODO check transaction successful
        if is_resource_sufficient():  # Check resource sufficiency once
            if payment():  # Check payment sufficiency
                make_coffee(order)
            else:
                print("Insufficient money")
                break  # Exit the loop only after payment failure
        else:
            print("Insufficient resources")
    else:
        print("Invalid coffee choice.")

