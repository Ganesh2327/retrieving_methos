"""
URL configuration for project20 project.

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
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_Topic/',insert_Topic,name='insert_Topic'),
    path('insert_Webpage/',insert_Webpage,name='insert_Webpage'),
    path('insert_AccessRecords/',insert_AccessRecords,name='insert_AccessRecords'), 
    path('display_topics/',display_topics,name='display_topics'),
    path('display_webpages/',display_webpages,name='display_webpages'),
    path('display_AccessRecords/',display_AccessRecords,name='display_AccessRecords'),
    path('update_webpages/',update_webpages,name='update_webpages'),
    path('delete_webpages/',delete_webpages,name='delete_webpages')
]
