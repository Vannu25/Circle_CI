# Given a string. Count the number of CamelCase characters in it

letters = "ckjkUUYII"

# Camel Case characters present: U, U, Y, I and I.

new_letters1 = []

for i in letters:
    if 'A' < i < 'Z':
        new_letters1.append(i)
print(new_letters1)

# ==============================================================================
new_letters2 = ""
for i in letters:
    if 'A' < i < 'Z':
        new_letters2 += i
print(new_letters2)

'==============================================================================='


def camelcase(n):
    return [i for i in n if i.isupper()]


print(camelcase("ckjkUUYII"))
