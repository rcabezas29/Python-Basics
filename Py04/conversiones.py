mi_moneda = input("¿Que moneda quieres convertir? (D)ollar, (E)uro or (P)ound ")
conver = input("¿A que moneda te gustaria convertirla? (D)ollar, (E)uro or (P)ound ")
dinero = int(input("¿Cuanto dinero quieres convertir? "))
if mi_moneda == "D" and conver == "E":
    dinero *= 0.83
elif mi_moneda == "D" and conver == "P":
    dinero *= 0.72
elif mi_moneda == "E" and conver == "D":
    dinero *= 1.21
elif mi_moneda == "E" and conver == "P":
    dinero *= 0.87
elif mi_moneda == "P" and conver == "D":
    dinero *= 1.39
elif mi_moneda == "P" and conver == "E":
    dinero *= 1.15
print("El valor de su dinero tras la conversion es {}".format(dinero))