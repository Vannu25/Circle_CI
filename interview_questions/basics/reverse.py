# reverse a number using while loop , as reversed method is only used to reverse a string and not integers.

n = int(input("Enter the Number: "))  # prompt the user to enter the number.
reverse = 0  # initialize the var to 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("The reverse number is : ", reverse)

# How is a Python Dictionary different from List comprehensions?

# list comprehension
list_comp = [i for i in range(5)]
print(list_comp)

# dict

dict1 = {i: i + 2 for i in range(5)}
print(dict1)

# sets are unordered
set1 = (1, 5, 7, 8, 10)
print(set1)


'=========================================================='
# rever a string using while

name = "vanashree"
reverse = ""
count = len(name)
while count > 0:
    reverse += name[count - 1]
    # print(reverse)
    count = count - 1
    # print(count)
print(reverse)


# =======================================================================

first_name = str(input("Enter the 1st name? "))
last_name = str(input("Enter the last name? "))

# reverse1 = first_name[::-1]
# reverse2 = last_name[::-1]

print(last_name + " " + first_name)

