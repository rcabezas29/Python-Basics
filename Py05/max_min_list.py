lista = input("Introduzca una lista de numeros separados por espacios: ")
lista = [int(numero) for numero in lista.split(" ")]
alto = lista[0]
bajo = lista[0]
for numero in lista[1:]:
    if alto < numero:
        alto = numero
    if bajo > numero:
        bajo = numero
print("Max: ", alto)
print("Min: ", bajo)