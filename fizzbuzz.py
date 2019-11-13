for i in range(1, 101):
    if i % 15 == 0:
        print(str(i) + " " * (4 - len(str(i))) + "FizzBuzz")
    elif i % 3 == 0:
        print(str(i) + " " * (4 - len(str(i))) + "Fizz")
    elif i % 5 == 0:
        print(str(i) + " " * (4 - len(str(i))) + "    Buzz")
    else:
        print(str(i))
