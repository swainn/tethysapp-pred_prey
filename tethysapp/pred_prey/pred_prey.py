import numpy as np
from scipy.integrate import odeint


def run_pred_prey_simulation(x0, y0, alpha, beta, delta, gamma,
                             time_duration=50, timesteps=1000):
    def simulate_timestep(variables, t, params):
        x, y = variables
        alpha, beta, delta, gamma = params
        dxdt = alpha * x - beta * x * y
        dydt = delta * x * y - gamma * y
        return [dxdt, dydt]

    z0 = [x0, y0]
    t = np.linspace(0, time_duration, num=timesteps)
    params = [alpha, beta, delta, gamma]
    z = odeint(simulate_timestep, z0, t, args=(params,))
    return t, z


