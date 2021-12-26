import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from scipy.integrate import odeint


# Initial Conditions
# x'' + gamma x' + k x = cos(omega t)
# x(0) = x0
# x'(0) = xp0
def harmonic_oscillator(gamma, k, omega, x0 = 0, xp0 = 0, steps=500, t = None):
    def derivs(f, t):
        x, xprime = f
        dfdt = [xprime, np.cos(omega * t) - k * x - gamma * xprime]
        return dfdt
    if any(t == None):
        t = np.linspace(0, 50, steps)
    x = odeint(derivs, [x0,xp0], t)[:,0]
    return x

# Define initial parameters
init_gamma = 0
init_k = 1
init_omega = 0

steps = 500
t = np.linspace(0, 50, steps)

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots(figsize=(12,8))
x = harmonic_oscillator(init_gamma, init_k, init_omega, t=t)
xmin = min(x)
xmax = max(x)
line, = plt.plot(t, x, lw=2)
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_ylim([xmin,xmax])
ax.set_title("Solution to x\'\' + gamma x\' + k x = cos(omega t)")

plt.subplots_adjust(left=.1,bottom=.25)

axes = plt.axes([0.1, 0.17, 0.8, 0.02])
k_slider = Slider(
    ax=axes,
    label='k',
    valmin= 1,
    valmax= 5,
    valinit=init_k,
)

axes = plt.axes([0.1, 0.12, 0.8, 0.02])
gamma_slider = Slider(
    ax=axes,
    label='gamma',
    valmin= 0,
    valmax= 1,
    valinit=init_gamma,
)

axes = plt.axes([0.1, 0.07, 0.8, 0.02])
omega_slider = Slider(
    ax=axes,
    label='omega',
    valmin= 0,
    valmax= 2*np.pi,
    valinit=init_omega,
)

# The function to be called anytime a slider's value changes
def update(val):
    x = harmonic_oscillator(gamma_slider.val, k_slider.val, omega_slider.val,
                            t=t)
    line.set_ydata(x)
    xmin = min(*x)
    xmax = max(*x)
    ax.set_ylim([xmin,xmax])
    fig.canvas.draw_idle()


# register the update function with each slider
gamma_slider.on_changed(update)
k_slider.on_changed(update)
omega_slider.on_changed(update)

plt.show()

