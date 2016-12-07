h = float(input("What is your height in m"))
w = float(input("What is your weight in kg"))
print()
bmi = w // (h*h)

if bmi<18.50:
    print ("You're BMI is",bmi,"You are underweight.")

elif bmi>18.50 and bmi > 25:
    print ("You're BMI is",bmi,"You are healthy.")
elif bmi>25 and bmi<30:
    print ("You're BMI is",bmi,"You are overweight.")

else:
    print ("You're BMI is",bmi,"You are Obese.")

print()
        
