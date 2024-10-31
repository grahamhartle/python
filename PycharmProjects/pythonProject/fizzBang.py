"""
This program creates a number range from 1 to 99.
If the number divides by 3 it prints 'bang'
If the number divides by 5 it prints 'fizz'
If the number divides by 3 & 5 it prints 'fizz bang'
"""

for num in range(1, 100):
    if num % 5 == 0 and num % 3 == 0:
        print(str(num) + " Fizz Bang!")
    elif num % 5 == 0:
        print(str(num) + " Fizz")
    else:
        if num % 3 == 0:
            print(str(num) + " Bang")
            