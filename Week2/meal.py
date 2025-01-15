def main():
    time = input("What time is it? ").strip()
    converted_time = convert(time)

    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = map(float, time.split(":"))
    converted_time = hours + minutes / 60
    return converted_time


if __name__ == "__main__":
    main()
