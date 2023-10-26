import datetime
import sys
import datetime
from math import pi

# python program to print the python version
ver = sys.version
print(ver)

# Write a Python program to display the current date and time.

curr_dt = datetime.datetime.now()
print(curr_dt)

# area pf circle

r = 1.1
# pi = 3.14159265359
area_of_circle = pi * r ** 2
print(area_of_circle)

# first_name = str(input("Enter the first name: "))
# last_name = str(input("Enter the last name: "))
first_name = 'vanu'
last_name = "bandla"

x = first_name[::-1]
y = last_name[::-1]

print(f"hello {last_name} {first_name}")
print(f"{x} {y}")


values = input("Input some comma separated numbers : ")
list1 = values.split(",")
tuple1 = tuple(list1)
print('List : ', list1)
print('Tuple : ', tuple1)
