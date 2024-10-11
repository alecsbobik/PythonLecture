# dictionary = a collection of {key:value} pairs 
#              ordered and changeable. No  duplicates

capitals = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# You can insert new key:value pair
# using update
# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

keys = capitals.keys()

# print(keys)

# Getting the keys
for key in capitals.keys():
    print(key)
print()

# Getting the values
values = capitals.values()
# print(values)
for value in capitals.values():
    print(value)
print()

# Getting the item
# items =  capitals.items()

# Getting every key and value
for key, value in capitals.items():
    print(f"{key}: {value}")