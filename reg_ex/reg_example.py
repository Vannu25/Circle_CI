import re

# regular expression is useful in complex string to search patterns

pattern = re.compile('this')  # can be used multiple times
string = "search this inside th ce text please!"

a = re.search('this', string)
b = pattern.search(string)
print(b)
print(a.group())
print(a.end())
