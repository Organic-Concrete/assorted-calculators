print("welcome to brayans mortgage calculator!")
mortgage = int(input("whats the amount of your mortgage ? \n"))
tenure = int(input("how many years is your mortgage ? \n"))
interest = float(input("what is the interest rate on your mortgage as a percentage ? \n"))

total_amount = mortgage*(1+(interest/100))**tenure
monthly_payment = total_amount/(tenure*12)
interest = total_amount - mortgage

total_amount_paid = round(total_amount, 2)
monthly_payment_paid = round(monthly_payment, 2)
interest_paid = round(interest, 2)

print("total amount paid :", total_amount_paid)
print("monthly payment :", monthly_payment_paid)
print("total interest paid :", interest_paid)
