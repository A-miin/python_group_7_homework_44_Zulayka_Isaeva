from django.urls import path
from .views import home, game, see_history



urlpatterns = [
    path('',home),
    path('game/', game),
    path('history/', see_history)
]
