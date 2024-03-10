import random

# Prepare the deck of cards.
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]

# The computer picks a random card.
chosen_card = random.choice(deck)
print("I've picked a card from the deck.")

# Player guesses the suit or rank.
player_guess = input("Guess the suit or rank of the card: ")

# Check if the guess is correct.
if player_guess in chosen_card:
    print(f"Correct! The card was {chosen_card}.")
else:
    print(f"Wrong guess. The card was {chosen_card}.")
