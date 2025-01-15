camel_case = input("Give me a variable in Camel Case: " )
print("Snake Case: ", end = "")

for char in camel_case:
    if char.isupper():
        print("_", char.lower(), end = "" )
    else:
        print(char, end = "")

print("")
