import matplotlib.pyplot as plt
from cycler import cycler
import matplotlib.cm as cm
from pathlib import Path
import numpy as np

#variables
dt    = np.linspace(0.05,0.0005,5,endpoint = True)
t_max = 10*np.pi

#initial conditions - y is velocity , dont ask WHY
x_0 = 0 
y_0 = 1
t_0 = 0

###

def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path


def sine_wave(num):                     #to compare with euler method
    t = np.linspace(0,t_max,num)
    x = np.sin(t)
    return x , t


def diff_funcs(x_0,y_0,t_0,dt,t_max): #eulers method to approximate sine wave
    x , y , t = x_0 , y_0 , t_0
    position = []
    time      = []
    while t <= t_max:
        position.append(x)
        time.append(t)
        dx = y
        dy = -x
        x = x + dx * dt
        y = y + dy * dt
        t = t + dt
    return position, time


fig     =  plt.figure(figsize = (10,5))
x_vs_t  = fig.add_subplot(2,1,1)
err     = fig.add_subplot(2,1,2)
err.set_xlabel("Time t")
err.set_ylabel("Error")
x_vs_t.set_ylabel("Amplitude")

cmap = cm.plasma  # try "plasma", "tab10", etc.
colors = cmap(np.linspace(0, 1, len(dt),endpoint = True))
x_vs_t.set_prop_cycle(cycler(color=colors))
err.set_prop_cycle(cycler(color=colors))

for dt_val in dt:
    position, time = diff_funcs(x_0,y_0,t_0,dt_val,t_max)
    x_exact,t_exact = sine_wave(len(time))
    x_vs_t.plot(time, position)
    err.plot(time, abs(position-x_exact),label=f'dt={dt_val:.4f}')

x_vs_t.plot(t_exact, x_exact, color = "black",linestyle = "-." , label = "x = sin(t)")
#x_vs_t.axhline(0,color="black")
err.axhline(0,color="black",linestyle = "-.")
x_vs_t.legend()
err.legend()
x_vs_t.axis([0,t_max,-2.2,2.2])
err.axis([0,t_max,0,1.2])

filename = generate_path(basename='E3-Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
plt.savefig(filename, bbox_inches='tight')
print("Output file saved to {}.".format(filename))
plt.show()