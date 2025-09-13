import matplotlib.pyplot as plt

#variables
dt    = 0.02
t_max = 20
omega = 2

#initial conditions
x_0 = 0 
y_0 = 1
t_0 = 0

###
def diff_funcs(x_0,y_0,t_0,dt,t_max):
    x = x_0
    y = y_0
    t = t_0
    positionx = []
    positiony = []
    time      = []
    while t <= t_max:
        dx = y
        x = x + dx * dt
        dy = -x
        y = y + dy * dt
        t = t + dt
        positionx.append(x*y)
        positiony.append(y)
        time.append(t)
    return positionx, positiony, time

positionx, positiony, time = diff_funcs(x_0,y_0,t_0,dt,t_max)

fig     =  plt.figure()
x_vs_t  = fig.add_subplot()
x_vs_t.set_xlabel("Time (s)")
x_vs_t.set_ylabel("Position")
x_vs_t.plot(time, positionx)
plt.show()