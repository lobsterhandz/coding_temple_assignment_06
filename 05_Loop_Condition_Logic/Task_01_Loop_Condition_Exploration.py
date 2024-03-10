# Initialize a counter
counter = 0

# Start an infinite loop
while True:  # This condition is always true, leading to an infinite loop
    print("Looping infinitely, or are we?")
    counter += 1  # Update the counter in each iteration
    
    # Check if the counter has reached 5
    if counter == 5:
        print("Reached 5 iterations, breaking out of the loop.")
        break  # Exit the loop

# The loop condition (while True) is designed to always be true, creating an infinite loop.
# using a counter and a break statement, we introduce a way to exit the loop based on a separate condition.
# This demonstrates the power of the break statement to control loop execution beyond the original loop condition.
                                                                                      