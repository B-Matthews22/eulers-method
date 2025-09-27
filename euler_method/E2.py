import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

#variables
dt = 0.05
t_max = 500

#initial conditions
x_0 = [0]
t_0 = 0

def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path
###
def diff_func(x_0,t_0,dt,t_max):
    x = x_0
    t = t_0
    position = []
    time     = []
    while t <= t_max:
        diff = t - x*x
        position.append(x), time.append(t)
        x = x + dt*diff
        t = t + dt
    return position , time

fig     =  plt.figure()
x_vs_t  = fig.add_subplot()


for x in x_0:
    position, time = diff_func(x,t_0,dt,t_max)
    x_vs_t.plot(time, position, label=f'Euler Approximation')

#This is for the x = sqrt(t) curve we need to compare our approximations to
root_t = [np.sqrt(t) for t in time]            

x_vs_t.set_xlabel("Time t")
x_vs_t.set_ylabel("x(t)")
x_vs_t.plot(time,root_t, color = "black", label = "x = $\sqrt{t}$",linestyle = "-.")
x_vs_t.legend()

filename = generate_path(basename='E2-Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
plt.savefig(filename, bbox_inches='tight')
print("Output file saved to {}.".format(filename))
plt.show()
