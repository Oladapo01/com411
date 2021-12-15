def display_ladder(step_number):
    for step in range(step_number):
        print("|  |")
        print("****")
    print("|  |")

def create_ladder():
    print("How many steps remain?")
    step_number = int(input())
    display_ladder(step_number)

create_ladder()
