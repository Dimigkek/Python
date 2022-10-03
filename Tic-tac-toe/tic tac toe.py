from random import *


def check_row_p1(row):
    return spots[row][0] == player_1 and spots[row][1] == player_1 and spots[row][2] == player_1


def check_row_p2(row):
    return spots[row][0] == player_2 and spots[row][1] == player_2 and spots[row][2] == player_2


def check_colm_p1(clm):
    return spots[0][clm] == player_1 and spots[1][clm] == player_1 and spots[2][clm] == player_1


def check_colm_p2(clm):
    return spots[0][clm] == player_2 and spots[1][clm] == player_2 and spots[2][clm] == player_2


def check_diag_p1():
    return (spots[0][0] == player_1 and spots[1][1] == player_1 and spots[2][2] == player_1) or (spots[0][2] == player_1 and spots[1][1] == player_1 and spots[2][0] == player_1)


def check_diag_p2():
    return (spots[0][0] == player_2 and spots[1][1] == player_2 and spots[2][2] == player_2) or (spots[0][2] == player_2 and spots[1][1] == player_2 and spots[2][0] == player_2)


counter = 0
game_active = True
computer_pick = randrange(2)
spots = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("For Player vs Computer press 0.")
print("For Player vs Player press 1.")
pc = int(input())
while pc != 1 and pc != 0:
    pc = input("1 or 0!\n")
if pc == 1:
    print("Player 1 : ")
    user_pick = input("Pick x or o!\n")
    while user_pick != "x" and user_pick != "o":
        user_pick = input("Pick x or o!\n")

    if user_pick == "x":
        player_1 = "x"
        player_2 = "o"
    else:
        player_1 = "o"
        player_2 = "x"

    x = int(input("pick row "))
    while x > 2 or x < 0:
        x = int(input("pick row "))

    y = int(input("pick column "))
    while y > 2 or y < 0:
        y = int(input("pick column "))

    while spots[x][y] != " ":
        print(x, y)
    spots[x][y] = player_1

    for q in range(3):
        for _ in range(3):
            print("+---", end="")
        print("+")
        for f in range(3):
            print(str("| " + spots[q][f]), end=" ")
        print("|")
    for _ in range(3):
        print("+---", end="")
    print("+")

    while game_active == True:
        if counter == 8 or counter == 9:
            game_active = False
            if counter == 8:
                print("Draw")

            jow = input("Wanna play again? \n")

            while jow != "Yes" and jow != "No" and jow != "yes" and jow != "no":
                jow = input("Please choose between Yes or No \n")
            if jow == "Yes":
                game_active = True
                spots = [
                    [" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "]
                ]
                user_pick = input("Pick x or o!\n")
                while user_pick != "x" and user_pick != "y":
                    user_pick = input("Pick x or o!\n")
            else:
                break

        computer_pick = randrange(1)
        if counter % 2 == 0:
            user_pick = player_2
            print("Player 2 : ")
        else:
            user_pick = player_1
            print("Player 1 : ")

        x = int(input("pick row "))
        while x > 2 or x < 0:
            x = int(input("pick row "))

        y = int(input("picks column "))
        while y > 2 or y < 0:
            y = int(input("pick column "))
        while spots[x][y] != " ":
            print("That spot is taken!")
            x = int(input("pick row "))
            while x > 2 or x < 0:
                x = int(input("pick row "))

            y = int(input("picks column "))
            while y > 2 or y < 0:
                y = int(input("pick column "))

        spots[x][y] = user_pick

        for q in range(3):
            for _ in range(3):
                print("+---", end="")
            print("+")
            for f in range(3):
                print(str("| " + spots[q][f]), end=" ")
            print("|")
        for _ in range(3):
            print("+---", end="")
        print("+")
        counter += 1
        for v in range(3):
            if check_row_p1(v):
                print("Player 1 Wins !!!")
                counter = 9
            elif check_colm_p1(v):
                print("Player 1 Wins !!!")
                counter = 9
            elif check_diag_p1():
                print("Player 1 Wins !!!")
                counter = 9
                break
            elif check_row_p2(v):
                print("Player 2 Wins !!!")
                counter = 9
            elif check_colm_p2(v):
                print("Player 2 Wins !!!")
                counter = 9
            elif check_diag_p2():
                print("Player 2 Wins !!!")
                counter = 9
                break
else:
    print("Player 1 : ")
    user_pick = input("Pick x or o!\n")
    while user_pick != "x" and user_pick != "o":
        user_pick = input("Pick x or o!\n")

    if user_pick == "x":
        player_1 = "x"
        computer = "o"
    else:
        player_1 = "o"
        computer = "x"

    x = int(input("pick row "))
    while x > 2 or x < 0:
        x = int(input("pick row "))

    y = int(input("pick column "))
    while y > 2 or y < 0:
        y = int(input("pick column "))

    while spots[x][y] != " ":
        print(x, y)
    spots[x][y] = player_1

    for q in range(3):
        for _ in range(3):
            print("+---", end="")
        print("+")
        for f in range(3):
            print(str("| " + spots[q][f]), end=" ")
        print("|")
    for _ in range(3):
        print("+---", end="")
    print("+")

    while game_active:
        if counter == 8 or counter == 9:
            game_active = False
            if counter == 8:
                print("Draw")

            jow = input("Wanna play again? \n")

            while jow != "Yes" and jow != "No" and jow != "yes" and jow != "no":
                jow = input("Please choose between Yes or No \n")
            if jow == "Yes" or jow == "yes":
                game_active = True
                spots = [
                    [" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "]
                ]
                user_pick = input("Pick x or o!\n")
                while user_pick != "x" and user_pick != "y":
                    user_pick = input("Pick x or o!\n")
            else:
                break

        if counter % 2 == 0:
            user_pick = computer
            print("Computer : ")
            x = randrange(2)

            y = randrange(2)

            while spots[x][y] != " ":
                x = randrange(2)

                y = randrange(2)

            spots[x][y] = user_pick
            print(x , y)
            for q in range(3):
                for _ in range(3):
                    print("+---", end="")
                print("+")
                for f in range(3):
                    print(str("| " + spots[q][f]), end=" ")
                print("|")
            for _ in range(3):
                print("+---", end="")
            print("+")
            counter += 1
        else:
            user_pick = player_1
            print("Player 1 : ")

            x = int(input("pick row "))
            while x > 2 or x < 0:
                x = int(input("pick row "))

            y = int(input("picks column "))
            while y > 2 or y < 0:
                y = int(input("pick column "))
            while spots[x][y] != " ":
                print("That spot is taken!")
                x = int(input("pick row "))
                while x > 2 or x < 0:
                    x = int(input("pick row "))

                y = int(input("picks column "))
                while y > 2 or y < 0:
                    y = int(input("pick column "))

            spots[x][y] = user_pick
            print(x, y)

            for q in range(3):
                for _ in range(3):
                    print("+---", end="")
                print("+")
                for f in range(3):
                    print(str("| " + spots[q][f]), end=" ")
                print("|")
            for _ in range(3):
                print("+---", end="")
            print("+")
            counter += 1

        if spots[0][0] == player_1 and spots[0][1] == player_1 and spots[0][2] == player_1:
            print("Player 1 Wins !!!")
            counter = 9
        elif spots[0][0] == player_1 and spots[1][0] == player_1 and spots[2][0] == player_1:
            print("Player 1 Wins !!!")
            counter = 9
        elif spots[0][0] == player_1 and spots[1][1] == player_1 and spots[2][2] == player_1:
            print("Player 1 Wins !!!")
            counter = 9
        elif spots[1][0] == player_1 and spots[1][1] == player_1 and spots[1][2] == player_1:
            print("Player 1 Wins !!!")
            counter = 9
        elif spots[2][0] == player_1 and spots[2][1] == player_1 and spots[2][2] == player_1:
            print("Player 1 Wins !!!")
            counter = 9
        elif spots[0][1] == player_1 and spots[1][1] == player_1 and spots[2][1] == player_1:
            print("Player 1 Wins !!!")
            counter = 9
        elif spots[0][2] == player_1 and spots[1][2] == player_1 and spots[2][2] == player_1:
            print("Player 1 Wins !!!")
            counter = 9
        elif spots[0][2] == player_1 and spots[1][1] == player_1 and spots[2][0] == player_1:
            print("Player 1 Wins !!!")
            counter = 9
        elif spots[0][0] == computer and spots[0][1] == computer and spots[0][2] == computer:
            print("Computer Wins !!!")
            counter = 9
        elif spots[0][0] == computer and spots[1][0] == computer and spots[2][0] == computer:
            print("Computer Wins !!!")
            counter = 9
        elif spots[0][0] == computer and spots[1][1] == computer and spots[2][2] == computer:
            print("Computer Wins !!!")
            counter = 9
        elif spots[1][0] == computer and spots[1][1] == computer and spots[1][2] == computer:
            print("Computer Wins !!!")
            counter = 9
        elif spots[2][0] == computer and spots[2][1] == computer and spots[2][2] == computer:
            print("Computer Wins !!!")
            counter = 9
        elif spots[0][1] == computer and spots[1][1] == computer and spots[2][1] == computer:
            print("Computer Wins !!!")
            counter = 9
        elif spots[0][2] == computer and spots[1][2] == computer and spots[2][2] == computer:
            print("Computer Wins !!!")
            counter = 9
        elif spots[0][2] == computer and spots[1][1] == computer and spots[2][0] == computer:
            print("Computer Wins !!!")
            counter = 9
