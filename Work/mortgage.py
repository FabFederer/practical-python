# mortgage.py
#
# Exercise 1.7
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage,
# Stock Investment, and Bitcoin trading corporation.
# The interest rate is 5% and the monthly payment is $2684.11.
# Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:

principal = 500000.00
interest_rate = 0.05
payment = 2684.11
total_paid = 0
month = 0
extra_payment_start_month = 1
extra_payment_end_month = 12
extra_payment = 1000

while principal > 0:
    month = month + 1
    principal = principal * (1 + interest_rate / 12) - payment
    total_paid = total_paid + payment
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(month, round(total_paid, 2), round(principal, 2))


print("Total paid", round(total_paid, 2))