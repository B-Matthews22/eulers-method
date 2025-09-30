import matplotlib.pyplot as plt
import numpy as np
import graph_function as gr


def get_vector(x, y):
    """
    x and y should be of the same length for most applications you'd use this for,
    but this function doesn't check
    """
    vx = np.cos(x) * y
    vy = np.sin(y) * x

    return vx, vy


def add_legend(x, y, vx, vy, x_pos=0.9, y_pos=0.9, key_size=2):
    """
    This function demonstrates how to add a key to your quiverplot. In addition to plotting the quiverplot
    It also puts the key at the x and y positions specified and with a size the user can specify
    """

    # plots the quiverplot. The return value of plt.quiver (an "Artist" datatype which contains the data
    # needed to draw the arrows) is returned to the variable q.
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    q = plt.quiver(x, y, vx, vy, pivot='mid', label='$v_x$ = cos($x$), $v_y$ = sin($y$)')

    # This then is passed to plt.quiverkey so the key knows what data it represents
    plt.quiverkey(q, x_pos, y_pos, key_size, r'2 $\frac{m}{s}$', labelpos='E', coordinates='figure')
    plt.show()
    return q


def main():
    start     = 0
    stop      = 2*np.pi
    stepsize  = 0
    numpoints = 21
    option    = "linspace"

    x , y   = gr.grid_options(start, stop, stepsize, numpoints, option)
    vx , vy = get_vector(x , y)

    add_legend(x, y, vx, vy)


if __name__ == '__main__':
    main()