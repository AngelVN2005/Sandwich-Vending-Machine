### Data ###Add commentMore actions

#hashmap with all the sandwich options
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}

### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input."""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        dollars = int(input("how many dollar coins?: ")) * 1.00
        halves = int(input("how many half dollar coins?: ")) * 0.50
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05
        total = dollars + halves + quarters + nickels
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins < cost:
            print("Insufficient Funds. Money refunded.")
            return False
        change = coins - cost
        print(f"Here is ${change} in change.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Your {sandwich_size} sandwich is ready.")

### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)

    #main loop
running = True
while running:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ")

        #turn off machine
    if choice == "off":
        running = False

        #see machine contents
    elif choice == "report":
        for item, value in machine.machine_resources.items():
            print(f"{item}: {value} slice(s)" if item != "cheese" else f"{item}: {value} ounce(s)")

        #if choice is within one of the recipe options: small, medium, large
    elif choice in recipes:
        sandwich = recipes[choice]
        ingredients = sandwich["ingredients"]
        cost = sandwich["cost"]

        if machine.check_resources(ingredients):
            coins_inserted = machine.process_coins()
            if machine.transaction_result(coins_inserted, cost):
                machine.make_sandwich(choice, ingredients)

    else:
        print("Invalid option. Please try again.")