# a program that checks for age and see if the user is eligible for a senior citisenship discount

age = int(input("enter your birthyear:   "))
year = int(input("enter current year:   "))

sum = age - year
discount = int(65)

if sum >= discount:
    print("your eligible for a senior citizen discount ")
elif  sum < discount:
    print(" your not eligible")

