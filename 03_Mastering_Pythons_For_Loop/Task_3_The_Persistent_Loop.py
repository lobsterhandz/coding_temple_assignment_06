numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
target = 13
for number in numbers:
    if number == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} was not found.")
