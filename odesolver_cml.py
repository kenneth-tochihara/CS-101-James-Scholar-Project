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
    '2rk': "2nd-Order Runge-Kutta Method",
    '4rk': "4th-Order Runge-Kutta Method",
    '3ab': "3rd-order Adams-Bashforth Method"
}

# Taking in the values
f    = StringFunction(input("f(u, t) =  "), independent_variables=('u','t'))
u0   = float(input("u0 =  ")) #initial condition
dt   = float(input("dt = "))  #time step
T    = float(input("T = "))   #Final time of simulation
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
def forwardEuler(u0, arrT, f):
    u = [u0]
    for i in range(1, len(arrT)):
        u.append(u[i-1] + dt * f(u[i-1], arrT[i-1]))
    return u

def midPoint(u0, arrT, f ,T):
    u = [u0]
    for i in range(1, len(arrT)):
        us = u[i-1] + dt * f(u[i-1], arrT[i-1])
        u.append(u[i-1] + (0.5 * dt * f(u[i-1], arrT[i-1])) + (0.5 * dt * f(us, arrT[i])))
    return u

def rungeKutta2(u0, arrT, f ,T):
    u = [u0]
    for i in range(1, len(arrT)):
        k1 = dt * f(u[i-1], arrT[i-1])
        k2 = dt * f(u[i-1] + 0.5 * k1, arrT[i-1] + 0.5 * dt)
        u.append(u[i-1] + k2)
    return u

def rungeKutta4(u0, arrT, f ,T):
    u = [u0]
    for i in range(1, len(arrT)):
        k1 = dt * f(u[i-1], arrT[i-1])
        k2 = dt * f(u[i-1] + 0.5 * k1, arrT[i-1] + 0.5 * dt)
        k3 = dt * f(u[i-1] + 0.5 * k2, arrT[i-1] + 0.5 * dt)
        k4 = dt * f(u[i-1] + k3, arrT[i-1] + dt)
        u.append(u[i-1] + k2)
    return u

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
