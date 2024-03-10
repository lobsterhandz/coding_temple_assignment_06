condition1 = True
condition2 = True
value = 0

# The loop continues as long as both condition1 and condition2 are true.
while (condition1 and condition2):
    print(f"Current Value: {value}")
    # When value reaches 5, change condition1 to False, which will cause the loop to exit.
    if value == 5:
        condition1 = False
    # The increment of value happens each loop iteration.
    value += 1