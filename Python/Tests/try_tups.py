#This is an excercise in writing over tuples:

menu_items = ("Lasagne", "Schnitzel", "Burger", "Salad", "Fried Rice")

print(menu_items)

for menu_item in menu_items:
    print(f"On our menu we have {menu_item}")

#menu_items[0] = "Bread Rolls"

print("Original Menu Items:")
for menu_item in menu_items:
    print(menu_item)

menu_items = ("Lasagne", "Schnitzel", "Burger", "Salad", "Bread Rolls")
print("\nNew Menu Items:")
for menu_item in menu_items:
    print(menu_item)
