import random

# First, let's set up a list of possible items the computer can choose from.
items = ['apple', 'banana', 'cherry', 'grape']

# The computer makes its choice secretly.
computer_choice = random.choice(items)

# Now, it's the player's turn to guess.
player_guess = input("I've chosen an item from this list: apple, banana, cherry, grape. Can you guess which one? ")

# We'll tell the player if they got it right or not.
if player_guess == computer_choice:
    print("You got it! Well done.")
else:
    print(f"Nice try, but I actually chose the {computer_choice}. Better luck next time!")

# Game summary:
# - The list 'items' holds all possible choices.
# - The computer picks one by 'random.choice(items)'.
# - The player inputs their guess.
# - We check if the player's guess matches the computer's choice.
# - The player receives feedback based on whether their guess was right or wrong.