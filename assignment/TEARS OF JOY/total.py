# a program that ask a user for input till the user opt out anad print out it total
total = 0
usernum = int(input("enter an integer (enter 0 to stop):   "))
while usernum != 0: 
        usernum += 1
        total += usernum
        usernum = int(input("enter an integer (enter 0 to stop):   "))

print(total)


