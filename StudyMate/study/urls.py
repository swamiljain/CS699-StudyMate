from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_fun,name='login'),
    path('register/', views.register_fun,name='register'),
    path('logout/', views.logout_fun, name='logout'),
]