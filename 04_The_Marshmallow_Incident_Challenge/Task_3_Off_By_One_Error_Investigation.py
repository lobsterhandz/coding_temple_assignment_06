marshmallows = 0
while marshmallows < 10:  # Ensures the loop runs exactly 10 times
    marshmallows += 1  # Increment before printing to reflect current state accurately
    # Placing the increment operation here ensures that the count of marshmallows is updated
    # immediately for the current iteration. This prevents off-by-one errors by making sure
    # the loop condition is checked against the updated count for each iteration, allowing
    # precise control over the number of loop executions and avoiding one iteration too many or too few.
    print(f"Added a marshmallow. Now there are {marshmallows} marshmallows.")
