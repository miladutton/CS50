import inflect

p = inflect.engine()

#initialize an emoty list to store the names the user will enter
name_list = []

while True:
    try:
        name = input("Name: ").strip().title()
        #store each name into the list
        name_list.append(name)
    except EOFError:
        print("Adieu, adieu, to", p.join(name_list))
        break
