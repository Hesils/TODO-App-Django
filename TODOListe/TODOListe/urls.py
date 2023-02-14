"""TODOListe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tasks import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', task_views.index, name="home"),
    path('', task_views.login, name="login_page"),
    path('sign_in', task_views.sign_in, name="sign_in"),
    path('sign_up', task_views.sign_up, name="sign_up"),
    path('logout', task_views.logout, name="logout"),
    path('add_user', task_views.add_user, name="add_user"),
    path('add_categorie', task_views.add_categorie, name="add_categorie"),
    path('add_task', task_views.add_task, name="add_task"),
    path('get_task/<int:categorie_pk>', task_views.get_tasks, name="get_task"),
]
