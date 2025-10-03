import matplotlib.pyplot as plt
import graph_function as gr
import numpy as np


def pendulum(x , v, b, omega):
    
    dxdt =  v
    dvdt = -b*v -(omega**2)*x

    return dxdt, dvdt


def main():
    start     = -np.pi
    stop      = np.pi
    stepsize  = 0
    numpoints = 101
    plt.close('all')
    x , v = gr.grid_options(start, stop, stepsize, numpoints, option = "linspace")
    dx, dv = pendulum(x, v, b = 2, omega = 1)
    plt.figure(figsize=(6,6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('v')
    plt.quiver(x, v, dx, dv)  # plot field as quiver
    plt.streamplot(x, v, dx, dv)  # plot streamlines of field.
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()