from django.urls import path
from . import views


urlpatterns = [
    path('orders/<int:client_id>/', views.get_items_by_client, name='get_items_by_client'),
]