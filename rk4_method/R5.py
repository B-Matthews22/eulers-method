import numpy as np
import matplotlib.pyplot as plt
import R4_function as rf

from scipy import integrate
from pathlib import Path

def main():
   

    # define the initial parameters
    x0     = 0  # initial position
    v0     = 1  # initial velocity
    b      = 0.1
    omega0 = 1
    y0     = (x0, v0)  # initial state
    t0     = 0  # initial time

    # define the final time and the number of time steps
    tf = 5*np.pi  # final time
    n = 1001  # Number of points at which output will be evaluated
    # Note: this does not mean the integrator will take only n steps
    # Scipy will take more steps if required to control the error in the solution

    # creates an array of the time steps
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated

    lfun = lambda t, y, : rf.damped_pendulum(t, y, b, omega0)

    # Calls the method integrate.solve_ivp()
    result = integrate.solve_ivp(fun=lfun,  # The function defining the derivative
                                 t_span=(t0, tf),  # Initial and final times
                                 y0=y0,  # Initial state
                                 method="RK45",  # Integration method
                                 t_eval=t)  # Time points for result to be defined at

    # Read the solution and time from the result array returned by Scipy
    x, v = result.y
    t = result.t

    
    # Pre-initialize figure and axes
    fig, (ax_time, ax_phase) = plt.subplots(1, 2, figsize=(12, 5))

    # time evolution subplot
    ax_time.set_xlabel("Time (s)")
    ax_time.set_ylabel("Amplitiude")
    ax_time.plot(t, x, label=r"$x(t)$")
    ax_time.plot(t, v, label=r"$v(t)$")
    ax_time.legend(loc=1)
    

    # phase space subplot
    rf.phase_space(ax_phase, x, v)
    
    
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    #filename = generate_path(basename='Harmonic-init', extension='png')  # uses the function defined above

    # saves and displays the file
    #plt.savefig(filename, bbox_inches='tight')
    #print("Output file saved to {}.".format(filename))
    plt.show()

if __name__ == '__main__':
    main()