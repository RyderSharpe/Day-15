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


espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g\n")
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

  # Check if payment is enough based on order cost (assuming 'order' is defined)
  if total_payment_rounded >= MENU[order]["cost"]:
      has_paid = True
      return True  # Payment sufficient
  else:
      print("Sorry, that is not enough money. Money refunded.")
      return False  # Payment insufficient
      break


# TODO print report and ask for order

def make_coffee(order):
    if not has_paid:  # Check if payment already successful
        if payment():
            has_paid = True  # Update flag only if payment successful here
            # ... (existing code)
    else:
        print("Payment already attempted. Please insert coins again or choose another option.")



# TODO check resources sufficient to make drink order
def is_resource_sufficient():
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

stop = False
while not stop:
    # TODO print report and ask for order
    order = input("What would you like? (espresso/latte/cappuccino): \n")

    if order == "report":
      report()
    elif order in MENU:  # Check if order is a valid coffee type
        if is_resource_sufficient() and payment() == True:
            make_coffee(order)
        elif is_resource_sufficient() and not payment():
            print("Insufficient money")
            break  # Exit the loop only after payment failure
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
