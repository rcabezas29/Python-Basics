salida = "Exit"
base = ["Pan", "Huevos", "Leche"]

def saving(lista):
    nombre = imput("What would be the list name? ")
    with open(nombre + ".txt", "w") as a:
        a.write("\n".join(lista))

def asking():
    return input("What would you like to add?\n")

def adding(lista, item):
    if item == "LISTA":
            print(base)
    elif item not in base:
        print("Not in database")
    if item not in lista and item in base:
        lista.append(item)

def main():
    lista = []
    user = asking()
    while user != salida:
        adding(lista, user)
        user = asking()
    saving(lista)

if __name__ == "__main__":
    main()