edad = int(input("Introduce tu edad "))
tipo = input("¿Qué tipo de carnet tienes?: (E)studiante, (P)ensionista, (F)amilia numerosa o (N)ormal ")
if (tipo != "E" and tipo != "P" and tipo != "N" and tipo != "F"):
    print("Error")
    exit()
coste = 25
if edad < 10 or edad > 65 or tipo == "N" or tipo == "P" or tipo == "E":
    print("Se te aplica el descuento")
    coste = 20
else:
    print("No se te aplica el descuento")
print("El precio es de {}€".format(coste))