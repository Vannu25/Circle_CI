def find_duplicate_char(str1):
    return set([i for i in str1 if str1.count(i) > 1])


# string = 'abcdab'
string = "vanashree"
print(find_duplicate_char(string))

# ============================================================

my_string = "Python-Interpreter"

max_frequency = {}
for i in my_string:
    if i in max_frequency:
        max_frequency[i] += 1
    else:
        max_frequency[i] = 1
my_result = max(max_frequency, key=max_frequency.get)

print("The maximum of all characters is : ")
print(my_result)
