# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Initialize track number and spin through the genres
track_number = 1
for genre in genres:
    print(f"Track {track_number}: Now playing {genre}")
    track_number += 1
