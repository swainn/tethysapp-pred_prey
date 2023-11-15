from django.shortcuts import render
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import Button

@controller
def home(request):
    """
    Controller for the app home page.
    """
    x0 = 10
    y0 = 1
    alpha = 1.1
    beta = 0.4
    delta = 0.1
    gamma = 0.4

    context = {
        "initial_x0": x0,
        "initial_y0": y0,
        "initial_alpha": alpha,
        "initial_beta": beta,
        "initial_delta": delta,
        "initial_gamma": gamma,
    }
    return render(request, 'pred_prey/home.html', context)