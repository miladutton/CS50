def main():
    x = int(input("Give me a mass "))
    print("mass as energy is", joules(x))

def joules(n):
    return n * 300000000 **2

main()
