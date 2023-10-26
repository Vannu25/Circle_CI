string = "geeks quiz practice code"

s = string.split()[::-1]
l = []
for i in s:
    # appending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))
