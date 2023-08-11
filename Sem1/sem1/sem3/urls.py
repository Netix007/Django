from django.urls import path
from . import views


urlpatterns = [
    path('game/coin/<int:count>/', views.coin, name='coin'),
    path('game/dice/<int:count>/', views.dice, name='dice'),
    path('game/ran_num/<int:count>/', views.ran_num, name='ran_num'),
    path('game/', views.single_games_form, name='single_games_form'),
]