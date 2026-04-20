total = 0
product = 1
ave = 0

for numbers in range(4):    
        user_value = int(input(" enter an integer:    "))
        

        total += user_value
        product *= user_value

ave = total / 4

print("total sum is:",total)
print("product is:",product)
print("average is:",ave)

