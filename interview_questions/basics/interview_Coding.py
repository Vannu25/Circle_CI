# In Python, in what ways can you make an empty NumPy array?
import numpy
import random

# method 1
array_1 = numpy.array([])
print(array_1)

# method 2
array_2 = numpy.empty(shape=(3, 3))
print(array_2)

a = [4, 6, 8, 3, 1, 7]
print(a[-3])
print(a[-5])
print(a[-1])

# How do you print the summation of all the numbers from 1 to 101?
print(sum(range(1, 102)))

# Python program that calculates the mean of numbers in a list?


n = int(input("enter the num: "))
l = []
for i in range(1, n + 1):
    ele = int(input("the element in a list: "))
    l.append(ele)
avg = sum(l) / n
print("the avg mean of numbers are : ", round(avg, 2))

# lambda function: nameless and acn take as many parameters/arguments but returns with only one expression /statement

sum_ = lambda x, y, z: x + y + z
print("Sum using lambda function is: ", sum_(4, 6, 8))

# Python program to show to randomise elements of a list

# Importing the random module


list_ = ["Python", "Interview", "Questions", "Randomise", "List"]
print("Original list: ", list_)
random.shuffle(list_)
print("After randomising the list: ", list_)

'============================================================================='

array = numpy.array([3, 6, 1, 6, 5, 2])
percentile = numpy.percentile(array, 45)  # Returns 45th percentile
print(percentile)
