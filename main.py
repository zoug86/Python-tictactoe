#### TIC-TAC-TOE PROJECT ######
# Done in December 15 2020

#1- Return the players names:

def player():
    print("Player 1")
    p1 = input("Enter the name: ")
    print()
    print("Player 2")
    p2 = input("Enter the name: ")
    return [p1, p2]


#2- Set the score board to keep track of losses/wins

def scoreboard(name1, name2, score1, score2):
    print()
    print("        ----------------------------")
    print("                 SCOREBOARD         ")
    print("        ----------------------------")
    print("          ", name1, "      ", score1)
    print("          ", name2, "       ", score2)
    print("        ----------------------------")


#3- Create a Tic Tac Toe board and fill it with dashes.

def print_board(board):
    print(board[1], board[2], board[3], sep="")
    print(board[4], board[5], board[6], sep="")
    print(board[7], board[8], board[9], sep="")
    print(board[10], board[11], board[12], sep="")
    print(board[13], board[14], board[15], sep="")
    print(board[16], board[17], board[18], sep="")
    print(board[19], board[20], board[21], sep="")
    print(board[22], board[23], board[24], sep="")
    print(board[25], board[26], board[27], sep="")
    print()


#4- Print an empty board to the screen at the beginning of each game:

def empty_board():
    print()
    board = {1: "             |", 2: "     |", 3: "     ", 4: "             |",
         5: "     |", 6: "     ", 7: "        _____|", 8: "_____|", 9: "_____",
         10: "             |", 11: "     |", 12: "     ", 13: "             |",
         14: "     |", 15: "     ", 16: "        _____|", 17: "_____|", 18: "_____",
         19: "             |", 20: "     |", 21: "     ", 22: "             |",
         23: "     |", 24: "     ", 25: "             |", 26: "     |", 27: "     "}

    print_board(board)

    return board

#5- Update and print out the new board version:

def update_board(d):
    print()

    print_board(d)


#6- Specify where each new symbol should go in the board:

def insert_symbol(d, symbol):
    if box == 1:
        d[4] = "          " + symbol + "  |"
    if box == 2:
        d[5] = "  " + symbol + "  |"
    if box == 3:
        d[6] = "  " + symbol + "  "
    if box == 4:
        d[13] = "          " + symbol + "  |"
    if box == 5:
        d[14] = "  " + symbol + "  |"
    if box == 6:
        d[15] = "  " + symbol + "  "
    if box == 7:
        d[22] = "          " + symbol + "  |"
    if box == 8:
        d[23] = "  " + symbol + "  |"
    if box == 9:
        d[24] = "  " + symbol + "  "

    return d


#7- Make a list of choices for the player:

def choice(name):
    print()
    print(name,", make a choice:", sep="")
    print("-Enter 1 for X")
    print("-Enter 2 for O")
    print("-Enter 3 to quit")

    choice = int(input("Choice: "))

    return choice


#8- Decide which player is winning:

def pre_check(num, box_holder, score1, score2, name1, name2, game_count, pick):
    temp = game_count
    symbols = {1: 'X', 2: 'O'}
    if box_holder[num] == symbols[pick]:
        print(pick)
        print(name1, "wins!")
        score1 += 1
        temp = 10
    else:
        print(pick)
        print(name2, "wins!")
        score2 += 1
        temp = 10
    game_count = temp
    return [game_count, score1, score2]


#9- Check winning scenarios:

def check(name1, name2, score1, score2, box_holder, pick, game_count):

    if box_holder[1] == box_holder[2] and box_holder[1] == box_holder[3] and box_holder[1] != '':
        [game_count, score1, score2] = pre_check(1, box_holder, score1, score2, name1, name2, game_count, pick)
    if box_holder[4] == box_holder[5] and box_holder[4] == box_holder[6] and box_holder[4] != '':
        [game_count, score1, score2] = pre_check(4, box_holder, score1, score2, name1, name2, game_count, pick)
    if box_holder[7] == box_holder[8] and box_holder[9] == box_holder[9] and box_holder[7] != '':
        [game_count, score1, score2] = pre_check(7, box_holder, score1, score2, name1, name2, game_count, pick)
    if box_holder[1] == box_holder[4] and box_holder[1] == box_holder[7] and box_holder[1] != '':
        [game_count, score1, score2] = pre_check(1, box_holder, score1, score2, name1, name2, game_count, pick)
    if box_holder[2] == box_holder[5] and box_holder[2] == box_holder[8] and box_holder[2] != '':
        [game_count, score1, score2] = pre_check(2, box_holder, score1, score2, name1, name2, game_count, pick)
    if box_holder[3] == box_holder[6] and box_holder[3] == box_holder[9] and box_holder[3] != '':
        [game_count, score1, score2] = pre_check(3, box_holder, score1, score2, name1, name2, game_count, pick)
    if box_holder[3] == box_holder[5] and box_holder[3] == box_holder[7] and box_holder[3] != '':
        [game_count, score1, score2] = pre_check(3, box_holder, score1, score2, name1, name2, game_count, pick)
    if box_holder[1] == box_holder[5] and box_holder[1] == box_holder[9] and box_holder[1] != '':
        [game_count, score1, score2] = pre_check(1, box_holder, score1, score2, name1, name2, game_count, pick)

    if game_count == 9 and score1 == 0 and score2 == 0:
        print("It is a draw!")
    return [game_count, score1, score2]

# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    game = True
    score1 = 0
    score2 = 0

    [name1, name2] = player()
    scoreboard(name1, name2, 0, 0)

    while game:
        game_count = 0
        symbols = {1: 'X', 2: 'O'}
        box_holder = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        pick = choice(name1)
        if pick == 3:
            break
        symbol1 = symbols[pick]
        del symbols[pick]
        symbol2 = list(symbols.values())[0]
        print(name1, "has chosen:", symbol1)
        print(name2, "is:", symbol2)
        while game_count < 10:

            if game_count == 0:
                board = empty_board()
            else:
                if game_count % 2 == 1:
                    print(name1, ", it is your turn!")
                    box = int(input("Choose a box 1-9: "))
                    box_holder[box] = symbol1
                    new_board = insert_symbol(board, symbol1)
                    update_board(new_board)
                else:
                    print(name2, ", it is your turn!")
                    box = int(input("Choose a box 1-9: "))
                    box_holder[box] = symbol2
                    new_board = insert_symbol(board, symbol2)
                    update_board(new_board)
            [game_count, score1, score2] = check(name1, name2, score1, score2, box_holder, pick, game_count)
            game_count += 1

        print("Final result: ")
        scoreboard(name1, name2, score1, score2)

        print("Play Again? Type 'Y' to continue or 'N' to exit: ")
        decision = input()
        if decision == 'N':
            game = False
