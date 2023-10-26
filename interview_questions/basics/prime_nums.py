n = int(input('Enter the number? '))

if n > 1:
    for i in range(2, int(n / 2)+1):
        if (n % i) == 0:
            print(n, "number is not a prime number")
            break
        else:
            print(n, 'number is prime number')
            break
else:
    print(n, 'Number is not a prime number')
