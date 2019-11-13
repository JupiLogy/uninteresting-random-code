import random as r

i = 0
w = 0
while True:
    i += 1
    n = r.randrange(1, 10)
    x = int(input("\n\nGuess the number!"))
    if x < n:
        print("Too low.")
    elif x > n:
        print("Too high.")
    else:
        w += 1
        print("Exactly right!")
    cont = input("\nContinue playing?")
    if cont == 'no' or cont == 'n' or cont == "N" or cont == "No":
        break
print("You won " + str(w) + " out of " + str(i) + " times!")
