def convert(face):
    return face.replace(":)" , "🙂").replace(":(" , "🙁")

def main():
    mood = input("how are you today? ")
    print(convert(mood))

main()
