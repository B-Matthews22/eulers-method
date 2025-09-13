import matplotlib.pyplot as plt
import numpy as np

#variables
dt = 0.005
t_max = 35

#initial conditions
t_0 = 0
x_0 = 0
v_0 = 1

###

def sine_wave():                     #to compare with euler method
    t = np.linspace(0,t_max,1000)
    x = np.sin(t)
    return x , t


def diff_funcs(x_0,v_0,t_0,dt,t_max): #eulers method to approximate sine wave
    x , v , t = x_0 , v_0 , t_0
    position = []
    time     = []
    while t <= t_max:
        position.append(x)
        time.append(t)
        xinit = x + dt * v
        vinit = v - dt * x
        x = x + dt * (v + vinit) * 0.5
        v = v - dt * (x + xinit) * 0.5
        t = t + dt
    return position, time

position, time = diff_funcs(x_0,v_0,t_0,dt,t_max)
x_exact , t_exact = sine_wave()

fig     =  plt.figure()
x_vs_t  = fig.add_subplot()
x_vs_t.set_xlabel("Time (s)")
x_vs_t.set_ylabel("Position")
x_vs_t.plot(time, position)
x_vs_t.plot(t_exact, x_exact)

plt.show()