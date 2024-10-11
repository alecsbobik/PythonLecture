# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to signed up!\n")
elif age >= 18:
    print("You are now signed up!\n")
elif age < 0:
    print("You haven't been born yet!\n")
else:
    print("You must be 18+ to sign up\n")

# second example
response = input("Would you like food? (Y/N): ")

if response == "Y" :
    print("Have some food!\n")
else:
    print("No food for you!\n")

# third example
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name\n")
else:
    print(f"Hello {name}!\n")

# forth example
for_sale = True

if for_sale:
    print("This item is for sale\n")
else:
    print("This item is not for sale\n")

online = False

if online:
    print("The user is online\n")
else:
    print("The user is offline\n")
