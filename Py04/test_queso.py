titulo = "¿Cuanto te gusta el queso?"
print(titulo)
print("-" * len(titulo))
print()
puntuacion = 0
opcion = input("Pregunta 1: ¿Que haces cuando ves una tabla de quesos?\n"
                "A- Salgo corriendo\n"
                "B- Cojo uno\n"
                "C- Me la como entera\n")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("No has introducido una opcion valida")
    exit()
    
opcion = input("Pregunta 2: ¿Como te gustan los macarrones?\n"
                "A- Sin queso\n"
                "B- Con queso\n"
                "C- Queso con macarrones\n")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("No has introducido una opcion valida")
    exit()

opcion = input("Pregunta 3: ¿Eres intolerante a la lactosa?\n"
                "A- Si\n"
                "B- No\n"
                "C- Si lo fuera estaria muerto\n")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("No has introducido una opcion valida")
    exit()

if puntuacion < 25:
    print("Parece que no te gusta mucho el queso")
else:
    print("Cheese fan")