def power(*args):
    lista = []
    i = 0
    n = 1
    for a in args:
        lista.append(a)
    if len(lista) == 2:
        p = lista[1]
    else:
        p = 2
    while i < p:
        n *= lista[0]
        i += 1
    return n

def main():
    print(power(3, 9))

if __name__ == "__main__":
    main()