# lambda exp - A lambda function is a small anonymous function. OR A lambda function is a type of nameless function
# A lambda function can take any number of arguments, but can only have one expression.

# lambda arguments : expression
# lambda param : action(param)


x = lambda a: a + 10  # a = 5
print(x(5))

my_list = [1, 2, 3]

print(list(map(lambda item: item * 2, my_list)))

sum_ = lambda x, y, z: x + y + z
print("Sum using lambda function is: ", sum_(4, 6, 8))
