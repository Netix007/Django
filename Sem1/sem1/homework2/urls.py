from django.urls import path
from . import views


urlpatterns = [
    path('orders/<int:client_id>/', views.get_items_by_client, name='get_items_by_client'),
    path('edit_item/<int:item_id>/', views.edit_item_by_id, name='edit_item_by_id'),
    path('upload/<int:item_id>/', views.upload_image, name='upload_image'),
]