import matplotlib.pyplot as plt
from scipy import integrate
import numpy as np
import graph_function as gr  # uses your functions

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
    seed_points = np.array([[4], [2]])  # initial position of (rabbit, fox)
    plt.streamplot(x, y, dx, dy, color='b', start_points=seed_points.T)
    plt.plot(seed_points[0], seed_points[1], 'bo', label="Initial point")


def main():
    # Initial conditions and parameters
    y0 = (4, 2)       # initial rabbit and fox population
    t0 = 0
    tf = 10
    n = 100
    a, b, c, d = 4, 2, 3/4, 1  # model parameters

    # Create grid and vector field
    x, y = gr.grid_options(start=-1, stop=5, stepsize=1, numpoints=101, option="linspace")
    dx, dy = rf_vector(x, y, a, b, c, d)

    # Plot the reduced vector density and seed points
    gr.reduced_density(x, y, dx, dy, label=0, x_pos=0.9, y_pos=0.9, key_size=0, reduction=5)
    plot_seed_points(x, y, dx, dy)
    plt.title("Rabbit-Fox Vector Field")
    plt.xlabel("Rabbits")
    plt.ylabel("Foxes")
    plt.legend()
    plt.show()

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
    plt.figure()
    plt.plot(rabbits, foxes, 'b-')
    plt.xlabel("Rabbits")
    plt.ylabel("Foxes")
    plt.title("Phase Plot: Rabbits vs Foxes")
    plt.show()

    # Populations vs Time
    plt.figure()
    plt.plot(t, rabbits, 'g-', label='Rabbits')
    plt.plot(t, foxes, 'r-', label='Foxes')
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.legend()
    plt.title("Population Over Time")
    plt.show()


if __name__ == '__main__':
    main()
