from random import choice

word = choice(["rainbows",
               "keyboard",
               "hungriest",
               "sausage",
               "television",
               "grandparents",
               "weather",
               "mountainous",
               "carefully",
               "realistic",
               "linguistics",
               "remember",
               "telephone",
               "antarctica",
               "scrambling",
               "extremely",
               "worrisome",
               "superbly",
               "fantastic",
               "overwhelming",
               "ostrich"])
wlist = list(word)

guessed = []
state = "_" * len(wlist)
lives = 10

print("\n\n     H A N G M A N\n")
while True:
    print("\n" + state + "     Guesses: " + ' '.join(guessed))
    letter = input("Guess a letter: ")
    if letter in guessed:
        print("Letter already guessed.")
    elif letter in wlist:
        guessed += letter
        state = list(state)
        for r in range(len(wlist)):
            if wlist[r] == letter:
                state[r] = letter
        if '_' not in state:
            print(''.join(state))
            print("You win!")
            break
        state = ''.join(state)
    else:
        lives -= 1
        print("Incorrect! You have " + str(lives) + " lives remaining.")
        guessed += letter
        if lives <= 0:
            print("You lose. The word was " + word)
            break
