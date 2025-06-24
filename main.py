from sandwich_makerr import SandwichMachine
from cashier import process_coins, transaction_result
import Data

machine = SandwichMachine(Data.resources)

running = True
while running:
    print("Welcome to your sandwich machine!\n")
    choice = input("What would you like? (small/ medium/ large/ off/ report): ")

    #turn off machine
    if choice == "off":
        running = False

    #see machine contents
    elif choice == "report":
        for item, value in machine.machine_resources.items():
            print(f"{item}: {value} slice(s)" if item != "cheese" else f"{item}: {value} ounce(s)")

    #if choice is within one of the recipe options: small, medium, large
    elif choice in Data.recipes:
        sandwich = Data.recipes[choice]
        ingredients = sandwich["ingredients"]
        cost = sandwich["cost"]

        if machine.check_resources(ingredients):
            coins_inserted = process_coins()
            if transaction_result(coins_inserted, cost):
                machine.make_sandwich(choice, ingredients)

    #if user wrote something stupid
    else:
        print("Invalid option. Please try again.")
        print("___________________________________________________")