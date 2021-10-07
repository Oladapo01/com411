print("Please enter first whole number")
first_number=input()
print("Please enter second whole number")
second_number=input()
print("Please enter the third whole number")
third_number=input()

even_number = 0
odd_number = 0

if int(first_number) % 2 == 0:
    odd_number += 1
elif int(first_number) % 2 != 0:
    even_number +=1

if int(second_number) % 2 == 0:
    odd_number += 1
elif int(second_number) % 2 != 0:
    even_number +=1

if int(third_number) % 2 == 0:
        odd_number += 1
elif int(third_number) % 2 != 0:
        even_number += 1

print(f"There were {even_number} even and {odd_number} odd number.")

