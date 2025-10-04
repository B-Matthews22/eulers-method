import matplotlib.pyplot as plt
import graph_function as gr
import numpy as np

def rabbit_fox(x, y, a, b, c, d):
    
    dx = a*x - b*x*y
    dy = c*x*y - d*y

    return dx,dy


def add_legend(x, y, vx, vy, label, x_pos=0.9, y_pos=0.9, key_size=2):
    """
    This function demonstrates how to add a key to your quiverplot. In addition to plotting the quiverplot
    It also puts the key at the x and y positions specified and with a size the user can specify
    """
    # plots the quiverplot. The return value of plt.quiver (an "Artist" datatype which contains the data
    # needed to draw the arrows) is returned to the variable q.
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    q = plt.quiver(x, y, vx, vy, pivot='mid', label=f'{label}')

    # This then is passed to plt.quiverkey so the key knows what data it represents
    plt.quiverkey(q, x_pos, y_pos, key_size, r'2 $\frac{m}{s}$', labelpos='E', coordinates='figure')
    plt.legend()
    return q


def main():
    start      = -1
    stop       = 5
    stepsize   = 1
    numpoints  = 101
    a, b, c, d = 4, 2, (3/4), 1

    x , y = gr.grid_options(start, stop, stepsize, numpoints, option = "linspace")
    dx, dy = rabbit_fox(x, y, a, b, c, d)
    #add_legend(x, y, dx, dy, label = "meow", x_pos=0.9, y_pos=0.9, key_size=2)
    gr.reduced_density(x, y, dx, dy, label = 0, x_pos=0.9, y_pos=0.9, key_size=2, reduction=5)
    #plt.streamplot(x, v, dx, dv)     # plot streamlines of field
    #gr.density_change(x, y, dx, dy)  # plot less streamlines of field
    plt.show()

if __name__ == '__main__':
    main()