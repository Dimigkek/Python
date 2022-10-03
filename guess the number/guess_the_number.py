import random
again = "Yes"
while again != "no" or again != "No" :
    count = 0
    hidden = int(random.randrange(1, 100, 1))

    difficulty = input("Choose a difficulty level (Easy , Normal and Hard) : ")
    while difficulty != "Easy" and difficulty != "Normal" and difficulty != "Hard" and difficulty != "easy" and difficulty != "normal" and difficulty != "hard":
        print("Choose between Easy , Normal and Hard")
        difficulty = input("Choose a difficulty level : ")
    if difficulty == "easy" or difficulty == "Easy":
        print("Easy mode activated you have 10 tries , good luck! ")
    elif difficulty == "normal" or difficulty == "Normal":
        print("Normal mode activated you have 5 tries , good luck! ")
    else:
        print("Hard mode activated you have 3 tries , good luck! ")
    guessed_number = int(input("Guess the number between 1 and 100 : "))
    y = 0
    while hidden != guessed_number:
        if difficulty == "Easy" or difficulty == "easy":
            count += 1
            if count == 10:
                y = 1
                break
            if guessed_number < hidden:
                print("The number we are looking for is bigger than yours")
                guessed_number = int(input("Try again, you still have ("+ str(10 - count) + ") try/tries! \n"))
            elif guessed_number > hidden:
                print("The number we are looking for is smaller than yours")
                guessed_number = int(input("Try again, you still have ("+ str(10 - count) + ") try/tries! \n"))
        elif difficulty == "Normal" or difficulty == "normal":
            count += 1
            if count == 5:
                y = 1
                break
            if guessed_number < hidden:
                print("The number we are looking for is bigger than yours")
                guessed_number = int(input("Try again, you still have ("+ str(5 - count) + ") try/tries! \n"))
            elif guessed_number > hidden:
                print("The number we are looking for is smaller than yours")
                guessed_number = int(input("Try again, you still have ("+ str(5 - count) + ") try/tries! \n"))
        elif difficulty == "Hard" or difficulty == "hard":
                count += 1
                if count == 3:
                    y = 1
                    break
                if guessed_number < hidden:
                    print("The number we are looking for is bigger than yours")
                    guessed_number = int(input("Try again, you still have ("+ str(3 - count) + ") try/tries! \n"))
                elif guessed_number > hidden:
                    print("The number we are looking for is smaller than yours")
                    guessed_number = int(input("Try again, you still have ("+ str(3 - count) + ") try/tries! \n"))

    if y == 0:
        print("You Won!")
        print("Times you guessed : " + str(count))
    else:
        print("You Lose!")
        print("The number was : " + str(hidden))
        print("Times you guessed : " + str(count))

    again = input("Wanna play again? \n")
    while again != "Yes" and again != "No" and again != "yes" and again != "no":
        again = input("Please choose between Yes or No \n")

    if again == "No" or again == "no":
        print("Good Bye! ♥")
        break