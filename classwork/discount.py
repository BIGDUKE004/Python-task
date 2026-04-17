''' A program that shows the discount of whatever amount the user spent,
 so it collect an input from a user 
 access the amount entered 
calculate it and print out the money spent by the user and discount gotten '''

user_amount = int(input("Enter amount spent:       "))

discount1 = user_amount * 0.05
user_amount1 = ( user_amount - (user_amount * 0.05))    
discount2  = user_amount * 0.10 
user_amount2 = ( user_amount - (user_amount * 0.10))  
discount3  = user_amount * 0.10             
user_amount3 =  ( user_amount - (user_amount * 0.10))  
                                                                                                                                                                                                                                                                                                                        
 

if user_amount >= 1000 and user_amount <= 10000:
        print(f"your amount is = {user_amount1} \n your discount is {discount1}" )

elif user_amount > 10000 and user_amount <= 50000: 
         print(f"your amount is = {user_amount2} \n your discount is {discount2}" )

elif user_amount > 50000: 
         print(f"your amount is = {user_amount3} \n your discount is {discount3}" )


