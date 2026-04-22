#a game that generate random numbers and tells the user if he failed or passed
import random
guess = 0
num = int(input("enter a number:     "))
for number in range(1):
 guess = random.randrange(1,100,1)
if num > guess:
        print(" higher")
elif num < guess:
        print("lower")
elif num == guess:
        print("correct")
