import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        update(sys.argv[1], sys.argv[2])

def update(input, output):
    try:
        # Open input CSV file for reading
        with open(input) as input:
            reader = csv.DictReader(input)

            # Open output CSV file for writing
            with open(output, "w") as output:
                  # Define the fieldnames for the output CSV
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(output, fieldnames=fieldnames)
                # Write the header row in the output CSV
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


if __name__ == "__main__":
    main()
