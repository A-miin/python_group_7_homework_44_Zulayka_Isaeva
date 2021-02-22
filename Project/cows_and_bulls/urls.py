from django.urls import path
from .views import home, game



urlpatterns = [
    path('',home),
    path('game/', game)
]
