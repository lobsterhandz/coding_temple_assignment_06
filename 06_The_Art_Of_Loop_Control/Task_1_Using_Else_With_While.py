# Imagine we have a list of numbers and we're looking for the number 8
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 8

# Start searching from the beginning of the list
index = 0

# Keep looking until we reach the end of the list
while index < len(numbers):
    # If we find the number, celebrate and stop searching
    if numbers[index] == target:
        print(f"We found {target}! Party time!")
        break
    # Move on to the next number in the list
    index += 1
else:
    # If we get here, it means we didn't find the number after checking the whole list
    print(f"Oh no, {target} was not in the list. Better luck next time.")

# This is how it works:
# - The 'while' loop goes through each number to check if it's the one we're looking for.
# - If we find our number, we print a success message and exit the loop with 'break'.
# - If we don't find the number and exit the loop normally, the 'else' part runs, telling us the number wasn't there.
