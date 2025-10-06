import matplotlib.pyplot as plt
from scipy import integrate
import numpy as np


def verhulst(x, r, k):
    
    dxdt = r * x *(1-x/k)

    return dxdt

def generate_path(home_folder= 'C:/Users/HP/', subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path


def main():
    start     = 0
    stop      = 50
    numpoints = 101
    r = 0.7
    k = 20
    initial_conditions = [0,0.1, 5, 20, 30]  # different starting values

    x = np.linspace(-5,25,numpoints,endpoint=True)
    dxdt = verhulst(x, r, k)

    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.axhline(0, color='k', linewidth=0.5)
    plt.ylim(-2,5)
    for xi in np.linspace(-5, 30, 15):
        dxi = verhulst(xi, r, k)
        if dxi > 0:
            plt.arrow(xi, 0, 0.5, 0, head_width=0.2, color="green")
        elif dxi < 0:
            plt.arrow(xi, 0, -0.5, 0, head_width=0.2, color="red")
    plt.scatter([0, 20], [0, 0], color=["red", "green"], zorder=4)
    plt.xlabel("x")
    plt.ylabel("x'")
    plt.text(-5.5, -1, "(a)", fontsize=12, 
    fontweight='bold', va='top', ha='left')
    plt.plot(x,dxdt,color="k")

    lfun = lambda t, x: verhulst(x, r, k)
    t = np.linspace(start, stop, numpoints)

    

    plt.subplot(1,2,2)
    
    for x0 in initial_conditions:
        result = integrate.solve_ivp(fun=lfun,
                                    t_span=(start, stop),
                                    y0=[x0],
                                    method="RK45",
                                    t_eval=t)
        plt.plot(result.t, result.y[0], label=f"x₀ = {x0}")

    plt.axhline(y=k, color="k", linestyle=":")
    plt.xlim(0,20)
    plt.xlabel("t")
    plt.ylabel("x(t)")
    plt.text(1, 3, "(b)", fontsize=12, 
    fontweight='bold', va='top', ha='left')
    plt.legend()
    
        # creates the path to store the data. Note that the data is not stored in the code repo directory.
    filename = generate_path(basename='G4-Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    
    plt.show()

# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()