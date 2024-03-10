import random

moods = ["Happy", "Sad", "Energetic", "Calm"]

hours_of_day = range(1, 25)  # 1 to 24 hours
lunchtime = 12
for hour in hours_of_day:
    if hour == lunchtime:
        continue
    mood = random.choice(moods)
    print(f"Hour {hour}: {mood}")
