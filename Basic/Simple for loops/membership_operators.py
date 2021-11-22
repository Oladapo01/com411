print("What phrase do you see?")
phrase = input()
print("\n")
print("Reversing.....")
print("\n")
print("The phrase is: ", end="")

reversed = ""

for letters in phrase:
    reversed = letters + reversed
print(reversed)