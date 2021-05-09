def to_upper(s):
    a = s.lower()
    return a.swapcase()


def main():
    print(to_upper("Hola"))

if __name__ == "__main__":
    main()