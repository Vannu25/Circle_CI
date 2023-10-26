def palindrome(n):
    try:
        reverse = n[::-1]
        print(reverse)
        if reverse == n:
            print("The string is palindrome")
        else:
            print("Not a palindrome")
    except Exception as e:
        print(e)


palindrome('malayalam')
palindrome('Vanashree')

# ======================================================================

word = str(input("Enter a word to check if it palindrome? "))

rev_word = word[::-1]

if rev_word == word:
    print("it's a palindrome")
else:
    print("Not a palindrome")
