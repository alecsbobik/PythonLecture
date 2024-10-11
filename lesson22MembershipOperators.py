# Membership operators = used to test whether a value  or variable is found in a sequence 
#                        (string, list, tuple, set, or dectionary) 
#                        1. in
#                        2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

# in or not in either of the two can use 
# as long as the if statement is true
# according to your preferred membership operator
if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")
print()

# Example for Set
students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found.")
print()

# Example in Dictionary
grades = {"Sandy":"A",
          "Squiward":"B",
          "Spongebob":"C",
          "Patrick":"D"}

student2 = input("Enter the name of a student: ")

if student2 in grades:
    print(f"{student2}'s grade is {grades[student2]}")
else:
    print(f"{student2} was not found.")
print()

# Another example with 2 conditions 
email = "Lecsbobic@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")