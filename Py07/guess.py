from random import randint

def guess():
    n = randint(1, 100)
    a = int(input("Guess a number from 1 to 100: "))
    while a != n:
        a = int(input("Guess a number from 1 to 100: "))
    print("You got it!")
        

def main():
    guess()

if __name__ == "__main__":
    main()