print("What strange markings do you see?")
markings = input()

for words in range(0, len(markings), 1):
    print(f"index {words}: ", markings[words])