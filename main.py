import mymath
import string_operations
import random
import datetime
import math
import random
import os

# Program 1
print("Addition =", mymath.add(10, 5))
print("Subtraction =", mymath.subtract(10, 5))

# Program 2
text = "Hello World"

print("Reversed string =", string_operations.reverse_string(text))
print("Number of vowels =", string_operations.count_vowels(text))

# Program 3: Generate 5 random integers

print("5 Random integers:")

for i in range(5):
    print(random.randint(1, 100))

    # Program 4: Display current date and time

current_datetime = datetime.datetime.now()

print("Current date and time =", current_datetime)
# Program 5: Find factorial using math module

n = int(input("Enter a number: "))

print("Factorial =", math.factorial(n))
# Program 6: Shapes package

from shapes import circle
from shapes import rectangle

radius = 5
length = 10
width = 5

print("Circle area =", circle.area(radius))
print("Circle circumference =", circle.circumference(radius))

print("Rectangle area =", rectangle.area(length, width))
print("Rectangle perimeter =", rectangle.perimeter(length, width))

# Program 7: Import multiple functions from one module

from mymath import add, subtract

print("Addition using imported function =", add(20, 10))
print("Subtraction using imported function =", subtract(20, 10))

# Program 8: Shuffle a list using random module

numbers = [1, 2, 3, 4, 5]

print("Original list =", numbers)

random.shuffle(numbers)

print("Shuffled list =", numbers)

# Program 9: Difference between two dates

from datetime import date

date1 = date(2026, 1, 1)
date2 = date(2026, 12, 31)

difference = date2 - date1

print("Difference between dates =", difference.days, "days")

# Program 10: List files in a directory

files = os.listdir(".")

print("Files and folders:")

for file in files:
    print(file)