N = 3
y = 0
id = 1004
student = {
    "id           ": id,
    "Όνομα        ": "",
    "Επώνυμο      ": "",
    "Πατρώνυμο    ": "",
    "Ηλικία       ": y,
    "Τάξη         ": y,
    "Αρ.Ταυτότητας": ""

}
student2 = {
    "id           ": id,
    "Όνομα        ": "",
    "Επώνυμο      ": "",
    "Πατρώνυμο    ": "",
    "Ηλικία       ": y,
    "Τάξη         ": y,
    "Αρ.Ταυτότητας": ""

}
students = [{
    "id           ": 1001,
    "Όνομα        ": "Κώστας",
    "Επώνυμο      ": "Κωστογλού",
    "Πατρώνυμο    ": "Μάνθος",
    "Ηλικία       ": 11,
    "Τάξη         ": 6,
    "Αρ.Ταυτότητας": "ΑΝ151458"

},
    {
        "id           ": 1002,
        "Όνομα        ": "Θανάσης",
        "Επώνυμο      ": "Κωστογλού",
        "Πατρώνυμο    ": "Μάνθος",
        "Ηλικία       ": 8,
        "Τάξη         ": 4,
        "Αρ.Ταυτότητας": "ΑΝ152358"

    },
    {
        "id           ": 1003,
        "Όνομα        ": "Γιάννης",
        "Επώνυμο      ": "Κωστής",
        "Πατρώνυμο    ": "Πέτρος",
        "Ηλικία       ": 6,
        "Τάξη         ": 1,
        "Αρ.Ταυτότητας": "-"

    }

]
x = ""
menu_active = True
while menu_active:
    student = student2.copy()
    print("1: Δημιουργία Εγγραφής\n"
          "2: Εκτύπωση\n"
          "3: Ενημέρωση Εγγραφής\n"
          "4: Διαγραφή Εγγραφής\n"
          "5: Έξοδος\n")
    option = int(input("Επιλέξτε μια δραστηριότητα "))

    if option == 1:

        student["id           "] = id
        x1 = input("Όνομα        ")
        student["Όνομα        "] = x1
        x2 = input("Επώνυμο      ")
        student["Επώνυμο      "] = x2
        x3 = input("Πατρώνυμο    ")
        student["Πατρώνυμο    "] = x3
        stop = False
        for s in students:
            if x1 == s["Όνομα        "] and x2 == s["Επώνυμο      "] and x3 == s["Πατρώνυμο    "]:
                print("Υπαρχει ήδη:\n")
                print(s)
                qu = input("Θέλετε να συνεχίσετε; (y/n)\n")
                if qu == "n":
                    stop = True
                    break
        if stop:
            continue
        y = int(input("Ηλικία       "))
        student["Ηλικία       "] = y
        y = int(input("Τάξη         "))
        student["Τάξη         "] = y
        qu1 = input("Έχει ταυτότητα;(y/n)\n")
        if qu1 == "y":
            x = input("Αρ.Ταυτότητας")
            student["Αρ.Ταυτότητας"] = x
        else:
            student["Αρ.Ταυτότητας"] = "-"

        students.append(student)
        print("Η εγγραφή ολοκληρώθηκε!")
        id += 1




    elif option == 2:
        for i in students:
            print(i)
    elif option == 3:
        print("b")
    elif option == 4:
        print("c")
    elif option == 5:
        print("Αντίο!")
        break
