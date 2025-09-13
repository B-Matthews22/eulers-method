import matplotlib.pyplot as plt
import numpy as np
#variables
dt    = 0.02
t_max = 35

#initial conditions
x_0 = 0 
y_0 = 1
t_0 = 0

###
def sine_wave():
    t = np.linspace(0,t_max,1000)
    x = np.sin(t)
    return x , t


def diff_funcs(x_0,y_0,t_0,dt,t_max):
    x = x_0
    y = y_0
    t = t_0
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

position, time = diff_funcs(x_0,y_0,t_0,dt,t_max)
x_exact , t_exact = sine_wave()

fig     =  plt.figure()
x_vs_t  = fig.add_subplot()
x_vs_t.set_xlabel("Time (s)")
x_vs_t.set_ylabel("Position")
x_vs_t.plot(time, position)
x_vs_t.plot(t_exact, x_exact)

plt.show()