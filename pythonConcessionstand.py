# Concession stand program

# dictionary {key:value}

menu = {"pizza": 8.75,
        "carbonara": 7.35,
        "chips": 3.85,
        "hamburger": 5.50,
        "fries": 4.00,
        "nachos": 5.00,
        "tea": 3.00,
        "soda": 3.50}

# Empty list for tracking user's cart
cart = []
total = 0

print("------- MENU -------")
for key, value in menu.items():
    print(f"{key:10}.....${value:.2f}")
print("--------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    # Elif will not store the item if 
    # its not in the Menu List
    elif menu.get(food) is not None:
        cart.append(food)
# print(cart)

print("------ YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total: ${total:.2f}")