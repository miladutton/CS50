import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

# the number of command line arguments includes the script name so we will subtract one
num_args = len(sys.argv) - 1

if num_args == 0:
    isRandomFont = True
elif num_args == 2 and (sys.argv[1] == "-f" or sys.argv[1] == "-font"):
    isRandomFont = False
else:
    sys.exit(1)

text = input("Input: ")

# get fonts
figlet.getFonts()

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid Usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

print(f"Output: {figlet.renderText(text)}")
