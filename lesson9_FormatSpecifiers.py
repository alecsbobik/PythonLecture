# format specifiers = {value:flags} format a value based on what
#                     flags are insereted

# .(number)f = rount to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before postive numbers
# :, = comma separator

price1 = 3.14519
price2 = -987.65
price3 = 12.34

# Number of decimal places
print(f"Price 1 is ${price1:.3f}")
# print(f"Price 2 is ${price2:.2f}")
# print(f"Price 3 is ${price3:.1f}")

#Allocate space
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:010}")

#Left align
print(f"Price 1 is ${price1:+,.2f}")