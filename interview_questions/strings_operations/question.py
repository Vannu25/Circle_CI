# // Make a public function that acts as "big number library" type of function

# //  the first one should be an "add" function that can take two numbers represented as strings

# // Make a public function that acts as "big number library" type of function

# //  the first one should be an "add" function that can take two numbers represented as strings

# //  and return their result.


# //  if that works, do the same with the multiply function

# //

# //  to make things easier to start with, you can assume positive integers

# //

# //  for example:

# //   "3" + "5"   -> "8"

# //   "105" + "237" -> "342"

# //   "34" + "41236" -> "41270"

# //   "34" + "0"   -> "34"

# //   "111222333333344444455555556666667777788888555444" + "1" ->

# //           "111222333333344444455555556666667777788888555445"

# //   "111222333333344444455555556666667777788888555444" + "100000000000000000000000000000000000000000000000" ->

# //           "211222333333344444455555556666667777788888555444"


def add(num1: str, num2: str):

    result = ""
    for i in num1[::-1] and num2[::-1]:
        result += i


        return result


print(add('105', '237'))

    # 419 - i
    # 327 - j
    # 747 - result

