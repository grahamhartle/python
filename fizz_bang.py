for num in range(1, 100):
    if num % 5 == 0 and num % 3 == 0:
        print(str(num) + " Fizz Bang!")
    elif num % 5 == 0:
        print(str(num) + " Fizz")
    else:
        if num % 3 == 0:
            print(str(num) + " Bang")
