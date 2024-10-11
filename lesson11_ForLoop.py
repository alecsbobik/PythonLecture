# for loops = execute a block of code a fixed number of times
#             You can iterate over a range, string, sequence, etc.

# Range
# to count backwards enclose the function into reversed() function
# if you want to count with step, just add another parameter
# for x in range(1,11,2):
#     print(x)

# print("HAPPY NEW YEAR!")

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# To skip any iteration, you can use continue
# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)

# To break any iteration, you can use break
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)