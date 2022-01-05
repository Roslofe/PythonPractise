"""
Instructions:
Write a program that uses nested loops to draw this pattern:
##
# #
#  #
#   #
#    #
#     #
"""

for num in range (5):
    print("#", end = '')
    for c in range (num):
        print(" ", end = '')
    print("#")