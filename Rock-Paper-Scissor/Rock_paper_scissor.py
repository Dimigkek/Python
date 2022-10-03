from random import *
k = 1
c = 0
u = 0
again = ""
lista = []
r_one = 1
# game
while again != "no" or again != "No" :
    k = 0
    u = 0
    c = 0
    lista.clear()
    print("Welcome to Paper,Rock,Scissor the first who gets three wins win!")
    while u < 3 and c < 3:
        print(f"Round : {str(r_one)}")
        print("User : "+ str(u) +" Computer : " + str(c))
        r_one += 1
        user = input("Rock,Paper,Scissor?\n")
        while user not in ["Rock", "Paper", "Scissor"]:
            user = input("Please choose between : Rock,Paper,Scissor?\n")
        computer = randrange(3)
        if computer == 0:
            computer = "Rock"
        elif computer == 1:
            computer = "Paper"
        else:
            computer = "Scissor"

        if user == "Rock":
            if computer == "Rock":
                print("Draw")
                r = "Player: "+user+" Computer: " + computer + " Draw "+ "Score : " + str(u) + "-" + str(c)
                lista.append(r)
            elif computer == "Paper":
                print("Computer win")
                c += 1
                r = "Player: " + user + " Computer: " + computer + " Computer win " + "Score : " + str(u) + "-" + str(c)
                lista.append(r)

            else:
                print("User win")
                u += 1
                r = "Player: " + user + " Computer: " + computer + " User win " + "Score : " + str(u) + "-" + str(c)
                lista.append(r)

        elif user == "Paper":
            if computer == "Rock":
                print("User win")
                u += 1
                r = "Player: "+user+" Computer: " + computer + " User win "+ "Score : " + str(u) + "-" + str(c)
                lista.append(r)

            elif computer == "Paper":
                print("Draw")
                r = "Player: " + user + " Computer: " + computer + "Draw " + "Score : " + str(u) + "-" + str(c)
                lista.append(r)
            else:
                print("Computer win")
                c += 1
                r = "Player: " + user + " Computer: " + computer + " Computer win " + "Score : " + str(u) + "-" + str(c)
                lista.append(r)

        else:
            if computer == "Rock":
                print("Computer win")
                c += 1
                r = "Player:" + user + " Computer: "+ computer + " Computer win " + "Score : " + str(u) + "-" + str(c)
                lista.append(r)

            elif computer == "Paper":
                print("User win")
                u += 1
                r = "Player: " + user + " Computer: " + computer + " User win " + "Score : " + str(u) + "-" + str(c)
                lista.append(r)

            else:
                print("Draw")
                r = "Player: " + user + " Computer: "+ computer  + " Computer win " + "Score : " + str(u) + "-" + str(c)
                lista.append(r)

    if c == 3:
        print("Computer Won!!!")
    else:
        print("User Win!!!")
    print("Match History :")
    for i in lista:
        print("Round :"+ str(k) + " " + str(i))
        k += 1
    again = input("Play again?")
    while again != "Yes" and again != "No" and again != "yes" and again != "no":
        again = input("Please choose between Yes or No \n")

    if again == "No" or again == "no":
        print("Goodbye! ♥")
        break