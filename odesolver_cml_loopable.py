'''
CS 101 James Scholar Project
Exercise E.4: Solve an ODE specified on the command line

By Kenneth Tochihara
'''

#------------------------------------------------------------------------------#
# Libraries utilized                                                           #
#------------------------------------------------------------------------------#
from scitools.StringFunction import StringFunction
from scipy.optimize import newton
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#------------------------------------------------------------------------------#
# Constants using in the program                                               #
#------------------------------------------------------------------------------#

#Establishing method solve types
methods = {
    'fe' : "Forward-Euler Method",
    'mp' : "Midpoint Method",
    '2rk': "2nd-Order Runge-Kutta Method",
    '4rk': "4th-Order Runge-Kutta Method",
    '3ab': "3rd-order Adams-Bashforth Method",
    'be' : "Backward-Euler Method"
}

#------------------------------------------------------------------------------#
# Defining the functions utilized in this program                              #
#------------------------------------------------------------------------------#

# Setting functions for the different methods
def forwardEuler(u0, f):
    u = [u0]
    for i in range(len(arrT)-1):
        u.append(u[i] + dt * float(f(u[i], arrT[i])))
    return u

def midPoint(u0, f):
    u = [u0]
    for i in range(len(arrT)-1):
        us = u[i] + dt * float(f(u[i], arrT[i]))
        u.append(u[i] + (0.5 * dt * float(f(u[i], arrT[i]))) + (0.5 * dt * float(f(us, arrT[i+1]))))
    return u

def rungeKutta2(u0, f):
    u = [u0]
    for i in range(len(arrT)-1):
        k1 = dt * float(f(u[i], arrT[i]))
        k2 = dt * float(f(u[i] + 0.5 * k1, arrT[i] + 0.5 * dt))
        u.append(u[i] + k2)
    return u

def rungeKutta4(u0, f):
    u = [u0]
    for i in range(len(arrT)-1):
        k1 = dt * float(f(u[i], arrT[i]))
        k2 = dt * float(f(u[i] + 0.5 * k1, arrT[i] + 0.5 * dt))
        k3 = dt * float(f(u[i] + 0.5 * k2, arrT[i] + 0.5 * dt))
        k4 = dt * float(f(u[i] + k3, arrT[i] + dt))
        u.append(u[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4))
    return u

def adamBashforth3(u0, f, N):
    u = [u0]
    for i in range(len(arrT)-1):
        v = [u[i]]
        for j in range(N-1):
            v.append(u[i] + (1/5) * dt * (float(f(v[j], arrT[i+1])) + float(f(u[i], arrT[i]))))
        u.append(v[N-1])
    return u

def backwardEuler(u0, f):
    def findU(x):
        return u[i] + f(x, arrT[i]) * dt - x

    u = [u0]
    for i in range(len(arrT)-1):
        u.append(newton(findU, u0))
    return u

#------------------------------------------------------------------------------#
# UI Management                                                                #
#------------------------------------------------------------------------------#

# Clear the terminal for readability
print("\033c" + "*************************************************")
print("CS 101 James Scholar Project By Kenneth Tochihara")
print("*************************************************")
print("\nCtrl + C to exit at anytime. ")

# Infinite loop until KeyboardInterrupt
while True:

    try:
        # Taking in the values
        f    = StringFunction(input("f(u, t) =  "), independent_variables=('u','t'))
        u0   = float(input("u0 =  ")) #initial condition
        dt   = float(input("dt = "))  #time step
        T    = float(input("T = "))   #Final time of simulation
        type = str(input("Solve Method: "))

        #Initializing the u array, arrU and time array, arrT
        arrU = []
        currentT = 0
        arrT = [currentT]
        while (currentT < T) or (np.isclose(currentT, T)):
            currentT += dt
            arrT.append(currentT)

#------------------------------------------------------------------------------#
# Deciding which method to use                                                 #
#------------------------------------------------------------------------------#

        if   ('fe'  == type):
            arrU = forwardEuler(u0, f)
        elif ('mp'  == type):
            arrU = midPoint(u0, f)
        elif ('2rk' == type):
            arrU = rungeKutta2(u0, f)
        elif ('4rk' == type):
            arrU = rungeKutta4(u0, f)
        elif ('3ab' == type):
            N = int(input("N = "))
            arrU = adamBashforth3(u0, f, N)
        elif ('be' == type):
            arrU = backwardEuler(u0, f)
        else:
            print("Method did not match.")

#------------------------------------------------------------------------------#
# Saving the plot as a picture                                                 #
#------------------------------------------------------------------------------#
        # Plotting the function
        plt.plot(arrT, arrU, "bo")
        plt.show()
        plt.title("Solution to F: U vs. T (" + methods[type]+ ")")
        plt.xlabel("t")
        plt.ylabel("u")

        # Saving the file to directory Saved-Figures
        today = datetime.now()
        plt.savefig('Saved-Figures/plot_'+ today.isoformat()[:-7].replace(":", "-", 2)  + '.png')
        print( "Saved plot_"+ today.isoformat()[:-7] + ".png")
        plt.clf()

#------------------------------------------------------------------------------#
# End program                                                                  #
#------------------------------------------------------------------------------#

    except KeyboardInterrupt:
        print("You have successfully ended the program. ")
        break
