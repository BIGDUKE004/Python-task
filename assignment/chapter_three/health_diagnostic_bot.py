""" this script will collect input from a user and give out hardcoded response 
collect input
assign input as none
give out response 
and goes again asking input from the user the second time and giving our an hardcoded answer"""


user_response = input("What is your problem? type exit to quit:      ")
user_respone_one = input("Have you had this problem before? (yes / no)  ")
if user_respone_one == "yes":
        print("well,so sorry to say this but you have it again")
elif user_respone_one == "no":
        print("well, so sorry to break this with you, you have it now")

