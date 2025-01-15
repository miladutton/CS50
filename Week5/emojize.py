import emoji
# Get user input
text = input("Input: ")

# Split input text into text before and after the emoji name
split_text = text.split(":", maxsplit=1)

# If the split resulted in more than one part (i.e., emoji name is found)
if len(split_text) > 1:
    # Extract emoji name and convert it to emoji
    emoji_name = split_text[1]
    create_emoji = emoji.emojize(":" + emoji_name, language = "alias")

    # Print the output
    print("Output:", split_text[0] + create_emoji)
else:
    # If no emoji name found, print the input text as it is
    print("Output:", text)
