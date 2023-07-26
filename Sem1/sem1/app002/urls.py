from django.urls import path
from . import views


urlpatterns = [
    path('coinplay/', views.coin, name='coinplay'),
    path('diceplay/', views.dice, name='diceplay'),
    path('randomnum/', views.random_num, name='randomnum'),
]
