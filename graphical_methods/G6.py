import matplotlib.pyplot as plt
from scipy import integrate
import numpy as np
import graph_function as gr 

def vectorf(x, y):
    dx = y
    dy = -x +(1-x**2)*y
    return dx, dy

def ode(t, z):
    x, y = z
    dx = y
    dy = -x +(1-x**2)*y
    return [dx, dy]


def main():
    # Initial conditions and parameters
    y0 = [(0.1, 0.1),(-2,2),(3,3),(0.5,1)]      
    t0 = 0
    tf = 30
    n = 501

    # Create grid and vector field
    x, y = gr.grid_options(start=-1, stop=1, stepsize=1, numpoints=101, option="linspace")
    dx, dy = vectorf(x, y)

    # Plot the reduced vector density and seed points
    gr.reduced_density(x, y, dx, dy, label=0, x_pos=0.9, y_pos=0.9, key_size=0, reduction=5)
    plt.xlabel("x(t)")
    plt.ylabel("y(t)")
    
    plt.legend()
    plt.show()

     # Time domain for solving ODE
    t = np.linspace(t0, tf, n)

    plt.figure()
    for init in y0:
    # Integrate using RK45
        result = integrate.solve_ivp(
            fun=ode,
            t_span=(t0, tf),
            y0=init,
            method="RK45",
            t_eval=t
        )

        # Extract results
        x, y = result.y
        t = result.t

        plt.plot(x,y)
    plt.show()
if __name__ == '__main__':
    main()
