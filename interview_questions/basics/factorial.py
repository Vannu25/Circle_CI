import math

n = math.factorial(23)
print(n)


# =====================================

n = int(input('enter the num? '))
fact = 1
for i in range(1, n+1):
    fact = fact*i

print(fact)
