 # Our playlist continues with a twist
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
i = 0  # Start from the first track
stop_genre = 'Hip-hop'

# Stop the party when we hit Hip-hop or end of list
while i < len(genres) and genres[i] != stop_genre:
    print(f"Remixing: {genres[i]}")
    i += 1  # Move to the next track
