print("Program started!")
code = int(input("Please enter an ASCII code:"))
if code >= 32 and code <= 127:
    print(f"The character represented by the ASCII code {code} is {chr(code)}")
else:
    print("Error")
print("Program Ended!")
