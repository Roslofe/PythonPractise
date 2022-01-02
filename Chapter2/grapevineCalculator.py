"""
Instructions:
A vineyard owner is planting several new rows of grapevines, and needs to know how many grapevines to plant in each row. 
She has determined that after measuring the length of a future row, she can use the following formula to calculate the 
nummber of vines that will fit in the row, along with the trellis end post assemblies that will need to be constructed 
at the end of each row: 
V=(R-2E)/S 
The terms in the formula are: 
V is the number of grapevines that will fit in the row. 
R is the length of the row, in feet. 
E is the amount of space, in feet, used by an end-post assembly. 
S is the space between vines, in feet. 
Write a program that makes the calculation for the vineyard owner. 
The program should ask the user to input the following: 
-The length of the row, in feet 
-The amount of space used by an end-post assembly, in feet 
-The amount of space in between the vines, in feet
"""

print("Welcome to grapevine calculator. Please provide all measurements in feet.")
R = int(input("Enter the length of the row: "))
E = int(input("Enter the amount of space used by the end-post assembly: "))
S = int(input("Enter the space in between the vines: "))
V = (R - 2 * E) / S
print("You can fit",  V, "vines in one row.")