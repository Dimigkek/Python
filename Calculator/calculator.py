num1=int(input("enter a number \n"))
num2=int(input("enter a number \n"))
calc=input("enter an operation \n")
def calculator(num1,num2,calc):
    if calc == "+":
        return num1+num2
    elif calc=="-":
        return num1-num2
    elif calc=="/":
        return num1/num2
    elif calc=="x":
        return num1*num2
    else:
        print("ERROR")

print(calculator(num1,num2,calc))