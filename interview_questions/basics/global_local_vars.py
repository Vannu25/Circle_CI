# Python program to show how global variables and local variables are different
import sys
var = 56


# Creating a function
def addition():
    var1 = 7
    c = var + var1
    print("In local scope: ", var1)
    print("Adding a global scope and a local scope variable: ", c)
    # print("In global scope: ", var)


addition()
print("In global scope: ", var)


# When a new object/instance of a class is created, this function is automatically called to reserve memory.
# The __init__ method is available in all classes.
# Python program to explain __init__

class Student:
    def __init__(self, st_name, st_class, st_marks):
        self.st_name = st_name
        self.st_class = st_class
        self.st_marks = 67


S1 = Student("Ivika", 10, 67)
print(S1.st_name)
print(S1.st_class)

# program to print the python version
version = sys.version
print(version)



