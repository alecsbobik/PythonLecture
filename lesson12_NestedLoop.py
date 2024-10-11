# nested loop = a loop within another loop (outer, inner)
#               outer loop:
#                   inner loop: 

# outer loop repeats the inner loop
# for x in range(3):
#     for y in range(1, 10):
#         # the output would print in 1 line
#         print(y, end="") 
#     print()

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()