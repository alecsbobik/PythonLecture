# List comprehension = A concise way to create lists in Python 
#                      Compact and easier to read than traditional loops 
#                      [expression for value in iterable if condition]

# Syntax
# variable = [expression for value in iterable if condition]

doubles = [x * 2 for x in range(1,10)]
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]

print(doubles)
print(triples)
print(squares)
print()

# Another example
fruits = ["apple", "orange", "mango", "grapes"]
fruit_chars = [fruit[0] for fruit in fruits]
fruits = [fruit.upper() for fruit in fruits]

# Or you can even cut down one of the steps
# but in this way you can delete your list above

# fruits = [fruit.upper() for fruit in ["apple", "orange", "mango", "grapes"]]

print(fruit_chars)
print(fruits)
print()

# Another sample with IF condition
numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)
print()

# Example
grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)
