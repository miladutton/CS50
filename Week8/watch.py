import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r"\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"", s):
        return f"https://youtu.be/{url.group(1)}"
    else:
       return None

if __name__ == "__main__":
    main()
