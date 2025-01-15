import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    else:
        print(count_lines(sys.argv[1]))


def count_lines(file_path):
    try:
        code_lines = 0
        with open(file_path, "r") as file:
            for line in file:
                line_stripped = line.strip()
                if line_stripped and not line_stripped.startswith("#"):
                    code_lines += 1
            return code_lines
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
