height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmı = round(weight / (height ** 2))

if bmı < 18.5:
    print(f"Your BMI is {bmı}, you are underweight.")
elif 18.5 < bmı < 25:
    print(f"Your BMI is {bmı}, you have a normal weight.")
elif 25 < bmı < 30:
    print(f"Your BMI is {bmı}, you are slightly overweight.")
elif 30 < bmı < 35:
    print(f"Your BMI is {bmı}, you are obese.")
else:
    print(f"Your BMI is {bmı}, you are clinically obese.")
