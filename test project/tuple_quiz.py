aTuple = (100, 200, 300, 400, 500)
# aTuple.pop  tuple does not have an attribute pop
print(aTuple)

aTuple = (100, 200, 300, 400, 500)
# aTuple[1] = 800 - 'tuple' object does not support item assignment
print(aTuple)

# tuple1 = (1120, 'a') - '>' not supported between instances of 'str' and 'int'

aTuple = ("Orange")
print(type(aTuple))

aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
x = aTuple[1][1]
print(x)

aTuple = "Yellow", 20, "Red"
a, b, c = aTuple
print(a)


aTuple = (100,)
print(aTuple * 2)

aTuple = (100, 200, 300, 400, 500)
print(aTuple[-2])
print(aTuple[-4:-1])