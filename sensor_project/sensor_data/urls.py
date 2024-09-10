from django.urls import path
from .views import register, login, plot_graph, control_fan  # Import control_fan

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('plot-graph/', plot_graph, name='plot_graph'),
    path('control-fan/', control_fan, name='control_fan'),  # Add URL for fan control
]
