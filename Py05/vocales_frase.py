vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
frase = input("Introduce una frase: ")
i = 0
for letra in frase:
    if letra in vocales:
        i += 1
print("Hay {} vocales".format(i))
