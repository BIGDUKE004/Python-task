''' this program will determine whether or not if the password entered by the user is strong or not
start by collecting input from a user
evalute it and determine what category it falls into; sentinell loop would work well for this'''

user_password = input("ENTER YOUR PASSWORD:    ")
user_passwordlength = len(user_password)

if user_passwordlength < 8:
        print("very weak")

elif user_passwordlength >= 8 :
        print("weak")

elif user_passwordlenghth > 8 and user_passwordlength <= 16:
        print("strong")

elif  user_passwordlength >= 16:
        print("very strong")
