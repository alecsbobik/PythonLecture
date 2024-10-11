# indexing = accessing elements of a sequence using [] (indexing operator) 
#            [star : end : step]

credit_number = "1234-5678-9012-3456"

# To reverse the string, make the STEP negative
credit_number = credit_number[::-1]

last_digits = credit_number[-4:]

print(credit_number)
print(f"XXXX-XXXX-XXXX-{last_digits}")

# Start
# print(credit_number[0])

# Start : End
# print(credit_number[0:4])
# print(credit_number[5:9])
# print(credit_number[5:])

# print(credit_number[-1])

# Step
# print(credit_number[::3])

