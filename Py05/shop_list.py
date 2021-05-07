lista = []
compra = input("What would you like to add to your shop list? [Q] to quit ")
while compra != "Q":
    if compra not in lista:
        lista.append(compra)
    compra = input("What would you like to add to your shop list? [Q] to quit ")
print("Su lista de la compra es:")
print(lista)
