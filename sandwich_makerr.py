class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input."""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                print("Insufficient ingredient")
                print("___________________________________________________")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Your {sandwich_size} sandwich is ready.")
        print("___________________________________________________")