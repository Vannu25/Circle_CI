name = 'desserts'
i = name[::-1]
print(i)

name = "desserts"
reverse_name = ""
count = len(name)
# print(count)
while count > 0:
    reverse_name += name[count - 1]
    count = count-1

print(reverse_name)


