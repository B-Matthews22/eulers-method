import matplotlib.pyplot as plt
import numpy as np
"""
Run the program for different size time steps, e.g. Δt={0.01, 0.005, 0.001}
Plot both the calculated and exact values of N(t) vs. t on the same graph.
Compare your results to the exact solution by calculating the difference between 
the exact solution and the computed solution and see how this varies with time t.
Comment on your results and observed errors
"""
# variables
dt      = 0.1
t_max   = 10
tau     = 2

# initial conditions
t_0, N_0 = 0, 10

time = np.linspace(t_0,t_max,num = int(t_max/dt)+1,endpoint=True)
N = []
t_approx = []
N_approx = []
error    = []

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

for i in range(len(N)):
    error.append(np.abs(N[i]-N_approx[i]))

fig     =  plt.figure(figsize =(6,10))
N_vs_t  = fig.add_subplot(2,1,1)
N_vs_t.set_xlabel("Time (s)")
N_vs_t.set_ylabel("Count")
N_vs_t.plot(time, N, color = 'red', label = "True Curve") 
N_vs_t.plot(t_approx, N_approx, color = 'black', label = "Approximated Curve",linestyle = "-.")
N_vs_t.legend()

err = fig.add_subplot(2,1,2)
err.set_xlabel("Time (s)")
err.set_ylabel("Error")
err.plot(time,error,color = "black",label = "Error")
err.legend()
#plt.savefig('E1_graph.svg', format='svg',dpi=1200)
plt.show()
