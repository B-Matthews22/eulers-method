import matplotlib.pyplot as plt
import numpy as np
import pathlib as Path


def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path


def get_vector(x, y):
    
    z = np.sqrt(x**2 + y**2)
    vx , vy = np.gradient(z) , np.gradient(z)

    return vx, vy

def main():
    plt.close()

    # Create Grid
    coords = np.linspace(-2*np.pi, 2*np.pi, 101)
    x, y = np.meshgrid(coords, coords)

    # Create Function and gradient
    z = np.sqrt(x**2 + y**2)
    dx, dy = np.gradient(z)  # Calculate the gradient

    # Create Figure
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('$f(x,y)=\sqrt{x^2+y^2}$')

    # Plot scalar function as color plot (contour map)
    contour = ax.contourf(x, y, z, 50, cmap='plasma')

    # Add colorbar that matches the height of the plot
    cbar = fig.colorbar(contour, ax=ax, fraction=0.046, pad=0.04, ticks = np.linspace(0,9,5,endpoint=True))

    # Plot Gradient as quiver plot
    skip = 5
    x_skipped, y_skipped = x[::skip, ::skip], y[::skip, ::skip]
    dx_skipped, dy_skipped = dx.T[::skip, ::skip], dy.T[::skip, ::skip]

    ax.quiver(x_skipped, y_skipped, dx_skipped, dy_skipped, scale=3, color='k')


    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    filename = generate_path(basename='G2-Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()