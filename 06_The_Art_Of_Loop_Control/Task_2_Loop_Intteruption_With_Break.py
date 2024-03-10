import time

# We'll start an infinite loop that always runs because True is always True!
while True:
    # Print the current time
    current_time = time.strftime("%H:%M:%S")
    print("Current time is:", current_time)
    
    # We'll check if the current time is exactly "12:00:00"
    if current_time == "12:00:00":
        print("It's noon! Let's break out of the loop.")
        break  # This line exits the loop
    
    # Wait for a second before checking the time again
    time.sleep(1)

# Here's what's happening in simple terms:
# - The loop starts and keeps going forever, constantly showing us the time.
# - Inside the loop, we keep an eye on the clock. If it hits noon (12:00:00), we stop the loop.
# - We use 'break' to immediately stop the loop because we reached our target time.
# - If it's not noon yet, we wait a bit (1 second) and then check the time again.
