"""
URL configuration for sem1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from sem1 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app001.urls')),
    path('games/', include('app002.urls')),
    path('main/', include('main_page.urls')),
    path('about/', include('about_page.urls')),
    path('sem3/', include('sem3.urls')),
    path('sem2_task1/', include('sem2_task1.urls')),
    path('homework2/', include('homework2.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
