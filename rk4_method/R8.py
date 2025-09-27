import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate
from pathlib import Path

def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path


def driven_pendulum(t, y, b, omega_0, A, omega_d):
    x, v = y
    dxdt = v
    dvdt = -b*v - (omega_0**2)*x - A * np.sin(omega_d * t)
    dydt = np.array([dxdt, dvdt])
    return dydt


def double_loop(y0, tf, n, omega_0, A):
    """
    The code in this function needs to be extracted and incorporated into existing code
    """
    # define an iterable (e.g. a list, numpy array) of damping coefficients
    # (put in your 5 different values of b here where 0 < b < 1):
    damping_coefficients = [0.05, 0.1, 0.2, 0.5, 1]

    # define the driving frequencies over which your inner loop will iterate
    # I recommend using a numpy linspace.
    # Consider: why am I defining this outside the loop?  Is that OK
    driving_frequencies = np.linspace(0, 2*omega_0, 100)

    # define your resonant frequency
    omega = 1.

    # creates an array of the time steps
    t = np.linspace(0.8*tf, tf, n)  # Points at which output will be evaluated

    # First (outer) loop through Damping coefficients
    for b in damping_coefficients:
        amplitudes = [] # Clear list to store amplitudes needs to be done for each b

        # Second (inner) loop through driving freq. define earlier!
        for omegad in driving_frequencies:
            # Define the anonymous function, including the changing omegad
            lfun = lambda t, y, : driven_pendulum(t, y, b, omega, A, omegad)

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
            # End of inner loop, continue with next omegad

        # Out of the inner loop
        # Save plot of amplitudes
        plt.plot(driving_frequencies, amplitudes,label = f"b = {b}")
        # End of outer loop
    plt.xlabel("$\omega$$_{d}$[$\omega$$_{0}$]")
    plt.ylabel("Amplitude")
    plt.legend()


def main():
   

    # define the initial parameters
    x0      = 0  # initial position
    v0      = 1  # initial velocity
    A       = 1
    omega_0 = 1
    y0      = (x0, v0)  # initial state
    t0      = 0  # initial time

    # define the final time and the number of time steps
    tf = 500  # final time
    n = 1001  # Number of points at which output will be evaluated
    # Note: this does not mean the integrator will take only n steps

    double_loop(y0, tf, n, omega_0, A)

    filename = generate_path(basename='R8_Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    plt.show()

if __name__ == '__main__':
    main()