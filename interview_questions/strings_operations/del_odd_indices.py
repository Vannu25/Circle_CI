# Input: S = "Geeks"
# Output: "Ges"
# Explanation: Deleted "e" at index 1 and "k" at index 3

s = "Geeks"
# output = ''

s1 = list(s)

output = s1[0:5:2]
print(output)


# ==========================================================================

def delAlternate(S):
    st = ''
    for i in range(len(S)):
        if i % 2 == 0:
            st += S[i]
    return st


S = "Geeks"
print(delAlternate(S))

# =============================================================

S = "Geeks"
st1 = ''
for i in range(len(S)):
    if i % 2 == 0:
        st1 += S[i]

print(st1)
