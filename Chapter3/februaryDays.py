"""
Instructions:
February normally has 28 days, but on leap years it has 29. 
Write a program that asks the user to enter a year. It should 
then display the number of days in February that year.
"""

year = int(input("Enter a year: "))
if (year % 100 == 0 and year % 400 == 0) or ( year % 100 != 0 and year % 4 == 0):
    print("In", year, "February has 29 days.")
else:
    print("In", year, "February has 28 days.")
