# This is about Variables
#Strings
print("===Start of Strings===")
first_name = "Alex"
food = "Pizza"
email = "alex00@gmail.com"

print(f"Hello {first_name}")
print(f"You love {food}")
print(f"Your email is {email}\n")

#Integers
print("===Start of Integers===")
age = 22
quantity = 6
num_of_students = 50
year = 2024

print(f"You are {age} years old")
print(f"You are buying {quantity} different flavors of ice cream")
print(f"You are one of the {num_of_students} students in the class {year}\n")

#Float
print("===Start of Float===")
price = 9.99
gpa = 1.0
distance = 5.1

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"Your usual running distance is {distance}km\n")

#Boolean
print("===Start of Boolean===")
is_student = True
for_sale = False
is_online = True

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

if is_online:
    print("You are online")
else:
    print("You are offline")

print("\n")

#Assignment
print("===Start of First Assignment===")
user_name = "Bro Code"
year = 2024
pi = 3.14
is_admin = True

if is_admin:
    print(f"Welcome Admin {user_name}")
else:
    print("Only authorize personnel here")

print(f"Copyright {year}")
print(f"In pi I only know the 2 decimals {pi}\n")

#Typecasting
print("===Start of Typecasting===")
your_name = "Alex"
your_age = 22
your_gpa = 1.25
# is_student = True is already declared above

new_gpa = int(gpa)
print(new_gpa)

new_age = str(your_age)
new_age += "1"

print(type(new_age))
print(new_age)

new_name = bool(your_name)
print(new_name)

#Input
print("\n===Start of Input===")

name = input("What is your name? :")
age = int(input("How old are you? :"))

# Age above is stored as String 
# so we need to typecast it into Integer
#age = int(age)
# Rather than this line we can enclose
# the input age into int()

age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old\n")