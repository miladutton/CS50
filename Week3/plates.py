def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):
    # make sure first 2 characters are letters
    if not p [:2].isalpha():
        return False
    # make sure it is between 2-6 characters
    if not 2<= len(p) <= 6:
        return False
    # make sure there is no punctuation
    if not p.isalnum():
        return False
   # first number cant be zero and numbers must come at end
    for char in p:
        if char.isdigit():
            index = p.index(char)
            if p[index:].isdigit() and int(char) != 0:
                return True
            else:
                return False
    return True

main()
