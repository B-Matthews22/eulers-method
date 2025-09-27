import numpy as np
import matplotlib.pyplot as plt
import R4_function as rf

from scipy import integrate
from pathlib import Path

def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path


def main():
    # define the damping values to test
    b_values = [0.5, 2.0, 5.0]  
    labels = ["Underdamped", "Critical", "Overdamped"]

    # initial parameters
    x0 = 1
    v0 = 0
    omega0 = 1
    y0 = (x0, v0)
    t0 = 0
    tf = 30
    n = 1001
    t_eval = np.linspace(t0, tf, n)

    # create 2x3 subplots
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))

    for i, (b, label) in enumerate(zip(b_values, labels)):
        # integrate system
        result = integrate.solve_ivp(
            fun=rf.damped_pendulum,
            t_span=(t0, tf),
            y0=y0,
            method="RK45",
            args=(b, omega0),
            t_eval=t_eval
        )
        x, v = result.y
        t = result.t

        # time evolution subplot (top row)
        ax_time = axes[0, i]
        ax_time.plot(t, x, label=r"$x(t)$")
        ax_time.plot(t, v, label=r"$v(t)$")
        ax_time.set_xlabel("Time (s)")
        ax_time.set_ylabel("Amplitude")
        ax_time.set_title(f"{label} (b={b})")
        ax_time.legend(loc=1)

        # phase space subplot (bottom row)
        ax_phase = axes[1, i]
        rf.phase_space(ax_phase, x, v)

    plt.tight_layout()
    
    
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    filename = generate_path(basename='R4-graph', extension='svg')  # uses the function defined above

    # saves and displays the file
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    plt.show()

if __name__ == '__main__':
    main()