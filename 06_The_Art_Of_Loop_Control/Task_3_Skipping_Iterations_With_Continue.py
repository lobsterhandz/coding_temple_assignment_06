# Start counting from 1 to 10.
number = 1

while number <= 10:
    # Check if the number is a multiple of 3.
    if number % 3 == 0:
        number += 1  # Go to the next number.
        continue  # Skip this one and go back to the start of the loop.
    
    # If the number is not a multiple of 3, print it.
    print("Number is:", number)
    number += 1  # Then go to the next number.

# What this does:
# - It looks at each number from 1 to 10.
# - If a number can be divided by 3 without leaving anything left over, we don't print it.
# - For all other numbers, we print them out.