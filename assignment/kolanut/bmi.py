# a program that calculate BMI from the user input which is weight and height 

weight = float(input("enter weight:    "))
height = float(input("enter height:    "))

sum = height * height 
sum1 = weight // sum

if sum1 < 18:
        print("underweight")
elif sum1 < 25:
        print("normal")
elif sum1 < 30:
        print("overweight")
elif sum1 > 30:
        print("obese")

 
