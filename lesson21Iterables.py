# Iterables = An object/collection that can return its element one at a time 
#             allowing it to be iterated over in a loop

numbers = (1,2,3,4,5)

for number in reversed(numbers):
    print(number)
print()

# Sets cannot be reversed
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)
print()

# Examples
name = "Lexbobic"

for character in name:
    print(character, end=" ")
print()

my_dictionary = {"A":1, "B":2, "C":3}

for key, value in my_dictionary.items():
    print(f"{key} = {value}")
print()