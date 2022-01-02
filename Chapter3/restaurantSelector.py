"""
Instructions:
Write a program that asks whether any members of your party are vegetarian, 
vegan, or gluten-fee, to which then displays only the restaurants to which 
you may take the group.

Restaurants:
Joe's Gourmet Burgers - Vegetarian: No, Vegan: No, Gluten-free: No
Main Street Pizza Company - Vegetarian: Yes, Vegan: No, Gluten-free: Yes
Corner Café - Vegetarian: Yes, Vegan: Yes, Gluten-free: Yes
Mama's Fine Italian - Vegetarian: Yes, Vegan: No, Gluten-free: No
The Chef's Kitchen - Vegetarian: Yes, Vegan: Yes, Gluten-free: Yes
"""

vegetarian = input("Is anyone in your party a vegetarian? ")
vegan = input("Is anyone in your party a vegan? ")
gluten = input("Is anyone in your party gluten-free? ")
print("Here are your restaurant choices:")
if vegetarian != "Yes" and vegan != "Yes" and gluten != "Yes":
    print("Joe's Gourmet Burgers")
if vegan != "Yes":
    print("Main Street Pizza Company")
print("Corner Café")
if vegetarian != "Yes":
    print("Mama's Fine Italian")
print("The Chef's Corner")
