dict = {key: number for key, number in zip(['rock', 'paper', 'scissors'], range(3))}

while True:
    a = input("Player 1's move: ")
    b = input("Player 2's move: ")

    a = int(dict.get(a))
    b = int(dict.get(b))

    if a == b:
        print('Draw!')
    elif (a - b) % 3 == 1:
        print('Winner is Player 1!')
    else:
        print('Winner is Player 2!')

    if input('Do you want to play again? ') == 'no':
        break
