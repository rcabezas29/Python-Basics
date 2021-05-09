def fibonacci_two(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a


def main():
    for f in range(8):
        print(fibonacci_two(f))

if __name__ == "__main__":
    main()