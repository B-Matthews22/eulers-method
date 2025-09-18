import matplotlib.pyplot as plt
import numpy as np

#variables
dt    = np.linspace(0.05,0.0005,5,endpoint = True)
t_max = 20*np.pi

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


fig     =  plt.figure()
x_vs_t  = fig.add_subplot()
x_vs_t.set_xlabel("Time (s)")
x_vs_t.set_ylabel("Amplitude (m)")
for dt_val in dt:
    position, time = diff_funcs(x_0,y_0,t_0,dt_val,t_max)
    x_exact,t_exact = sine_wave(len(time))
    x_vs_t.plot(time, position,label = f"dt = {dt_val:.4f}")

x_vs_t.plot(t_exact, x_exact, color = "black",linestyle = "-." , label = "x = sin(t)")
x_vs_t.legend(loc = 2)

plt.show()