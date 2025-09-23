import matplotlib.pyplot as plt
from cycler import cycler
import matplotlib.cm as cm
import numpy as np

#variables
dt    = np.linspace(0.05,0.0005,5,endpoint = True)
t_max = 10*np.pi

#initial conditions - y is velocity , dont ask WHY
x_0 = 0 
y_0 = 1
t_0 = 0

###
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
x_vs_t  = fig.add_subplot(1,2,1)
err     = fig.add_subplot(1,2,2)
x_vs_t.set_xlabel("Time (s)")
x_vs_t.set_ylabel("Amplitude (m)")

cmap = cm.plasma  # try "plasma", "tab10", etc.
colors = cmap(np.linspace(0, 1, len(dt)))
x_vs_t.set_prop_cycle(cycler(color=colors))
err.set_prop_cycle(cycler(color=colors))

for dt_val in dt:
    position, time = diff_funcs(x_0,y_0,t_0,dt_val,t_max)
    x_exact,t_exact = sine_wave(len(time))
    x_vs_t.plot(time, position)
    err.plot(time, abs(position-x_exact))

x_vs_t.plot(t_exact, x_exact, color = "black",linestyle = "-." , label = "x = sin(t)")
#x_vs_t.axhline(0,color="black")
err.axhline(0,color="black",linestyle = "-.")
x_vs_t.legend()
x_vs_t.axis([0,t_max,-2.2,2.2])
err.axis([0,t_max,-2.2,2.2])
plt.show()