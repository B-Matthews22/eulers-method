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


def diff_rl(t,i,v, r, l):
    """
    Calculates the change in current over time from the formula
    L(dI/dt) = V - RI
    """
    di_dt = (v-r*i)/l

    return di_dt 


def exact_solution_rl(v, r, l, t):
    """
    Calculates the change in current over time from the formula
    I = (V/R)(1-exp(-Rt/L))
    """
    i = (v/r)*(1-np.exp(-r*t/l))
    
    return i

def main():

    v   = 10
    r   = 50
    l   = 100
    i_0 = np.array([0])
    t_0 = 0
    t_f = 40
    n   = 101
    t   = np.linspace(t_0, t_f, n)

    result = integrate.solve_ivp(fun=diff_rl,  # The function defining the derivative
                                    t_span=(t_0, t_f),  # Initial and final times
                                    y0=i_0,  # Initial state
                                    method="RK45",  # Integration method
                                    args = (v,r,l),
                                    t_eval=t)  # Time points for result to be reported

    # Read the solution and time from the array returned by Scipy
    i = result.y[0]
    t = result.t

    i_exact = exact_solution_rl(v,r,l,t)
    plt.plot(t, i_exact,color = "r",label = "Exact")
    plt.plot(t,i, color = "k", linestyle = "-.", label = "Approximation")
    plt.xlabel("Time (s)")
    plt.ylabel("Current (A)")
    plt.legend()
     # creates the path to store the data. Note that the data is not stored in the code repo directory.
    filename = generate_path(basename='R2-Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    plt.show()
    
    err = []
    for x in range(len(i)):
        err.append(abs(i[x]-i_exact[x]))
    max_err = np.max(err)
    print(float(f"{max_err:.4f}"))

if __name__ == "__main__":
    main()