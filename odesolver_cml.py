'''
CS 101 James Scholar Project
Exercise E.4: Solve an ODE specified on the command line

By Kenneth Tochihara
'''

#------------------------------------------------------------------------------#
# Libraries utilized                                                           #
#------------------------------------------------------------------------------#
from scitools import StringFunction
import numpy as np
import matplotlib.pyplot as plt


#------------------------------------------------------------------------------#
# Constants using in the program                                               #
#------------------------------------------------------------------------------#

#Establishing method solve types
methods = {
    'fe' : "Forward-Euler Method",
    'mp' : "Midpoint Method",
    'h'  : "Heum's Method",
    '2rk': "2nd-Order Runge-Kutta Method",
    '4rk': "4th-Order Runge-Kutta Method",
    '3ab': "3rd-order Adams-Bashforth Method"
}

# Taking in the values
f    = StringFunction(input("f(u, t) =  "), independent_variables=('u','t'))
u0   = float(input("u0 =  "))
dt   = float(input("dt = "))
T    = float(input("T = "))
type = input("Solve Method: ")

#Calclating the time array, arrT
arrT = [0]
currentT = 0
while currentT < T:
    arrT.append(currentT + dt)
arrT.append(T)


#------------------------------------------------------------------------------#
# Defining the functions utilized in this program                              #
#------------------------------------------------------------------------------#

# Setting functions for the different methods
def forwardEuler(u0, arrT, f ,T):
    return 0

def midPoint(u0, arrT, f ,T):
    return 0

def heum(u0, arrT, f ,T):
    return 0

def rungeKutta2(u0, arrT, f ,T):
    return 0

def rungeKutta4(u0, arrT, f ,T):
    return 0

def adamBashforth3(u0, arrT, f ,T):
    return 0

def backwardEuler(u0, arrT, f ,T):
    return 0


#------------------------------------------------------------------------------#
# Deciding which method to use (Forward-Euler is default)                      #
#------------------------------------------------------------------------------#

if   ('fe'  == type):
    arrU = forwardEuler(u0, arrT, f ,T)
elif ('mp'  == type):
    arrU = midPoint(u0, arrT, f ,T)
elif ('h'   == type):
    arrU = heum(u0, arrT, f ,T)
elif ('2rk' == type):
    arrU = rungeKutta2(u0, arrT, f ,T)
elif ('4rk' == type):
    arrU = rungeKutta4(u0, arrT, f ,T)
elif ('3ab' == type):
    arrU = adamBashforth3(u0, arrT, f ,T)
else:
    arrU = forwardEuler(u0, arrT, f ,T)


#------------------------------------------------------------------------------#
# Saving the plot as a picture                                                 #
#------------------------------------------------------------------------------#

plt.plot(arrU, arrT, "b-")
plt.title("Solution to F: U vs. T (" + method[type]+ ")")
plt.xlim(0, T)
plt.xlabel("t")
plt.ylabel("u")
plt.savefig('plot.png')
