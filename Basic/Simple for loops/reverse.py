print("What phrase do you see?")
phrase = input()
print()
print("Reversing......")
print()
print("The phrase is:", end= "")
for name in range(len(phrase) - 1, -1, -1):
    print(phrase[name], end= "")
