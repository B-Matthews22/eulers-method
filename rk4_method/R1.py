# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from pathlib import Path

# define the nonlinear derivative function
def nonlinear1(t, y,a,b):
    """
    Calculates the derivative value for the differential equation given in experiment R1
    """
    # Calculate the derivative explicitly
    dydt = -a*y**3 + b*np.sin(t)

    # return the value
    return dydt


def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path


def main():
    """
    A main function used to ensure that the code is portable. By using if __name__ == '__main__': main() we can ensure
    that python will not execute the code when functions or methods in this module are imported, only if we run it
    directly. At this point, this structure isn't needed, but it's a good habit to get into.
    :return:
    """
    # define the initial variables
    a = [1,4,20] 
    b = [1,20,0.5]
    y0 = np.array([0])  # initial state at t = 0
    t0 = 0  # initial time
    tf = 20  # final time
    n = 101  # Number of points at which output will be evaluated (note 101 points are needed for 100 spaces)
    # Note: this does not mean the integrator will take only n steps SciPy
    # will control this to control the error in the solution

    # create a numpy array of n times linearly spaced between t0 and tf
    t = np.linspace(t0, tf, n)

    # Call the RK integrator and return the solution in the array "result"
    # Note that because the brackets aren't closed, the method integrate.solve_ivp()
    # behaves as though it was on just one line.
    for a, b in zip(a,b):
        result = integrate.solve_ivp(fun=nonlinear1,  # The function defining the derivative
                                    t_span=(t0, tf),  # Initial and final times
                                    y0=y0,  # Initial state
                                    method="RK45",  # Integration method
                                    args = (a,b),
                                    t_eval=t)  # Time points for result to be reported

        # Read the solution and time from the array returned by Scipy
        y = result.y[0]
        t = result.t

        # plot the solution
        plt.plot(t,y,label = f"a = {a}, b = {b}")
    plt.legend()
    plt.xlabel("Time t")
    plt.ylabel("Amplitude")
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    filename = generate_path(basename='R1-Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    plt.show()


if __name__ == '__main__':
    main()