import random

def main():
    level = get_level()
    questions = 10
    chances = 3
    score = 0

    for _ in range(questions):
        x , y = generate_integer(level)
        correct_answer = x + y
        attempts = 0
        while attempts < chances:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1
                    questions -= 1
                    break
                else:
                    attempts += 1
                    print("EEE")
            except ValueError:
                attempts += 1
                print("EEE")
                continue
        if attempts == chances:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1<= level <= 3:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
       x = random.randint(0, 9)
       y = random.randint(0, 9)
    elif level == 2:
       x = random.randint(10, 99)
       y = random.randint(10, 99)
    else:
       x = random.randint(100, 999)
       y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
