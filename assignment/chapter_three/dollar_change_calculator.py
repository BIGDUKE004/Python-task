item = int(input('enter amount of item ($):   '))
conv = item * 100

quaters1 = conv // 25
quaters2 = conv % 25

dimes1 = quaters2 // 10 
dimes1 = quaters2 % 10

pennies1 = dimes1

print(' your changes is: ')
print( quaters1, ' quarters ')
print(dimes1, ' dimes')
print(pennies1, ' pennies')
