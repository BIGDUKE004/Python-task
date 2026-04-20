digit = int(input("enter a digit:  "))

while  digit  > 0:
        rev = digit % 10        
        digit = digit // 10
        print(rev)
       
