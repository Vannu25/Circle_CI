def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


print(is_prime(6))
'========================================================================================='
n = int(input("Num is :"))

if n <= 1:
    print("Not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("The given number is a composite number")
            break
        if i == n - 1:
            print("The given number is a prime number")


