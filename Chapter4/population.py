"""
Instructions:
Write a program predicting the approximate size of a 
population of organisms. The user should input the initial 
number of organisms, the daily increase, and the number of 
days the organisms will be left to multiply.
"""

print("To start, enter the following information:")
population = int(input("Starting number of organisms: "))
increase = float(input("Average daily increase (as a percentage): ")) / 100
days = int(input("Number of days to multiply: "))
print("Day Approximate\tPopulation")
for day in range(days):
    print(day + 1, "\t\t", population)
    population += population * increase
