grocery_list = {}

while True:
    try:
        item = input().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        break
print("\n")
for item, count in sorted(grocery_list.items()):
                print(count, item)
