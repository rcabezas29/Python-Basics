def one_more(n):
    print(n)
    n += 1
    if n < 100:
        one_more(n)

def main():
    one_more(1)

if __name__ == "__main__":
    main()