print("Welcome to The Lotus Hotel!")

Menu = {
    "Pizza" : 200,
    "Burger" : 70,
    "White Sauce Pasta": 350,
    "Red Sauce Pasta": 400,
    "Kurkure Momo's" : 280,
    "Classic Salad" : 360,
    "Bisleri Water" : 70
}

print("Pizza : ₹200\n", "Burger : ₹70\n", "White Sauce Pasta : ₹350\n", 
      "Red Sauce Pasta : ₹400\n", "Kurkure Momo's : ₹280\n", 
      "Classic Salad : ₹360\n", "Bisleri Water : ₹70\n")

order_total = 0

item = input("Enter the item you want to order: ")
if item in Menu:
    order_total += Menu[item]
    print(f"{item} added to your order")
else:
    print("This item is not available in menu")

another_order = input("Do you want to add another item ? (Yes/No): ")
if another_order.lower() == "yes":
    item2 = input("Enter the name of second item: ")
    if item2 in Menu:
        order_total += Menu[item2]
        print(f"{item2} is added to your order")
    else:
        print("This item is not available in menu")

print(f"The Total Amount of items: ₹{order_total}")
