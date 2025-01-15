
def main():
    word = (input("Input: "))
    print(shorten(word))


def shorten(word):
    vowels = ["a", "e", "u", "i", "o"]
    new_word = []
    for char in word:
        if char.casefold() not in vowels:
            new_word.append(char)
    output = str("".join(new_word))
    return output


if __name__ == "__main__":
    main()
