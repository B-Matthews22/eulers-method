import matplotlib.pyplot as plt
from scipy import integrate
import numpy as np


def verhulst(x, r, k):
    
    dxdt = r * x *(1-x/k)

    return dxdt


def main():
    start     = 0
    stop      = 50
    numpoints = 101
    r = 0.7
    k = 20

    x = np.linspace(-5,25,numpoints,endpoint=True)
    dxdt = verhulst(x, r, k)
    plt.axhline(y=0, color = "k")
    plt.plot(x,dxdt)
    plt.show()

    lfun = lambda t, x: verhulst(x, r, k)
    t_eval = np.linspace(start, stop, numpoints)

    initial_conditions = [0.1, 5, 15, 25]  # different starting values

    plt.figure()
    for x0 in initial_conditions:
        result = integrate.solve_ivp(fun=lfun,
                                    t_span=(start, stop),
                                    y0=[x0],
                                    method="RK45",
                                    t_eval=t_eval)
        plt.plot(result.t, result.y[0], label=f"x₀ = {x0}")

    plt.axhline(y=k, color="red", linestyle="--", label=f"K = {k}")
    plt.xlabel("t (time)")
    plt.ylabel("x(t)")
    plt.title("Verhulst (Logistic) Growth for Multiple Initial Conditions")
    plt.legend()
    plt.show()

# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()