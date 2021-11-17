# display message for number
print("Please enter a number?")
number = int(input())

count = 0
total = 1

# while loop
while count < number:
    count = count + 1
    total = total * count

# print total
print(f"The factorial is {total}")