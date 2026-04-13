principal = input(" put in principal amount:   ")
principal = float(principal)

annual_rate = input(" put in interest rate:   ")
annual_rate = float(annual_rate)

duration = input(" put in your duration in years:   ")
duration = float(duration)


monthly_rate = (annual_rate / 100) / 12
month = duration * years

print (principal * (monthly_rate * (1 + monthly_rate) ** month) // ((1 + monthly_rate) ** month - 1 ))
