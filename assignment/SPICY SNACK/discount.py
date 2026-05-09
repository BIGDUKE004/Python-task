#collect input
#give out result based on the input


total_bill = int(input("enter total bill: "))
is_member = input("are you a member: ")

if(total_bill >= 1000 and is_member == "yes" ):
    print("10% off")
elif (total_bill >= 1000 and is_member != "yes" ):
    print("5% off")

