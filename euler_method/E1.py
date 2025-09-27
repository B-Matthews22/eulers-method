import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

# Parameters
dt_values = [0.5, 0.1, 0.01]   # step sizes
t_f = 10
tau = 2
t_0, N_0 = 0, 10

def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path

def euler_decay(x_0, t_0, t_f, dt, tau):
    N = []
    N_true = []
    time = []
    t, x = t_0, x_0
    while t <= t_f + 1e-12:
        N_true.append(x_0 * np.exp(-t/tau))   # exact solution
        N.append(x)                           # Euler solution
        time.append(t)
        x = x - (x/tau) * dt
        t = t + dt
    return np.array(time), np.array(N), np.array(N_true)

fig, axes = plt.subplots(
    2, 1, figsize=(12, 6), sharex=True,
    gridspec_kw={'height_ratios': [3, 1]}
)

# Top: Euler solutions vs exact
for h in dt_values:
    time, N, Nt = euler_decay(N_0, t_0, t_f, h, tau)
    axes[0].plot(time, N, '--', label=f'dt={h}')
axes[0].plot(time, Nt, 'k', label='Exact')
axes[0].set_ylabel('N(t)')
axes[0].legend()

# Bottom: Errors
for h in dt_values:
    time, N, Nt = euler_decay(N_0, t_0, t_f, h, tau)
    error = np.abs(N - Nt)
    axes[1].plot(time, error)
axes[1].set_xlabel('Time t')
axes[1].set_ylabel('Error')


plt.tight_layout()

filename = generate_path(basename='Decay-Error-Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
plt.savefig(filename, bbox_inches='tight')
print("Output file saved to {}.".format(filename))
plt.show()

