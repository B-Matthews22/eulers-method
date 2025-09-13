import matplotlib.pyplot as plt
import numpy as np

#variables
dt = 0.05
t_max = 400

#initial conditions
x_0 = [3,1,0.5,0,-0.5,-0.7]
t_0 = 0

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
x_vs_t.set_xlabel("Time (s)")
x_vs_t.set_ylabel("Position")

for x in x_0:
    position, time = diff_func(x,t_0,dt,t_max)
    x_vs_t.plot(time, position)

plt.show()



