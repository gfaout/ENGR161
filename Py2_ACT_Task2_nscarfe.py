# Activity 2 Task 2 Part A and B
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
# This program takes differnt aspects of a rover and prints
# the distance the rover has driven and the required solar panel
# area power it
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
speed = 1
time = 2
power = 100
irradiance = 590
efficiency = 0.25
#---------------------------------------------------
#  Computations
#---------------------------------------------------
def distanceRover(speed,time):
    return (speed * time)

def solarPanelArea(requPow, solarIrradiance,matEfficiency):
    return (requPow/(solarIrradiance * matEfficiency))
#---------------------------------------------------
#  Outputs
#---------------------------------------------------
print(distanceRover(speed,time))
print(solarPanelArea(power, irradiance, efficiency))