import matplotlib.pyplot as plt

# variables
dt      = 1
t_max   = 10
tau     = 2

# initial conditions
t_0, N_0 = 0, 10

t = [t_0]
N = [N_0]

def decay():
    for i in range(t_0,t_max,dt):
        N_dt = N[i] - N[i]/tau * dt
        t_dt = t[i] + dt
        N.append(N_dt)
        t.append(t_dt)
    return 0

decay()

fig     =  plt.figure()
N_vs_t  = fig.add_subplot()
N_vs_t.plot(N,t) 
plt.show()