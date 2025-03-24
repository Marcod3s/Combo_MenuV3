# Amari
# Comp Sci per A V1
# Combo menu V3

import order as o
import item as i

orders = []
sauce_amt = 0

print("Welcome to Goaty's\n------------------")

all_order = False
# sandwich
while not all_order:
    new_order = o.Order("", "", "", "", 0, 0)

    # sandwich
    sandwich_done = False
    while not sandwich_done:
        # shows menu options
        id = 1
        for x in i.sandwiches:
            print(f"{id}:{x}")
            id += 1
        print("What would you like to order today? <3")
        sandwich_type = int(input("Enter a sandwich type (Pick a number):"))

        if sandwich_type == 1:
            new_order.set_sandwich(i.sandwiches[0])
            new_order.add_to_cost(i.sandwiches[0].get_price())
            sandwich_done = True
        elif sandwich_type == 2:
            new_order.set_sandwich(i.sandwiches[1])
            new_order.add_to_cost(i.sandwiches[1].get_price())
            sandwich_done = True
        elif sandwich_type == 3:
            new_order.set_sandwich(i.sandwiches[2])
            new_order.add_to_cost(i.sandwiches[2].get_price())
            sandwich_done = True
        else:
            print("Not a valid choice")

    # drinks
    drink_done = False
    while not drink_done:
        drink_choice = int(input("Would you like a slurp juice?(1 for yes, 2 for no): "))

        if drink_choice == 1:
            id = 1
            for x in i.drinks:
                print(f"{id}:{x}")
                id += 1
            drink_size = int(input("Enter a drink size (Pick a number):"))
            if drink_size == 1:
                new_order.set_drink(i.drinks[0])
                new_order.add_to_cost(i.drinks[0].get_price())
                drink_done = True

            elif drink_size == 2:
                new_order.set_drink(i.drinks[1])
                new_order.add_to_cost(i.drinks[1].get_price())
                drink_done = True

            elif drink_size == 3:
                new_order.set_drink(i.drinks[2])
                new_order.add_to_cost(i.drinks[2].get_price())
                drink_done = True

            else:
                print("Not a valid choice choose sumn else")
        elif drink_choice == 2:
            drink_done = True
        else:
            print("Not a valid choice choose sumn else")

    # sides
    side_done = False
    while not side_done:
        side_dil = int(input("Would you like a side?(1 for yes, 2 for no): "))
        if side_dil == 1:

            print("What side would you like?")
            id = 1
            for x in i.sides[0:3]:
                print(f"{id}:{x}")
                id += 1

            side_choice = int(input("Enter a side choice (Pick a number): "))
            if side_choice == 1:
                new_order.set_side(i.sides[0])
                new_order.add_to_cost(i.sides[0].get_price())
                side_done = True

            elif side_choice == 2:
                new_order.set_side(i.sides[1])
                new_order.add_to_cost(i.sides[1].get_price())
                side_done = True

            elif side_choice == 3:
                new_order.set_side(i.sides[2])
                new_order.add_to_cost(i.sides[2].get_price())
                side_done = True
            else:
                print("Not a valid choice choose sumn else")

        elif side_dil == 2:
            side_done = True
        else:
            print("Not a valid choice, choose sumn else")

        # Sauce
    sauce_done = False

    while not sauce_done:
        sauce_amt = int(input("How much goat sauce would you like? "))
        print(i.sauce)

        if sauce_amt >= 0:
            new_order.set_sauce_amt(sauce_amt)
            new_order.set_sauce(i.sauce)
            new_order.add_to_cost(i.sauce.get_price() * sauce_amt)
        if sauce_amt > 5:
            print("You really love your goat sauce dontcha")
        sauce_done = True

    new_order.set_discount()
    new_order.format_empties()
    orders.append(new_order)

    print(f"\nYou got {len(orders)} order(s)")
    for index, order in enumerate(orders):
        print(f"Order ID: {index + 1}\n {order}")

    # order again func
    order_agn = int(input("Would you like to order again? (1 for yes, 2 for no)"))
    if order_agn == 1:
        all_order = False
        sandwich_done = False
        drink_done = False
        side_done = False
        sauce_done = False
    elif order_agn == 2:
        all_order = True
    else:
        print("Erm make a real choice bud")
print("Thank you for eating at Goaty's\n Enjoy your food and have a good day!")

