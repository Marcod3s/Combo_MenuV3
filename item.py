class Item:

    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def __str__(self):
        return f". {self.name} - ${self.price} - {self.calories} calories"

    def get_price(self):
        return self.price


Item('Goat Sauce', .25, 20, )

# sauce
sauce = Item('Goat Sauce', .25, 20, )

# list of sandwiches
sandwiches = [Item('Chicken Samwitch', 5.25, 670, ), Item('Durr Burger', 6.25, 730, ),
              Item('Tofu Sandwich', 5.25, 350, ), ]

# list of drinks
drinks = [Item("Chug Jug", 2.50, 250), Item("Big Pot", 1.75, 150), Item("Minis", 1, 100), ]

# list of sides
sides = [Item('Cheesy fries', 2, 300, ), Item('Chili Dog', 3, 175, ), Item("Zorian Gobnites", 4, 200),
         Item("Zorian Gobnites with Trunker Glaze", 6, 300), Item("Zorian Gobnites without Trunker Glaze", 4, 200), ]

