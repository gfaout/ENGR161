# Activity 2, Task 3
# File: Py2_ACT_Task3_gfotedar.py
# Date: 14 September 2018
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
# This function determines whether the integer inputted is negative, zero, 
# or positive.  If negative, it returns the output message as 'Error'.  If zero, 
# it returns the message that the factorial is 1.  If positive, it uses a for loop
# to find the factorial of a positive number and returns the message of the 
# factorial value.  
def MyFactorial(x):
    if x < 0:
        message = 'Error[Negative input].'
        return message
    elif x > 0:
        factorial = 1
        for i in range (x):
            factorial = factorial * (i + 1) 
        message = 'The factorial of ' + str(x) + ' is ' + str(factorial) + '.'
        return message
    else:
        message = 'The Factorial of 0 is 1.'
        return message
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
number = int(input('Enter a nonnegative integer: '))  #Number inputted by the user

#---------------------------------------------------
#  Computations
#---------------------------------------------------
message = MyFactorial(number)  #message to be outputted

#---------------------------------------------------
#  Outputs
#---------------------------------------------------
print(message)    #Final Output