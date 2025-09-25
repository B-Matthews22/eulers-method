import numpy as np


def damped_pendulum(t, y, b, omega0):
    x, v = y
    dxdt = v
    dvdt = -b*v-(omega0**2)*x
    dydt = np.array([dxdt, dvdt])
    return dydt


def phase_space(ax, x, v, label = None):
    """Plot phase space (v vs. x) on a given Axes object."""
    ax.plot(v, x, 'k',label=label)
    ax.axis('equal')
    ax.set_xlabel(r"$Position$")
    ax.set_ylabel(r"$Velocity$")