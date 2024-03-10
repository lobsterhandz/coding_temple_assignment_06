import random

# Create a deck of cards.
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]

# Now shuffle the deck.
random.shuffle(deck)

# see the shuffled deck
print("Shuffled deck:")
for card in deck:
    print(card)