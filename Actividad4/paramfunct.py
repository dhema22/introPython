#Definition of function with parameters

def paramFunct(nombrePersona, age):
    print("hola ", nombrePersona, "tienes ",age," años")
    
print("Dime tu nombre")
nombrePersona=input()
print("Dime tu edad: ")
age=int(input())

paramFunct(nombrePersona, age)