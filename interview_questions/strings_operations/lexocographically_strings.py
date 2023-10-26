# Input:N = 3
# strings = a , ab , abc
# Output: a abc
# Explanation: Lexicographically smallest is "a" and lexicographically largest is "abc".

N = 3
strings = ['a', 'ab', 'abc']

s = min(strings)
s1 = max(strings)

print(s, s1)
