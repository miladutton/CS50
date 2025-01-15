answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().replace(" ", "")
if answer == "42" or answer == "fortytwo" or answer == "forty-two":
    print("Yes")
else:
    print("No")
