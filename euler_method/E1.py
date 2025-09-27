import matplotlib.pyplot as plt
import numpy as np

# Parameters
dt_values = [0.5, 0.1, 0.01]   # step sizes
t_f = 10
tau = 2
t_0, N_0 = 0, 10

def euler_decay(x_0, t_0, t_f, dt, tau):
    N = []
    N_true = []
    time = []
    t, x = t_0, x_0
    while t <= t_f + 1e-12:
        N_true.append(x_0 * np.exp(-t/tau))   # exact solution
        N.append(x)                           # Euler solution
        time.append(t)
        x = x - (x/tau) * dt
        t = t + dt
    return np.array(time), np.array(N), np.array(N_true)

# Plot solutions
plt.figure(figsize=(10, 5))
for h in dt_values:
    time, N, Nt = euler_decay(N_0, t_0, t_f, h, tau)
    plt.plot(time, N, '--', label=f'Euler dt={h}')
plt.plot(time, Nt, 'k', label='Exact')
plt.xlabel('t')
plt.ylabel('N(t)')
plt.legend()
plt.show()

# Plot errors
plt.figure(figsize=(10, 5))
for h in dt_values:
    time, N, Nt = euler_decay(N_0, t_0, t_f, h, tau)
    error = np.abs(N - Nt)
    plt.plot(time, error, label=f'Error dt={h}')
plt.xlabel('t')
plt.ylabel('|N_exact - N_euler|')
plt.title('Error in Euler Approximation')
plt.legend()
plt.show()

