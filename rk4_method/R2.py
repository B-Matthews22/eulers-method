import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

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

    v   = 2
    r   = 2
    l   = 2
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

    plt.plot(t,i)
    plt.show()

if __name__ == "__main__":
    main()