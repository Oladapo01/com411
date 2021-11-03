#Ask for the age
print("What is your name?")
name=input()
print(f"My name is {name}")
print("What is your age?")
age=input()
print(f"{age}yrs")
print("How tall are you (in meters)?")
height=float(input())
print(f"{height}m")
print("How much do you weigh (in kilograms)?")
weight=float(input())
print(f"{weight}Kg")
bmi = float(weight/(height ** 2))
print(f"{name} your bmi is {bmi}")

#BMI Categories:
#Underweight = <18.5
if bmi < 18.5:
    print(f"{name} you are underweight")
#Normal weight = 18.5–24.9
elif bmi >= 18.5 and bmi <=24.9:
    print(f"{name} you are of normal weight")
#Overweight = 25–29.9
elif bmi >= 25 and bmi <= 29.9:
    print(f"{name} you are overweight. Hit the gym")
#Obesity = BMI of 30 or greater
else:
    print(f"Obesity")