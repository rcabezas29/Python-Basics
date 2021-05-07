import random
import os

print("Your first Pokemon battle starts\n")
vida_pikachu = 45
vida_squirtle = 50
placaje = 10
pistola_agua = 12
burbuja = 9
at_rapido = 7
impactrueno = 15

while vida_pikachu > 0 and vida_squirtle > 0:
    print("Pikachu's turn")
    attack_pika = random.randint(1, 2)
    if (attack_pika == 1):
        print("Pikachu used Quick Attack")
        vida_squirtle -= at_rapido
    elif(attack_pika == 2):
        print("Pikachu used Thunderbolt")
        vida_squirtle -= impactrueno
    if vida_squirtle < 0: vida_squirtle = 0
    print("Squirtle's HP: ", vida_squirtle * "-", vida_squirtle)
    if (vida_squirtle < 0):
        break
    print("Squirtle's turn")
    attack_squirtle = int(input("What Squirtle should do:\n"
                                    "1.- Tackle\n"
                                    "2.- Water Gun\n"
                                    "3.- Bubble\n"))
    if (attack_squirtle == 1):
        print("Squirtle used Tackle")
        vida_pikachu -= placaje
    elif(attack_squirtle == 2):
        print("Squirtle used Water Gun")
        vida_pikachu -= pistola_agua
    elif(attack_squirtle == 3):
        print("Squirtle used Bubble")
        vida_pikachu -= burbuja
    if vida_pikachu < 0: vida_pikachu = 0
    print("Pikachu's HP: ", vida_pikachu * "-", vida_pikachu)
    input("Press Enter to continue...\n\n")
    os.system("cls")
if vida_pikachu <= 0:
    print("Congratulations, you won!")
elif vida_squirtle <= 0:
    print("You lose")