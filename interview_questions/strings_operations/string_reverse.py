# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i

s = 'i.like.this.program.very.much'
s1 = s.split('.')
list(s1)
res = s1[::-1]

# print(res)

# =====================================================================================


name = "python code"
rev_name = ""
count = len(name)
while count > 0:
    rev_name = rev_name + name[count - 1]
    count = count - 1

# print(rev_name)


# ========================================================================================

def reverse_string(str):
    new_str = ""
    for i in str:
        new_str = i + new_str
    return new_str


new_str = "python"
print(reverse_string(new_str))
