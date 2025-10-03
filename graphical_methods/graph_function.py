import matplotlib.pyplot as plt
import numpy as np

def grid_options(start, stop, stepsize, numpoints, option):
    
    if option == "arange":
        # arange creates a set of values between a start point and a stop point in steps of stepsize.
        x, y = np.meshgrid(np.arange(start, stop, stepsize), np.arange(start, stop, stepsize))
    elif option == "linspace":
        # linspace creates a set of numpoints values between a start point and a stop point
        # start point and stop point are both always included
        x, y = np.meshgrid(np.linspace(start, stop, numpoints), np.linspace(start, stop, numpoints))
    else:
        raise NameError("Invalid option {} selected.".format(option))
    return x, y


def reduced_density(x, y, vx, vy, label, x_pos=0.9, y_pos=0.9, key_size=2, reduction=5):
    

    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square

    
    # plots a scatter plot with the same reduction factor
    # specifies the colour of the points and their size
    plt.scatter(x[::reduction, ::reduction], y[::reduction, ::reduction], color='r', s=3)

    q = plt.quiver(x[::reduction, ::reduction], y[::reduction, ::reduction],  # coordinates at reduced density
                   vx[::reduction, ::reduction], vy[::reduction, ::reduction],  # arrow x/y lengths at reduced density
                   pivot='mid',  # position of the pivot of the arrow
                   label=f'{label}')  # label using LaTex notation

    # creates the quiver key as above in the position specified
    plt.quiverkey(q, x_pos, y_pos, key_size, labelpos='E', coordinates='figure')
    plt.legend()


def add_legend(x, y, vx, vy, label, unit_label, x_pos=0.9, y_pos=0.9, key_size=2):
    """
    This function demonstrates how to add a key to your quiverplot. In addition to plotting the quiverplot
    It also puts the key at the x and y positions specified and with a size the user can specify
    """
    
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    q = plt.quiver(x, y, vx, vy, pivot='mid', label=f'{label}')

    # This then is passed to plt.quiverkey so the key knows what data it represents
    plt.quiverkey(q, x_pos, y_pos, key_size, f"{unit_label}", labelpos='E', coordinates='figure')
    plt.legend()
    return q


def density_change(x, y, dx, dy):
    """
    Substituting this streamplot command in for the one in G3_baseline.py would reduce the density of the
    streamlines to a quarter of their original density (a half in each direction). You can change the
    density to suit your application as needed.
    """
    plt.streamplot(x, y, dx, dy, density=[0.5, 0.5])
    
    
def plot_seed_points(x, y, dx, dy):
    """
    It is also possible to draw one or more streamlines by defining the seed points (where the streamline starts from)
    on the plot. Seed points are defined as an [N×2] array.
    So for example, if we want to define the seed points as (x1=−2, y1=−2), (x2=1, y2=0), and (x3=2, y3=2),
    there are a few ways to do it.
    In the below example, we define the seed points with a 2-dimensional array, with two sub-arrays, one for x- and
    one for y- coordinates, which is a [2x3] array. As a result, we have to use the .T transpose operation to make a
    [3x2] array which will be acceptable by the streamplot method. Consider how you might create a [3x2] array directly,
    and in your report comment on which is more suitable.
    """
    seed_points = np.array([[-2, 1, 1.5], [-2, 0, -1.5]])
    plt.streamplot(x, y, dx, dy, color='b', start_points=seed_points.T)
    plt.plot(seed_points[0], seed_points[1], 'bo')  # show seeds on graph


def integration_direction(x, y, dx, dy):
    """
    In the seed_points example, note that the streamline solutions propagate in both the forward and backward directions
    from the seed point. We can control the integration directions using the option integration_direction='forward' and
    integration_direction='backward' as shown in the code below.
    """
    seed_points = np.array([[-2, 1, 1.5], [-2, 0, -1.5]])
    plt.streamplot(x, y, dx, dy, color='b', start_points=seed_points.T, integration_direction='forward')
    plt.plot(seed_points[0], seed_points[1], 'bo')  # show seeds on graph


def colour_streamlines(x, y, dx, dy):
    """
    We can specify a function to assign a specific color to each point on the streamline. This example does so by using
    the magnitude of the vector as scale by applying pythagoras to the dx and dy c components of the vector field.
    This is then assigned to the variable color, and the colormap (cmap) 'gnuplot' applied.
    Check out https://matplotlib.org/stable/users/explain/colors/colormaps.html for alternative colourmaps
    """
    strm = plt.streamplot(x, y, dx, dy, color=np.sqrt(dx ** 2 + dy ** 2), linewidth=2, cmap='gnuplot')
    plt.colorbar(strm.lines)


def size_streamlines(x, y, dx, dy):
    """
    Instead of changing the color we can change the thickness of the streamline, in proportion to its magnitude.
    We first calculate the array of magnitudes and then calculate a linewidth which is normalised to that magnitude and
    then multiplied by a factor that makes it visible.
    We then set the colour of all the streamlines to black. If you want to select other colours, you can pick ones from
    this list https://matplotlib.org/stable/gallery/color/named_colors.html or follow the tutorial on using colours from
    this link https://matplotlib.org/stable/users/explain/colors/colors.html
    """
    mag = np.sqrt(dx ** 2 + dy ** 2)  # using numpy square root method
    lw = 10 * mag/mag.max()
    plt.streamplot(x, y, dx, dy, linewidth=lw, color='black')


def both_streamlines(x, y, dx, dy):
    """
    These modifications can also be combined, creating coloured lines with varying thickness
    """
    mag = np.sqrt(dx ** 2 + dy ** 2)  # using numpy square root method
    lw = 10 * mag/mag.max()
    strm = plt.streamplot(x, y, dx, dy, linewidth=lw, color=mag, cmap='gnuplot')
    plt.colorbar(strm.lines, fraction=0.046, pad=0.04)

