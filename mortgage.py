#calculator with user input 
print("welcome to organic's mortgage calculator!") #intro message <3

#gets user input for each item
mortgage = int(input("whats the amount of your mortgage ? \n"))
tenure = int(input("how many years is your mortgage ? \n"))
interest = float(input("what is the interest rate on your mortgage as a percentage ? \n"))

#calculate all total items using compound interest formula
total_amount = mortgage*(1+(interest/100))**tenure 
monthly_payment = total_amount/(tenure*12) 
interest = total_amount - mortgage 

#round all items to 2 decimals
total_amount_paid = round(total_amount, 2)
monthly_payment_paid = round(monthly_payment, 2)
interest_paid = round(interest, 2)

#display all items using print
print("total amount paid :", total_amount_paid) 
print("monthly payment :", monthly_payment_paid)
print("total interest paid :", interest_paid)

#function version
def calc(mortgage, tenure, interest) : #initialises calc function

  #calculate all total items using compound interest formula
  total_amount = mortgage*(1+(interest/100))**tenure 
  monthly_payment = total_amount/(tenure*12)
  interest = total_amount - mortgage

  #round all items to 2 decimals
  total_amount_paid = round(total_amount, 2)
  monthly_payment_paid = round(monthly_payment, 2)
  interest_paid = round(interest, 2)

  #creates string elements for each item
  first = f"total amount paid : {total_amount_paid}" 
  second = f"monthly payment : {monthly_payment_paid}"
  third = f"total interest paid : {interest_paid}"

  #create output list by appending all string elements
  output = []
  output.append(first)
  output.append(second)
  output.append(third)

  #creates loop to display first two elements in list
  while len(output) > 1 :
    print(output[0])
    output = output[1:]

  #returns last element in list
  if len(output) == 1 :
    return output[0]
