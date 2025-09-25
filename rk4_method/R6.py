import numpy as np
import matplotlib.pyplot as plt
import R4_function as rf

from scipy import integrate
from pathlib import Path


def loop_through(t,omega, A, b, tf, y0):
    """
        THIS ISN'T REALLY A USABLE FUNCTION. IT'S INTENDED TO BE MERGED INTO YOUR REAL CODE

        This code plots the response for three different driving frequencies and displays
        the results on the same graph. It's important to note that the command plot(t,x)
        is placed within the loop.
    """

    # Loop through list of three driving frequencies (100%, 90%, 50% of omega0)
    for omegad in (omega, 0.9 * omega, 0.5 * omega):
        # Define the anonymous function, including the changing omegad
        lfun = lambda t, y,: rf.driven_pendulum(t, y, b, omega, A, omegad)
        # Call the solver for this definition of lfun
        result = integrate.solve_ivp(fun=lfun,
                                     t_span=(0, tf),
                                     y0=y0,
                                     method="RK45",
                                     t_eval=t)
        # Store result of this run in variables t, x, v
        t = result.t
        x, v = result.y
        # Plot the result x(t) for this run, lable it with omegad as well
        plt.plot(t, x)
    # End of loop, continue with next omegad
    # Out of the loop
    # Save and show plot
    plt.legend()  # Make the plot labels visible
    #plt.savefig('Oscillator-driven-multi.pdf', bbox_inches ='tight')
    plt.show()


def main():
   

    # define the initial parameters
    x0     = 1  # initial position
    v0     = 0  # initial velocity
    b      = 2
    omega0 = 1
    A = 1
    y0     = (x0, v0)  # initial state
    t0     = 0  # initial time

    # define the final time and the number of time steps
    tf = 5*np.pi  # final time
    n = 1001  # Number of points at which output will be evaluated
    # Note: this does not mean the integrator will take only n steps
    # Scipy will take more steps if required to control the error in the solution

    # creates an array of the time steps
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated

    #loop_through(t,omega0, A, b, tf, y0)
    print("Available names:", dir(rf))

if __name__ == '__main__':
    main()