import random

# The computer picks a random number between 1 and 100.
secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

# The player guesses until they get it right.
while True:
    guess = int(input("Make your guess: "))
    
    # Provide feedback about the guess.
    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("That's right! You guessed my number!")
        break
