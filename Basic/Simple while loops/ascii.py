print("How many bars should be charged?")

bars = int(input())

numbers_of_bar = 0
print("\n")

while numbers_of_bar < bars:
    numbers_of_bar = numbers_of_bar + 1
    print(f"Charging: {'█ ' * numbers_of_bar}")

print("\n")
print("The battery is fully charged")