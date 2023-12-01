#Conditional if 
print ("how old are you: ")
age = input()
edad=int(age)
if edad>=18:
    print("puedes entrar")
else:
    print("No puedes entrar")

#nest
edad=20
if edad<25:
    if edad<13:
        print("eres un niño")
    else:
        print("eres un adolescente")
else:
    print("eres un adulto")
