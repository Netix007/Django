from django.urls import path
from . import views


urlpatterns = [
    path('articles/<int:author_id>/', views.get_article_by_author, name='get_article_by_author'),
    path('article/<int:article_id>/', views.get_article, name='get_article'),
    path('author_forms/', views.add_author, name='add_author'),
    path('article_forms/', views.add_article, name='add_article'),
]
