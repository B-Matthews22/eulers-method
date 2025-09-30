import matplotlib.pyplot as plt
import matplotlib.cm as cm
from cycler import cycler
from pathlib import Path
import numpy as np

'''
need to graph the difference between approx and exact function
'''
#variables
dt = np.linspace(0.05,0.0005,5,endpoint = True)
t_max = 10*np.pi

#initial conditions
t_0 = 0
x_0 = 0
v_0 = 1

###

def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path


def wave(num):                     #to compare with euler method
    t = np.linspace(0,t_max,num)
    x = np.sin(t)
    v = np.cos(t)
    return x , v , t

def diff_funcs(x_0,v_0,t_0,dt,t_max): #eulers method to approximate sine wave
    x , v , t = x_0 , v_0 , t_0
    position = []
    velocity = []
    time     = []
    while t <= t_max:
        position.append(x)
        velocity.append(v)
        time.append(t)
        xinit = x + dt * v
        vinit = v - dt * x
        x = x + dt * (v + vinit) * 0.5
        v = v - dt * (x + xinit) * 0.5
        t = t + dt
    return position, velocity, time


fig     =  plt.figure(figsize = (10,5))
x_vs_t  = fig.add_subplot(2,1,1)
err     = fig.add_subplot(2,1,2)

cmap = cm.plasma  # try "plasma", "tab10", etc.
colors = cmap(np.linspace(0, 1, len(dt),endpoint = True))
x_vs_t.set_prop_cycle(cycler(color=colors))
err.set_prop_cycle(cycler(color=colors))

for dt_val in dt:
    position,velocity, time = diff_funcs(x_0,v_0,t_0,dt_val,t_max)
    x_exact,v_exact, t_exact = wave(len(time))
    x_vs_t.plot(time, position)
    err.plot(time, abs(position-x_exact),label=f'dt={dt_val:.4f}')
    err.set_xlabel("Time (s)")
    err.set_ylabel("Error")
    x_vs_t.set_ylabel("Amplitude")

x_vs_t.plot(t_exact, x_exact, color = "black",linestyle = "-." , label = "x = sin(t)")
#x_vs_t.axhline(0,color="black")
err.axhline(0,color="black",linestyle = "-.")
x_vs_t.legend(loc=2)
err.legend()
x_vs_t.axis([0,t_max,-1.2,1.2])
err.axis([0,t_max,0,0.5])

filename = generate_path(basename='E4-Graph', extension='svg')  # uses the function defined above

    # saves and displays the file
plt.savefig(filename, bbox_inches='tight')
print("Output file saved to {}.".format(filename))
plt.show()