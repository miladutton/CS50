import os
import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        valid_extensions = [".jpg", ".jpeg", ".png"]
        input_extension = os.path.splitext(sys.argv[1])[1].lower()
        output_extension = os.path.splitext(sys.argv[2])[1].lower()
        if input_extension not in valid_extensions:
            sys.exit("Invalid Input")
        elif output_extension not in valid_extensions:
            sys.exit("Invalid Output")
        elif input_extension != output_extension:
            sys.exit("Input and output have different extensions")
        else:
            edit_photo(sys.argv[1], sys.argv[2])

def edit_photo(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


if __name__ == "__main__":
    main()
