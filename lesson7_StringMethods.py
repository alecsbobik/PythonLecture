# String Methods
# You can use the below code to see other string methods
# print(help(str))

# name = input("Enter your full name: ")
phone_number = input("Enter your phone #: ")

# result = name.find("e") 

# first occurence
# result = len(name)

# last occurence
# result = name.rfind("e") 

# Capitalize
# name = name.capitalize()

# Uppercase
# name = name.upper()

# Lower
# name = name.lower()

# Boolean checks if the entered chars is digit
# result = name.isdigit()

# Boolean checks if the entered chars is alphabet/letters
# Note: Space is not in alphabet
# result = name.isalpha()

# Count Method
# result = phone_number.count("-")

#Replace Method
result = phone_number.replace("-", "")

print(result)