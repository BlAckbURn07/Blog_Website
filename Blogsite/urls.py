"""firstblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
#from . import views
from .views import HomeView
from .views import ArticleView
from .views import AddView
from .views import Edit
from .views import Delete
urlpatterns = [
    #path('', views.home, name="home"),
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleView.as_view(),name="articlelink"),
    path('add_post/',AddView.as_view(), name="addlink"),
    path('article/<int:pk>/edit_post',Edit.as_view(), name="editlink"),
    path('article/<int:pk>/delete_post',Delete.as_view(), name="deletelink"),
]
