def sum_weight(bop_weight, beep_weight):
    total = bop_weight + beep_weight
    return total
def calc_avg_weight(bop_weight, beep_weight):
    average = sum_weight(bop_weight, beep_weight) / 2
    return average
def run():
    print("What is the weight of Beep?")
    beep_weight = int(input())
    print("What is the weight of Bop?")
    bop_weight = int(input())
    print("Enter command (Sum/Average)?")
    command = input()
    if command == "sum":
        result = sum_weight(bop_weight, beep_weight)
        print(f"The sum of Beep and Bop's weight is {result}")
    elif command == "average":
        result = calc_avg_weight(bop_weight, beep_weight)
        print(f"The average of Beep and Bop's weight is {result}")
    else:
        print("What do you want me to do?")

run()