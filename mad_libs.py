# mad_libs.py

# Ask the user for words
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
adjective4 = input("Enter the last adjective: ")

# Story template
story = f"On a beautiful {adjective1} day, I went to the zoo. I saw a funny {adjective2} monkey swinging from the trees. Then, I spotted a majestic {adjective3} lion lounging in the sun. What a wild and {adjective4} experience!"

# Conditional twist
if adjective4.lower() == "boring":
    story += "\nHmm... maybe I should have stayed home instead. 🏠"
else:
    story += "\nIt was the best zoo trip ever! 🎉"

# Print the story
print("\nHere’s your Mad Libs story:\n")
print(story)
