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

    has_errors = False
    x0_error = ""
    y0_error = ""
    alpha_error = ""
    beta_error = ""
    delta_error = ""
    gamma_error = ""
    
    if request.POST and 'update-plots-submit' in request.POST:
        print(request.POST)
        x0 = int(request.POST.get('x0', x0))
        y0 = int(request.POST.get('y0', y0))
        alpha = float(request.POST.get('alpha', alpha))
        beta = float(request.POST.get('beta', beta))
        delta = float(request.POST.get('delta', delta))
        gamma = float(request.POST.get('gamma', gamma))

        if x0 <= 0:
            has_errors = True
            x0_error = "x0 must be positive."

        if y0 <= 0:
            has_errors = True
            y0_error = "y0 must be positive."

        if alpha <= 0:
            has_errors = True
            alpha_error = "alpha must be positive."

        if beta <= 0:
            has_errors = True
            beta_error = "beta must be positive."

        if delta <= 0:
            has_errors = True
            delta_error = "delta must be positive."

        if gamma <= 0:
            has_errors = True
            gamma_error = "gamma must be positive."

    context = {
        "initial_x0": x0,
        "initial_y0": y0,
        "initial_alpha": alpha,
        "initial_beta": beta,
        "initial_delta": delta,
        "initial_gamma": gamma,
        "x0_error": x0_error,
        "y0_error": y0_error,
        "alpha_error": alpha_error,
        "beta_error": beta_error,
        "delta_error": delta_error,
        "gamma_error": gamma_error,
    }
    return render(request, 'pred_prey/home.html', context)