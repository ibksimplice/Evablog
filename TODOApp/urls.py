"""TODOApp URL Configuration

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
from django.contrib import admin
from django.urls import path
from home.views import home, tododetails, CreateTodo, update, todo_delete, fulltime, internship,parttime,remote,freelance,createForm


urlpatterns = [
    path('admin/', admin.site.urls), 

    path('', home, name="home"),
    path('fulltime/',fulltime, name="fulltime"),
    
    path('createForm/',createForm, name="createForm"),
    
    path('internship/',internship, name="internship"),
    path('parttime/',parttime, name="parttime"),
    path('remote/',remote, name="remote"),
    path('freelance/',freelance, name="freelance"),
    path('create', CreateTodo, name="create"),
    path('<id>/update/', update, name="update"),
    path('<id>/delete/', todo_delete, name="todo_delete"),
    path('<str:pk>/',tododetails, name="tododetails"),
   

]
