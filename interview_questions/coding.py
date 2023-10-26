def fizzBuzz(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
            continue
        elif i % 3 == 0:
            print('Fizz')
            continue
        elif i % 5 == 0:
            print('Buzz')
            break


fizzBuzz(15)
fizzBuzz(18)
fizzBuzz(7)
