test_list1 = ['a', 'b', 'c']
test_list2 = [5, 7, 3, 0, 1, 8, 4]

ls = []
while len(test_list2) > len(test_list1):
    for i in test_list1:
        ls.append(i)
        for j in test_list2:
            ls.append(j)
            test_list2.remove(j)
            break
print(ls)
