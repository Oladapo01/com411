print("How many cables must I avoid?")
cables = int(input())

number_of_cables = 0
print("\n")
while cables > number_of_cables:
    print(f"Avoiding....", end="")
    number_of_cables = number_of_cables + 1
    print(f"...Done {number_of_cables} live cable avoided!")
print("\n")
print("All live cables have been avoided.")