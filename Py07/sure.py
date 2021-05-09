def sure():
    res = input("Are you sure? ")
    if res == "SI" or res == "Si" or res =="si":
        return True
    else:
        return False

def main():
    print(sure())

if __name__ == "__main__":
    main()