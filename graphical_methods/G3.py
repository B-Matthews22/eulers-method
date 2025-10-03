import matplotlib.pyplot as plt
import graph_function as gr
import numpy as np


def pendulum(x , v, b, omega):
    
    dxdt =  v
    dvdt = -b*v -(omega**2)*x

    return dxdt, dvdt


def main():
    start     = -2*np.pi
    stop      = 2*np.pi
    stepsize  = 0
    numpoints = 101
    
    x , v = gr.grid_options(start, stop, stepsize, numpoints, option = "linspace")
    dx, dv = pendulum(x, v, b = 2, omega = 1)
    gr.reduced_density(x, v, dx, dv, label = 0, x_pos=0.9, y_pos=0.9, key_size=2, reduction=5)
    #plt.streamplot(x, v, dx, dv)     # plot streamlines of field
    gr.density_change(x, v, dx, dv)  # plot less streamlines of field
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()