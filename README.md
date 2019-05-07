# CS 101 Project
## Exercise E.4: Solve an ODE specified on the command line 
We want to make a program **odesolver_cml.py** which accepts an ODE problem to be specified on the command line. The command-line arguments are `f`, `u0`, `dt`, and  `T`, where `f` is the right-hand side f(u, t) specified as a string formula, `u0` is the initial condition, `dt` is the time step, and `T` is the final time of the simulation. A fifth optional argument can be given to specify the name of the numerical solution method (set any method of your choice as default value). A curve plot of the solution versus time should be produced and stored in a file **plot.png**. 
- Use `StringFunction` from `scitools.StringFunction` for convenient conversion of a formula on the command line to a Python function. 
- Use the ODESolver hierarchy to solve the ODE and let the fifth command-line argument be the class name in the ODESolver hierarchy (E.3). Filename: **odesolver_cml.py**
