import numpy as np
import matplotlib.pyplot as plt

#m y'' + tau y' + k y = F cos(omega t)
m = 1
tau = 0
k = 1
F = 1

# Initial Conditions
t0=0
y0=0

t1=0
doty1=0



# Plotting the solution
plt.plot(x,y)
plt.quiver(xv,yv,1,dy(xv,yv))
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximate solution using Euler's method")
plt.show()
