import numpy as np
from scipy.integrate import odeint
import plotly.graph_objs as go


PLOT_MARGINS = dict(l=20, r=20, t=30, b=20)
LEGEND_POSITION = dict(yanchor='top', xanchor='right', y=0.99, x=0.99)
PLOT_HEIGHT = 275


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


def generate_population_dynamics_plot(t, z):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=t,
        y=z[:, 0],
        name='Prey',
    ))
    fig.add_trace(go.Scatter(
        x=t,
        y=z[:, 1],
        name='Predators',
    ))
    fig.update_layout(
        autosize=True,
        height=PLOT_HEIGHT,
        xaxis_title='Time',
        yaxis_title='Population (per sq. kilometer)',
        legend=LEGEND_POSITION,
        margin=PLOT_MARGINS,
    )
    return fig


def generate_phase_space_plot(t, z):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=z[:, 0],
        y=z[:, 1],
    ))
    fig.update_layout(
        autosize=True,
        height=PLOT_HEIGHT,
        xaxis_title='Prey (per sq. kilometer)',
        yaxis_title='Predators (per sq. kilometer)',
        legend=LEGEND_POSITION,
        margin=PLOT_MARGINS,
    )
    return fig
