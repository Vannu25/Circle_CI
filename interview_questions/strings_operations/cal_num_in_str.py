# Calculate sum of all numbers present in a string.
# Input : s = "Geeks123ks45"
# Output : 168


s = "Geeks123ks45"
ls = '0'
sum = 0

for i in s:
    if i.isdigit():
        ls += i
    else:
        sum += int(ls)
        ls = '0'
print(sum + int(ls))

