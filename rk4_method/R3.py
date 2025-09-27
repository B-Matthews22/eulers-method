import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate
from pathlib import Path


def simple_pendulum(t, y, m, k):
    x, v = y  # extracts the x and v values from the tuple
    dydt = np.array([v, -(k/m) * x])  # generates an array with the rates of change: dxdt = v, dvdt = -x
    return dydt  # returns the array


def phase_space(ax, x, v, label = None):
    """Plot phase space (v vs. x) on a given Axes object."""
    ax.plot(v, x, 'k',label=label)
    ax.axis('equal')
    ax.set_xlabel(r"$Velocity$")
    ax.set_ylabel(r"$Position$")

def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path


def main():
   

    # define the initial parameters
    x0 = 0  # initial position
    v0 = 1  # initial velocity
    m = 2
    k = 0.3
    y0 = (x0, v0)  # initial state
    t0 = 0  # initial time

    # define the final time and the number of time steps
    tf = 50*np.pi  # final time
    n = 1001  # Number of points at which output will be evaluated
    # Note: this does not mean the integrator will take only n steps
    # Scipy will take more steps if required to control the error in the solution

    # creates an array of the time steps
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated

    # Calls the method integrate.solve_ivp()
    result = integrate.solve_ivp(fun=simple_pendulum,  # The function defining the derivative
                                 t_span=(t0, tf),  # Initial and final times
                                 y0=y0,  # Initial state
                                 method="RK45",
                                 args = (m,k), # Integration method
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
    phase_space(ax_phase, x, v)
    
    
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    filename = generate_path(basename='R3-Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    plt.show()

if __name__ == '__main__':
    main()