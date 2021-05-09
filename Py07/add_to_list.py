def add_to_list(lista, item):
    if item not in lista:
        lista.append(item)
    else:
        print("That's already in the list")

def main():
    lista = ["Huevos", "Leche", "Pescado"]
    add_to_list(lista, "Pan")

if __name__ == "__main__":
    main()