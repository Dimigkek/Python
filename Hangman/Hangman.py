from random import *

max_round = 0
lista = []
hangman_list = ["Grandfather", "Jocker", "Ace", "Paper", "Basketball", "Mountain", "Groove",
                "Zeppelin", "Moonlight", "Landmark", "Gravity", "Umbrella", "Tutor", "Friend",
                "Balloon"]

hidden_word = hangman_list[randrange(len(hangman_list))]

game_active = True

guessed_letters = []

while game_active:

    print(f"We are on round {max_round+1}")
    max_round += 1
    while True:
        letter = input("Give a letter : \n").lower()

        if len(letter) !=1:
            print("ERROR.Give ONE letter!\n")
        elif not letter.isalpha():
            print("ERROR.Give ONE letter\n")
        elif letter in lista:
            print("ERROR. You have chose this letter before!\n")
        else:
           break
    guessed_letters.append(letter)

    lista.append(letter)
    print(f"There is/are {hidden_word.count(letter)} {letter} in the word.\n")

    game = True

    for char in hidden_word:
        if char in guessed_letters:
            print(char, end="")
        else:
            print("_", end="")
            game = False
    print("")

    if max_round == 10:
        print("You ve reached max number of tries, You lose!")
        print(f"The word was {hidden_word}")
        game_active = False
        again = input("Play again?")
        while again != "Yes" and again != "No" and again != "yes" and again != "no":
            again = input("Please choose between Yes or No \n")

        if again == "No" or again == "no":
            print("Good Bye! ♥")
            break


    if game:
        game_active = False
        print("You found the word, You win!")
        again = input("Play again?")
        while again != "Yes" and again != "No" and again != "yes" and again != "no":
            again = input("Please choose between Yes or No \n")

        if again == "No" or again == "no":
            print("Good Bye! ♥")
            break
