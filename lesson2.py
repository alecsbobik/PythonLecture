# First Activity
print("===Start of First Activity===")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The are is: {area}cm")

# Second Activity
print("\n===Start of Second Activity===")

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} {item}/s")
print(f"Your total is ${total}")