#calculator 
print("introduce your name")
nombre=input()
print("hello, ", nombre, "this is going to be your calculator")
def calculator():
    print("Introduce the first number you need: ")
    number1=int(input())
    print("Which operation are you going to do?:"+
        "\n -1 add"+
        "\n -2 substract"+
        "\n -3 multiplication"+
        "\n -4 divition")
    option=int(input())
    print("Introduce the second number: ")
    number2=int(input())
    if option==1:
        number3=number1+number2
        print("result: ",number3)
    elif option==2:
        number3=number1-number2
        print("result: ",number3)
    elif option==3:
        number3=number1*number2
        print("result: ",number3)
    else:
        if number2==0:
            print("you cant divide by 0, please introduce other number:")
            number2=int(input())
            while number2==0:
                print("you cant divide by 0, please introduce other number:")
                number2=int(input())
            number3=number1/number2
            print("result: ",number3)
        else:
            number3=number1/number2
            print("result: ",number3)
    calculator()
calculator()