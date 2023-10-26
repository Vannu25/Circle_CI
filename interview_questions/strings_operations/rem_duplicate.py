# today is Thursday. Thursday is the 4th day of the week
sentence = "Today is Thursday Thursday is the 4th day of the week"

sentence_new = sentence.split()
res_sent = []

# print(set(sentence_new)) - using sets is not feasible as it is unordered

for i in sentence_new:
    if sentence.count(i) >= 1 and (i not in res_sent):
        res_sent.append(i)
print(res_sent)
