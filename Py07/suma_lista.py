def longest(*args):
    suma = 0
    for i in args:
        suma += i
    return suma

def main():
    print(longest(1, 2, 3, 4, 5))

if __name__ == "__main__":
    main()