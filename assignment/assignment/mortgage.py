principal = input(" put in principal amount:   ")
principal = float(principal)

interest = input(" put in interest rate:   ")
interest = float(interest)

duration = input(" put in your duration in years:   ")
duration = float(duration)

duration = float (duration * 12 )
interest =  float (interest / 12 )



print(principal * (interest * (1 + interest) ** duration) / (1 + interest) ** duration - 1)
