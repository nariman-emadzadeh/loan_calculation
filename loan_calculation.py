import numpy as np

type_of_loan = input("What type of loan are you looking to pay off?")
user_loan = str(type_of_loan)

principal = input("What is the initial amount you barrowed? ")
user_prinicipal = int(principal)

interest_rate = input("What is your interest rate on your loan? ")
user_i = (float(interest_rate)/100)/12

n_payments = input("What is the number of payments over the life of the loan?\
 Ex) If you take out a 30- year fixed rate mortgage, 30 years\
   12 months per year would be 360 payments")
user_n_payments = int(n_payments)

monthly_loan_payment = user_prinicipal*(user_i*(1+user_i)**user_n_payments)/((1+user_i)**user_n_payments-1)
print("Your monthly", user_loan, "payment is: $", monthly_loan_payment)

total_payments = monthly_loan_payment * user_n_payments
print("Total payment paid over the duration of the loan: $", total_payments)
