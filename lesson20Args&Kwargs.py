# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows yout to pass multiple keyword-arguments
#             * unpacking operator
#             1.positional, 2. default, 3. keyword, 4. ARBITRARY

# *args 
def add(*nums):
    # print(type(args))
    # args is a tuple type
    total = 0
    for num in nums:
        total += num
    return total

print(add(1,2,3,4))
print()

# another sample of *args
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("1C","Yuji", "A", "Itadori")
print()

# **kwargs
def print_address(**kwargs):
    # print(type(kwargs))
    # kwargs is dict type
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print()

print_address(street="382 Col S Cruz St.",
               city="Montalban",
               province="Rizal", 
               state="Philippines", 
               zip="1860")


# args & kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    # for value in kwargs.values():
    #     print(value, end=" ") 

    if "apt" in kwargs:
        # if there's an apt key in kwargs
        # then print this line
        print(f"{kwargs.get("street")} {kwargs.get("apt")}")  
    elif "pobox" in kwargs:
        print(f"{kwargs.get("street")}")
        print(f"{kwargs.get("pobox")}")
    else: 
        print(f"{kwargs.get("street")}")

    print(f"{kwargs.get("city")}")
    print(f"{kwargs.get("province")}")    
    print(f"{kwargs.get("state")}")   
    print(f"{kwargs.get("zip")}")

shipping_label("1C","Yuji", "A", "Itadori",
            #    apt="#304 CSC Bldg.",
               pobox = "PO box #1001",
               street="382 Col S Cruz St.",
               city="Montalban",
               province="Rizal", 
               state="Philippines", 
               zip="1860")