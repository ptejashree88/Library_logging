"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Book import views
from book2 import views as second_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homepage,name='welcome'),
    path('save_book/', views.save_book),
    path('edit/<int:id>/',views.edit),
    path('delete/<int:id>/',views.delete),
    path('show_deleted/',views.show_deleted),
    path('hard_delete/<int:id>/',views.hard_delete),
    path('restore/<int:id>/',views.restore),
    path('delete_all/',views.delete_all),
    path('restore_all/',views.restore_all),

    #second app
    path('second',second_views.home),
]
