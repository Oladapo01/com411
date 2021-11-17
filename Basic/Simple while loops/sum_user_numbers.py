# Display message
print("How many numbers should I sum up?")

# input the amount of numbers to call
number = int(input())

# variable for counting
sum_number = 0

# sum numbers
summed_number = 0


while sum_number < number:
    print(f"please enter number {sum_number} of {number}")
    input_number = int(input())
    summed_number = summed_number + input_number
    sum_number = sum_number + 1

# display final result
print(f"The total is {summed_number}")