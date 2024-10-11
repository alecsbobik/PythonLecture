import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K", "A"]

# set the range of the number inside randint()
number = random.randint(low, high)

# random floating point
# number = random.random()

# choice is a great use for games
# if you need a random element
option = random.choice(options)
print(option)

# Shuffle
random.shuffle(cards)
print(cards)