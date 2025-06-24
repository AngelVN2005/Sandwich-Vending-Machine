from sandwich_makerr import SandwichMachine

def transaction_result(coins, cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if coins < cost:
        print("Insufficient Funds. Money refunded.")
        print("___________________________________________________")
        return False
    change = coins - cost
    print(f"Here is ${change} in change.")
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    dollars = int(input("how many dollar coins?: ")) * 1.00
    halves = int(input("how many half dollar coins?: ")) * 0.50
    quarters = int(input("how many quarters?: ")) * 0.25
    nickels = int(input("how many nickels?: ")) * 0.05
    total = dollars + halves + quarters + nickels
    return total


class cashier(SandwichMachine):

    def __init__(self, coins, cost, machine_resources):
        super().__init__(machine_resources)
        self.coins = coins
        self.cost = cost
