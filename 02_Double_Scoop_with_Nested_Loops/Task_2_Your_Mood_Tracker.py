import random

# Items
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["morning", "afternoon", "evening"]
moods = ["Happy", "Sad", "Energetic", "Calm"]

# Mood Tracker
for day in days_of_week:
    for time in times_of_day:
        mood = random.choice(moods)
        print(f"{day} {time}: Mood - {mood}")
    