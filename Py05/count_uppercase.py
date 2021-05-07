import string

texto = input("Introduzca un texto: ")
i = 0
for char in texto:
    if char in string.ascii_uppercase:
        i += 1
print("Hay {} mayusculas".format(i))