# the fibonacci series are 0, 1, 1, 2, 3, 5, 8 and so on
# Python program to generate Fibonacci series based on n value
n = int(input("The num is: "))
a = 0
b = 1
sum_ = a + b
count = 1

while count <= n:
    count += 1
    a = b
    b = sum_
    sum_ = a + b

print("Fibonacci series is: ", end=" ")



"==================================================================================="
n = 9
first = 0  # first value of series
second = 1  # second value of series
series = [first, second]
if n == 0:
    print("The required fibonacci series is", first)
else:
    for i in range(0, n - 2):
        num = series[i] + series[i + 1]
        series.append(num)
print(series, end=" ")
