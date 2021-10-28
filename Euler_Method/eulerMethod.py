# Code for an Euler's method visualizer
import numpy as np
import matplotlib.pyplot as plt

#Example difeq of the form y' = dy(x,y)
def dy(x,y):
    return np.sin(y)/(3*x + 1) - np.cos(x)


# Plots a visualization of Euler's method with n steps up to input target xf
# for equation y' = dy with initial conditions y(x0) = y0. 
def Eulers_method(dy, xf=10, x0=0, y0=0, n=500):
    if xf < x0:
        raise ValueError('Initial input less than target input: \ninitial input = %d\ntarget input = %d' % (x0, xf))
        return
    deltax=(xf-x0)/n
    x=np.linspace(x0,xf,n+1)
    y=np.zeros([n+1])

    # For loop for Euler's method
    miny, maxy = y0, y0
    y[0]=y0
    for i in range (1,n+1):
        y[i]=deltax*dy(x[i-1],y[i-1])+y[i-1]
        miny, maxy = min(miny,y[i]), max(maxy,y[i])

    #Initializing VectorField
    xv,yv = np.meshgrid(np.linspace(x0,xf,15), np.linspace(miny,maxy,15))

    # Plotting the solution
    print('dy:')
    print(dy(xv,yv))
    print(type(dy(xv,yv)))
    ones = np.ones((15,15))
    plt.plot(x,y)
    plt.quiver(xv,yv,ones,dy(xv,yv), angles='xy')
    plt.xlabel("Value of x")
    plt.ylabel("Value of y")
    plt.title("Approximate solution using Euler's method")
    plt.show()
    return plt
