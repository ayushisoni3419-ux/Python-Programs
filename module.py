# ================================
# MODULES PRACTICE IN PYTHON
# Author: Ayushi Soni
# Topics: import, from...import, math, random
# ================================

# -------------------------------
# import math
# -------------------------------
import math

print("----- MATH MODULE -----")

print("Square Root of 144:", math.sqrt(144))
print("Factorial of 6:", math.factorial(6))
print("2 raised to 5:", math.pow(2, 5))
print("Value of PI:", math.pi)
print("Ceil of 6.2:", math.ceil(6.2))
print("Floor of 6.8:", math.floor(6.8))
print("GCD of 54 and 24:", math.gcd(54, 24))

print()

# -------------------------------
# from...import
# -------------------------------
from math import sqrt, factorial

print("----- FROM...IMPORT -----")

print("Square Root of 49:", sqrt(49))
print("Factorial of 5:", factorial(5))

print()

# -------------------------------
# random module
# -------------------------------
import random

print("----- RANDOM MODULE -----")

# Random integer
print("Random Integer (1-10):", random.randint(1, 10))

# Random decimal
print("Random Decimal:", random.random())

# Random float
print("Random Float (1-5):", random.uniform(1, 5))

# Random choice
colors = ["Red", "Blue", "Green", "Yellow"]
print("Random Color:", random.choice(colors))

# Random range
print("Random Number using randrange:", random.randrange(1, 10))

print()

# -------------------------------
# shuffle()
# -------------------------------
print("----- SHUFFLE LIST -----")

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

random.shuffle(numbers)

print("Shuffled List:", numbers)