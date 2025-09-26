import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate
from pathlib import Path



def driven_pendulum(t, y, b, omega_0, A, omega_d):
    x, v = y
    dxdt = v
    dvdt = -b*v - (omega_0**2)*x - A * np.sin(omega_d * t)
    dydt = np.array([dxdt, dvdt])
    return dydt


def amplitudes(tf, n, omega_0, b, A, y0):

    amplitudes = []  # Create empty list to store amplitudes
    t = np.linspace(0.8*tf, tf, n)  # Change time array to include only later points

    driving_freq = np.linspace(0, 2*omega_0, 200)  # Create range of omega_d 20%-200% of omega_0

    # Loop through driving frequencies
    for omega_d in driving_freq:
        # Define the anonymous function, including the changing omegad
        lfun = lambda t, y, : driven_pendulum(t, y, b, omega_0, A, omega_d)
        # Call the solver for this definition of lfun
        result = integrate.solve_ivp(fun=lfun,
                                     t_span=(0, tf),
                                     y0=y0,
                                     method="RK45",
                                     t_eval=t)

        # Store result of this run in variables t, x, v
        t = result.t
        v, x = result.y

        amplitudes.append((max(x)-min(x))/2)  # Find peak to peak amplitude
        # End of loop, continue with next omegad
    # Out of the loop
    # Plot the amplitudes
    plt.plot(driving_freq, amplitudes)
    plt.show()


def main():
   

    # define the initial parameters
    x0      = 1  # initial position
    v0      = 0  # initial velocity
    b       = 0.5
    A       = 0.5
    omega_0 = 1
    y0      = (x0, v0)  # initial state
    t0      = 0  # initial time

    # define the final time and the number of time steps
    tf = 20*np.pi  # final time
    n = 1001  # Number of points at which output will be evaluated
    # Note: this does not mean the integrator will take only n steps
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated

    amplitudes(tf, n, omega_0, b, A, y0)

if __name__ == '__main__':
    main()