frase = input("Introduzca una frase\n")
espacios = 0
puntos = 0
comas = 0
for caracter in frase:
    if caracter == " ":
        espacios += 1
    elif caracter == ".":
        puntos += 1
    elif caracter == ",":
        comas += 1
print("Hay {} espacios, {} puntos y {} comas".format(espacios, puntos, comas))
