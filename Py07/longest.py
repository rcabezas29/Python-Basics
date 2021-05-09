def longest(*args):
    longest = ""
    for a in args:
        if len(longest) < len(a):
            longest = a
    return longest

def main():
    print(longest("hola", "que tal", "Raul"))

if __name__ == "__main__":
    main()