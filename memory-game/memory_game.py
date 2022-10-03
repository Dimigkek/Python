array = [1, 4, 3, 2, 3, 4, 2, 1]
N = 8
score = 0
high_score = 100
state = ["closed", "closed", "closed", "closed", "closed", "closed", "closed", "closed"]
active_game = True
score_counter = 0
for position in range(N):
    if state[position] == "open":
        print(array[position], end=" ")
    elif state[position] == "temp_open":
        print(array[position], end=" ")
    else:
        print("◘", end=" ")
while  active_game:

    first_card = int(input("Choose a card between 0 and " + str(N-1) + ": \n"))

    while first_card < 0 or first_card>N-1 or state[first_card] == "open":
        first_card = int(input("Choose another card.\n"))



    second_card = int(input("Chose your second card :"))

    while second_card < 0 or second_card >N-1 or state[second_card] == "open" or second_card== first_card:
        second_card = int(input("Choose another card."))

    state[first_card] = "temp_open"
    state[second_card] = "temp_open"
    print("")
    for position in range(N):
        if state[position] == "open":
            print(array[position],end=" ")
        elif state[position] == "temp_open":
            print(array[position],end=" ")
        else:
            print("◘",end=" ")
    print("")

    if array[first_card] == array[second_card]:
        print("Success")
        state[first_card] = "open"
        state[second_card] = "open"
        score += 1
    else:
        print("Fail")
        state[first_card] = "closed"
        state[second_card] = "closed"
        score += 1
    for position in range(N):
        if state[position] == "open":
            print(array[position],end=" ")
        elif state[position] == "temp_open":
            print(array[position],end=" ")
        else:
            print("◘",end=" ")

    if state == ["open", "open", "open", "open", "open", "open", "open", "open"]:
        active_game = False
        print("You Win!\n")
        print("Attempts : " + str(score))
        if score < high_score:
            high_score = score
        print("Highscore :" + str(high_score) + " attempts")
        x = input("Play again?")
        while x != "Yes" and x != "No":
            x = Yinput("Play again?(Yes or No)")
        if x == "Yes":
            active_game = True
            state = ["closed", "closed", "closed", "closed", "closed", "closed", "closed", "closed"]
            high_score = score
            score = 0
        else:
            print("Good Bye!")