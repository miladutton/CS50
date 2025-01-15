import random

while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            number = random.randint(1, level)
        else:
            continue
        while True:
            try:
                guess = int(input("Guess: "))
                if guess == number:
                    print("Just right!")
                    raise EOFError
                if guess < number and guess > 0:
                    print("Too small!")
                elif guess > number and guess > 0:
                    print("Too large!")
                else:
                    continue
            except ValueError:
                continue
    except ValueError:
        continue
    except EOFError:
        break
