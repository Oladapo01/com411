print("What level of brightness is required?")
brightness = int(input())
print()
print("Adjusting brightness.......")
print("\n")

for count in range(2, brightness + 1, 2):
    print(f"Beep's brightness level: {'*' * count}")
    print(f"Bop's brightness level: {'*' * count}\n")

print("Adjustment complete!")