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


def rf_vector(x, y, a, b, c, d):
    dx = a * x - b * x * y
    dy = c * x * y - d * y
    return dx, dy


def rabbit_fox(t, z, a, b, c, d):
    x, y = z
    dx = a * x - b * x * y
    dy = c * x * y - d * y
    return [dx, dy]


def plot_seed_points(x, y, dx, dy):
    seed_points = np.array([[2], [3]])  # initial position of (rabbit, fox)
    plt.streamplot(x, y, dx, dy, color='b', start_points=seed_points.T)
    plt.plot(seed_points[0], seed_points[1], 'bo')


def main():
    # Initial conditions and parameters
    y0 = (2, 3)       # initial rabbit and fox population
    t0 = 0
    tf = 10
    n = 501
    a, b, c, d = 4, 2, 1/3, 1  # model parameters

    # Create grid and vector field
    x, y = gr.grid_options(start=-1, stop=8, stepsize=1, numpoints=101, option="linspace")
    dx, dy = rf_vector(x, y, a, b, c, d)
    reduction = 5
    plt.figure(figsize=(12,4))
    # Plot the reduced vector density and seed points
    plt.subplot(1,3,1)
    plt.quiver(x[::reduction, ::reduction], y[::reduction, ::reduction],  # coordinates at reduced density
                   dx[::reduction, ::reduction], dy[::reduction, ::reduction],  # arrow x/y lengths at reduced density
                   pivot='mid'  # position of the pivot of the arrow
                   )  
    plot_seed_points(x, y, dx, dy)
    plt.title("(a)")
    plt.xlabel("Rabbits")
    plt.ylabel("Foxes")
    plt.legend()
    

    # Time domain for solving ODE
    t = np.linspace(t0, tf, n)

    # Integrate using RK45
    result = integrate.solve_ivp(
        fun=rabbit_fox,
        t_span=(t0, tf),
        y0=y0,
        method="RK45",
        args=(a, b, c, d),
        t_eval=t
    )

    # Extract results
    rabbits, foxes = result.y
    t = result.t

    # Phase plot (Rabbits vs Foxes)
    plt.subplot(1,3,2)
    plt.plot(rabbits, foxes, 'b-')
    plt.xlabel("Rabbits")
    
    plt.title("(b)")

    # Populations vs Time
    plt.subplot(1,3,3)
    plt.plot(t, rabbits, 'g-', label='Rabbits',linestyle = "--")
    plt.plot(t, foxes, 'r-', label='Foxes',linestyle = "--")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.legend()
    plt.title("(c)")

    filename = generate_path(basename='G5-Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    
    plt.show()


if __name__ == '__main__':
    main()
