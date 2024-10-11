# While Loop

# name =  input("Enter your name: ")
# age = int(input("Enter your age: "))
# food = input("Enter the food you like (q to quit): ")
num = int(input("Enter a number between 1-10: "))


# while name == "":
#     print("You did not enter your name\n")
#     name =  input("Enter your name: ")

# print(f"Hello {name}")

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")
# print("bye")

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1-10: "))
print(f"Your number is {num}")
