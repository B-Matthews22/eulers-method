import matplotlib.pyplot as plt
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


fig     =  plt.figure()
x_vs_t  = fig.add_subplot(1,2,1)
err     = fig.add_subplot(1,2,2)

for step in dt:
    position, velocity, time = diff_funcs(x_0,v_0,t_0,step,t_max)
    x_vs_t.plot(time, position)
    #x_vs_t.plot(time, velocity)
    x,v,t = wave(len(time))
    err.plot(time,x - position)

x_vs_t.plot(t, x,label = "x(t)",color = "black")
#x_vs_t.plot(t, v,label = "v(t)",color = "red")
x_vs_t.set_xlabel("Time (s)")
x_vs_t.set_ylabel("Amplitude")
#x_vs_t.plot(t_exact, x_exact,color = "red",label = "Sine wave")
x_vs_t.legend(loc=2)

plt.show()