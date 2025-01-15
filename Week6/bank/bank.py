
def main():
    greeting = input("Input: ")
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        value = 0
    elif "h" == greeting[0]:
        value = 20
    else:
        value = 100
    return value



if __name__ == "__main__":
    main()
