import matplotlib.pyplot as plt
import numpy as np

# variables
dt      = 1
t_max   = 10
tau     = 2

# initial conditions
t_0, N_0 = 0, 10

time = np.linspace(t_0,t_max,num = 100,endpoint=True)
N = []
t_approx = []
N_approx = []

def decay():
    for t in time:
        N_dt = N_0 * np.exp(-t/tau)
        N.append(N_dt)
    return 0

def approx_decay():
    t = t_0
    N = N_0

    while t <= t_max:
        t_approx.append(t)
        N_approx.append(N)
        N = N - (N/tau) * dt  # Euler method update
        t = t + dt

    return t_approx, N_approx

        

decay()
approx_decay()

fig     =  plt.figure()
N_vs_t  = fig.add_subplot()
N_vs_t.set_xlabel("Time (s)")
N_vs_t.set_ylabel("Count")
N_vs_t.plot(time,N, color = 'red') 
N_vs_t.plot(t_approx,N_approx, color = 'black')
plt.show()