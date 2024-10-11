# function = block of reausable code 
#            place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print("Happy birthday, Happy birthday...")
    print(f"Happy {age} birthday to you!")
    print()

happy_birthday("Culas", 8)
print()

# Example
def display_invoice(username, amount, due_date):
    print(f"Hello {username}!")
    print(f"Your bill of ${amount} is due on {due_date}")

display_invoice("lecsbobik", 538.08, "11/11")
print()

# Return = statement used to end a function 
#          and send a result back to the caller

def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multi(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multi(1, 2))
print(divide(1, 2))
print()

# Another Example
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("lecs", "bobik")

print(full_name)