# Let's count from 1 to 5, but pretend we're thinking about doing something special when we get to 3.
number = 1

while number <= 5:
    if number == 3:
        # Hmm, not sure what to do here yet, so let's just skip it for now.
        pass
    else:
        # For all other numbers, just print them.
        print("Number is:", number)
    
    # Move on to the next number, regardless of what happened above.
    number += 1

# Why use 'pass'?
# - Sometimes, you might not be ready to write code for a specific condition.
# - Using 'pass' lets you acknowledge that this is a place you intend to come back to, without causing any errors.
# - It's like putting a bookmark in your code that says, "I'll deal with this part later."
