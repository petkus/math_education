import numpy as np
import matplotlib.pyplot as plt

# Plots a visualization of Euler's method with n steps up to input target xf
# for equation y' = dy with initial conditions y(x0) = y0. vector_plots
# determines how many vectors to plot on the vectorfield.
def eulers_method(dy, xf=10, x0=0, y0=0, n=500, vector_plots=20):
    if xf < x0:
        raise ValueError('Initial input less than target input: \ninitial input = %d\ntarget input = %d' % (x0, xf))
    deltax=(xf-x0)/n
    x=np.linspace(x0,xf,n+1)
    y=np.zeros([n+1])

    miny, maxy = y0, y0
    y[0]=y0
    for i in range (1,n+1):
        y[i]=deltax*dy(x[i-1],y[i-1])+y[i-1]
        miny, maxy = min(miny,y[i]), max(maxy,y[i])
    xv,yv = np.meshgrid(np.linspace(x0,xf,vector_plots),
                        np.linspace(miny,maxy,vector_plots))

    # Plotting the solution
    ones = np.ones((vector_plots,vector_plots))
    plt.plot(x,y)
    plt.quiver(xv,yv,ones,dy(xv,yv), angles='xy')
    plt.xlabel("Value of x")
    plt.ylabel("Value of y")
    plt.title("Approximate solution using Euler's method")
    plt.show()
    return plt
