#calculator with user input 
print("welcome to organic's mortgage calculator!") #intro message <3
mortgage = int(input("whats the amount of your mortgage ? \n")) #gets user input for principle
tenure = int(input("how many years is your mortgage ? \n")) #gets user input for length 
interest = float(input("what is the interest rate on your mortgage as a percentage ? \n")) #gets user input for interest rate

total_amount = mortgage*(1+(interest/100))**tenure #total amount calculated using mortgage formula
monthly_payment = total_amount/(tenure*12) #monthly payment calculated using average
interest = total_amount - mortgage #calculates total interest sum

total_amount_paid = round(total_amount, 2) #rounds total amount to 2 decimals
monthly_payment_paid = round(monthly_payment, 2) #rounds monthly payment to 2 decimals
interest_paid = round(interest, 2) #round total interest to 2 decimals

print("total amount paid :", total_amount_paid) 
print("monthly payment :", monthly_payment_paid)
print("total interest paid :", interest_paid)

