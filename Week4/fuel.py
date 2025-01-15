def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = map(int, fraction.split("/"))
            percent = round(x / y * 100)
            if x > y:
               continue
            else:
                if percent >= 99:
                    print("F")
                elif percent <= 1:
                    print("E")
                else:
                    print(f"{percent}%")
                break
        except (ValueError, ZeroDivisionError):
            continue
main()
