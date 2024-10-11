# Collection = single "variable" used to store multiple values
# List  = [] ordered and changeble. Duplicates OK
# Set   = {} unordered and immutable, but Add/Removes OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# List
# fruits = ["apple", "orange", "banana", "coconut"]
# print("pineapple" in fruits)

# fruits[1] = "pineapple"
# fruits.append("pineapple")
# for fruit in fruits:
#     print(fruit)
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("banana"))
# print(fruits.count("banana"))

# print(fruits)
# print(fruits[::-1])
# for fruit in fruits:
#     print(fruit)

# Set
# fruits = {"apple", "orange", "banana", "coconut", "coconut"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()

# print(fruits)

# Tuple
colors = ("red", "green", "blue", "white", "grey", "white")
# print(dir(colors))
# print(help(colors))
# print(len(colors))
# print("pink" in colors)

# print(colors.index("red"))
# print(colors.count("white"))

for color in colors:
    print(color)  

# print(colors)