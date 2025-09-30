import matplotlib.pyplot as plt
import numpy as np
import graph_function as gr


def get_vector(x, y):
    """
    x and y should be of the same length for most applications you'd use this for,
    but this function doesn't check
    """
    vx = np.cos(x)
    vy = np.sin(y)

    return vx, vy


def add_legend(x, y, vx, vy, x_pos=0.9, y_pos=0.9, key_size=2):
    """
    This function demonstrates how to add a key to your quiverplot. In addition to plotting the quiverplot
    It also puts the key at the x and y positions specified and with a size the user can specify
    """

    # plots the quiverplot. The return value of plt.quiver (an "Artist" datatype which contains the data
    # needed to draw the arrows) is returned to the variable q.
    q = plt.quiver(x, y, vx, vy, pivot='mid', label='$v_x$ = cos($x$), $v_y$ = sin($y$)')

    # This then is passed to plt.quiverkey so the key knows what data it represents
    plt.quiverkey(q, x_pos, y_pos, key_size, r'$2\frac{m}{s}$', labelpos='E', coordinates='figure')
    return q


def main():


    
    pass

if __name__ == '__main__':
    main()