count = 120
count1 = 41
count2 = 41
count3 = 41
question = "Yes"
print("Available seats First class : " + str(count3 - 1) + " ,Business class : " + str(count2 - 1) + " ,Economy class : " + str(count1 - 1))

plane_class = input("Select class\n")
while plane_class != "First class" and plane_class !="Business" and plane_class != "Economy":
    plane_class = input("Select class between Fist class , Business and Economy\n")

while count > 0 :

    if plane_class == "Economy":
        print("Reminder!\n Available seats :" + str(count1 - 1))
    elif plane_class == "Business":
        print("Reminder!\n Available seats :" + str(count2 - 1))
    else:
        print("Reminder!\n Available seats :" + str(count3 - 1))
    seats = int(input("How many seats? \n"))
    if count == 0:
        print("Airplane is full")
        break
    while seats < 1 or seats > 40:
        print("Please pick a valid number of seats.")
        seats=int(input())
    if plane_class == "Economy":
        if count1 == 1:
            print("There is no available seat.")
            break
        while count1 <= 0 or count1 <= seats:
            print("Please enter a valid number of seats.")
            seats = int(input())
        count1 = count1 - seats
        count = count - seats
        question = input("Continue shopping? (Type Yes or No)\n")
        while question != "Yes" and question != "No":
            print("Please type Yes or No\n")
            question = input()

        if question == "No":
            break
        print("Available seats First class : " + str(count3 - 1) + " ,Business class : " + str(
            count2 - 1) + " ,Economy class : " + str(count1 - 1))
        plane_class = input("Select class\n")
        while plane_class != "First class" and plane_class != "Business" and plane_class != "Economy":
            plane_class = input("Select class between Fist class , Business and Economy\n")
    elif plane_class == "Business":
        if count2 == 1:
            print("There is no available seat.")
            break
        while count2 <= 0 or count2 <= seats:
            print("Please enter a valid number of seats.")
            seats = int(input())
        count2 = count2 - seats
        count = count - seats
        question = input("Continue shopping? (Type Yes or No)\n")
        while question != "Yes" and question != "No":
            print("Please type Yes or No\n")
            question = input()
        if question == "No":
            break
        print("Available seats First class : " + str(count3 - 1) + " ,Business class : " + str(
            count2 - 1) + " ,Economy class : " + str(count1 - 1))
        plane_class = input("Select class\n")
        while plane_class != "First class" and plane_class != "Business" and plane_class != "Economy":
            plane_class = input("Select class between Fist class , Business and Economy\n")
    elif plane_class == "First class":
        if count3 == 1:
            print("There is no available seat.")
            break
        while count3 <= 0 or count3 <= seats:
            print("Please enter a valid number of seats.")
            seats = int(input())
        count3 = count3 - seats
        count = count - seats
        question = input("Continue shopping? (Type Yes or No)\n")
        while question != "Yes" and question != "No":
            print("Please type Yes or No\n")
            question = input()
        if question == "No":
            break
        if count == 0:
            print("Airplane is full")
            break
        print("Available seats First class : " + str(count3 - 1) + " ,Business class : " + str(
            count2 - 1) + " ,Economy class : " + str(count1 - 1))
        plane_class = input("Select class\n")
        while plane_class != "First class" and plane_class != "Business" and plane_class != "Economy":
            plane_class = input("Select class between Fist class , Business and Economy\n")


print("Thank you ,Goodbye!")
