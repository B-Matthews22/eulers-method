import matplotlib.pyplot as plt
from scipy import integrate
import numpy as np
import graph_function as gr 


def generate_path(home_folder= 'C:/Users/HP/', subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path


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
    y0 = [(0.1, 0.1),(3,3),(1.5,-1.5),(-2,2),(0.5,1)]      
    t0 = 0
    tf = 30
    n = 501
    # Time domain for solving ODE
    t = np.linspace(t0, tf, n)

    # Create grid and vector field
    x, y = gr.grid_options(start=-3, stop=3, stepsize=1, numpoints=101, option="linspace")
    dx, dy = vectorf(x, y)

    plt.figure(figsize=(12,4))
    plt.subplot(1,3,1)

    reduction = 5
    # Plot the reduced vector density and seed points
    plt.quiver(x[::reduction, ::reduction], y[::reduction, ::reduction],  # coordinates at reduced density
                dx[::reduction, ::reduction], dy[::reduction, ::reduction],  # arrow x/y lengths at reduced density
                pivot='mid')
    gr.colour_streamlines(x, y, dx, dy)
    plt.xlabel("x")
    plt.ylabel("y")

    plt.subplot(1,3,2)
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

        plt.plot(x,y,label = f"x$_0$={init[0]}, y$_0$={init[0]}")
    
    x_vals = np.linspace(-3, 3, 400)
    y_isocline = x_vals / (1 - x_vals**2)  # y-isocline
    plt.plot(x_vals, np.zeros_like(x_vals), 'r--')  # x-isocline
    plt.plot(x_vals, y_isocline, 'g--')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.xlabel("x")
    plt.legend(fontsize=8)
    
    plt.subplot(1,3,3)
    plt.plot(t,x,label="x(t), x$_0$= 1.5")
    plt.plot(t,y,label="y(t), y$_0$= 1.5")
    plt.xlabel("t")
    plt.ylabel("x(t), y(t)")
    plt.legend()
    filename = generate_path(basename='G6-Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    
    plt.show()
if __name__ == '__main__':
    main()
