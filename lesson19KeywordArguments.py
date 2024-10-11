# keyword arguments = an argument preceded by an identifier 
#                     helps with readability 
#                     order of arguments doens't matter 
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", first="Gojo", last="Satoro")

# Another Example
for x in range(1, 11):
    print(x, end=" ")
print()

print("1", "2", "3","4","5", sep="-")
print()

# Exercise
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=63, area=916, first=5404,last=0)

print(phone_num)