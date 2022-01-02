"""
Instructions:
The formula for calculating compound interest is:
A = P(1+r/n)^(nt)
The terms in the formula are: 
A is the amount of money in the account after the specified number of years.
P is the principal amount that was originally deposited into the account
r is the annual interest rate
n is the number of times per year that the interest is compounded
t is the specified number of years

Write a program that makes the calculation for you. The program should the user to input the following:
- The amount of principal originally deposited into the account
- The annual interest rate paid by the account, as a percentage
- The number of times per year that the interest is compounded
- The number of years the account will be left to earn interest
"""

print("Welcome to compoud interest calulator.")
P = float(input("Enter the amount of money originally deposited into the account in Euros: "))
r = int(input("Enter the annual interest rate, as a percentage: ")) / 100
n = int(input("Enter the number of times interest is compounded per year: "))
t = int(input("Enter the numer of years the account will be earning interest: "))
A = round(P * (1 + (r / n)) ** (n * t))
print("After", t, "years, the account will have", A, "€.")