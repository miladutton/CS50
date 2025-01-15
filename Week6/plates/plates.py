def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
        # make sure first 2 characters are letters
    if not s [:2].isalpha():
        return False
    # make sure it is between 2-6 characters
    if not 2<= len(s) <= 6:
        return False
    # make sure there is no punctuation
    if not s.isalnum():
        return False
   # first number cant be zero and numbers must come at end
    for char in s:
        if char.isdigit():
            index = s.index(char)
            if s[index:].isdigit() and int(char) != 0:
                return True
            else:
                return False
    return True


if __name__ == "__main__":
    main()
