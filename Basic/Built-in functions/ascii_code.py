print("Program started!")
print("Please enter a letter:")
letter= str(input())
if len(letter) == 1:
    print(f"The ASCII code for {letter} is: {ord(letter)}")
else:
    print("")
print("Program Ended!")
