# this is an atm simulator which shows invalid pin if the pin inputed by the user is more than 4 digit

pin = int(input("input your pin:    "))

if pin >= 1000  and  pin  <= 9999:
        print("Valid pin")
else :
        print("Invalid pin")


