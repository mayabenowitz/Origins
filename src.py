def packages(all=True):
    if all is True:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        import matplotlib.dates as mdates
        import seaborn as sns
        import ipyvuetify as v
        import plotly.graph_objects as go
        from jupyterthemes import jtplot
    jtplot.style()


def display():
    from IPython.core.display import display, HTML
    display(HTML("<style>.container { width:70% !important; }</style>"))