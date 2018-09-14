# Activity 2 Task 4 Part C
# File: Py2_ACT_Task_nscarfe.py
# Date: 13 September 2018
# By: Nicholas Giovanni Scarfe
# nscarfe
# Stella Erickson
# ericks30
# Emily Tonkovich
# etonkovi
# Gautam Fotedar
# gfotedar
# Section: 1
# Team: 20
#
# ELECTRONIC SIGNATURE
# Nicholas Giovanni Scarfe
# Stella Erickson
# Emily Tonkovich
# Gautam Fotedar
#
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE PROGRAM OR FUNCTION DOES
# takes the unit vector of the hour hand on a clock and converts
# that to an hour
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
import math as m
x = input()
y = input()
#---------------------------------------------------
#  Computations
#---------------------------------------------------
def calcHour(xVec,yVec):
    return (m.atan2(-int(yVec),int(xVec)) * (180 / m.pi) + 105) / 30
#---------------------------------------------------
#  Outputs
#---------------------------------------------------
print(calcHour(x,y))