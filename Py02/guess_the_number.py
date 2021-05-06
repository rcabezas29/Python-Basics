import random

n = random.randint(1, 10)
guess = int(input("Introduzca un número del 1 al 10 "))
if guess < 1 or guess > 10 :
    print("Ese numero no es valido")
    exit()
if n == guess :
    print("Enhorabuena, has acertado")
else :
    print("Fallaste, el numero era el", n)