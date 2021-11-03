print("What is your name?")
name = input()
print("What is the time?")
time = input()
if (time == "00:00") and (time <= "12:00"):
    print(f"Good morning {name}.The time is {time}")
elif (time == "12:00") and (time <= "16:00"):
    print(f"Good afternoon {name}. The time is {time}")
elif (time >= "16:00") and (time <= "22:00"):
    print(f"It is getting late {name}")
else:
    print(f"Go to bed {name}")

print("Have a nice time!")