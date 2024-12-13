from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('homeProfe', views.homeProfe, name='homeProfe'),
    path('regAsistencia', views.regAsistencia, name='regAsistencia'),
    path('login', views.login, name='login'),
    path('cel', views.cel, name='cel'),
    
]