import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        number_list = ip.split(".")
        for number in number_list:
            if int(number) > 255 or int(number) < 0 :
                return False
        else:
            return True
    return False


if __name__ == "__main__":
    main()
