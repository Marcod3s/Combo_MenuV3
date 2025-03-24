import item as i


class Order:
    orderid = 0
    total = 0

    def __init__(self, sandwich, drink, side, sauce, sauce_amt, total):
        self.sandwich = sandwich
        self.drink = drink
        self.side = side
        self.sauce = sauce
        self.sauce = sauce_amt
        self.total
        self.orderid = Order.orderid
        Order.orderid += 1

    def __str__(self):
        return f"\n {self.sandwich} \n {self.drink} \n {self.side} \n {self.sauce} x {self.sauce_amt} \n Your total is:$ {self.total}"

    # set sandwich
    def set_sandwich(self, sandwich):
        self.sandwich = sandwich

    # sets drink
    def set_drink(self, drink):
        self.drink = drink

    # sets side
    def set_side(self, side):
        self.side = side

    # sets sauce
    def set_sauce(self, sauce):
        self.sauce = sauce

    # sets sauce amount
    def set_sauce_amt(self, sauce_amt):
        self.sauce_amt = sauce_amt

    # add cost to total
    def add_to_cost(self, amount):
        self.total += amount

    # retrieves total cost
    def get_total_cost(self):
        return self.total

    # makes the empty space if chose no order not exist
    def format_empties(self):
        if self.drink == "":
            self.drink = i.Item("No drink", 0, 0)
        if self.side == "":
            self.side = i.Item("No side", 0, 0)

    # sets discount if order has drink and side
    def set_discount(self):
        if self.drink and self.side:
            self.total -= 1
            print("\n You got a $1 discount")