import matplotlib.pyplot as plt
import numpy as np

#variables
dt = 0.05
t_max = 9

#initial conditions
x_0 = 1
t_0 = 0
position = []
time     = []

###
def diff_func(x_0,t_0,dt,t_max):
    x = x_0
    t = t_0
    while t <= t_max:
        diff = t - x*x
        position.append(x), time.append(t)
        x = x + dt*diff
        t = t + dt
    return 0

diff_func(x_0,t_0,dt,t_max)

fig     =  plt.figure()
x_vs_t  = fig.add_subplot()
x_vs_t.set_xlabel("Time (s)")
x_vs_t.set_ylabel("Position")
x_vs_t.plot(time,position, color = 'red') 
plt.show()