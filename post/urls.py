from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.current_time, name='current_time'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
]
