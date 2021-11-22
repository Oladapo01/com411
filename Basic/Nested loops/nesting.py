print("Please enter a sequence:")
sequence = input()
print("Please enter a character for the marker:")
marker = input()

first_marker = -1
second_marker = -1

for character in range(0, len(sequence), 1):
    letters = sequence[character]

    if letters == marker:
        if(first_marker == -1):
            first_marker = character

        else:
            second_marker = character

print(f"The distance between the markers is: {second_marker - first_marker - 1}.")
