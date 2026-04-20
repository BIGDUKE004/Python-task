""" this is a nested for loop, the first for loop is to make the nested loop inside of it to print 10 times, while the nested loop is to print 10 times in every loop the first loop goes. so there's if else statement in it instructing the program to print < if the number displayed is divisible by 2 and have a remiander and > if theres no remainder and the new line embedded in the print was override to just only put spaces inbetween the text generated and not enter a new line for every text generated
"""

for row in range(10):
        for row in range(10):
                print('<' if row % 2 == 1  else '>', end='')
        print()

