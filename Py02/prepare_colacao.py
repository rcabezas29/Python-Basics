leche = input("¿Hay leche? S/N ")
if leche == "S" or leche == "s":
    print("Sacamos la leche")
elif leche == "N" or leche == "n":
    print("Hay que comprar leche")
else :
    print ("Error")
    exit()
colacao = input("¿Hay colacao? S/N ")
if colacao == "S" or colacao == "s":
    print("Sacamos el colacao")
elif leche == "N" or leche == "n":
    print("Hay que comprar colacao")
else :
    print ("Error")
    exit()
if (leche == "S" or leche == "s") and (colacao == "S" or colacao == "s"):
    print("Echo la leche en un vaso")
    print("Echo el colacao también")
    print("Remuevo mi colacao")
else :
    print("Me voy al super")