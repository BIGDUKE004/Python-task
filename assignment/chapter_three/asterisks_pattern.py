driver = 0
miles = float(input("enter the miles driven (-1 to end):    "))
gallons = float(input("enter the gallon used (-1 to end):    "))

while driver != -1:
        driver += 1
        gallons += driver
        miles += driver
        print(miles / gallons)
        gallons = float(input("enter the gallon used (-1 to end):    "))
        miles = float(input("enter the miles driven (-1 to end):    "))
        


