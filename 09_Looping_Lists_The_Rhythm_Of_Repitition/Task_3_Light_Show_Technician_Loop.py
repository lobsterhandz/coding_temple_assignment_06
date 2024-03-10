# Setting up for a spectacular light show, except for classical
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
unsuitable_genre = 'Classical'

for index in range(len(genres)):
    if genres[index] == unsuitable_genre:
        continue  # Classical needs no flashy lights
    print(f"Track {index + 1}: {genres[index]} - Light show is ready!")
