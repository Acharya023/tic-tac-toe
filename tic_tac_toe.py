square = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    player = 1
    status = -1

    while status == -1:
        board()

        if player % 2 == 1:
            player = 1
        else:
            player = 2

        print('\nPlayer', player)
        choice = int(input('Enter a number:'))

        if player == 1:
            mark = 'X'
        else:
            mark = 'O'

        if choice == 1 :
            square[0] = mark
        elif choice == 2:
            square[1] = mark
        elif choice == 3:
            square[2] = mark
        elif choice == 4:
            square[3] = mark
        elif choice == 5:
            square[4] = mark
        elif choice == 6:
            square[5] = mark
        elif choice == 7:
            square[6] = mark
        elif choice == 8:
            square[7] = mark
        elif choice == 9:
            square[8] = mark
        else:
            print('Invalid move ')
            player -= 1

        status = game_status()
        player += 1

    print('RESULT')
    if status == 1:
        print('Player', player - 1, 'win')
    else:
        print('Game draw')


def game_status():
    if square[0] == square[1] and square[1] == square[2]:
        return 1
    elif square[3] == square[4] and square[4] == square[5]:
        return 1
    elif square[6] == square[7] and square[7] == square[8]:
        return 1
    elif square[0] == square[3] and square[3] == square[6]:
        return 1
    elif square[1] == square[4] and square[4] == square[7]:
        return 1
    elif square[2] == square[5] and square[5] == square[8]:
        return 1
    elif square[0] == square[4] and square[4] == square[8]:
        return 1
    elif square[2] == square[4] and square[4] == square[6]:
        return 1
    elif square[0] != 1 and square[1] != 2 and square[2] != 3 and square[3] != 4 and square[4] != 5 and square[
        5] != 6 and square[6] != 7 and square[7] != 8 and square[8] != 9:
        return 0
    else:
        return -1




def board():
    print('\n\n\tTic Tac Toe\n\n')

    print('Player 1 (X)  -  Player 2 (O)')
    print()

    print('     |     |     ')
    print(' ', square[0], ' | ', square[1], ' |  ', square[2])

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ', square[3], ' | ', square[4], ' |  ', square[5])

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ', square[6], ' | ', square[7], ' |  ', square[8])

    print('     |     |     ')


main()