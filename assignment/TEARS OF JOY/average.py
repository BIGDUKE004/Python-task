# a program that collects the list of average from user and gives the average back to the user
total = 0
count = 0
num = int(input("enter list of average(enetr 0 to opt out and get result):   "))
while  num != 0:
        count += 1 
        total += num
        numtotal = total / count          
        num = int(input("enter list of average(enetr 0 to opt out and get result):   "))

print("number", "=", total, "average", ":", numtotal)
