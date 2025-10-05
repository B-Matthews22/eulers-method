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
    b = [0,0.5,2,5]
    reduction = 5

    x , y = gr.grid_options(start, stop, stepsize, numpoints, option = "linspace")
    
    plt.figure(figsize=(8,8))
    plt.subplot(2,2,1)
    plt.gca().set_aspect('equal', adjustable='box')
    vx, vy = pendulum(x, y, b = 0, omega = 1)
    plt.quiver(x[::reduction, ::reduction], y[::reduction, ::reduction],  # coordinates at reduced density
                   vx[::reduction, ::reduction], vy[::reduction, ::reduction],  # arrow x/y lengths at reduced density
                   pivot='mid',  # position of the pivot of the arrow
                   label='SHO (b = 0)')  # label using LaTex notation
    #plt.streamplot(x, v, dx, dv)     # plot streamlines of field
    #gr.density_change(x, v, dx, dv)  # plot less streamlines of field
    gr.both_streamlines(x, y, vx, vy)
    plt.xlabel("x")
    plt.ylabel("v")
    plt.legend()
    
    plt.subplot(2,2,2)
    plt.gca().set_aspect('equal', adjustable='box')
    vx, vy = pendulum(x, y, b = 0.5, omega = 1)
    plt.quiver(x[::reduction, ::reduction], y[::reduction, ::reduction],  # coordinates at reduced density
                   vx[::reduction, ::reduction], vy[::reduction, ::reduction],  # arrow x/y lengths at reduced density
                   pivot='mid',  # position of the pivot of the arrow
                   label='b = 0.5')  # label using LaTex notation
    #plt.streamplot(x, v, dx, dv)     # plot streamlines of field
    #gr.density_change(x, v, dx, dv)  # plot less streamlines of field
    gr.both_streamlines(x, y, vx, vy)
    plt.xlabel("x")
    plt.ylabel("v")
    plt.legend(loc = 2)

    plt.subplot(2,2,3)
    plt.gca().set_aspect('equal', adjustable='box')
    vx, vy = pendulum(x, y, b = 2, omega = 1)
    plt.quiver(x[::reduction, ::reduction], y[::reduction, ::reduction],  # coordinates at reduced density
                   vx[::reduction, ::reduction], vy[::reduction, ::reduction],  # arrow x/y lengths at reduced density
                   pivot='mid',  # position of the pivot of the arrow
                   label='b = 2')  # label using LaTex notation
    #plt.streamplot(x, v, dx, dv)     # plot streamlines of field
    #gr.density_change(x, v, dx, dv)  # plot less streamlines of field
    gr.both_streamlines(x, y, vx, vy)
    plt.xlabel("x")
    plt.ylabel("v")
    plt.legend()

    plt.subplot(2,2,4)
    plt.gca().set_aspect('equal', adjustable='box')
    vx, vy = pendulum(x, y, b = 5, omega = 1)
    plt.quiver(x[::reduction, ::reduction], y[::reduction, ::reduction],  # coordinates at reduced density
                   vx[::reduction, ::reduction], vy[::reduction, ::reduction],  # arrow x/y lengths at reduced density
                   pivot='mid',  # position of the pivot of the arrow
                   label='b = 5')  # label using LaTex notation
    #plt.streamplot(x, v, dx, dv)     # plot streamlines of field
    #gr.density_change(x, v, dx, dv)  # plot less streamlines of field
    gr.both_streamlines(x, y, vx, vy)
    plt.xlabel("x")
    plt.ylabel("v")
    plt.legend(loc = 1)

    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()