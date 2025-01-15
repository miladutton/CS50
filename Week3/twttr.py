
word = (input("Tell me anything! "))
vowels = ["a", "e", "u", "i", "o"]
new_word = word



for char in word:
    if char.lower() in vowels:
        new_word = new_word.replace(char, "")

print(new_word)
