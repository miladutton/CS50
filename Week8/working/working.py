import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    check_format = re.search(r"^(([0-9][0-2]?):?([0-5][0-9])?) (AM|PM) to (([0-9][0-2]?):?([0-5][0-9])?) (AM|PM)$", s)
    if check_format:
        blocks = check_format.groups()
        if int(blocks[1]) > 12 or int(blocks[5]) > 12:
            raise ValueError
        start_time = convert_time(blocks[1], blocks[2], blocks[3])
        end_time = convert_time(blocks[5], blocks[6], blocks[7])
        return(f"{start_time} to {end_time}")
    else:
        raise ValueError


def convert_time(hour, minute, t):
    if t == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:  # AM
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    if minute is None:
        minute = "00"

    return f"{new_hour:02}:{minute}"

if __name__ == "__main__":
    main()
