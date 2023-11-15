from tethys_sdk.base import TethysAppBase


class PredPrey(TethysAppBase):
    """
    Tethys app class for Pred Prey.
    """

    name = 'Pred Prey'
    description = ''
    package = 'pred_prey'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'pred-prey'
    color = '#a81414'
    tags = ''
    enable_feedback = False
    feedback_emails = []