row = int(input("enter the num of rows: "))
for i in range(1, row + 1):
    # print(i)
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(1, n - 1 + 1):
        print(end=" ")
    for j in range(1, 2 * i):
        print("*", end="")
    print("")
