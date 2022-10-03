from random import *

kind = {"♥", "♦", "♣", "♠"}
number = {"Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"}

cards = {(k, n) for k in kind for n in number}
print(cards)

player1 = set()

player2 = set()

lists = list(cards)  # kanoume thn metratoph gia na mporoume na paiksoume mazi tous.

# def share():
for i in range(0, 5):
    pos1 = randrange(0, len(lists))
    player1.add(lists.pop(pos1))
    pos2 = randrange(0, len(lists))
    player2.add(lists.pop(pos2))

# def kare_check():
count = 0

for card in player1:
    if card[1] == "ace":
        count += 1
if count == 4:
    print("Player 1 has kare!")

count = 0

for card in player2:
    if card[1] == "ace":
        count += 1
if count == 4:
    print("Player 2 has kare!")

hand_numbers = []

for card in player1:
    if card[1] == "ace":
        hand_numbers.append(1)
    elif card[1] == "jack":
        hand_numbers.append(11)
    elif card[1] == "queen":
        hand_numbers.append(12)
    elif card[1] == "king":
        hand_numbers.append(13)
    else:
        hand_numbers.append(card[1])

hand_numbers.sort()

for pos in range(4):
    if hand_numbers[pos] != hand_numbers[pos + 1] - 1:
        break
else:
    print("Player 1 has kenta! ")

hand_numbers = []
for card in player2:
    if card[1] == "ace":
        hand_numbers.append(1)
    elif card[1] == "jack":
        hand_numbers.append(11)
    elif card[1] == "queen":
        hand_numbers.append(12)
    elif card[1] == "king":
        hand_numbers.append(13)
    else:
        hand_numbers.append(card[1])

hand_numbers.sort()

for pos in range(4):
    if hand_numbers[pos] != hand_numbers[pos + 1] - 1:
        break
else:
    print("Player 2 has kenta! ")
